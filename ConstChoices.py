# coding=utf8



import six

class ChoicesMetaclass(type):
    def __new__(cls, name, bases, attrs):
        choices = []
        values = {}
        ks = []
        for k, v in six.iteritems(attrs):
            if k.isupper() and not k.startswith('_'):
                if isinstance(v, tuple) and len(v) == 2:
                    pass
                else:
                    v = v, v
                ks.append(k)
                choices.append(v)
                values[v[0]] = v[1]
                attrs[k] = v[0]
        attrs['choices'] = choices
        attrs['values'] = values
        return type.__new__(cls, name, bases, attrs)


class ConstChoices(six.with_metaclass(ChoicesMetaclass)):
    @classmethod
    def is_valid(cls, value):
        return value in cls.values

    @classmethod
    def get_value_display(cls, value):
        return cls.values.get(value)
