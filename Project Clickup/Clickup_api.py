import dlt

from typing import Any, Optional
from dlt.sources.rest_api import (
    RESTAPIConfig,
    rest_api_resources,
)


@dlt.source(name="Click_up")
def clickup_source(access_token: Optional[str] = dlt.secrets.value) -> Any:
    print("Api Token Loaded : " ,access_token)

    config = RESTAPIConfig(
        {
            "client": {
                "base_url": "https://api.clickup.com/api/v2/team",
                "auth": (
                    {
                        "type": "bearer",
                        "token": access_token,
                    }
                    if access_token else None
                ),
            },
            "resource_defaults": {
            # "primary_key": "id",
            # "write_disposition": "merge",
            # "endpoint": {
            #     "params": {
            #         "per_page": 100,
            #     },
            # },
        },
            "resources": [ "user"],
        }
    )
    yield from rest_api_resources(config)

def load_clickup() -> None:
    pipeline = dlt.pipeline(
        pipeline_name="rest_api_click_up",
        destination="snowflake",
        dataset_name="rest_api_data",
    )

    load_info = pipeline.run(clickup_source())
    print(load_info)

if __name__ == "__main__":
    load_clickup()
