# -*- coding: utf-8 -*-
""" Dumping csv file
This script allows the user to dump bunch of synthetically generated csv file to a given directory
This file contains the following function:

    * main - the main function of the script


"""
# Built-In functions
import random
import os
from datetime import timedelta, date as dt



def main():
    """ Main function to dump csv file """

    directory = 'D:\\Profession\\Intern\\Assignments\\Codes\\Assignement Codes\\Part 2\\data_dumps'
    para = input('Please enter the start date, month, year and end date, month, year: \n')
    para = para.split(',')
    para = list(map(lambda x: int(x), para))
    date_format = input("Enter the date format: \n")
    dump = int(input("Enter the Dump Number: \n"))

    path = os.path.join(directory, 'dump_' + str(dump))
    if not (os.path.exists(path)):
        os.mkdir(path)

    start_dt = dt(year=para[2], month=para[1], day=para[0])
    end_dt = dt(year=para[5], month=para[4], day=para[3])
    d = end_dt - start_dt
    DAYS = [(start_dt + timedelta(n)).strftime(date_format) for n in range(d.days + 1)]

    for date in DAYS:
        file_name1 = path + '\\' + date + '_file' + str((dump*2)-1) + '.csv'
        file_name2 = path + '\\' + date + '_file' + str((dump*2)) + '.csv'

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