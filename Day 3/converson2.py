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
    with open("Day 3/Data.json",'w') as f:
     json.dump(data,f,indent=2)
     print("Data")
     
def json_to_csv():
    with open("Day 3/Data.json",'r')as f:
         data =json.load(f)
    with open("data.csv","w")as f:
        writer = csv.writer(f)
        print(writer)
        writer.writerow(data.keys())
        print(data.keys())
        writer.writerow(data.values())
    print("Data has been converted to CSV format and saved as data.csv")    
       
   
if __name__ == "__main__":
     json_writing()
     json_to_csv()