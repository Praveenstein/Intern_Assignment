from decimal import Decimal as d
from fractions import Fraction as f
import math
def main():
    # basic numeric data types in python
    print(type(6))
    print(type(6.5))
    print(type(6+7j))
    num=6+7j
    print(isinstance(num, complex))
    #operations using binary, octal, hexadecimal
    print(0b100010010)
    print(0b100010010+0o15)
    print(0b100010010+0xFB)

    #python casting
    print(int(63.7))
    print(float(63))
    print(float('63.26'))

    #using Decimal module to get more precise values
    print(0.1)
    print(d(0.1))
    print(d(202.5624) *d(1235.984316))

    #using fractions module
    print(f('1.1')+f(12,10))
    print(f(-3,5)>0)

    #using math module
    print(math.pi)
    print(math.cos(math.pi))
    print(math.factorial(26))
    print(math.cos(math.pi)+math.sin(math.pi))


if __name__ == '__main__':
    main()
