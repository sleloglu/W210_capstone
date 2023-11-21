import pandas as pd

# Load the target dataset
data_path = "/Users/canleloglu/Downloads/cleaned_target_furniture_dataset.csv"
df = pd.read_csv(data_path)

# Look at invalid URLs
invalid_urls_path = "/Users/canleloglu/Downloads/invalid_urls.txt"
with open(invalid_urls_path, 'r') as file:
    invalid_urls = [line.strip() for line in file]

# Filter DataFrame to get unique ids for invalid URLs
invalid_ids = df[df['url'].isin(invalid_urls)]['uniq_id'].unique()

# Write unique IDs to a new text file
output_path = "/Users/canleloglu/Downloads/invalid_url_ids.txt"
with open(output_path, 'w') as output_file:
    for unique_id in invalid_ids:
        output_file.write(str(unique_id) + '\n')

print("Unique IDs corresponding to invalid URLs written to:", output_path)