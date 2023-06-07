import pandas as pd
import csv
from datetime import datetime

def convert_timestamp(unique_temp):
    ts = int(unique_temp, base=16)/1000000
    date = datetime.utcfromtimestamp(int(ts))
    return date.strftime('%Y%m%d')

# Path to the input CSV file
input_file = 'csv/Foldersnl-WitteVogel-RawData.csv'

# Path to the output CSV file
output_file = 'csv/output.csv'

# Read the input CSV file
with open(input_file, 'r') as file:
    reader = pd.read_csv(file)
    rows = list(reader)  # Convert the reader object to a list

    # Modify the first column for each row
    for row in rows:
        timestamp = row[0]
        formatted_date = convert_timestamp(timestamp)
        row[0] = formatted_date

# Save the modified data to the output CSV file
with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)

print("CSV file converted and saved successfully.")

