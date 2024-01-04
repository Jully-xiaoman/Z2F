import json

finalsample = []
filename0 = r"E:\experiment\mal\super\super3.json"
filename1 = r"E:\experiment\mal\trash3.json"
filename2 = r"E:\experiment\mal\super\super3final.json"
with open(filename0, 'r') as f0:
    data0 = json.load(f0)
with open(filename1, 'r') as f1:
    data1 = json.load(f1)
for i in data0:
    if list(i.keys())[0] not in data1:
        finalsample.append(i)
print(len(finalsample))
with open(filename2, 'w') as f2:
    json.dump(finalsample,f2)

# trashsamples = []
# filename0 = r"E:\experiment\benign\api\6apitrash.json"
# filename1 = r'E:\experiment\benign\interface\6interfacetrash.json'
# filename2 = r"E:\experiment\benign\package\6packagetrash.json"
# filename3 = r"E:\experiment\benign\permission\6permissiontrash.json"
# filename4 = r"E:\experiment\benign\super\6supertrash.json"
# filenamefinal =r"E:\experiment\benign\trash6.json"
# with open(filename0, 'r') as f0:
#     data0 = json.load(f0)
# with open(filename1, 'r') as f0:
#     data1 = json.load(f0)
# with open(filename2, 'r') as f0:
#     data2 = json.load(f0)
# with open(filename3, 'r') as f0:
#     data3 = json.load(f0)
# with open(filename4, 'r') as f0:
#     data4 = json.load(f0)
# for i0 in data0:
#     if i0 not in trashsamples:
#         trashsamples.append(i0)
# for i1 in data1:
#     if i1 not in trashsamples:
#         trashsamples.append(i1)
# for i0 in data0:
#     if i0 not in trashsamples:
#         trashsamples.append(i0)
# for i3 in data3:
#     if i3 not in trashsamples:
#         trashsamples.append(i3)
# for i4 in data4:
#     if i4 not in trashsamples:
#         trashsamples.append(i4)
# print(len(trashsamples))
# print(trashsamples)
# with open(filenamefinal, 'w') as f5:
#     json.dump(trashsamples,f5)
#

# trashsamples = []
# filename0 = r"E:\experiment\mal\api\api3trash.json"
# filename1 = r'E:\experiment\mal\interface\interface3trash.json'
# filename2 = r"E:\experiment\mal\package\package3trash.json"
# filename3 = r"E:\experiment\mal\permission\permission3trash.json"
# filename4 = r"E:\experiment\mal\super\super3trash.json"
# filenamefinal =r"E:\experiment\mal\trash3.json"
# with open(filename0, 'r') as f0:
#     data0 = json.load(f0)
# with open(filename1, 'r') as f0:
#     data1 = json.load(f0)
# with open(filename2, 'r') as f0:
#     data2 = json.load(f0)
# with open(filename3, 'r') as f0:
#     data3 = json.load(f0)
# with open(filename4, 'r') as f0:
#     data4 = json.load(f0)
# for i0 in data0:
#     if i0 not in trashsamples:
#         trashsamples.append(i0)
# for i1 in data1:
#     if i1 not in trashsamples:
#         trashsamples.append(i1)
# for i0 in data0:
#     if i0 not in trashsamples:
#         trashsamples.append(i0)
# for i3 in data3:
#     if i3 not in trashsamples:
#         trashsamples.append(i3)
# for i4 in data4:
#     if i4 not in trashsamples:
#         trashsamples.append(i4)
# print(len(trashsamples))
# print(trashsamples)
# with open(filenamefinal, 'w') as f5:
#     json.dump(trashsamples,f5)

