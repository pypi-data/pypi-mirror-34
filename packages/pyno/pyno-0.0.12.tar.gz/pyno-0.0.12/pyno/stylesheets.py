class StyleVariable:
    def __init__(self):
        self.value = None

    def __call__(self, value):
        self.value = value
        return self

    def __str__(self):
        return str(self.value)


class StyleVariableStorage:
    def __getattr__(self, item):
        if item in self.__dict__:
            return self.__dict__[item]
        else:
            self.__dict__[item] = StyleVariable()
            return self.__dict__[item]

    def __setattr__(self, key, value):
        if key in self.__dict__:
            self.__dict__[key](value)
        else:
            self.__dict__[key] = StyleVariable()
            self.__dict__[key](value)

class joinable_dict(dict):
    """ A slightly changed dict that allows extending values contained using += """
    def __iadd__(self, other):
        self = joinable_dict(**self, **other)
        return self

from collections import defaultdict
class Style(defaultdict):
    def __init__(self):
        super().__init__(lambda: joinable_dict())
        self.variable = StyleVariableStorage()


    def __str__(self):
        out = ''
        tab = '  '
        for selector, attributes in self.items():
            # out += selector + ' {' + '; '.join(f'{k.replace("_", "-")}: {v}' for k, v in attributes.items()) + ';} '
            out += selector + ' {\n' + tab + f';\n{tab}'.join(f'{k.replace("_", "-")}: {v}' for k, v in attributes.items()) + ';\n}\n\n'
        return out

    def list_variables(self):
        return [x for x in dir(self.variable) if not x.startswith('_')]

    def __setitem__(self, key, value):
        """ This method overload allows for += assignment to simpply add values to the contained dict"""
        super().__setitem__(key, joinable_dict(value))

# There is an issue with asignment not resetting. using = multiple times just appends