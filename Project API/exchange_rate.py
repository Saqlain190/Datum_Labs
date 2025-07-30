from typing import Any, Optional
import dlt
from dlt.sources.rest_api import RESTAPIConfig, rest_api_resources

@dlt.source()
def exchange_rate_source(exchange_rate_api: Optional[str] = dlt.secrets.value) -> Any:
    print("Loaded Exchange Rate API Key:", exchange_rate_api)

    config: RESTAPIConfig = {
        "client": {
            "base_url": f"https://v6.exchangerate-api.com/v6/f8ac5265bf59b334815a7f38/",
        },
        "resources": [
            {
                "name": "latest_usd",
                "endpoint": {
                    "path": "latest/USD"
                },
            },
            {
                "name": "latest_eur",
                "endpoint": {
                    "path": "latest/EUR"
                },
            },
            {
                "name": "pair_usd_to_pkr",
                "endpoint": {
                    "path": "pair/USD/PKR"
                },
            },
            {
                "name": "supported_codes",
                "endpoint": {
                    "path": "codes"
                },
            }
        ]
    }

    yield from rest_api_resources(config)


def load_news() -> None:
    pipeline = dlt.pipeline(
        pipeline_name="rest_api_rate",
        destination='snowflake',
        dataset_name="exchange_rate",
    )

    load_info = pipeline.run(exchange_rate_source())
    print(load_info)


if __name__ == "__main__":
    load_news()
