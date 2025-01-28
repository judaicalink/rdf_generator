import csv

class CSVParser:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_csv(self):
        with open(self.file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            return [row for row in reader]
