import pandas as pd
import os

# Folder containing your CSV files
folder_path = 'Day 4'


csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
df_list = []

for file in csv_files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_csv(file_path)
    df_list.append(df)


merged_df = pd.concat(df_list, ignore_index=True)


merged_df.to_csv('Day 4/merged_output.csv', index=False)

print("Merged CSV saved as 'merged_output.csv'")
