import pandas as pd 
import os

# define which excel files here 

file = 
input_dir = "path_to_excel"
output_dir = "path_to_cleansed"

# here we need to put our df.drop etc bits 

clean_data(df):

file_path = os.path.join(input_dir, file)

print(f"Processing: {file_path}")

df = pd.read_excel(file_path)

cleaned_df = clean_data(df)

cleaned_file_path = os.path.join(output_dir, f"cleaned_{file}")
cleaned_df.to_excel(cleaned_file_path, index=False)

print(f"Saved cleaned file to : {cleaned_file_path}")