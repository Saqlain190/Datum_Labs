import dlt
from dlt.sources.rest_api import rest_api_source

@dlt.source(name="github")
clickup_source = rest_api_source({
    "client": {
        "base_url": "https://api.clickup.com/api/v2/",
        "headers": {
            "Authorization": dlt.secrets["sources.rest_api.click_up.click_up_api_key"]
        }
    },
    
})
pipeline = dlt.pipeline(
    pipeline_name="clickup_rest_api_pipeline",
    destination="snowflake", 
    dataset_name="clickup_data_new",
)


load_info = pipeline.run(clickup_source)
print(load_info)
