import os
import time
import json
import concurrent.futures
# 对于so文件的提取
# 没有lib文件夹就打标为NULL

# 多进程 每次处理20个 开16进程 2.0976274013519287
apkfilename = []
permission_frequency={}
path = r'E:\pythonProject\Experiment\out_benign_samples'
apk_list=os.listdir(path)
for apk in apk_list:
    apk = os.path.join(path,apk)
    apkfilename.append(apk)

def get_so(dir, packagelist):
    newdir = dir
    if os.path.isfile(dir):  # 如果是文件
        name = dir.split("apk")[-1][5:-3]
        if name not in packagelist:
           packagelist.append(name)
    elif os.path.isdir(dir):  # 如果是文件夹
        for s in os.listdir(dir):
            newdir = os.path.join(dir, s)
            get_so(newdir, packagelist)

def  extract_so(apk_filename):
    allfile = os.listdir(apk_filename)
    soinfo = []
    if "lib" not in allfile:
        soinfo.append("Null")
    else:
        dir = os.path.join(apk_filename ,"lib")
        get_so(dir, soinfo)
    filename = os.path.basename(apk_filename)
    # print({f"{filename}": soinfo})
    return {f"{filename}": soinfo}

if __name__ == "__main__":
    begin = time.time()
    apkinfo = []  # 存放一组的字典信息
    for i in range(0,1+1):
        apk_filename = apkfilename[20 * i:20 * i + 20]
        with concurrent.futures.ProcessPoolExecutor(max_workers=16) as pool:
            futures = [pool.submit(extract_so, filename) for filename in apk_filename]
        for future in futures:
            apkinfo.append(future.result())

    with open(r'E:\pythonProject\Experiment\Test\data_so.json', 'w') as f:
        json.dump(apkinfo, f)
    with open(r'E:\pythonProject\Experiment\Test\data_so.json', 'r') as f:
        data = json.load(f)
    end = time.time()
    consume = end - begin
    print(data)
    print(len(data))
    print(consume)

