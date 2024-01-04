import json

json_file = r"E:\experiment\samples\api.json"
count_file = r"E:\experiment\frequencydata\all_api.json"
entitylist = []
with open(json_file, 'r') as f0:
    data = json.load(f0)
for i in data:
    info = list(i.values())[0]
    for s_info in info:
        if s_info not in entitylist:
            entitylist.append(s_info)
print(len(entitylist))
with open(count_file, 'w') as f1:
     json.dump(entitylist,f1)