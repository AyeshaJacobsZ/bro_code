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
    def __init__(self, folder_location):
        # self.keys = []
        self.folder_location = folder_location
        self.data = self.read_data()


    def convert_to_float(self, data):
        data["Area"] = data["Area"].map(lambda x: float((str(x).replace("m\u00b2", ""))))
        data["Surface Area"] = data["Surface Area"].map(lambda x: float((str(x).replace("m\u00b2", ""))))
        data["Count"] = data["Count"].map(lambda x: float(x))

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

    def split_size(self, data):
        needed_cols = data['Size']
        split_size = needed_cols.str.split('[x|-]', expand=True)

        cols = len(split_size.columns)

        while cols < 6:
            split_size[cols] = np.nan
            split_size[cols + 1] = np.nan
            cols = cols + 2

        # split_size = pd.DataFrame()
        split_size.columns = ['width_1', 'height_1', 'width_2', 'height_2', 'width_3', 'height_3']

        # converting data type to float
        split_size_float = split_size.astype(float)

        # getting min width and height
        split_size_float['min_width'] = split_size_float.iloc[:,[0,2,4]].min(axis=1)
        split_size_float['min_height'] = split_size_float.iloc[:,[1,3,5]].min(axis=1)

        # merging dfs
        combined_df = pd.concat([data, split_size_float], axis=1)

        return combined_df
        # return needed_cols

    def calculate_total_area(self, data):

        data = self.convert_to_float(data)
        data['Calculated Area m\u00b2'] = data.apply(
            lambda x: self.get_calculated_area(x['Count'], x['Area'], x['Surface Area']),
            axis=1)

        return data


