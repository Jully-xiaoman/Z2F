import os
import concurrent.futures
import json
import time


# json里存的是列表，列表里存放的每个元素是字典，需要按照json的文件名顺序输出对应的权限类型
# 一次匹配一个,普通权限权限类型就是0
# 单线程的已经写完了，开始写多进程
# 单进程花费时间：consume= 0.0030291080474853516
# 多线程花费时间：consume= 0.7890021800994873
def match(dict):
    apkname = list(dict.keys())[0]
    permissiontype = []
    for key,value in dict.items():
       for s_permission in value:
          if is_dangerous(s_permission):
             permissiontype.append(group_match(s_permission))# 判断属于哪个权限组
          else:
             permissiontype.append("Normal") # 普通权限建议修改为normal
    dict[apkname]=permissiontype
    return dict        # 判断是否是危险权限


def is_dangerous(permission):
    dangerous_permission = ['READ_CALENDAR', 'WRITE_CALENDAR','CAMERA','READ_CONTACTS', 'WRITE_CONTACTS', 'GET_ACCOUNTS','ACCESS_FINE_LOCATION', 'ACCESS_COARSE_LOCATION',
                            'RECORD_AUDIO','READ_PHONE_STATE','CALL_PHONE', 'READ_CALL_LOG', 'WRITE_CALL_LOG', 'ADD_VOICEMAIL', 'USE_SIP', 'PROCESS_OUTGOING_CALLS','BODY_SENSORS',
                            'SEND_SMS', 'RECEIVE_SMS', 'READ_SMS', 'RECEIVE_WAP_PUSH','RECEIVE_MMS','READ_EXTERNAL_STORAGE', 'WRITE_EXTERNAL_STORAGE']
    if permission in dangerous_permission:
        return 1
    else:
        return 0

def group_match(s_permission):
    d = {'CALENDAR': ['READ_CALENDAR', 'WRITE_CALENDAR'], 'CAMERA': ['CAMERA'],
                                       'CONTACTS': ['READ_CONTACTS', 'WRITE_CONTACTS', 'GET_ACCOUNTS'],
                                       'LOCATION': ['ACCESS_FINE_LOCATION', 'ACCESS_COARSE_LOCATION'],
                                       'MICROPHONE': ['RECORD_AUDIO'],
                                       'PHONE': ['READ_PHONE_STATE', 'CALL_PHONE',
                                                 'READ_CALL_LOG', 'WRITE_CALL_LOG', 'ADD_VOICEMAIL', 'USE_SIP',
                                                 'PROCESS_OUTGOING_CALLS'],
                                       'SENSORS': ['BODY_SENSORS'],
                                       'SMS': ['SEND_SMS', 'RECEIVE_SMS', 'READ_SMS', 'RECEIVE_WAP_PUSH',
                                               'RECEIVE_MMS'],
                                       'STORAGE': ['READ_EXTERNAL_STORAGE', 'WRITE_EXTERNAL_STORAGE']}
    for k, v in d.items():
            if s_permission in v:
                return k

if __name__ == "__main__":
    start = time.time()
    permissiontype = []
    with open(r'E:\pythonProject\Experiment\Test\data_permission.json', 'r') as f:
        data = json.load(f)
    for s_data in data:
        permissiontype.append(match(s_data))
    with open(r'E:\pythonProject\Experiment\Test\data_permission_permissiontype.json', 'w') as f:
        json.dump(permissiontype,f)
    end = time.time()
    print("consume=",end - start)


    # with open('Trash/data_permission_permissiontype.json', 'r') as f:
    #     data1 = json.load(f)
    #     print(data1)

    # with open('data_permission.json', 'r') as f:
    #     data = json.load(f)
    # with concurrent.futures.ProcessPoolExecutor(max_workers=16) as pool:
    #     futures = [pool.submit(match, dict) for dict in data]
    #     for future in futures:
    #         permissiontype.append(future.result())
    # pool.shutdown(True)
    # end = time.time()
    # print("consume=",end - start)
    # with open('data_permission_permissiontype.json', 'w') as f:
    #     json.dump(permissiontype,f)
    # with open('data_permission_permissiontype.json', 'r') as f:
    #     data1 = json.load(f)
    #     print(data1)
