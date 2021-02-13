import logging
logging.basicConfig(level=logging.INFO)

class Foo(object):
    def __new__(cls, x, *args, **kwargs):
        self = object.__new__(cls)
        self.x = x
        return self

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs


class LoggedAgeAccess:

    def __get__(self, obj, objtype=None):
        value = obj._age
        logging.info('Accessing %r giving %r', 'age', value)
        return value

    def __set__(self, obj, value):
        logging.info('Updating %r to %r', 'age', value)
        obj._age = value

class Person:

    age = LoggedAgeAccess()             # Descriptor instance

    def __init__(self, name, age):
        self.name = name                # Regular instance attribute
        self.age = age                  # Calls __set__()

    def birthday(self):
        self.age += 1

mary = Person('Mary M', 30)
