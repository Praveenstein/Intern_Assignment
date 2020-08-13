# -*- coding: utf-8 -*-
""" Dumping txt file
This script allows the user to dump bunch of synthetically generated txt file to a given directory
This file contains the following function:

    * main - the main function of the script


"""

import os


def main():
    """ Main function to dump txt file """

    directory = 'D:\\Profession\\Intern\\Assignments\\Codes\\Assignement Codes\\Part 2\\data_dumps'
    path = os.path.join(directory, 'dump_3')
    if not (os.path.exists(path)):
        os.mkdir(path)

    for date in range(1, 31):
        # date-month-year
        # file_name1 = path + '\\' + str(date) + '-8-2020' + '_file1.txt'

        # year-month-date
        # file_name1 = path + '\\' + '2020-08-' + str(date) + '_file3.txt'

        # month_year_date
        file_name1 = path + '\\' + 'Aug_2020_' + str(date) + '_file5.txt'

        # date-month-year
        # file_name2 = path + '\\' + str(date) + '-8-2020' + '_file2.txt'

        # year-month-date
        # file_name2 = path + '\\' + '2020-08-' + str(date) + '_file4.txt'

        # month_year_date
        file_name2 = path + '\\' + 'Aug_2020_' + str(date) + '_file6.txt'

        rows = []
        for row in range(100):
            string = 'asddfgfhgkhjghkweoriuywoipywbnxvnmznvnmbatr'
            rows.append(string)
        with open(file_name1, 'w') as f1, open(file_name2, 'w') as f2:
            f1.writelines(rows)
            f2.writelines(rows)


if __name__ == '__main__':
    main()
