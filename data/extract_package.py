import os
import json
import concurrent.futures
import time

# 多进程 原始提取函数:18.002195835113525
# 多进程 改造提取函数:8.507536172866821
apkfilename = []
permission_frequency={}
path = r'E:\pythonProject\Experiment\out_benign_samples'
apk_list=os.listdir(path)
for apk in apk_list:
    apk = os.path.join(path,apk)
    apkfilename.append(apk)

def get(dir, packagelist):
    newdir = dir
    if os.path.isfile(dir):  # 如果是文件
        name = os.path.dirname(dir).split("smali")[-1]
        if name not in packagelist:
           packagelist.append(name)
    elif os.path.isdir(dir):  # 如果是文件夹
        for s in os.listdir(dir):
            newdir = os.path.join(dir, s)
            get(newdir, packagelist)
    return packagelist

def extract_package(apk_filename):
    package_list = []
    dir = os.path.join(apk_filename, "smali")
    packagelist = get(dir, package_list)
    filename = os.path.basename(apk_filename)
    print(f"{filename}已处理完毕")
    # print({f"{filename}": package_list})
    return {f"{filename}": packagelist}


if __name__ == "__main__":
    begin = time.time()
    apkinfo = []  # 存放一组的字典信息
    for i in range(0,1+1):
        apk_filename = apkfilename[20 * i:20 * i + 20]
        with concurrent.futures.ProcessPoolExecutor(max_workers=16) as pool:
            futures = [pool.submit(extract_package, filename) for filename in apk_filename]
        for future in futures:
            apkinfo.append(future.result())

    with open(r'E:\pythonProject\Experiment\Test\data_package_new.json', 'w') as f:
        json.dump(apkinfo, f)
    with open(r'E:\pythonProject\Experiment\Test\data_package_new.json', 'r') as f:
        data = json.load(f)
    end = time.time()
    consume = end - begin
    print(data)
    print(len(data))
    print(consume)
   