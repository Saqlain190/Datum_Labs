import dlt
...
@dlt.resource(
    table_name="issues",
    write_disposition="merge",
    primary_key="id",
)
def get_issues(
        updated_at=dlt.sources.incremental("updated_at", initial_value="1970-01-01T00:00:00Z")
):
    url = (
        f"{BASE_URL}?since={updated_at.last_value}&per_page=100&sort=updated"
        "&direction=desc&state=open"
    )
    yield pagination(url)

@dlt.source
def github_source():
    return get_issues()