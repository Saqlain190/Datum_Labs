from dagster import asset
import pandas as pd

sample_data_file = "myfile.csv"

@asset
def hello_asset():
    df = pd.read_csv(sample_data_file)
    df["age_group"] = pd.cut(
        df["age"], bins=[0, 30, 40, 100], labels=["Young", "Middle", "Senior"]
    )

    ## Save processed data
    df.to_csv("processed_data_file", index=False)
    return "Data loaded successfully"
    


all_assets = [hello_asset]
