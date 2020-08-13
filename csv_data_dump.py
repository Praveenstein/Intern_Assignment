# -*- coding: utf-8 -*-
""" Dumping csv file
This script allows the user to dump bunch of synthetically generated csv file to a given directory
This file contains the following function:

    * main - the main function of the script


"""
# Built-In functions
import random
import os


def main():
    """ Main function to dump csv file """

    directory = 'D:\\Profession\\Intern\\Assignments\\Codes\\Assignement Codes\\Part 2\\data_dumps'
    path = os.path.join(directory, 'dump_1')
    if not (os.path.exists(path)):
        os.mkdir(path)

    for date in range(1, 31):
        # date-month-year
        file_name1 = path + '\\' + str(date) + '-8-2020' + '_file1.csv'

        # year-month-date
        # file_name1 = path + '\\' + '2020-08-' + str(date) + '_file3.csv'

        # month_year_date
        # file_name1 = path + '\\' + 'Aug_2020_' + str(date) + '_file5.csv'

        # date-month-year
        file_name2 = path + '\\' + str(date) + '-8-2020' + '_file2.csv'

        # year-month-date
        # file_name2 = path + '\\' + '2020-08-' + str(date) + '_file4.csv'

        # month_year_date
        # file_name2 = path + '\\' + 'Aug_2020_' + str(date) + '_file6.csv'

        rows = []
        for row in range(100):
            string = ''
            for i in range(10):
                if i == 9:
                    string += str(random.randint(1, 100)) + '\n'
                else:
                    string += str(random.randint(1, 100)) + ','
            rows.append(string)
        with open(file_name1, 'w') as f1, open(file_name2, 'w') as f2:
            f1.writelines(rows)
            f2.writelines(rows)


if __name__ == '__main__':
    main()