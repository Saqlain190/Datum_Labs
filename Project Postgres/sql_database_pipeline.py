import dlt
from dlt.sources.sql_database import sql_database

def run_postgres_to_snowflake():
    credentials = "postgresql+psycopg2://postgres:neEs2w6QNU0YplJMChzGuxA8Zo7DI93@104.248.248.69:54321/postgres"

    source = sql_database(credentials)
    print("Loaded source with credentials:", credentials)

    pipeline = dlt.pipeline(
        pipeline_name="postgres_to_snowflake",
        destination="snowflake",
        dataset_name="postgres_all_data_test"
    )
    info = pipeline.run(source,write_disposition="replace") 
    print("DLT load info:", info)

if __name__ == "__main__":
    run_postgres_to_snowflake()