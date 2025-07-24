import dlt
from dlt.sources.sql_database import sql_database


@dlt.source
def postgres_source():
    credentials = "postgresql+psycopg2://postgres:neEs2w6QNU0YplJMChzGuxA8Zo7DI93@104.248.248.69:54321/postgres"
    return sql_database(credentials)


@dlt.resource(name="customers")
def customers_resource(db):
    resource = db.customers
    resource.max_table_nesting = 1
    yield from resource


def run_postgres_to_snowflake():
    source = postgres_source()

    pipeline = dlt.pipeline(
        pipeline_name="postgres_to_snowflake",
        destination="snowflake",
        dataset_name="postgres_all_data_new"
    )

    # Note: pass source to the resource function
    info = pipeline.run(customers_resource(source))
    print("DLT load info:", info)


if __name__ == "__main__":
    run_postgres_to_snowflake()
