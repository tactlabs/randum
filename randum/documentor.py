import inspect
import warnings


class Documentor:

    def __init__(self, generator):
        """
        :param generator: a localized Generator with providers filled,
                          for which to write the documentation
        :type generator: randum.Generator()
        """
        self.generator = generator
        self.max_name_len = 0
        self.already_generated = []

    def get_formatters(self, locale=None, excludes=None, **kwargs):
        self.max_name_len = 0
        self.already_generated = [] if excludes is None else excludes[:]
        formatters = []
        providers = self.generator.get_providers()
        for provider in providers[::-1]:  # reverse
            if locale and provider.__lang__ != locale:
                continue
            formatters.append(
                (provider, self.get_provider_formatters(provider, **kwargs)),
            )
        return formatters

    def get_provider_formatters(self, provider, prefix='fake.',
                                with_args=True, with_defaults=True):

        formatters = {}

        for name, method in inspect.getmembers(provider, inspect.ismethod):
            # skip 'private' method and inherited methods
            if name.startswith('_') or name in self.already_generated:
                continue

            arguments = []
            randum_args = []
            randum_kwargs = {}

            if name == 'binary':
                randum_kwargs['length'] = 1024
            elif name in ['zip', 'tar']:
                randum_kwargs.update({
                    'uncompressed_size': 1024,
                    'min_file_size': 512,
                })

            if with_args:
                # retrieve all parameter
                argspec = inspect.getfullargspec(method)

                lst = [x for x in argspec.args if x not in ['self', 'cls']]
                for i, arg in enumerate(lst):

                    if argspec.defaults and with_defaults:

                        try:
                            default = argspec.defaults[i]
                            if isinstance(default, str):
                                default = repr(default)
                            else:
                                # TODO check default type
                                default = f"{default}"

                            arg = f'{arg}={default}'

                        except IndexError:
                            pass

                    arguments.append(arg)
                    if with_args == 'first':
                        break

                if with_args != 'first':
                    if argspec.varargs:
                        arguments.append('*' + argspec.varargs)
                    if argspec.varkw:
                        arguments.append('**' + argspec.varkw)

            # build fake method signature
            signature = f"{prefix}{name}({', '.join(arguments)})"

            try:
                # make a fake example
                example = self.generator.format(name, *randum_args, **randum_kwargs)
            except (AttributeError, ValueError) as e:
                warnings.warn(str(e))
                continue
            formatters[signature] = example

            self.max_name_len = max(self.max_name_len, len(signature))
            self.already_generated.append(name)

        return formatters

    @staticmethod
    def get_provider_name(provider_class):
        return provider_class.__provider__
