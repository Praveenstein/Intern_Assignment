# -*- coding: utf-8 -*-
""" Grouping files into a directory
This script allows the user to group the csv files in a given directory
based on the date prefixed to the file

This script requires the following packages be installed within the Python
environment you are running this script in:
    * os - The os module gives useful methods to manipulate files and directories.
    * shutil - The shutil module offers a number of high-level operations on files and collections of files.
    * dateparser - The dateparser parses localized dates in almost any string formats.

This file contains the following function:

    * format_finder - The function which accepts a list of files with date as prefix and returns the date format
    * main - the main function of the script


"""

# Build-In modules
import os
import shutil

# 3rd party modules
import dateparser


def format_finder(files):
    """Finding the date format of files in a directory

        Parameters
        ----------
        files : list
                Accepts a list of file names as string

        Returns
        -------
        format : str, None
            If the file contains date format which is not of decimal then it will return None
            since these dateformats can be read directly by the date parser (Eg: Aug_15_2020)
            If it contains only decimal then it goes through all the elements to find the date format
            and return it as string (Eg: 2020-08-25 -> '%Y-%m-%d')
        """

    file_format = ['%Y', '%m', '%d']
    year = ''
    month = ''
    da = ''
    separators = ['~', '-', '_', '-']

    for file in files:

        # This loop is to find the index which separates the date prefix from the filename
        # And to find the separator character in the date prefix
        count = 0
        for char in range(len(file)):
            if file[char] in separators:
                count += 1
                if count == 1:
                    separator = file[char]
                if count == 3:
                    index = char

        date = file[: index]
        date = date.split(separator)

        for d in range(len(date)):

            # If the date doesn't contain decimal (Eg: August) then it would return None
            if not date[d].isdecimal():
                return None

            # If the element in the date is of length greater then 2 then it would be a year (Eg: 2020)
            # And that value is set as the index of year
            if len(date[d]) > 2:
                year = d

            # If the integer of element in the date is of length greater then 12 then it would be a date (Eg: 25)
            # And that value is set as the index of date
            elif int(date[d]) > 12:
                da = d

            # If Both year and date are set, then the correct index for the month would be 3- (year+date)
            # Eg: 3 -(0+1)
            if (year != '') and (da != ''):
                month = 3 - (year + da)
                break

        # If Month is set, then we change the format according to their set value
        # Eg: format = ['%Y', '%m', '%d'], and year = 1, da = 0, month = 2
        # Then format[year=1] = '%Y'
        # Then format[da=0] =  '%d'
        # Then format[month=2] = '%m'
        # format = ['%d', '%Y', '%m']
        if month:
            file_format[year] = '%Y'
            file_format[month] = '%m'
            file_format[da] = '%d'
            break
    else:
        # The script executes this only if none of the files had an date element( Which is not year)
        # That was greater than 12, Eg: 2020-06-10
        # Meaning that we cannot know for sure which element represents the date/month
        # Hence we arbitrarily assign one element as date and another as month
        if year != 0:
            # If the index of year is zero, we let the format to be same as it was assigned first
            # Else we arbitrarily assign '0' th index to month
            file_format[year] = '%Y'
            file_format[0] = '%m'
            file_format[3 - year] = '%d'
    return f'{file_format[0]}-{file_format[1]}-{file_format[2]}'


def main():
    """ Main function to find group files into directory """
    parent_dir = 'D:\\Profession\\Intern\\Assignments\\Codes\\Assignement Codes\\Part 2\\data_dumps'

    if not (os.path.isdir(parent_dir)):
        raise Exception("The directory doesn't exist")

    directories = []

    for directory in os.listdir(parent_dir):
        directories.append(os.path.join(parent_dir, directory))

    # The group_dic represents the dictionary with keys equal to the unique dates in the directories
    # And the values represent a list of all files that have the same date prefix across the data_dumps
    group_dic = {}
    separators = ['~', '-', '_', '-']

    for directory in directories:

        files = os.listdir(directory)
        csv_files = [files[i] for i in range(len(files)) if files[i].endswith('.csv')]

        # Finding the format of files in the given directory
        file_format = format_finder(csv_files)

        for file in csv_files:

            count = 0

            # Looping over the filename characters to get the index of the separator which separates
            # the filename and the date prefix
            for char in range(len(file)):
                if file[char] in separators:
                    count += 1
                    if count == 3:
                        # A given date prefix cannot have more than three separators
                        # and hence the 3rd separator would be the separator between the filename
                        # and the date prefix, Eg: 2020-08-16_file1.csv (The third separator is '_')
                        separator_index = char
                        break
            else:
                raise Exception('Improper File Naming')

            # Extracting the date prefix alone from the filename
            date = file[: separator_index]

            # If the file format returned by the format_finder is None, meaning it has non decimal characters
            # These formats could be directly passed to dateparser to get the datetime object
            if file_format is None:
                date = dateparser.parse(date).date()
            else:
                # If the format returned is not None, then that needs to be passed as argument in the dateparser
                date = dateparser.parse(date, date_formats=[file_format]).date()

            # If the date obtained is not in the keys, then it is created with value as a list of the directory
            # of the file, if it is in the key, the the value is update by appending it
            if not (date in group_dic.keys()):
                group_dic[date] = [os.path.join(directory, file)]
            else:
                group_dic[date].append(os.path.join(directory, file))

    # Moving Files into New Directory
    for key, values in group_dic.items():
        path = os.path.join(parent_dir, str(key))
        os.mkdir(path)
        for item in values:
            shutil.move(item, path)


if __name__ == '__main__':
    main()
