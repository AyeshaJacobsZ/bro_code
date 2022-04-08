import os
from src.category import Category
from src.csv_writer import CsvWriter
from src.read_csv import ReadCsv

path = os.getcwd()
duct_input_data = ReadCsv(f"{path}\data")
duct_input_data = Category(duct_input_data.read_data())
boq = duct_input_data.build_boq()

for filename, boq in boq.items():
    export = CsvWriter(f"BOQ_{filename}", boq)
    export.write_to_csv()

