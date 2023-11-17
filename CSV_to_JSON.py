import csv
import json

def csv_to_json(csv_file, json_file):
    das1718_voyages = []

    with open(csv_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            das1718_voyages.append(row)

    with open(json_file, 'w') as jsonfile:
        json.dump({"STR_voyages": das1718_voyages}, jsonfile, indent=4)

if __name__ == "__main__":
    csv_file_path = "/users/axel22/documents/trade project/data harmonisation/copies of raw data csv files/raw united STR.csv"
    json_file_path = "zvoc_json.json" 

    csv_to_json(csv_file_path, json_file_path)

