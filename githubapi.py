import dlt
from dlt.sources.rest_api import rest_api_source

github_source = rest_api_source({
    "client": {
        "base_url": "https://api.github.com/",
        "headers": {
            "Authorization": dlt.secrets["sources.rest_api.github.github_api_key"]
        }
    },
    "resources": [
        {
            "name": "user",
            "endpoint": "user"
        },
        {
            "name": "repos",
            "endpoint": "user/repos"
        }
    ]
})

pipeline = dlt.pipeline(
    pipeline_name="Github_rest_api_pipeline",
    destination="snowflake", 
    dataset_name="github",
)

load_info = pipeline.run(github_source)
print(load_info)
