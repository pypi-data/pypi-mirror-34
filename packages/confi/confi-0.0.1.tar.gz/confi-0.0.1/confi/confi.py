import os
from distutils.util import strtobool


class ConfigError(Exception):
    pass


class ConfigField:
    def __init__(self, processor=str, default=None, required=False, from_var=None):
        self.processor = processor
        self.default = default
        self.required = required
        self.from_var = from_var


class EnvironConfigurationMeta(type):
    def __call__(cls, *args, **kwargs):
        raise TypeError("Can't instance a configuration class")

    def __init__(cls, name, bases, dct):
        super(EnvironConfigurationMeta, cls).__init__(name, bases, dct)

        cls._config_fields = []
        for k, field in dct.items():
            if isinstance(field, ConfigField):
                var_name = field.from_var or k
                config_val = os.environ.get(var_name)
                if config_val:
                    config_val = field.processor(config_val)
                elif field.default:
                    if callable(field.default):
                        config_val = field.default()
                    else:
                        config_val = field.default
                if config_val is None and field.required:
                    raise ConfigError(f'Config param {k} must be provided')

                cls._config_fields.append(k)
                setattr(cls, k, config_val)

    def __getitem__(cls, item):
        return getattr(cls, item)


class BaseEnvironConfig(metaclass=EnvironConfigurationMeta):
    """Base config class.
    Loads all config params that are instances of ConfigField from environ,
    applies preprocessor, validates if required.

    Example:
    ```
    >>> class Config(BaseEnvironConfig):
    ...  DEBUG = ConfigField(processor=strtobool, default=True)
    ...
    >>> Config.DEBUG
    True
    ```

    Loads env var "DEBUG", applies function `string_to_bool` to the returned value,
    if the result is None uses default of True.

    Since its a global class it's __VERY IMPORTANT__ to import it like this:

    ```
    from package import module
    print(module.ConfigClass.as_text())
    ```

    and __not__ like this:

    ```
    from package.module import ConfigClass
    print(ConfigClass.as_text())
    ```

    The first variant allows you to monkey patch the config during testing.
    Pytest example:

    ```
    from package.module import ConfigClass

    class TestConfig(ConfigClass):
        pass

    TestConfig.TEST = True

    monkeypatch.setattr('package.module.ConfigClass', TestConfig)
    ```

    After this all code accesing `module.ConfigClass` will get `TestConfig`.
    """

    @classmethod
    def _filter_attrs(cls, include_private, exclude):
        attrs = [(k, getattr(cls, k)) for k in cls._config_fields if
                 not callable(getattr(cls, k))]
        if not include_private:
            attrs = filter(lambda p: not p[0].startswith('_'), attrs)
        if exclude:
            attrs = filter(lambda p: p[0] in exclude, attrs)
        return attrs

    @classmethod
    def as_dict(cls, include_private=False, exclude=None, censor=None):
        if not exclude:
            exclude = []
        if not censor:
            censor = []
        attrs = dict(cls._filter_attrs(include_private, exclude=exclude))
        for censored in censor:
            attrs[censored] = '*' * len(attrs[censored])
        return attrs

    @classmethod
    def as_text(cls, include_private=False, exclude=None, censor=None):
        data_fields = cls.as_dict(include_private, exclude=exclude, censor=censor)
        attrs = [
            "{}={}".format(k, str(v)) for k, v in data_fields.items()]
        attrs.sort()  # alphabetical order
        attrs.sort(key=len, reverse=False)  # sort by descending length
        attr_list = "\n\t".join(attrs)
        return f'{cls.__name__}:\n\t{attr_list}'
