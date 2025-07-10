import csv, json

with open('Datum_Labs/Day 1 /people.csv', 'r') as f:
    csv_reader = csv.DictReader(f)
    data = list(csv_reader)

with open('people.json', 'w') as f:
    json.dump(data, f, indent=0)

