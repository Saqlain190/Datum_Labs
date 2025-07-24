import dlt
from dlt.common import pendulum
from dlt.common.pipeline import LoadInfo
from dlt.pipeline.pipeline import Pipeline
from dlt.extract.incremental import Incremental


try:
    from mongodb import mongodb  
except ImportError:
    from .mongodb import mongodb


def load_mongodb_to_snowflake(pipeline: Pipeline = None) -> LoadInfo:
    if pipeline is None:
        pipeline = dlt.pipeline(
            pipeline_name="mongo_to_snowflake",
            destination="snowflake",
            dataset_name="mongo_data_increment3"
        )

    # Apply incremental loading on the resource
    source = mongodb()
    source.with_resources("comments")
    source.comments.apply_hints(
        Incremental(
            "date",
            initial_value=pendulum.DateTime(2022, 1, 1, 0, 0, 0).in_tz("UTC"),
            primary_key="_id"
        )
    )


    info = pipeline.run(source, write_disposition="merge")  
    return info


if __name__ == "__main__":
    print(load_mongodb_to_snowflake())
