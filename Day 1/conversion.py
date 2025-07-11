import csv, json

with open('people.csv', 'r') as f:
    csv_reader = csv.DictReader(f)
    data = list(csv_reader)

with open('people.json', 'w') as f:
    json.dump(data, f, indent=2)

with open('people.json','r') as f:
    data =json.load(f)

with open('people.csv','w')as f:
    writer= csv .DictWriter(f, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)
