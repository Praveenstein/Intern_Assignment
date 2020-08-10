# -*- coding: utf-8 -*-
""" Finding the closest number

This script allows the user to find the closest number
to a given positive integer N, that could be expressed
as 2^p

This script requires that `math` be installed within the Python
environment you are running this script in.

This file contains the following function:

    * main - the main function of the script

"""


import math


def main():
    """
    Main function to find the closest number that could be expressed as 2^p
    """
    n = int(input("Please enter a positive integer"))

    # using log base2 to find the approximate p value
    x = (math.log2(n)) // 1

    # finding the possible values 1 & 2
    p1 = 2 ** x
    p2 = 2 ** (x+1)

    # finding the difference between the possible values and the given number
    difference1 = abs(p1 - n)
    difference2 = abs(p2 - n)

    # Assigning the closest value and p based upon the differences
    if difference1 <= difference2:
        closest = p1
        p = x
    else:
        closest = p2
        p = x+1

    # printing the output
    print(f'The closest Value to the Given Positive Integer {n} is {closest} and could be expressed as 2^{p} : ')


if __name__ == '__main__':
    main()
