import dlt
from dlt.sources.rest_api import rest_api_source


def load_data() -> None:

    access_token = dlt.secrets.value 

    pipeline = dlt.pipeline(
        pipeline_name="rest_api_click_up",
        destination="snowflake",
        dataset_name="rest_api_data",
    )

    api_source = rest_api_source(
        {
            "client": {
                "base_url": "https://api.clickup.com/api/v2/",
                "auth": {
                    "type": "bearer",
                    "token": access_token,
                }
            },
            "resources": [
                "users",
            ],
        }
    )

    load_info = pipeline.run(api_source)
    print(load_info)


if __name__ == "__main__":
    load_data()
