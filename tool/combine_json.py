# 合并所有json文件，良性为一组，恶性为一组
import json
# finalsamples = []
# filename0 = r"E:\experiment\mal\api\api1final.json"
# filename1 = r"E:\experiment\mal\api\api2final.json"
# filename2 = r"E:\experiment\mal\api\api3final.json"
# filename3 = r"E:\experiment\benign\super\4superfinal.json"
# filename4 = r"E:\experiment\benign\super\5superfinal.json"
# filename5 = r"E:\experiment\benign\super\6superfinal.json"
# filenamefinal = r"E:\experiment\benign\super\benign_super.json"
# with open(filename0, 'r') as f0:
#     data0 = json.load(f0)
# with open(filename1, 'r') as f1:
#     data1 = json.load(f1)
# with open(filename2, 'r') as f2:
#     data2 = json.load(f2)
# with open(filename3, 'r') as f3:
#     data3 = json.load(f3)
# with open(filename4, 'r') as f4:
#     data4 = json.load(f4)
# with open(filename5, 'r') as f5:
#     data5 = json.load(f5)
# for i0 in data0:
#     finalsamples.append(i0)
# for i1 in data1:
#     finalsamples.append(i1)
# for i2 in data2:
#     finalsamples.append(i2)
# for i3 in data3:
#     finalsamples.append(i3)
# for i4 in data4:
#     finalsamples.append(i4)
# for i5 in data5:
#     finalsamples.append(i5)
# print(len(finalsamples))
# # print(trashsamples)
# with open(filenamefinal, 'w') as f6:
#     json.dump(finalsamples,f6)



# for i in data0:
#     if list(i.keys())[0] not in data1:
#         finalsample.append(i)
# print(len(finalsample))
# with open(filename2, 'w') as f2:
#     json.dump(finalsample,f2)

# filename0 = r"E:\experiment\mal\super\super1final.json"
# filename1 = r"E:\experiment\mal\super\super2final.json"
# filename2 = r"E:\experiment\mal\package\package3final.json"
# filenamefinal = r"E:\experiment\mal\api\mal_super.json"
# with open(filename0, 'r') as f0:
#     data0 = json.load(f0)
# with open(filename1, 'r') as f1:
#     data1 = json.load(f1)
# with open(filename2, 'r') as f2:
#     data2 = json.load(f2)
#     print(len(data2))
# for i0 in data0:
#     finalsamples.append(i0)
# for i1 in data1:
#     finalsamples.append(i1)
# for i2 in data2:
#     finalsamples.append(i2)
# print(len(finalsamples))
# with open(filenamefinal, 'w') as f6:
#     json.dump(finalsamples,f6)

filename0 = r"E:\experiment\benign\benign_super.json"
filename1 = r"E:\experiment\mal\mal_super.json"
filename = r"E:\experiment\samples\super.json"
finalsamples = []
with open(filename0, 'r') as f0:
    data0 = json.load(f0)
with open(filename1, 'r') as f1:
    data1 = json.load(f1)
for i0 in data0:
    finalsamples.append(i0)
for i1 in data1:
    finalsamples.append(i1)
print(len(finalsamples))
with open(filename, 'w') as f6:
    json.dump(finalsamples,f6)
