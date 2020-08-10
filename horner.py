# -*- coding: utf-8 -*-
""" Horner's method for polynomial evaluation

This script allows the user to evaluate a given polynomial in O(n) time
A polynomial 2x^2 + 3x -1 is given as a list of coefficients as: [2, 3, -1]

This file contains the following function:

    * main - the main function of the script

"""


def main():
    """
    Main function to evaluate the polynomial function
    """

    coef = [1,0,0,-1,-10]
    x = 2

    # The algorithm initializes result as coefficient of x^n, where n is the degree of polynomial and then
    # Repeatedly multiply result with x and add next coefficient to result
    result = coef[0]
    for i in range(1, len(coef)):
        result = (result * x) + coef[i]

    print(f'The function evaluate to : {result} for given x value: {x}')

if __name__ == '__main__':
    main()
