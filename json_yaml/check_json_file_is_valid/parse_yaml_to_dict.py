import yaml


# 1. Open the YAML file and load it as a dict

with open("servers.yaml", "r") as yaml_file:
    servers = yaml.safe_load(yaml_file)
    # yaml.safe_load() converts YAML → Python dictionary



# 2. Print the type of the "servers" variable

print("Type of 'servers':", type(servers))



# 3. Print server1 and server2 individually

print("Record for server1:")
print(servers["server1"])

print("Record for server2:")
print(servers["server2"])


# 4. Loop through all keys + values in dict

print("All keys and values")

for key, value in servers.items():
    # key = "server1", value = nested dict
    print(f"Key and value: '{key}' = '{value}'")

    # Loop through nested dictionary for each server
    for sub_key, sub_value in value.items():
        print(f"  Record key and sub value: '{sub_key}' = '{sub_value}'")
