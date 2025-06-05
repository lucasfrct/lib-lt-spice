import os
import sys

# Adjust the Python path to include the parent directory of 'transistores'
# to allow importing from transistores.parser
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from transistores.parser import parse_transistor_models

def get_transistor_models_data():
    """
    Reads transistor models, parses them, and returns the dictionary.
    """
    base_dir = "transistores"
    input_file_path = os.path.join(base_dir, "vários transistores.txt")

    file_content = ""
    try:
        with open(input_file_path, 'r') as f:
            file_content = f.read()
    except FileNotFoundError:
        print(f"Error: Input file not found at {input_file_path}", file=sys.stderr)
        return None

    parsed_models = parse_transistor_models(file_content)

    if not parsed_models:
        print("No models found.", file=sys.stderr)
        return None

    return parsed_models

if __name__ == "__main__":
    models_data = get_transistor_models_data()
    if models_data:
        # Print only the model names (keys) for easier processing in the next step
        model_names = list(models_data.keys())
        print(model_names)
        # To print the full data for manual checking if needed:
        # import json
        # print(json.dumps(models_data, indent=2))
