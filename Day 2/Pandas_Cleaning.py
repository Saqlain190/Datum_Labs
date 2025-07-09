import pandas as pd

df = pd.read_csv('automobile.csv')
print(df.columns.str)

df.columns = df.columns.str.strip().str.lower().str.replace('-','_')

print(df.columns)
df= df.drop_duplicates()
print(df.isnull().sum())
df = df.dropna()
print(df.isnull().sum())


for col in df.select_dtypes(include=['float']):  
  
    if (df[col].dropna() % 1 == 0).all():
        df[col] = df[col].astype('Int64')
        
df = df.sort_values(by='price', ascending=True)

df.to_csv("cleaned_file3.csv", index=False)