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
    def __init__(self, folder_location):
        # self.keys = []
        self.folder_location = folder_location
        self.data = self.read_data()

    def read_data(self):
        path = os.getcwd()
        files = glob.glob(self.folder_location + '\*.csv')
        duct = {}
        for file in files:
            key = file.replace(f"{path}\\data\\", "")
            # self.keys.append(key)
            data = pd.read_csv(file)
            data = self.clear_nan_rows(data)
            data = self.convert_to_float(data)
            data = self.calculate_total_area(data)
            duct[key] = data
        return duct

    def convert_to_float(self, data):

        data["Area"] = data["Area"].map(lambda x: float((str(x).replace("m\u00b2", ""))))
        data["Surface Area"] = data["Surface Area"].map(lambda x: float((str(x).replace("m\u00b2", ""))))
        data["Area"] = data["Area"].map(lambda x: float(x))

        return data

    def clear_nan_rows(self, data):
        data = data[data["Insulation Type"].notna()]
        return data

    def get_calculated_area(self, count, area, surface_area):

        if area != 0:
            calculated_area = area * count
        else:
            calculated_area = surface_area * count

        return calculated_area

    def calculate_total_area(self, data):

        data = self.convert_to_float(data)
        data['Calculated Area m\u00b2'] = data.apply(
            lambda x: self.get_calculated_area(x['Count'], x['Area'], x['Surface Area']),
            axis=1)

        return data

