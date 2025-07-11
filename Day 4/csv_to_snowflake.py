import pandas as pd
import snowflake.connector


df = pd.read_csv("Day 4/Haelthcare_data_cleaned.csv")

df = df.where(pd.notnull(df), None)


conn = snowflake.connector.connect(
    user='SAQLAIN67I',
    password='Msaqlain@11223344',
    account='KPEZHMH-QT84420',
    warehouse='COMPUTE_WH',
    database='MY_DB',
    schema='PUBLIC'
)

cursor = conn.cursor()


cursor.execute("""
CREATE OR REPLACE TABLE patients (
    patient_name STRING,
    age INT,
    gender STRING,
    condition STRING,
    medication STRING,
    visit_date DATE,
    blood_pressure STRING,
    cholesterol STRING,
    email STRING,
    phone_number STRING
)
""")

for index, row in df.iterrows():
    try:
        cursor.execute("""
            INSERT INTO patients (
                patient_name, age, gender, condition, medication,
                visit_date, blood_pressure, cholesterol, email, phone_number
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            row['patient_name'],
            int(row['age']) if row['age'] is not None else None,
            row['gender'],
            row['condition'],
            row['medication'],
            row['visit_date'],
            row['blood_pressure'],
            row['cholesterol'],
            row['email'],
            row['phone_number']
        ))
    except Exception as e:
        print(f"Error on row {index}: {e}")

conn.commit()
cursor.close()
conn.close()
