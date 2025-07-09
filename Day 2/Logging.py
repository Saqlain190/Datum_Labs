import logging
import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s-%(levelno)s -%(funcName)s- %(message)s',
    filename='cleaning.log',
    filemode='w'
)

try: 
    def say_hello():
        logging.info("Reading The CSV file")
        df = pd.read_csv('automobile1.csv')
        print(df.columns.str)
    say_hello()
except Exception as e:
    logging.error(f"Error occurred while reading the CSV: {e}")
    print("File not Found, PLease check file name or file path")

    