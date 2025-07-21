import dlt
from dlt.sources.sql_database import sql_table

@dlt.source
def postgres_source():
    # DLT auto-loads credentials from .dlt/secrets.toml
    return sql_table(
        table="employees",    # your table name
        schema="public",      # your Postgres schema
        credentials=None      # explicit not needed; defaults to TOML
    )

if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="pg_to_sf",
        destination="snowflake",
        dataset_name="employees_data"
        # no need for credentials here; DLT picks them up from TOML
    )
    info = pipeline.run(postgres_source())
    print("✅ Pipeline run info:", info)
