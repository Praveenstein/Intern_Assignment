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
import argparse


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

    for file in files:

        index = file.find('_')
        date = file[: index]
        if '-' in date:
            separator = '-'
        else:
            separator = '_'
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


def grouping(directories):
    """Finding Files with same date prefix and grouping them

        Parameters
        ----------
        directories : list
                Accepts a list of directories across which the files needs to be grouped

        Returns
        -------
        group_dic : dict
            It returns a dictionary with key value equal to unique date values
            and values equal to a list of file directories that have same date prefix as the key
    """

    group_dic = {}

    for directory in directories:

        files = os.listdir(directory)
        if len(files) == 0:
            continue
        csv_files = [files[i] for i in range(len(files)) if files[i].endswith('.csv')]

        # Finding the format of files in the given directory
        file_format = format_finder(csv_files)

        for file in csv_files:

            separator_index = file.find('_')

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

    if not group_dic:
        raise Exception("All Files are Empty")

    return group_dic


def move(group_dic, output_parent_dir):
    """Moving the files with same date to a new directory

        Parameters
        ----------
        group_dic : dict
                Its a dictionary with key value equal to unique date values and values equal
                 to a list of file directories that have same date prefix as the key
        output_parent_dir : str
                It contains a string of the parent directory

    """

    for key, values in group_dic.items():
        path = os.path.join(output_parent_dir, key.strftime("%Y-%m-%d"))
        if not os.path.isdir(path):
            os.mkdir(path)
        for item in values:
            if os.path.samefile(os.path.dirname(item), path):
                continue
            shutil.move(item, path)


def main():
    """ Main function to find group files into directory """

    my_parser = argparse.ArgumentParser(allow_abbrev=False)
    my_parser.add_argument('--input', action='store', type=str, required=True)
    my_parser.add_argument('--output', action='store', type=str, required=True)

    args = my_parser.parse_args()
    if (not os.path.isabs(args.input)) or (not os.path.isabs(args.output)):
        raise Exception("Please Enter only absolute path of the directory")
    parent_dir = args.input

    if not (os.path.isdir(parent_dir)):
        raise Exception("The Input directory doesn't exist")

    if not (os.path.isdir(args.output)):
        raise Exception("The Output directory doesn't exist")

    directories = []

    for directory in os.listdir(parent_dir):
        directories.append(os.path.join(parent_dir, directory))

    # The group_dic represents the dictionary with keys equal to the unique dates in the directories
    # And the values represent a list of all files that have the same date prefix across the data_dumps
    group_dic = grouping(directories)

    # Moving Files into New Directory
    move(group_dic, args.output)
    print("Files Moved Successfully")


if __name__ == '__main__':
    main()
