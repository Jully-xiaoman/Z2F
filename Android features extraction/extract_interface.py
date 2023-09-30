import os
import json
import concurrent.futures
import time

apkfilename = []
permission_frequency={}
path = r'E:\pythonProject\Experiment\out_benign_samples'
apk_list=os.listdir(path)
for apk in apk_list:
    apk = os.path.join(path,apk)
    apkfilename.append(apk)

def GetSmaliFileList(dir, fileList):
    newDir = dir
    if os.path.isfile(dir):  # 如果是文件
        fileList.append(dir)
    elif os.path.isdir(dir):
        for s in os.listdir(dir):  # 如果是文件夹
            newDir = os.path.join(dir, s)
            GetSmaliFileList(newDir, fileList)
    return fileList

def extract_interface(apk_filename):
    InterfaceList = []
    fileList = []
    dir = os.path.join(apk_filename, "smali")
    SmaliFileList = GetSmaliFileList(dir, fileList)
    for per_smalifile in SmaliFileList:
        f = open(per_smalifile,encoding='utf-8', errors='ignore')
        contents = f.read()
        contentslist = contents.split("\n")
        for line in contentslist:
            if ".implements" in line:
                # per_interface = line.split(" ")[-1][1:]
                per_interface = line.split(" ")[-1]
                if "$" in per_interface:
                    per_interface = per_interface.split("$")[0]
                if per_interface not in InterfaceList:
                    InterfaceList.append(per_interface)
    filename = os.path.basename(apk_filename)
    print(f"{filename}已处理完毕")
    return {f"{filename}": InterfaceList}

if __name__ == "__main__":
    begin = time.time()
    apkinfo = []  # 存放一组的字典信息
    for i in range(0,1+1):
        apk_filename = apkfilename[20 * i:20 * i + 20]
        with concurrent.futures.ProcessPoolExecutor(max_workers=16) as pool:
            futures = [pool.submit(extract_interface, filename) for filename in apk_filename]
        for future in futures:
            apkinfo.append(future.result())

    with open(r'E:\pythonProject\Experiment\Test\data_interface.json', 'w') as f:
        json.dump(apkinfo, f)
    with open(r'E:\pythonProject\Experiment\Test\data_interface.json', 'r') as f:
        data = json.load(f)

    end = time.time()
    consume = end - begin
    print(data)
    print(len(data))
    print(consume)