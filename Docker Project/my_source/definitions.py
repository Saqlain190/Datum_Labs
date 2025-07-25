from dagster import Definitions
from my_source.assets import load_postgres_data
from my_source.job import postgres_sync_job,my_schedule

defs = Definitions(
    assets=[load_postgres_data],
    jobs= [postgres_sync_job],
    schedules=[my_schedule]
)
