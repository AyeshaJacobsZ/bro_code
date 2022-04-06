import pandas as pd
import os
from src.category import Category
from src.duct import Duct
from src.csv_writer import CsvWriter

path = os.getcwd()


data = Duct(f"{path}\data")
data = data.read_data()
print(data)

print(data.keys())
for key in data.keys():
    print(key)

for key, value in data.items():
    print(key)
    print(value)



