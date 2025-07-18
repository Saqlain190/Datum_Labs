import json
import csv
data = {
    "user":{
        "id" :123,
        "name" : {
            "first" : "Alice",
             "last" : "Johnson"
        },
        "Location " : {
            "country" : "Germany",
            "city" : {
                "name" : "Berlin",
                "postal" : {
                    "code" : "10115" ,
                    "area" : "Mitte" 
                 }

            }
        }

    },
    "account" : {
        "created_at " : "2024-01-11",
        "status" : "active"
    }
}
with open("Data.json","w",newline='') as f:
 json.dump(data , f)

with open("Data.json", "r") as f:
   Data = json.load(f)


with open("Data.csv", "w") as f:
  writer = csv.writer(f)
  writer.writerow(Data.keys())
  writer.writerow(Data.values())


