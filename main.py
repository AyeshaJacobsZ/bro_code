from src.csv_writer import CsvWriter



if __name__=="__main__":
    csv_files_path = r'data\\..something with glob?'
    csv_output = CsvWriter(csv_files_path)
    csv_output.write_to_csv()