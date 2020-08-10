# -*- coding: utf-8 -*-
""" Taylor series expansion of sine function

This script allows the user to expand the taylor series of sine function

This script requires the following packages be installed within the Python
environment you are running this script in:
    * math - To perform mathematical operations such as finding the factorial
    * decimal - To get more precise decimal points

This file contains the following function:

    * main - the main function of the script

"""


import math
from decimal import Decimal as D


def main():
    """
    Main function to find expand the taylor series of sine function
    """

    x = float(input('Please Enter the angle in radians: '))
    n = int(input('Please Enter the Number of Terms: '))

    # Creating a list with each element being the taylor series's terms for sine function Using a
    # Decimal module to get more precision and to work with more terms (as factorial could get really large fast)
    terms = [D(((-1)**p) * (x**((2 * p) + 1)))/D(math.factorial((2 * p) + 1)) for p in range(n)]

    # Finding the sum of all the terms
    value = sum(terms)

    # Printing the output
    print(f'The Value of sine({x}) found using taylors expansion with {n} terms is {round(value, 5)}')

    # Showing the error decreases as the number of terms increases
    # By printing the error with number of terms = 1,2,3 ..... n
    for i in range (n):
        error = round(abs(D(math.sin(x)) - sum(terms[0:i+1])), 7)
        print(f'\nNumber of terms: {i+1} -- Error: {error}\n------------------------------')


if __name__ == '__main__':
    main()
