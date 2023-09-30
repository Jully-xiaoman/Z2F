import os
import json
import concurrent.futures
import time

# 多进程 每次处理20个 开16进程 7.231800556182861
# 多进程 新函数 16.66970205307007
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

def extract_super_new(apk_filename):
    super_list = []
    fileList = []
    dir = os.path.join(apk_filename, "smali")
    SmaliFileList = GetSmaliFileList(dir, fileList)
    for per_smalifile in SmaliFileList:
        with open(per_smalifile, encoding='UTF-8',errors="ignore") as myfile:
              head = [next(myfile) for x in range(2)]
              superline =head[1].split(" ")[-1].replace("\n","")
              if superline not in super_list:
                     super_list.append(superline)
    filename = os.path.basename(apk_filename)
    print(f"{filename}已处理完毕")
    # print({f"{filename}": super_list})
    return {f"{filename}": super_list}

if __name__ == "__main__":
    begin = time.time()
    apkinfo = []  # 存放一组的字典信息
    for i in range(0,1+1):
        apk_filename = apkfilename[20 * i:20 * i + 20]
        with concurrent.futures.ProcessPoolExecutor(max_workers=16) as pool:
            futures = [pool.submit(extract_super_new, filename) for filename in apk_filename]
        for future in futures:
            apkinfo.append(future.result())

    with open(r'E:\pythonProject\Experiment\Test\data_super.json', 'w') as f:
        json.dump(apkinfo, f)
    with open(r'E:\pythonProject\Experiment\Test\data_super.json', 'r') as f:
        data = json.load(f)
    end = time.time()
    consume = end - begin
    print(data)
    print(len(data))
    print(consume)


