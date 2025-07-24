import dlt
from dlt.sources.sql_database import sql_database
from dlt.common.pendulum import pendulum

def run_postgres_to_snowflake():
    pipeline = dlt.pipeline(
        pipeline_name="postgres_to_snowflake",
        destination="snowflake",
        dataset_name="postgres_data_testing3"
    )

    credentials = "postgresql+psycopg2://postgres:neEs2w6QNU0YplJMChzGuxA8Zo7DI93@104.248.248.69:54321/postgres"
    source = sql_database(credentials=credentials).with_resources("customers","orders")
    source.max_table_nesting=0
    for resource in source.resources.values():
        resource.apply_hints(
            incremental=dlt.sources.incremental(
                "last_modified", initial_value=pendulum.DateTime(1990, 1, 1, 0, 0, 0)
            )
        )
    info = pipeline.run(source, write_disposition="replace")
    print("DLT load info:", info)
    

if __name__ == "__main__":
    run_postgres_to_snowflake()