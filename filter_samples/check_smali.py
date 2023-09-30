import os
import time
import concurrent.futures
import json

# 该函数用于检查反编译后没有samli文件的apk,没有smali文件的apk就记为废物样本
path = r'E:\pythonProject\Experiment\out_benign_samples'
allapkfiles = os.listdir(path)

def check(apkfilename):
    abspath = os.path.join(path, apkfilename)
    files = os.listdir(abspath)
    if "smali" not in files:
        return apkfilename
    else:
        return 0

if __name__ == "__main__":
    # 生成带路径的文件名
    start = time.time()
    apkfilenames = []
    needremove = []
    for i in range(0, 1+ 1):
        apk_filename = allapkfiles[20 * i:20 * i + 20]
        with concurrent.futures.ProcessPoolExecutor(max_workers=16) as pool:
            futures = [pool.submit(check, filename) for filename in apk_filename]
            for future in futures:
                apkfilenames.append(future.result())
    pool.shutdown(True)
    for item in apkfilenames:
        if item != 0:
            needremove.append(item)
    with open('check_no_smali.json', 'w') as f:
        json.dump(needremove, f)
    with open('check_no_smali.json', 'r') as f:
        data = json.load(f)
        print(len(data))
    end = time.time()
    consume = end - start
    print(consume)

    # check(r'E:\pythonProject\Experiment\out_benign_samples\hahah')
    # print("shun")