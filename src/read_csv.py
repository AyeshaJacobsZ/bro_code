import os
import pandas as pd
import glob
from src.duct import Duct


class ReadCsv(Duct):
    def __init__(self, folder_location):
        super().__init__()
        self.folder_location = folder_location

    def read_data(self):
        path = os.getcwd()
        files = glob.glob(self.folder_location + '\*.csv')
        duct = {}
        for file in files:
            key = file.replace(f"{path}\\data\\", "")
            data = pd.read_csv(file)
            data = self.clear_nan_rows(data)
            data = self.convert_to_float(data)
            data = self.calculate_total_area(data)
            data = self.split_size(data)
            data = self.get_minimum_width_and_height(data)
            duct[key] = data

        return duct
