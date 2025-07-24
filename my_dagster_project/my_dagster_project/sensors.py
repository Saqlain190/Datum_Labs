from dagster import sensor,RunRequest
from my_dagster_project.jobs import do_stuff

@sensor(
    job=do_stuff,
    minimum_interval_seconds= 5,
)
def simple_sensort():
    yield RunRequest(run_key=None, run_config={})