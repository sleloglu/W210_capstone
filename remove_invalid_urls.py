import pandas as pd

# Load the cleaned dataset
data_path = "/Users/canleloglu/Downloads/cleaned_target_furniture_dataset.csv"
df = pd.read_csv(data_path)

# Load the list of invalid URLs from the text file
invalid_urls_file = "invalid_urls.txt"
with open(invalid_urls_file, "r") as f:
    invalid_urls = f.read().splitlines()

# Filter out rows with invalid URLs
df_cleaned = df[~df['url'].isin(invalid_urls)]

# Save the cleaned DataFrame to a new CSV file
cleaned_data_path = "/Users/canleloglu/Downloads/cleaned_target_furniture_dataset_remove_invalid_urls.csv"
df_cleaned.to_csv(cleaned_data_path, index=False)

print(f"Cleaned data saved to {cleaned_data_path}")