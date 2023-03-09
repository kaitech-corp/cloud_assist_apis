import json
from typing import List

# File paths
cloudData = ["api/cloud_data.json","api/cloud_networking.json","api/database_data.json","api/security_data.json"]
output_file = "api/combined_data.json"

def check_json(json_file):
    with open(json_file) as f:
        data = json.load(f)
        for item in data:
            # Check if all required keys are present
            if not all(key in item for key in ["service", "description", "detail", "benefits", "cons", "useCases", "link", "example"]):
                # Add missing keys with empty strings as value
                for key in ["service", "description", "detail", "benefits", "cons", "useCases", "link", "example"]:
                    if key not in item:
                        item[key] = ""

                print(f"Missing keys in item {item}")

            # Remove any additional keys
            valid_keys = ["service", "description", "detail", "benefits", "cons", "useCases", "link", "example"]
            for key in list(item.keys()):
                if key not in valid_keys:
                    item.pop(key)
                    print(f"Removed invalid key {key} from item {item}")

    with open(json_file, "w") as f:
        json.dump(data, f, indent=2)


def combine_json_files(files: List[str], output_file: str) -> None:
    """
    Combine multiple JSON files into a single JSON array.

    Args:
        files (List[str]): A list of filepaths to the JSON files.
        output_file (str): The filepath where the combined JSON file will be saved.

    Returns:
        None
    """
    # Initialize an empty list to store the contents of each file.
    data = []

    # Iterate over each filepath in the list.
    for file in files:
        # Open the file and load its contents into a dictionary.
        with open(file, 'r') as f:
            file_data = json.load(f)

        # Append the dictionary to the list.
        data.extend(file_data)

    # Write the combined list of dictionaries to a new file.
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=2)

def main():
    for json_file in cloudData:
        check_json(json_file)

    combine_json_files(cloudData, output_file)

# Run script
main()