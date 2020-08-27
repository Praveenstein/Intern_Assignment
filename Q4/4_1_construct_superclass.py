# -*- coding: utf-8 -*-
"""
Constructing an instance of superclass given an instance of subclass

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


def main():
    # Given an instance of B (Subclass),
    # Constructing an instance of A (SuperClass)
    b = B()     # Given SubClass

    base = b.__class__.__base__
    a = base()
    print(a)
    print(type(a))


if __name__ == '__main__':
    main()
