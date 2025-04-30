import csv

def read_csv(file_path):
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            return list(reader)
    except FileNotFoundError:
        return []

def write_csv(file_path, data):
    with open(file_path, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(data)
        return "CSV ma'lumotlari yozildi."
