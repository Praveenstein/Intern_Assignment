# -*- coding: utf-8 -*-
"""Balance Checker

This script allows the user to check if the braces in the given string are balanced
The braces could be (), {}, [] or any combination of these

This file contains the following function:

    * main - the main function of the script
"""


def main():
    """
    Main function to Check the balance, using the count of the opening and closing braces
    """

    string = input('Please enter a string: \n')
    if (string.count('(') == string.count(')')) and\
            (string.count('[') == string.count(']')) and\
            (string.count('{') == string.count('}')):
        # All condition satisfied
        print('They are Balanced')
    else:
        print('They are not balanced')


if __name__ == '__main__':
    main()
