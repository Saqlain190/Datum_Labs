import json,csv
data = {
    "name": "Ali",
    "age": 20,
    "grades": {
        "math": 85,
        "science": 90,
        "english": 78
    },
    "address": {
        "city": "Lahore",
        "zip": "54000"
    }
}
def json_writing():
    with open("Data.json",'w') as f:
     json.dump(data,f,indent=2)
     
def json_to_csv():
    with open("Data.json",'r')as f:
         data =json.load(f)
    with open("data.csv","w")as f:
        writer = csv.writer(f)
        writer.writerow(data.keys())
        writer.writerow(data.values())
       
   
if __name__ == "__main__":
     json_to_csv()