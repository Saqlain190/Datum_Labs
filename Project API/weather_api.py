from typing import Any, Optional
import dlt
from dlt.sources.rest_api import RESTAPIConfig, rest_api_resources
import logging

@dlt.source(name="weather_api_key")
def weather_source(api_key: Optional[str] = dlt.secrets.value) -> Any:

    if not api_key:
        logging.error("Api key is Missing")
    
    logging.info("Api Key is Correct")

    config: RESTAPIConfig = {
        "client": {
            "base_url": "https://api.openweathermap.org/data/2.5",
        },
        "resources": [
            {
                "name": "current_weather",
                "endpoint": {
                    "path": "weather",
                    "params": {
                        "q": "Lahore",
                        "appid": api_key,
                        "units": "metric"
                    },
                },
            },
            {
                "name": "forecast_weather",
                "endpoint": {
                    "path": "forecast",
                    "params": {
                        "q": "Lahore",
                        "appid": api_key,
                        "units": "metric"
                    },
                },
            },
            {
                "name": "air_pollution",
                "endpoint": {
                    "path": "air_pollution",
                    "params": {
                        "lat": "31.5204",  # Lahore latitude
                        "lon": "74.3587",  # Lahore longitude
                        "appid": api_key
                    },
                },
            },
            {
                "name": "uv_index",  # Note: This endpoint might be deprecated
                "endpoint": {
                    "path": "uvi",
                    "params": {
                        "lat": "31.5204",
                        "lon": "74.3587",
                        "appid": api_key
                    },
                },
            }
        ]
    }

    yield from rest_api_resources(config)



def load_weather() -> None:
    try:
     pipeline = dlt.pipeline(
        pipeline_name="rest_api_weather",
        destination='snowflake',
        dataset_name="weather_data",
    )
     load_info = pipeline.run(weather_source())
     print(load_info)
     logging.info("Pipeline Run Sucessfulyy")
     
    except Exception as e:
       logging.exception("Pipeline Failed")


if __name__ == "__main__":
    load_weather()
