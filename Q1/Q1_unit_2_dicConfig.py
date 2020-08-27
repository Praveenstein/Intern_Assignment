# -*- coding: utf-8 -*-
""" Class to store Units and perform conversion

This script requires that `logging` be installed within the Python
environment you are running this script in.
"""
import logging
import json
from os import path
import logging.config


class Unit:
    """It represents the physical unit
         It has the following methods
                *convert(): It converts the given unit of quantity to the specified one
    """

    # Units of time
    SECONDS = "seconds"
    MINUTES = "minutes"
    HOURS = "hours"

    # Units of length
    METER = "meter"
    KILOMETER = "kilometer"
    INCH = "inch"
    FOOT = "foot"
    CENTIMETER = "centimeter"

    # Units of mass
    GRAM = "gram"
    KILOGRAM = "kilogram"
    MILLIGRAM = "milligram"
    TONNE = "tonne"

    # Temperature
    KELVIN = "kelvin"
    CELSIUS = "celsius"

    # Custom Units
    ONE = "one"
    NEW = "new"

    def __init__(self, value, unit, conversion_data):

        if unit == self.__class__.CELSIUS:
            if value < -273.15:
                logger.error("Celsius cannot be below -273.15", exc_info=True)
                raise Exception("Celsius cannot be below -273.15")
            else:
                self.value = value
                self.unit = unit
                self.conversion_data = conversion_data
        elif value < 0:
            logger.error(f"{unit} cannot be below 0", exc_info=True)
            raise Exception(f"{unit} cannot be below 0")
        else:
            self.value = value
            self.unit = unit
            self.conversion_data = conversion_data

    def convert(self, to_unit):
        """

        :param to_unit: The conversion unit
        :return Unit: New instance of the unit class with value and unit equal to the conversion
        """
        if self.unit == to_unit:
            logger.info("Same Unit Conversion")
            return Unit(self.value, self.unit, self.conversion_data)
        try:
            coef = self.conversion_data[self.unit][to_unit]
            result = coef[0]

            for i in range(1, len(coef)):
                result = (result * self.value) + coef[i]

            logger.info("Successfully Converted")
            return Unit(result, to_unit, self.conversion_data)
        except Exception:
            logger.error("Unit conversion not compatible", exc_info=True)

    def __str__(self):
        return f"{self.value}-{self.unit}"


def log():
    """
    Creates a custom logger from the configuration dictionary
    """
    with open('UnitsLog.json', 'r') as f:
        config = json.load(f)
        logging.config.dictConfig(config)
    global logger
    logger = logging.getLogger(__name__)


def main():
    """
        Main function to store units
    """
    log()

    file = 'conversion.json'
    if not path.exists(file):
        logger.error("The given file does not exist")
        return
    with open(file) as f:
        data = json.load(f)
    try:
        g = Unit(273.15, Unit.GRAM, data)
        print(g)
        Tk = g.convert(g.KELVIN)
        print(Tk)
    except Exception:
        logger.error("Error Occurred", exc_info=True)


if __name__ == '__main__':
    main()
