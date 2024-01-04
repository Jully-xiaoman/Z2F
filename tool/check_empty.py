import json

trashlist = []
filename0 = r"E:\experiment\mal\super\super3.json"
filename1 = r"E:\experiment\mal\super\super3trash.json"
with open(filename0, 'r') as f:
    data = json.load(f)
print(len(data))
for i in data:
    if bool( list(i.values())[0] ) == False:
        trashlist.append(list(i.keys())[0])
with open(filename1, 'w') as f1:
    json.dump(trashlist,f1)
print(trashlist)
print(len(trashlist))


