import json

a = input("OPTIONEN:\n1] User ansehen")
if a == "1":
    file = open("debug.json", "r")
    data = json.load(file)
    g = data["user"]
    print(g)
