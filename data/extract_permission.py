import os
import json
import concurrent.futures
import time
from collections import defaultdict
# 提取permission ，并统计频次
# 此处的filename传入的是反编译后的apk文件名
# 遍历提取每个文件的permission并存储
# 写多线程

# 多进程 一次处理20个 开16进程：
permission_frequency = {} #统计所有权限出现的频次
apkfilename = [] #带绝对路径的文件名列表
path = r'E:\pythonProject\Experiment\out_benign_samples'
apk_list=os.listdir(path)
for apk in apk_list:
    apk = os.path.join(path,apk)
    apkfilename.append(apk)

def extract_permission(apk_filename):
    xml_filename=os.path.join(apk_filename,"AndroidManifest.xml")
    f = open(xml_filename, encoding='UTF-8', errors="ignore")
    contents = f.read()
    outList = contents.split('\n')
    listtem = []
    for line in outList:
        line = line.replace(" ", "")
        if line.startswith('<uses-permissionandroid:') and ("android.permission") in line:
            s_permission = line.split(':')[1].split('\"')[1].split('.')[2].replace(" ", "").upper()
            if (s_permission not in listtem):
                listtem.append(s_permission)
    filename = os.path.basename(apk_filename)
    return {f"{filename}": listtem}


if __name__ == "__main__":
    begin = time.time()
    apkinfo = []  # 存放所有提取出的信息，每一个元素是字典类型，键是文件名，键值是提取出的权限信息
    for i in range(0,1+1):
        apk_filename = apkfilename[20 * i:20 * i + 20]
        with concurrent.futures.ProcessPoolExecutor(max_workers=16) as pool:
            futures = [pool.submit(extract_permission, filename) for filename in apk_filename]
        for future in futures:
            apkinfo.append(future.result())
    with open(r'E:\pythonProject\Experiment\Test\data_permission.json', 'w') as f:
        json.dump(apkinfo, f)
    # with open('Trash/data_permission.json', 'r') as f:
    #     data = json.load(f)
    end = time.time()
    consume = end - begin
    # print(data)
    # print(len(data))
    print(consume)
