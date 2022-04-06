import pandas as pd
import os
from src.category import Category
from src.duct import Duct
from src.csv_writer import CsvWriter

filename = "Duct Fitting Schedule Low Pressure Insulated Cladded Rect.csv"
path = os.getcwd()
print(path)
data = pd.read_csv(f"{path}\data\\{filename}")
data = data[data["Insulation Type"].notna()]

# print(data)

cat = Category(1, data)

print(cat.calculate_total_area())

df = Duct(f"Duct Fitting Schedule Low Pressure Insulated Cladded Rect.csv")

df = df.read_data()

df = CsvWriter(filename=filename, data=df)

df.write_to_csv()



