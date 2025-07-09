import pandas as pd
import re

df = pd.read_csv('messy_HR_data.csv')


df.columns = df.columns.str.lower().str.replace(' ','_')
df= df.dropna()
print(df.isnull().sum())

df['joining_date'] = pd.to_datetime(df['joining_date'], errors='coerce')


def format_phone(phone):
    
    digits = re.sub(r'\D', '', str(phone))
    if len(digits) == 10:
        return f"({digits[0:3]}) {digits[3:6]}-{digits[6:]}"
    else:
        return "Invalid"

df['phone_number']= df['phone_number'].apply(format_phone)

df = df.sort_values(by=['joining_date'],ascending=True)

df.to_csv("cleaned_HR_data.csv", index=False)