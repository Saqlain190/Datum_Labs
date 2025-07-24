import psycopg2
import pandas as pd
import sqlite3
import dlt
from dlt.sources.sql_database import sql_database
import json
import os

STATE_FILE = "last_modified.txt"
TABLE_NAME = "customers"
TIMESTAMP_COLUMN = "last_modified"  
def get_last_modified():
    if not os.path.exists(STATE_FILE):
        return None
    with open(STATE_FILE, "r") as f:
        return f.read().strip()

def save_last_modified(ts):
    with open(STATE_FILE, "w") as f:
        f.write(ts)

def extract_incremental_to_dataframe():
    last_ts = get_last_modified()

    conn = psycopg2.connect(
        host="104.248.248.69",
        port=54321,
        user="postgres",
        password="neEs2w6QNU0YplJMChzGuxA8Zo7DI93",
        dbname="postgres"
    )
    cur = conn.cursor()

    if last_ts:
        query = f"""
            SELECT * FROM {TABLE_NAME}
            WHERE {TIMESTAMP_COLUMN} > %s
            ORDER BY {TIMESTAMP_COLUMN} ASC
            LIMIT 100
        """
        cur.execute(query, (last_ts,))
    else:
        query = f"""
            SELECT * FROM {TABLE_NAME}
            ORDER BY {TIMESTAMP_COLUMN} ASC
            LIMIT 100
        """
        cur.execute(query)

    rows = cur.fetchall()
    columns = [desc[0] for desc in cur.description]

    cur.close()
    conn.close()

    df = pd.DataFrame(rows, columns=columns)
    return df

def save_df_to_sqlite(df):
    # Convert dict/list columns to strings
    for col in df.columns:
        if df[col].apply(lambda x: isinstance(x, (dict, list))).any():
            df[col] = df[col].apply(json.dumps)

    conn = sqlite3.connect("temp.db")
    df.to_sql(TABLE_NAME, conn, if_exists="replace", index=False)
    conn.close()

def load_sqlite_to_snowflake():
    source = sql_database("sqlite:///temp.db").with_resources(TABLE_NAME)

    pipeline = dlt.pipeline(
        pipeline_name="incremental_sqlite_to_snowflake",
        destination="snowflake",
        dataset_name="incremental_customer_data"
    )

    info = pipeline.run(source, write_disposition="append")
    print("DLT load info:", info)

def main():
    df = extract_incremental_to_dataframe()

    if df.empty:
        print("No new or updated rows found.")
        return

    # Save latest last_modified timestamp
    latest_ts = df[TIMESTAMP_COLUMN].max()
    save_last_modified(str(latest_ts))

    save_df_to_sqlite(df)
    load_sqlite_to_snowflake()

if __name__ == "__main__":
    main()
