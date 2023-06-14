import pandas as pd
import os

df = pd.read_excel('Sample.xlsx') #input file name here
column_name = 'Country' #input column that need filtering
unique_values = df[column_name].unique()

for unique_value in unique_values:
    df_output = df[df[column_name].str.contains(unique_value)]
    output_path = os.path.join('output', unique_value + '.xlsx')
    df_output.to_excel(output_path, sheet_name=unique_value, index=False)
