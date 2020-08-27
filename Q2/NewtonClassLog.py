# -*- coding: utf-8 -*-
""" Newton-Raphson method for finding the real roots

This script allows the user to find the real roots of
Nth degree polynomial

This script requires that `math` be installed within the Python
environment you are running this script in.

This file contains a class of name Newton with the following methods:

    * eval_horner - This function allows the user to evaluate a given polynomial in O(n) time
    * poly_div - This function allows the user to perform synthetic division on polynomials
    * poly_eval - Evaluating a given polynomial for x= infinity and -infinity and returns it's sign
    * no_real_roots - This function allows the user to find the number of real roots
    * newton - Approximate solution of f(x)=0 by Newton's method.
    * main - the main function of the script

"""

import math
import logging
import argparse
import json
import logging.config
import yaml


class Newton:

    def __init__(self, max_iter: int, stop_value: float, coef: list):
        self.coef = coef
        self.stop_value = stop_value
        self.max_iter = max_iter
        self.deg = len(coef) - 1
        self.dfun_terms = [coef[i] * ((len(coef) - 1) - i) for i in range((len(coef) - 1))]
        self.data = []

    @staticmethod
    def _eval_horner(coefficients, x):
        """Horner's method for polynomial evaluation

        This function allows the user to evaluate a given polynomial in O(n) time

        Parameters
        ----------
        coefficients : list
            The list which contains the coefficient value.
            A polynomial 2x^2 + 3x -1 is given as a list of coefficients as: [2, 3, -1]

        x : int, float
            The value for which the function needs to be evaluated f(x).

        Returns
        -------
        result : integer, float
            Implements horner's method to evaluate the given polynomial
        """

        _result = coefficients[0]
        for i in range(1, len(coefficients)):
            _result = (_result * x) + coefficients[i]
        return _result

    @staticmethod
    def _poly_div(dividend, divisor):
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

        _out = list(dividend)
        _normalizer = divisor[0]
        for i in range(len(dividend) - (len(divisor) - 1)):
            # For general polynomial division (when polynomials are non-monic),
            # we need to normalize by dividing the coefficient with the divisor's first coefficient
            _out[i] /= _normalizer
            _coef = _out[i]
            if _coef != 0:
                # In synthetic division, we always skip the first coefficient of the divisor,
                # because it's only used to normalize the dividend coefficients
                for j in range(1, len(divisor)):
                    _out[i + j] += -divisor[j] * _coef

        # The resulting out contains both the quotient and the remainder,
        # the remainder being the size of the divisor (the remainder has necessarily
        # the same degree as the divisor since it's what we couldn't divide from the dividend),
        # so we compute the index where this separation is, and return the quotient and remainder.
        _separator = -(len(divisor) - 1)
        return _out[:_separator], _out[_separator:]  # return quotient, remainder.

    def _poly_eval(self, poly):
        """Evaluating a given polynomial and returns it's sign

        This function allows the user to evaluate a given polynomial for two
        values 'Infinity' and '-Infinity' and returns it's sign to be used by
        sturm sequence for finding the number of real roots

        Parameters
        ----------
        poly : coefficients -> List
            The list which contains the coefficient value.
            A polynomial 2x^2 + 3x -1 is given as a list of coefficients as: [2, 3, -1]

        Returns
        -------
        result_pos, result_neg : string -> Either '+' or '-'
            It uses the eval(coef, x) function to evaluate the given
            polynomial for x = infinity and x = -infinity
        """
        _x_pos = math.inf
        _x_neg = -math.inf

        # Evaluating the given polynomial for two extremes inf and -inf
        _result_pos = self._eval_horner(poly, _x_pos)
        _result_neg = self._eval_horner(poly, _x_neg)

        # Assigning the result_neg and result_pos to indicate the sign it evaluated for -inf and inf respectively
        if _result_neg > 0:
            _result_neg = '+'
        else:
            _result_neg = '-'
        if _result_pos > 0:
            _result_pos = '+'
        else:
            _result_pos = '-'

        return _result_pos, _result_neg

    def _no_real_roots(self) -> int:
        """Find the number of real roots using sturm's theorem

        This function allows the user to find the number of real roots
        using sturm's sequence and sturm's theorem


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
        _sturm = [self.coef, self.dfun_terms]

        # The first two terms of strum's sequence are the function itself and it's derivative
        # The 3rd term is found out by dividing the first term with the second term
        # And multiplied by -1 and so on for the remaining terms until the polynomial has only one term
        while len(_sturm[-1]) != 1:
            _remainder = self._poly_div(_sturm[-2], _sturm[-1])[-1]
            for i in range(len(_remainder)):
                _remainder[i] = -1 * _remainder[i]
            _sturm.append(_remainder)

        # Eva evaluates all the sturm terms with x= infinity and -infinity and generates a list of sign changes
        # in the strum's sequence
        _eva = list(map(self._poly_eval, _sturm))
        _pre_eva = _eva[0]  # Represents the previous sign of the strum's sequence to count the number of sign changes

        # Counts the number of sign changes in x = infinity (c1)
        # And x = -infinity (c2)
        _c1 = 0
        _c2 = 0
        for i in range(1, len(_eva)):
            if _eva[i][0] != _pre_eva[0]:
                _c1 += 1
            if _eva[i][1] != _pre_eva[1]:
                _c2 += 1
            _pre_eva = _eva[i]

        return _c2 - _c1

    def _newton(self):
        """Approximate solution of f(x)=0 by Newton's method.

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

        xn = 2
        for i in range(0, self.max_iter):
            fxn = self._eval_horner(self.coef, xn)
            dfxn = self._eval_horner(self.dfun_terms, xn)
            if dfxn == 0:
                print('Zero derivative. No solution found.')
                return None
            _nxn = xn - (fxn / dfxn)
            error = abs(xn - _nxn)
            info_ = {"Value of Xn": round(xn, 5), "Value of Function(Xn)": round(fxn, 5),\
                     "Value of Derivative-Function(Xn)": round(dfxn, 5), "The residual error": round(error, 5)}
            self.data.append(info_)

            if error < self.stop_value:
                return _nxn

            xn = _nxn

        print('Exceeded maximum iterations')
        return None

    def solve(self):
        """
        Solves the Given polynomial and prints out it's roots
        """
        if self.deg % 2 == 0:
            _no_real = self._no_real_roots()
            if _no_real == 0:
                raise Exception("The polynomial has no real roots")

        root = self._newton()
        print(f'The root of the equation is : {round(root, 5)}')

    def __str__(self):
        _data = ""
        for i in range(len(self.data)):
            _data += f"\nIteration: {i}\n"
            for keys, values in self.data[i].items():
                _data += f"{keys}: {values}\n"
            _data += "----------------------------------------"

        return _data


def get_data(file):
    """
    This function uses the argparse module to get the filename consisting of the
    parameters required for creating the Newton class

    :return dic data: returns a dictionary containing the parameters required for
    """

    try:
        with open(file) as f:
            data = json.load(f)
        return data
    except ValueError:
        logger.error("Incorrect Type of Input", exc_info=True)
        raise Exception("Incorrect Type of Input")


def log():
    """
    Creates a custom logger from the configuration dictionary
    """
    with open('Newton.json', 'r') as f:
        config = json.load(f)
        logging.config.dictConfig(config)
    global logger
    logger = logging.getLogger(__name__)


def main():
    """
    Main function to find the solution of an equation
    """
    log()
    data = get_data("data.json")

    print('\n-------------------------------------------------\n')

    newton = Newton(**data)
    try:
        newton.solve()
        logger.info("Successfully Solved")
    except Exception:
        logger.error("Error Occurred", exc_info=True)
        return

    print("\n-------------------------------------------------\n")
    print(newton)


if __name__ == '__main__':
    main()
