# -*- coding: utf-8 -*-
"""
Constructing an instance of class without explicitly calling the class constructor

This script requires that `Json` be installed within the Python
environment you are running this script in.

This file contains the following class:

    * Student - This class represent a students data such as age, name

This file contains the following function:

    * creator - This class represent a students data such as age, name
"""

import json
import logging
from os import path


class Student:
    """It represents a students data """

    def __init__(self, name, age, roll_number):
        self.roll_number = roll_number
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old and his roll number is {self.roll_number}"


def creator(dic):
    """This function will be used as object hook by the json-loads function
    Parameters
    ----------
    dic : dict
         A dictionary in json format which contains the instances attributes

    Returns
    -------
    Student(**dic) : object
        It instantiates the student class and returns it to the json-loads
    """
    return Student(**dic)


def main():
    """
    Main function to find the solution of an equation
    """
    #data = {"name": "Rahul", "age": 24, "roll_number": 42}
    file = 'student.json'
    if not path.exists(file):
        raise Exception("The given file does not exist")
        return
    with open(file) as f:
        data = json.load(f)

    data = json.dumps(data)
    try:
        student = json.loads(data, object_hook=creator)
        print("Successfully Created Student")
        print(student)
    except Exception:
        raise Exception("Error Occurred")


    #for student in students:
    #    print(student)


if __name__ == '__main__':
    main()
