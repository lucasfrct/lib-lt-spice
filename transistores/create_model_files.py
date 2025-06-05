import os
import sys

def create_single_model_file(base_dir, model_name, model_definition):
    """
    Creates a folder and .lib file for a single transistor model.

    Args:
        base_dir (str): The base directory where the model folder should be created.
        model_name (str): The name of the transistor model.
        model_definition (str): The definition line for the model.
    """
    model_folder_path = os.path.join(base_dir, model_name)

    try:
        if not os.path.exists(model_folder_path):
            os.makedirs(model_folder_path)
            # print(f"Created folder: {model_folder_path}") # Optional: for verbose output
        # else:
            # print(f"Folder already exists: {model_folder_path}")
    except OSError as e:
        print(f"Error creating folder {model_folder_path}: {e}", file=sys.stderr)
        return # Do not proceed if folder creation fails

    model_lib_file_path = os.path.join(model_folder_path, f"{model_name}.lib")

    try:
        with open(model_lib_file_path, 'w') as lib_f:
            lib_f.write(model_definition + "\n")
        # print(f"Created file: {model_lib_file_path}") # Optional: for verbose output
    except IOError as e:
        print(f"Error writing file {model_lib_file_path}: {e}", file=sys.stderr)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python create_model_files.py <model_name> \"<model_definition>\"", file=sys.stderr)
        sys.exit(1)

    model_name_arg = sys.argv[1]
    model_definition_arg = sys.argv[2]

    # The base directory is 'transistores' relative to where the script is run from
    # Assuming this script is run from the repository root.
    # current_script_path = os.path.dirname(os.path.abspath(__file__))
    # base_directory_for_models = current_script_path # This would be transistores/transistores
    base_directory_for_models = "transistores"


    create_single_model_file(base_directory_for_models, model_name_arg, model_definition_arg)
    # print(f"Processed model: {model_name_arg}") # Optional: for verbose output
