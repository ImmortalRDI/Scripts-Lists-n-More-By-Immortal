import os
import re
import sys

# Check if the input folder path is provided as an argument
if len(sys.argv) < 2:
    print("Please provide the path to the input folder.")
    sys.exit(1)

# Get the input folder path from the command line argument
input_folder_path = sys.argv[1]

# Output file path for extracted UUIDs
output_file_path = "path\\to\\your\\output.txt"  # Update with desired output file path

# Regex pattern to match UUIDs
uuid_pattern = r'[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}"'

# Function to extract UUIDs from a file
def extract_uuids_from_file(file_path):
    try:
        with open(file_path, 'r') as input_file:
            content = input_file.read()
            return re.findall(uuid_pattern, content)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []

# Iterate through files in the input folder
try:
    with open(output_file_path, 'w') as output_file:
        for root, _, files in os.walk(input_folder_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                extracted_uuids = extract_uuids_from_file(file_path)

                if extracted_uuids:
                    # Write file name as header for the group of UUIDs
                    output_file.write(f"File: {file_name}\n")

                    # Track unique UUIDs for each file
                    unique_uuids = set()

                    # Write extracted unique UUIDs to the output file
                    for uuid in extracted_uuids:
                        if uuid not in unique_uuids:
                            output_file.write(f'<node id="DependentResource">\n\t<attribute id="Object" type="FixedString" value="{uuid}" />\n</node>\n')
                            unique_uuids.add(uuid)

    print(f"Extracted unique UUIDs written to {output_file_path}")

except Exception as e:
    print(f"An error occurred: {e}")