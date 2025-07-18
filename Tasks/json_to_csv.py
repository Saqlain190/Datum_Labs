import json
import csv

data = {
    "user": {
        "id": 123,
        "name": {
            "first": "Alice",
            "last": "Johnson"
        },
        "Location ": {
            "country": "Germany",
            "city": {
                "name": "Berlin",
                "postal": {
                    "code": "10115",
                    "area": "Mitte"
                }
            }
        }
    },
    "account": {
        "created_at ": "2024-01-11",
        "status": "active"
    }
}

# Flatten function
def flatten_dict(d, parent_key='', sep='.'):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k.strip()}" if parent_key else k.strip()
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

flattened_data = flatten_dict(data)



with open("Data.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(flattened_data.keys())
    writer.writerow(flattened_data.values())
