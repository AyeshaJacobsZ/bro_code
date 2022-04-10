import os

class CsvWriter:
    def __init__(self, filename, data):
        self.filename = filename
        self.data = data

    def write_to_csv(self):
        path = os.getcwd()
        output_path = f"{path}\\output\\csv\\"
        self.data.to_csv(f"{output_path}{self.filename}", index=False)

