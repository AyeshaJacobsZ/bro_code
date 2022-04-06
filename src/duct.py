import pandas as pd
import os
import glob
import numpy as np

# when duct is instantiated it immediately cleans the data ready to categorize
# maybe need to keep total column for unit testing

"""
Duct class: 
- reads data
- cleans data
- gets sizes
- gets total area needed for calculation
- data gets pased to Category
"""


class Duct:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.read_data()
        # need to save filename of that class and use when writing BOQ (append BOQ to front)

    def read_data(self):
        path = os.getcwd()
        data = pd.read_csv(f"{path}\\data\\{self.filename}")
        data = self.clean_data(data)
        return data

    def clean_data(self, data):
        data = data[data["Insulation Type"].notna()]
        return data


