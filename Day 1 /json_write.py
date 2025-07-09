import json

data = {'name': 'Saqlain Ahmad', 'age': 30, 'Designation': 'Data Engineer'}

with open('data.json', 'w') as f:
    json.dump(data,f, indent=2)

with open('data.json', 'r') as f:
    data =json.load(f)
    print(data['age'])
