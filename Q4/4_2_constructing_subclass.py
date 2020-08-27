# -*- coding: utf-8 -*-
"""
Constructing an instance of subclass given an instance of superclass

This file contains the following class:

    * Class A - This is a superclass which will be inherited by class B
    * Class B - This is a subclass which inherits class A

"""


class A:
    # SuperClass
    def __str__(self):
        return 'This is class A'


class B(A):
    # SubClass
    def __str__(self):
        return 'This is class B'
    pass


class C(A):
    # SubClass
    def __str__(self):
        return 'This is class B'
    pass


def main():
    # Given an instance of A (SuperClass),
    # Constructing an instance of B (SubClass)
    a = A()

    sub = a.__class__.__subclasses__()[0]
    b = sub()
    print(b)
    print(type(b))


if __name__ == '__main__':
    main()
