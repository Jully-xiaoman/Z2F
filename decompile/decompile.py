import multiprocessing
import threading
import os
import time
import concurrent.futures
# 多线程反编译函数
# @Jully_xiaoman
def multi_decompile(apk_list):
    threads = []
    for filename in apk_list:
       inputpath = os.path.join(path, filename)
       outputpath = os.path.join(outpath, filename)
       threads.append(threading.Thread(target=decompilation,args=(inputpath,outputpath)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

def decompilation(inputpath, outputpath):
    command = "apktool d {0} -o {1}".format(inputpath, outputpath)
    os.system(command)


if __name__ == "__main__":
    # 池化多线程
    path = r'E:\pythonProject\Experiment\benign_samples'
    outpath = r"E:\pythonProject\Experiment\out_benign_samples"
    apklist = os.listdir(path)
    time_start = time.time()
    for i in range(0,8+1):
        apk_list=apklist[5*i:5*i+5]
        multi_decompile(apk_list)
    time_end = time.time()
    total_time = time_end - time_start
    print(total_time)


