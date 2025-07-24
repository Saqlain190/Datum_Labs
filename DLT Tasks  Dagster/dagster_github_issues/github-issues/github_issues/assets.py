
import dlt
from dagster import AssetExecutionContext
from dagster_embedded_elt.dlt import DagsterDltResource, dlt_assets
from github_source import git_hub_pipeline

@dlt_assets(
    dlt_source=git_hub_pipeline(),
    dlt_pipeline=dlt.pipeline(
        pipeline_name="github_issues",
        dataset_name="github",
        destination="duckdb",
        progress="log",
    ),
    name="github",
    group_name="github",
)
def dagster_github_assets(context: AssetExecutionContext, dlt: DagsterDltResource):
    yield from dlt.run(context=context)