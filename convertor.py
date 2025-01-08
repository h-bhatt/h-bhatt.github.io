import csv
import json

# Open CSV file and read its contents
csv_file = 'trade_bal.csv'  # Replace with your CSV file name
json_file = 'data.json'  # Output JSON file name

csv_data = []
with open(csv_file, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        csv_data.append(row)

# Write the JSON data to a file
with open(json_file, mode='w') as file:
    json.dump(csv_data, file, indent=4)

print("CSV has been successfully converted to JSON!")
