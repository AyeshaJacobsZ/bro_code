import pandas as pd
import os
from src.category import Category
from src.duct import Duct
from src.csv_writer import CsvWriter
from src.read_csv_files import ReadCsv

path = os.getcwd()


data = ReadCsv(f"{path}\data")
data = data.read_data()

cat_data = Category(data)
cat_data = cat_data.boq()
print(cat_data['Duct Schedule Medium Pressure Insulated Rect.csv'])
# print(cat_data)
#
# data = Category(data)
# data.categorize()

# print(data.keys())
# for key in data.keys():
#     print(key)
#
# for key, value in data.items():
#     print(key)
#     print(value)

# test = data['Duct Fitting Schedule Low Pressure Insulated Cladded Rect.csv']
# test = test[["Count", "Area", "Surface Area"]].head(1)
# print(test.dtypes)
#
# float_series = pd.Series(['float64', 'float64', 'float64'], index=["Count", "Area", "Surface Area"])
# print(float_series)
#
# if test.dtypes.all == float_series.all:
#     print("True")
# else:
#     print("False")
# x = 9.41
#
# print(pd.api.types.is_object_dtype(test))
#
