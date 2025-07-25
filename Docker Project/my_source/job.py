from dagster import define_asset_job
from .assets import load_postgres_data
from dagster import ScheduleDefinition
postgres_sync_job = define_asset_job(
    name="postgres_sync_job",
    selection=[load_postgres_data]
)


my_schedule = ScheduleDefinition(
    job=postgres_sync_job,
    cron_schedule="0 2 * * *", 
)