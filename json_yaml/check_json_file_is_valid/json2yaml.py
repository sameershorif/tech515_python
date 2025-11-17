import json
import os
import sys
import yaml


# VALIDATE INPUT ARGUMENTS

# Expected usage:
#python json2yaml.py source.json target.yaml
#
# sys.argv[1] = source file
# sys.argv[2] = target file (optional)

if len(sys.argv) > 1:
    source_path = sys.argv[1]

    # Check source file exists
    if os.path.exists(source_path):
        with open(source_path, "r") as source_file:
            source_content = json.load(source_file)
            # Converts JSON → Python dictionary
    else:
        print("ERROR: " + source_path + " not found")
        exit(1)
else:
    print("ERROR: No JSON file was specified")
    print("Usage: json2yaml.py <source_file.json> <target_file.yaml>")
    exit(1)


# CONVERT JSON OBJECT → YAML STRING

yaml_output = yaml.dump(
    source_content,
    default_flow_style=False,   # Makes YAML look clean & multi-line
    sort_keys=False             # Keeps original JSON order
)


# SAVE YAML TO FILE (OR PRINT IF NO TARGET FILE)

# sys.argv[2] is optional
if len(sys.argv) < 3:
    # No target file provided → print YAML to screen
    print("No YAML output file specified — printing YAML:")
    print("\n" + yaml_output)
    exit(0)

target_path = sys.argv[2]

#  Check that target file doesn't already exist
if os.path.exists(target_path):
    print(f"ERROR: Target file '{target_path}' already exists. Not overwriting.")
    exit(1)

# 2.3 Save YAML to file
with open(target_path, "w") as target_file:
    target_file.write(yaml_output)

print(f"SUCCESS: YAML saved to {target_path}")