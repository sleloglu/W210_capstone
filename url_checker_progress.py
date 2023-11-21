import pandas as pd
import requests

data_path = "/Users/canleloglu/Downloads/cleaned_target_furniture_dataset.csv"
df = pd.read_csv(data_path)

def check_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 404:
            return "404 Error"
        elif "We're sorry! This page is currently unavailable." in response.text:
            return "Page Unavailable"
        elif "product not available" in response.text.lower():
            return "Product Not Available"
        elif "out of stock" in response.text.lower():
            return "Out of Stock"
        # Add more patterns to check as needed
        else:
            return "Valid"
    except Exception as e:
        return "Error"

# Choose the range of rows to process (for example, the first 100 rows)
start_row = 0
end_row = 14533
step_size = 100  # Set the step size for printing progress

# Create a list to store invalid URLs
invalid_urls = []

# Display rows with errors or page unavailable
for i in range(start_row, end_row, step_size):
    batch_end = min(i + step_size, end_row)
    t = f"Processing rows {i+1}-{batch_end}..."
    print(t)
    
    batch_df = df['url'].iloc[i:batch_end].apply(check_url)
    
    # Get the indices of invalid URLs
    invalid_indices = batch_df[batch_df.isin(["404 Error", "Page Unavailable", "Product Not Available", "Out of Stock"])].index
    
    # Filter the DataFrame using the indices
    invalid_batch = df.iloc[invalid_indices]
    
    # Append invalid URLs to the list
    invalid_urls.extend(invalid_batch['url'].tolist())

# Write invalid URLs to a text file
output_file = "invalid_urls.txt"
with open(output_file, "w") as f:
    for url in invalid_urls:
        f.write(f"{url}\n")

print(f"\nInvalid URLs written to {output_file}")