

import dlt
from dlt.sources.sql_database import sql_database


def load_postgres_data() -> None:


 
    credentials = "postgresql+psycopg2://postgres:neEs2w6QNU0YplJMChzGuxA8Zo7DI93@104.248.248.69:54321/postgres"


    source = sql_database(credentials)
    print("Loaded Postgres source with credentials:", credentials)

    pipeline = dlt.pipeline(
        pipeline_name="postgres_to_snowflake",
        destination="snowflake",
        dataset_name="postgres_all_data_test"
    )


    load_info = pipeline.run(source, write_disposition="replace")
    print("DLT load info:", load_info)  # noqa: T201


if __name__ == "__main__":
    load_postgres_data()
