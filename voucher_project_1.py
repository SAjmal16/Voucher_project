import pandas as pd 
from glob import glob

files_dir = "path_to_xlsx_files"

file_path = glob(files_dir + "/*.xlsx")

merged_df = pd.concat([pd.read_excel("file") for file in file_path], ignore_index=True)

df = df.dropna(inplace=True)
df = df.fillna(inpace=True)

output_file = (files_dir + "/cleaned_data.xlsx", merged_df.to_excel)

print(f"Data cleaning complete. Cleaned file saved as {output_file}.")