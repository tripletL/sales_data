import pandas as pd
import numpy as np

df =pd.read_csv("")
df['research'] = df['research'].astype('str')

mask = (df['research'].str.len() > 6) & (df['email'].str.len() > 6) & (df['college'].str.contains("生|医|农|植|药|园艺|命|动物|林|食")) 


df = df.loc[mask]


print(df)
df.to_excel("")
