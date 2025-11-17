import json


# 1. Open the JSON file and load it into dict

with open("servers.json", "r") as json_file:
    servers = json.load(json_file)
    # json.load() converts JSON file → Python dictionary



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
    # key = "server1", value = nested dict for that server
    print(f"Key and value: '{key}' = '{value}'")

    # Loop through nested dictionary inside each server record
    for sub_key, sub_value in value.items():
        print(f"  Record key and sub value: '{sub_key}' = '{sub_value}'")