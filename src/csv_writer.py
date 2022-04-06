import pandas as pd
import openpyxl
import os

"""
CsvWriter:
- gets information form BOQ (by either passing or inheritance)
- writes all information to correct folder with correct filename 
"""


# filename = "Duct Fitting Schedule Low Pressure Insulated Cladded Rect.csv"
# path = os.getcwd()[:-3]
# output_path = f"{path}output\\csv\\"
# example_data = pd.read_csv(f"{path}\data\Duct Fitting Schedule Low Pressure Insulated Cladded Rect.csv")
# example_data.to_csv(f"{output_path}{filename}")


class CsvWriter:
    def __init__(self, filename, data):
        self.filename = filename
        self.data = data

    def write_to_csv(self):
        path = os.getcwd()
        output_path = f"{path}\\output\\csv\\"
        self.data.to_csv(f"{output_path}{self.filename}")


# filename = "Duct Fitting Schedule Low Pressure Insulated Cladded Rect.csv"
# data = pd.read_csv(f"{os.getcwd()[:-3]}\data\Duct Fitting Schedule Low Pressure Insulated Cladded Rect.csv")
#
# export_data = CsvWriter(filename, data)
#
# export_data.write_to_csv()

