import json

file_path = r"C:/Users/Daulet/Downloads/sample-data.json"  


with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 70)
print(f"{'DN':<50} {'Description':<20} {'Speed':<10} {'MTU':<5}")
print("-" * 70)


for item in data["imdata"]:
    attr = item["l1PhysIf"]["attributes"]
    dn = attr["dn"]
    description = attr.get("descr", "") 
    speed = attr["speed"]
    mtu = attr["mtu"]

    
    print(f"{dn:<50} {description:<20} {speed:<10} {mtu:<5}")
