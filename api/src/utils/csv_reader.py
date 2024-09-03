import csv

def read_csv_from_file(file_path):
    with open(file_path, mode='r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        return list(reader)