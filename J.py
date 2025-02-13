import json
with open('sample-data.json') as file:
    d = json.load(file)
print("Interface Status")
print("=" * 120)
print("{:<50} {:<20} {:<10} {:<5}".format("DN", "Description", "Speed", "MTU"))
print("-" * 120)
for intr in d["imdata"]:
    a = intr["l1PhysIf"]["attributes"]
    dn = a.get("dn")
    desc = a.get("descr")  
    speed = a.get("speed", "inherit") 
    mtu = a.get("mtu")
    print("{:<50} {:<20} {:<10} {:<5}".format(dn, desc, speed, mtu))
