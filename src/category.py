import pandas as pd
import numpy as np

"""
Category class:
- gets cleaned data
- places ducts into categories using size columns
- calculates total m^2 for that category in that duct file
- calculates total amount in R for BOQ (either dictionary or dataframe format)
- information gets passed to BOQ 
"""


class Category:
    """
    Gets cleaned data in the category, whole row
    Distributes data into categories
    Calculates sum to be put into csv and xlsx
    maybe category inherits form Duct? - for any duct dataset it can do anything, but for specific
    category it could do something specific?
    """

    def __init__(self, category_number, data):
        self.category_number = category_number  # for if x.category_number == 1, cost..
        self.data = data

    def convert_to_float(self):
        """
        Might have to go in clean data/duct class
        :return:
        """
        self.data["Area"] = self.data["Area"].map(lambda x: float(str(x)[:-3]))
        self.data["Count"] = self.data["Count"].map(lambda x: float(str(x)))
        self.data["Surface Area"] = self.data["Surface Area"].map(lambda x: float(str(x)[:-3]))

        return self.data

    def get_calculated_area(self, count, area, surface_area):
        """
        Move to duct
        :param count:
        :param area:
        :param surface_area:
        :return:
        """
        if area != 0:
            calculated_area = area * count
        else:
            calculated_area = surface_area * count

        return calculated_area

    def calculate_total_area(self):
        """
        Move to duct
        :return:
        """
        self.data = self.convert_to_float()
        self.data['Calculated Area m^2'] = self.data.apply(
            lambda x: self.get_calculated_area(x['Count'], x['Area'], x['Surface Area']),
            axis=1)
        return self.data

