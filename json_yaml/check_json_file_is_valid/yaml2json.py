import sys
import os
import yaml
import json

# Expected usage:
#   python yaml2json.py source.yaml target.json


# 1. Check source YAML file argument

if len(sys.argv) < 2:
    print("ERROR: No YAML file was specified")
    print("Usage: yaml2json.py <source_file.yaml> <target_file.json>")
    sys.exit(1)

source_path = sys.argv[1]

# Check if source file exists
if not os.path.exists(source_path):
    print(f"ERROR: Source file '{source_path}' not found")
    sys.exit(1)


# 2. Load YAML → Python dict

with open(source_path, "r") as source_file:
    try:
        data = yaml.safe_load(source_file)
    except yaml.YAMLError as e:
        print(f"ERROR: '{source_path}' is not valid YAML")
        print("Details:")
        print(e)
        sys.exit(1)


# 3. Decide where to send JSON

if len(sys.argv) < 3:
    # No target file specified → print JSON to screen
    print("No target JSON file specified — printing JSON:\n")
    print(json.dumps(data, indent=4))
    sys.exit(0)

target_path = sys.argv[2]

# 2.2 Check the target file doesn't already exist
if os.path.exists(target_path):
    print(f"ERROR: Target file '{target_path}' already exists. Not overwriting.")
    sys.exit(1)

# 2.3 Save JSON to file
with open(target_path, "w") as target_file:
    json.dump(data, target_file, indent=4)

print(f"SUCCESS: JSON saved to {target_path}")
