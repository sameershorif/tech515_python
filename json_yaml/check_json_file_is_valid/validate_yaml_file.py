import sys
import os
import yaml 


# 1. Check a file name was passed as an arg

if len(sys.argv) < 2:
    print("ERROR: No YAML file was specified")
    print("Usage: validate_yaml_file.py <file.yaml>")
    sys.exit(1)

yaml_path = sys.argv[1]


# 2. Check the file exists

if not os.path.exists(yaml_path):
    print(f"ERROR: File '{yaml_path}' not found")
    sys.exit(1)


# 3. Try to load / parse YAML

try:
    with open(yaml_path, "r") as yaml_file:
        data = yaml.safe_load(yaml_file)

    print(f"SUCCESS: '{yaml_path}' is valid YAML")
    print("Top-level Python type:", type(data))

except yaml.YAMLError as e:
    print(f"ERROR: '{yaml_path}' is NOT valid YAML")
    print("Details:")
    print(e)