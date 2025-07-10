import logging
import pandas as pd

logging.basicConfig( 
    level= logging.INFO,
    format = '%(asctime)s-%(levelname)s-%(funcName)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='script.log',
    filemode= 'w'
)
# Logging configuration
try:  
    logging.info("Reading CSV File")
    df = pd.read_csv("Datum_Labs/Day 3/healthcare_data.csv")

    logging.info("Transformaing Column Names")
    df.columns =df.columns.str.strip().str.lower().str.replace(' ','_')
    df= df.dropna()

    logging.info("Finding Null Values")
    print(df.isnull().sum())

    logging.info("Removing Null Values")
    df= df.dropna()
    print(df.isnull().sum())



except Exception as e:
    logging.error(f"Error while reading the file: {e}")

# Error Handling
try:
     logging.warning("Dates are not in the correct format, converting them to datetime")
     df['visit_date']= pd.to_datetime(df['visit_date'],errors='coerce')
 
     logging.info("Removing Null Dates")
     df =df.dropna(subset=['visit_date'])
except KeyError:
    logging.error("Visit_date column not Founded")




df.to_csv("Haelthcare_data_cleaned.csv", index=False)
