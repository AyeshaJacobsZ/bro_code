import pandas as pd
import os
import glob
import numpy as np

# when duct is instantiated it immediately cleans the data ready to categorize
# maybe need to keep total column for unit testing


class Duct:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.read_data()

    def read_data(self):
        path = os.getcwd()
        data = pd.read_csv(f"{path}\\data\\{self.filename}")
        data = self.clean_data(data)
        return data

    def clean_data(self, data):
        data = data[data["Insulation Type"].notna()]
        return data


