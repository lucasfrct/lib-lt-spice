def parse_transistor_models(file_content):
    """
    Parses the transistor models from the given file content.

    Args:
        file_content (str): The content of the transistor model file.

    Returns:
        dict: A dictionary where keys are transistor model names
              and values are the corresponding lines.
    """
    models = {}
    for line in file_content.splitlines():
        line = line.strip()
        if line.startswith(".model"):
            parts = line.split()
            if len(parts) > 1:
                model_name = parts[1]
                models[model_name] = line
    return models

if __name__ == "__main__":
    # This is an example of how to use the parser.
    # In a real scenario, you might read the file content from disk.
    # For this subtask, we'll define a placeholder for the file content
    # which would be replaced by the actual content in the next steps.

    example_file_content = """
.model KT940A NPN(bf=150 is=400f vaf=200 ikf=60m xtb=1.5 br=1 cjc=24p vjc=.75 mjc=.5 fc=.5 cje=50p vje=.75 mje=.33 tr=50n tf=2.5n itf=50m vtf=10 xtf=2 xti=3 eg=1.11 isc=10f nc=2 ise=700p ne=2 rb=30 rbm=3 irb=.1m rc=3 rco=60 Vo=7 GAMMA=1E-6 QCO=1E-11 Vceo=300 Icrating=100m mfg=USSR)
.model kt361g PNP(bf=350 br=5 is=400f rb=100 rbm=10 irb=50u rc=10 ikf=70m xti=3 xtb=1.5 xtf=1.1 vaf=70 itf=40m vtf=75 cje=20p xcjc=0.5 cjc=15p tf=0.3n tr=25n vjc=.7 mjc=.33 mje=.33 vje=.5 xcjc=0.15 ne=2 ise=315p nc=2 isc=600p Vceo=35 Icrating=100m mfg=USSR)
.model kt342v NPN(is=20f xti=3 eg=1.11 vaf=90 bf=1400 xtb=1.5 br=1 rb=1.5k rbm=10 rc=1 irb=50u cjc=10p mjc=.39 vjc=.75 fc=.5 cje=14p xcjc=0.1 tf=.4n tr=300n ne=1.33 ise=10f nc=1.34 isc=24f Vceo=10 Icrating=50m mfg=USSR)
    """

    # In the actual application, we would pass the content of
    # "transistores/vários transistores.txt" to this function.
    # For now, we use the example content.
    # parsed_models = parse_transistor_models(example_file_content)
    # print(parsed_models)

    # The following lines will be used to process the actual file
    # when this script is called from another script or integrated
    # into a larger workflow.

    # Read the actual file content
    # The script expects to be run from the root of the repository.
    file_path = "transistores/vários transistores.txt"
    try:
        with open(file_path, 'r') as f:
            actual_file_content = f.read()
        parsed_models_actual = parse_transistor_models(actual_file_content)
        # Instead of printing, we might want to store this data
        # or pass it to another function. For now, let's print it.
        # This print will be removed or commented out in the final version
        # if the data is intended to be used by other scripts.
        print(parsed_models_actual)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
