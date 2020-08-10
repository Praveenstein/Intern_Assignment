# -*- coding: utf-8 -*-
""" Newton-Raphson method for finding the real roots

This script allows the user to find the real roots of
Nth degree polynomial

This script requires that `math` be installed within the Python
environment you are running this script in.

This script requires that `math` be installed within the Python
environment you are running this script in.

This file contains the following function:

    * eval_horner - This function allows the user to evaluate a given polynomial in O(n) time
    * poly_div - This function allows the user to perform synthetic division on polynomials
    * poly_eval - Evaluating a given polynomial and returns it's sign for x= infinity and -infinity
    * no_real_roots - This function allows the user to find the number of real roots
    * newton - Approximate solution of f(x)=0 by Newton's method.
    * main - the main function of the script

"""


import math


def eval_horner(coef, x):
    """Horner's method for polynomial evaluation

    This function allows the user to evaluate a given polynomial in O(n) time

    Parameters
    ----------
    coef : list
        The list which contains the coefficient value.
        A polynomial 2x^2 + 3x -1 is given as a list of coefficients as: [2, 3, -1]

    x : int, float
        The value for which the function needs to be evaluated f(x).

    Returns
    -------
    result : Value -> integer, float
        Implements horner's method to evaluate the given polynomial
    """

    result = coef[0]
    for i in range(1, len(coef)):
        result = (result * x) + coef[i]
    return result


def poly_div(dividend, divisor):
    """Polynomial synthetic division

    This function allows the user to perform synthetic division on polynomials and return the
    quotient and remainder, which will further be used for finding the sturm's sequence

    Parameters
    ----------
    dividend : list
        The list which contains the coefficient value of the dividend polynomial.
        A polynomial 2x^2 + 3x -1 is given as a list of coefficients as: [2, 3, -1]

    divisor : list
        The list which contains the coefficient value of the divisor polynomial.

    Returns
    -------
    result : list
        list of coefficients of the quotient and remainder

    """

    out = list(dividend)
    normalizer = divisor[0]
    for i in range(len(dividend) - (len(divisor) - 1)):
        # For general polynomial division (when polynomials are non-monic),
        # we need to normalize by dividing the coefficient with the divisor's first coefficient
        out[i] /= normalizer
        coef = out[i]
        if coef != 0:
            # In synthetic division, we always skip the first coefficient of the divisor,
            # because it's only used to normalize the dividend coefficients
            for j in range(1, len(divisor)):
                out[i + j] += -divisor[j] * coef

    # The resulting out contains both the quotient and the remainder,
    # the remainder being the size of the divisor (the remainder has necessarily
    # the same degree as the divisor since it's what we couldn't divide from the dividend),
    # so we compute the index where this separation is, and return the quotient and remainder.
    separator = -(len(divisor) - 1)
    return out[:separator], out[separator:]  # return quotient, remainder.


def poly_eval(coef):
    """Evaluating a given polynomial and returns it's sign

    This function allows the user to evaluate a given polynomial for two
    values 'Infinity' and '-Infinity' and returns it's sign to be used by
    sturm sequence for finding the number of real roots

    Parameters
    ----------
    coef : coefficients -> List
        The list which contains the coefficient value.
        A polynomial 2x^2 + 3x -1 is given as a list of coefficients as: [2, 3, -1]

    Returns
    -------
    result_pos, result_neg : string -> Either '+' or '-'
        It uses the eval(coef, x) function to evaluate the given
        polynomial for x = infinity and x = -infinity
    """
    x_pos = math.inf
    x_neg = -math.inf

    # Evaluating the given polynomial for two extremes inf and -inf
    result_pos = eval_horner(coef, x_pos)
    result_neg = eval_horner(coef, x_neg)

    # Assigning the result_neg and result_pos to indicate the sign it evaluated for -inf and inf respectively
    if result_neg > 0:
        result_neg = '+'
    else:
        result_neg = '-'
    if result_pos > 0:
        result_pos = '+'
    else:
        result_pos = '-'

    return result_pos, result_neg


def no_real_roots(coef, dfun_terms):
    """Find the number of real roots using sturm's theorem

    This function allows the user to find the number of real roots
    using sturm's sequence and sturm's theorem

    Parameters
    ----------
    coef : coefficients -> List
        The list which contains the coefficient values.
        A polynomial 2x^2 + 3x -1 is given as a list of coefficients as: [2, 3, -1]
    dfun_terms : coefficients -> List
        The list which contains the coefficient values of the derivative of the given polynomial.

    Returns
    -------
    c2-c1 : number -> Integer
        It uses strum's theorem to find the strum sequence terms
        and then evaluates the sequence over infinity and -infinity
        to find the number of real roots
        c1 is the sign changes over the strum's sequence for infinity
        c2 is the sign changes over the strum's sequence for -infinity
    """

    # Sturm list stores the sequence of sturm terms
    sturm = [coef, dfun_terms]

    # The first two terms of strum's sequence are the function itself and it's derivative
    # The 3rd term is found out by dividing the first term with the second term
    # And multiplied by -1 and so on for the remaining terms until the polynomial has only one term
    while len(sturm[-1]) != 1:
        remainder = poly_div(sturm[-2], sturm[-1])[-1]
        for i in range(len(remainder)):
            remainder[i] = -1 * remainder[i]
        sturm.append(remainder)

    # Eva evaluates all the sturm terms with x= infinity and -infinity and generates a list of sign changes
    # in the strum's sequence
    eva = list(map(poly_eval, sturm))
    pre_eva = eva[0]  # Represents the previous sign of the strum's sequence to count the number of sign changes

    # Counts the number of sign changes in x = infinity (c1)
    # And x = -infinity (c2)
    c1 = 0
    c2 = 0
    for i in range(1, len(eva)):
        if eva[i][0] != pre_eva[0]:
            c1 += 1
        if eva[i][1] != pre_eva[1]:
            c2 += 1
        pre_eva = eva[i]

    return c2 - c1


def newton(f, df, e, n, x0, debug=False):
    """Approximate solution of f(x)=0 by Newton's method.

    Parameters
    ----------
    f : function
        Function for which we are searching for a solution f(x)=0.
    df : function
        Derivative of f(x).
    e : integer, float
        Stopping criteria is abs(x(n+1)-x(n)) < epsilon.
    n : integer
        Maximum number of iterations of Newton's method.
    x0 : integer, float
        Initial guess for a solution f(x)=0.
    debug : boolean
        When set to True prints the following:
            * Iteration number
            * Function value
            * Gradient value
            * Residual error

    Returns
    -------
    xn : number
        Implement Newton's method: compute the linear approximation
        of f(x) at xn and find x intercept by the formula
            x = xn - f(xn)/df(xn)
        Continue until abs(x(n+1)-x(n)) < epsilon and return xn.
        If df(xn) == 0, return None. If the number of iterations
        exceeds max_iter, then return None.
    """

    xn = x0
    for i in range(0, n):
        fxn = f(xn)
        dfxn = df(xn)
        if dfxn == 0:
            print('Zero derivative. No solution found.')
            return None
        nxn = xn - (fxn / dfxn)
        error = abs(xn - nxn)
        if debug:
            print('Iteration: ', i)
            print('Value of Xn: ', round(xn, 5))
            print('Value of Function(Xn) :', round(fxn, 5))
            print('Value of Derivative-Function(Xn) :', round(dfxn, 5))
            print('The residual error :', round(error, 5))
            print('\n-------------------------------------------------\n')

        if error < e:
            return nxn

        xn = nxn

    print('Exceeded maximum iterations')
    return None


def main():
    """
    Main function to Check the balance, using the count of the opening and closing braces
    """

    poly = input('Please enter the coefficients separated by "," ')
    coef = poly.split(',')
    deg = len(coef) - 1
    max_iter = int(input('Please enter the Maximum number of iteration: '))
    stop_value = float(input('Please enter the stopping criteria value: '))
    print('\n-------------------------------------------------\n')

    # Converting the string values of coefficients to float value
    coef = list(map((lambda x: float(x)), coef))

    # Finding the derivative of the given function
    dfun_terms = [coef[i] * (deg - i) for i in range(deg)]

    # Defining the function which returns the evaluated value
    fun = lambda x, coe=coef: sum((coe[i] * (x ** (deg - i)) for i in range(deg + 1)))
    dfun = lambda x, coe=coef: sum((coe[i] * (deg - i) * (x ** (deg - i - 1)) for i in range(deg)))

    # Checking if real roots exist, It is to be noted that a polynomial of odd degree must have
    # atleast one real root, hence we need to check for existence of real roots only for even number degree
    if deg % 2 == 0:
        no_real = no_real_roots(coef, dfun_terms)
        if no_real == 0:
            raise Exception("The polynomial has no real roots")

    # Finding the root with initial value of 2
    x0 = 2
    root = newton(fun, dfun, stop_value, max_iter, x0, True)
    print(f'The root of the equation is : {root}')


if __name__ == '__main__':
    main()
