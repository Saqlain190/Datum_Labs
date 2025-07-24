import dlt
from dlt.common import pendulum
from dlt.common.pipeline import LoadInfo
from dlt.pipeline.pipeline import Pipeline

try:
    from mongodb import mongodb  
except ImportError:
    from .mongodb import mongodb
def load_mongodb_to_snowflake(pipeline: Pipeline = None) -> LoadInfo:
    if pipeline is None:
        pipeline = dlt.pipeline(
            pipeline_name="mongo_to_snowflake",
            destination="snowflake",
            dataset_name="mongo_data"
        )
    

    source = mongodb()
    info = pipeline.run(source, write_disposition="replace")
    return info


if __name__ == "__main__":
    print(load_mongodb_to_snowflake())
