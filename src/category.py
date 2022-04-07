import pandas as pd
import numpy as np

"""
Category class:
- gets cleaned data 0
- places ducts into categories using size columns 0
- calculates total m^2 for that category in that duct file 0
- calculates total amount in R for BOQ (either dictionary or dataframe format) 0
- information gets passed to BOQ 0
"""


class Category:
    """
    Gets cleaned data in the category, whole row
    Distributes data into categories
    Calculates sum to be put into csv and xlsx
    maybe category inherits form Duct? - for any duct dataset it can do anything, but for specific
    category it could do something specific?
    """

    def __init__(self, data):
        self.data = data

    def get_categories(self, width, height):

        maximum = max(width, height)
        addition = width + height
        if maximum < 750 and addition <= 1150:
            category = 'category_1'
        elif maximum < 750 and addition > 1150:
            category = 'category_2'
        elif 750 <= maximum < 1350:
            category = 'category_3'
        elif 1350 <= maximum < 2100:
            category = 'category_4'
        elif 2100 <= maximum:
            category = 'category_5'

        return category

    def sort_data_into_categories(self, data):
        data['category'] = data.apply(lambda x: self.get_categories(x['min_width'], x['min_height']), axis=1)
        return data

    def sum_area_in_categories(self, data):
        summed_categories = data[['Area', 'category']].groupby(['category']).sum()
        return summed_categories



