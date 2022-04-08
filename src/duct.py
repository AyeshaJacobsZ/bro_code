import pandas as pd
import os
import glob
import numpy as np

# when duct is instantiated it immediately cleans the data ready to categorize
# maybe need to keep total column for unit testing

"""
Duct class: 
- cleans data 1
- gets sizes 0
- gets total area needed for calculation 1
- data gets pased to Category 0
"""


class Duct:
    def __init__(self):
        pass
        # self.keys = []
        # self.folder_location = folder_location
        # self.data = self.read_data()


    def convert_to_float(self, data):
        data["Area"] = data["Area"].map(lambda x: float((str(x).replace("m\u00b2", ""))))
        data["Surface Area"] = data["Surface Area"].map(lambda x: float((str(x).replace("m\u00b2", ""))))
        data["Count"] = data["Count"].map(lambda x: float(x))

        return data

    def clear_nan_rows(self, data):
        data = data[data["Insulation Type"].notna()]
        return data

    def get_calculated_area(self, count, area, surface_area):
        calculated_area = area * count if area != 0 else surface_area * count
        return calculated_area

    def split_size(self, data):
        split_size = data['Size'].str.split('[x|-]', expand=True)
        cols = len(split_size.columns)
        while cols < 6:
            split_size[cols] = np.nan
            split_size[cols + 1] = np.nan
            cols = cols + 2
        split_size.columns = ['width_1', 'height_1', 'width_2', 'height_2', 'width_3', 'height_3']
        split_size = split_size.astype(float)

        return pd.concat([data, split_size], axis=1)

    def get_minimum_width_and_height(self, data):
        data = self.split_size(data)
        data['min_width'] = data.loc[:, ['width_1', 'width_2', 'width_3']].min(axis=1)
        data['min_height'] = data.loc[:, ['height_1', 'height_2', 'height_3']].min(axis=1)

        return data

    def calculate_total_area(self, data):
        data = self.convert_to_float(data)
        data['Calculated Area m\u00b2'] = data.apply(
            lambda x: self.get_calculated_area(x['Count'], x['Area'], x['Surface Area']),
            axis=1)

        return data


