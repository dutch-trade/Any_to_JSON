import csv
import json

def csv_to_json(csv_file, json_file):
    str_voyages = []

    with open(csv_file, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            str_voyages.append(row)

    with open(json_file, 'w', encoding='utf-8') as jsonfile:
        json.dump({"STR_voyages": str_voyages}, jsonfile, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    csv_file_path = "/users/axel22/documents/trade project/data harmonisation/copies of raw data csv files/zvoc.csv"
    json_file_path = "zvoc_json.json"

    csv_to_json(csv_file_path, json_file_path)
