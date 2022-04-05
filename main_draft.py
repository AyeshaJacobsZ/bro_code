import pandas as pd
import os
from src.category import Category
from src.duct import Duct
path = os.getcwd()
# print(path)
data = pd.read_csv(f"{path}\data\Duct Fitting Schedule Low Pressure Insulated Cladded Rect.csv")
data = data[data["Insulation Type"].notna()]

# print(data)

cat = Category(1, data)

# print(cat.calculate_total_area())

df = Duct(f"Duct Fitting Schedule Low Pressure Insulated Cladded Rect.csv")

print(df.read_data())

