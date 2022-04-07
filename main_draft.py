import pandas as pd
import os
from src.category import Category
from src.duct import Duct
from src.csv_writer import CsvWriter

path = os.getcwd()


data = Duct(f"{path}\data")
data = data.read_data()
# print(data)
#
# print(data.keys())
# for key in data.keys():
#     print(key)
#
# for key, value in data.items():
#     print(key)
#     print(value)

test = data['Duct Fitting Schedule Low Pressure Insulated Cladded Rect.csv']
test = test[["Count", "Area", "Surface Area"]].head(1)
print(test.dtypes)

float_series = pd.Series(['float64', 'float64', 'float64'], index=["Count", "Area", "Surface Area"])
print(float_series)

if test.dtypes.all == float_series.all:
    print("True")
else:
    print("False")
x = 9.41

print(pd.api.types.is_object_dtype(test))

