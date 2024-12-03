import pandas as pd

# List of Excel file paths
file_paths = [
    'friday_voucher_data.xlsx',
    'saturday_voucher_data.xlsx',
    'sunday_voucher_data.xlsx',
    'thursday_voucher_data.xlsx',
    'tuesday_voucher_data.xlsx',
    'wednesday_voucher_data.xlsx'
]

# Read and merge all Excel files into a single DataFrame
dataframes = [pd.read_excel(file) for file in file_paths]
merged_df = pd.concat(dataframes, ignore_index=True)

# Basic data cleaning
merged_df.drop_duplicates(inplace=True)  # Remove duplicate rows
merged_df.fillna('', inplace=True)        # Fill missing values with empty strings

# Save the cleaned DataFrame to a new Excel file
output_file = 'cleaned_voucher_data.xlsx'
merged_df.to_excel(output_file, index=False)

print(f"Data cleaning complete. Cleaned file saved as '{output_file}'.")
