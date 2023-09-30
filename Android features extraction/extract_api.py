import os
import time
import concurrent.futures
import json


apkinfo_api = [] #存放一组字典信息
apkfilename = []
path = r'E:\pythonProject\Experiment\out_benign_samples'
apk_list = os.listdir(path)
for apk in apk_list:
    apk = os.path.join(path, apk)
    apkfilename.append(apk)
apiheadlist=["Landroid/", "Lcom/android/internal/util", "Ldalvik/", "Ljava/", "Ljavax/", "Lorg/apache/",
                  "Lorg/json/", "Lorg/w3c/dom/", "Lorg/xml/sax", "Lorg/xmlpull/v1/", "Ljunit/"]

# dir进的是smali目录
def GetSmaliFileList(dir, fileList):
    newDir = dir
    if os.path.isfile(dir):  # 如果是文件
        fileList.append(dir)
    elif os.path.isdir(dir):
        for s in os.listdir(dir):  # 如果是文件夹
            newDir = os.path.join(dir, s)
            GetSmaliFileList(newDir, fileList)
    return fileList


def extract_api(apk_filename):
    apilist = []
    fileList = []
    dir = os.path.join(apk_filename,"smali")
    fileList = GetSmaliFileList(dir, fileList)
    for per_smalifile in fileList:
        f = open(per_smalifile, encoding='UTF-8')
        contents = f.read()
        contentslist = contents.split("\n")
        for line in contentslist:
            if "invoke" in line:
                invoke_line = line.split(',')[-1].replace(" ", "").split("(")[0]
                for s_apihead in apiheadlist:
                    if invoke_line.startswith(s_apihead):
                        s_api = invoke_line
                        if (s_api not in apilist):
                            apilist.append(s_api)
    filename = os.path.basename(apk_filename)
    print(f"{filename}已处理完毕")
    return {f"{filename}": apilist}

if __name__ == "__main__":
    start = time.time()
    apkinfo_api = []
    for i in range(0, 1+ 1):
        apk_filename = apkfilename[20 * i:20 * i + 20]
        with concurrent.futures.ProcessPoolExecutor(max_workers=16) as pool:
            futures = [pool.submit(extract_api, filename) for filename in apk_filename]
            for future in futures:
                apkinfo_api.append(future.result())
    with open(r'E:\pythonProject\Experiment\Test\data_api.json', 'w') as f:
        json.dump(apkinfo_api, f)
    # with open(r'E:\pythonProject\Experiment\Test\data_api.json', 'r') as f:
    #     data = json.load(f)
    #     print(len(data))
    end = time.time()
    consume = end - start
    print(consume)