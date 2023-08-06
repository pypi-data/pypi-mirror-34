import os


class OptionMeta(type):
    def __new__(cls, name, bases, namespace, env_name=None, required=False, default=None):
        if name != 'Option' and env_name is not None:
            # subclass, set class name = env_name in globals
            if required:
                value = os.getenv(env_name)
            else:
                value = os.getenv(env_name, default)
            set_or_raise(name, value)
        new_space = dict(namespace)
        for attr, option in namespace.items():
            if not OptionMeta.is_dunder(attr) and isinstance(option, Option):
                new_space[attr] = option.value
        return type.__new__(cls, name, bases, new_space)

    @staticmethod
    def is_dunder(name):
        return name.startswith('__') and name.endswith('__') and len(name) > 4


class Option(metaclass=OptionMeta):
    def __init__(self, env_name, required=False, default=None):
        if required:
            value = os.getenv(env_name)
            if value is None:
                raise ValueError('env var {} for option not found'.format(env_name))
        else:
            value = os.getenv(env_name, default)

        if value is None:
            self.value = 'NOT_SET'
        else:
            self.value = value


def set_or_raise(name, value):
    if name in globals():
        raise Exception('{} already exists in globals'.format(name))
    else:
        globals()[name] = value
