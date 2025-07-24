from dagster import Definitions
from my_dagster_project.jobs import do_stuff, simple_schedule  # noqa: TID252
from my_dagster_project.assets import hello_asset
from my_dagster_project.sensors import simple_sensort


defs = Definitions(
    assets=[hello_asset],
    jobs=[do_stuff],
    sensors=[simple_sensort],
    schedules=[simple_schedule],
)
