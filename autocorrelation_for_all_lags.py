# -*- coding: utf-8 -*-
""" Computing autocorrelation for a given signal

This script allows the user to compute the autocorrelation value
of a given signal for lags = 1, 2, 3.....N-2, where N is the length
of the signal

This file contains the following function:

    * main - the main function of the script

"""


def main():
    """
    Main function to find the autocorrelation for lags = 1,2,3.....N-2
    """
    signal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    n = len(signal)
    mean = sum(signal)/n

    # Finding variance - ignoring to  divide by n
    # as it will be cancelled with the n in numerator while calculating the autocorrelation
    variance = sum(map((lambda x: (x - mean)**2), signal))

    # The corrs calculates the autocorrelation for all lags and stores as a list
    #
    # The inner most function lambda-function computes the sum of individual terms
    # that make up the autocorrelation formula and divides it by the variance
    #
    # The map function is used to compute the autocorrelation for all lags using
    # a range function denoting all the lags and the lambda function
    corrs = list(map((lambda k: sum(((signal[i] - mean) * (signal[i+k] - mean)
                                     for i in range(n-k)))/variance),
                     range(1, n-1)))

    # Printing the lag value and corresponding correlation
    print(list(enumerate(corrs, 1)))


if __name__ == '__main__':
    main()
