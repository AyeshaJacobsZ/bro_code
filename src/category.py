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


