import os
from src.category import Category
from src.csv_writer import CsvWriter
from src.read_csv_files import ReadCsv

path = os.getcwd()
data = ReadCsv(f"{path}\data")
data = Category(data.read_data())
boq = data.build_boq()

for filename, boq in boq.items():
    export = CsvWriter(f"BOQ_{filename}", boq)
    export.write_to_csv()
