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

    string = input('Please enter the string:\n')
    stack = []
    open_bracket = ['(', '[', '{']
    close_bracket = [')', ']', '}']
    for char in string:
        if char in open_bracket:
            stack.append(char)
        elif char in close_bracket:
            if ((len(stack) > 0) and
                    open_bracket[close_bracket.index(char)] == stack[-1]):
                stack.pop()
            else:
                print('Unbalanced')
                return
        else:
            continue

    if len(stack) == 0:
        print('Balanced')
    else:
        print('Unbalanced')


if __name__ == '__main__':
    main()
