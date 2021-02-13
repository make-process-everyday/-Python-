import functools


class Person(object):
    def __init__(self, age):
        self.age = age

    def add(self, a, b):
        return self.age + a + b  # 在原来年纪上面加上a,b两个数

    age_01 = functools.partialmethod(add, a=3)  # 先给a绑定一个参数
    age_02 = functools.partialmethod(add, a=3, b=4)  # 先给a b都绑定一个参数


p = Person(10)
age1 = p.age_01(b=4)
age2 = p.age_02()
print(age1)
print(age2)

class Foo(object):
    """docstring for Foo"""

    def __init__(self, arg=''):
        super(Foo, self).__init__()
        self.arg = arg

    def foo(self):
        print(self)
        print('foo:', 123)


# print(Foo.foo.__get__(Foo(), Foo)())
# print(Foo.__dict__['foo'].__get__(Foo(), Foo)())
#
# c = Foo()
# print(Foo.foo.__get__(c, Foo)())