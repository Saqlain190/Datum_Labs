# import dlt
# from dlt.sources.sql_database import sql_database

# def run_postgres_to_snowflake():
#     credentials = "postgresql+psycopg2://postgres:neEs2w6QNU0YplJMChzGuxA8Zo7DI93@104.248.248.69:54321/postgres"

  



#     pipeline = dlt.pipeline(
#         pipeline_name="postgres_to_snowflake",
#         destination="snowflake",
#         dataset_name="postgres_all_data_new"
#     )
#     info = pipeline.run(source,write_disposition="replace") 
#     print("DLT load info:", info)

# if __name__ == "__main__":
#     run_postgres_to_snowflake()
import dlt
from dlt.sources.sql_database import sql_database

def run_postgres_to_snowflake():
    credentials = "postgresql+psycopg2://postgres:neEs2w6QNU0YplJMChzGuxA8Zo7DI93@104.248.248.69:54321/postgres"

    source = sql_database(credentials)
    print("Loaded source with credentials:", credentials)

    source.with_resources("customers")
    source.customers.apply_hints(incremental=dlt.sources.incremental("last_modified"))

    pipeline = dlt.pipeline(
        pipeline_name="postgres_to_snowflake",
        destination="snowflake",
        dataset_name="postgres_all_datatest"
    )


    info = pipeline.run(source,write_disposition="merge") 
    print("DLT load info:", info)

if __name__ == "__main__":
    run_postgres_to_snowflake()