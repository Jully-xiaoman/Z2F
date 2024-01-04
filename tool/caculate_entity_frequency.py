import json
# 传入总体的json文件，读取json文件的键值数据，一个一个遍历扫描
# 然后字典统计频次
def text_save(filename,allfilename, data, data1):
    file = open(filename,'a',encoding='utf8')
    for i in range(len(data)):
        s= str(data[i])+"\n"
        file.write(s)
    file.close()
    print("保存频率文件成功")
    with open(allfilename, 'w',encoding='utf8') as f:
        json.dump(data1, f)
    print("保存实体统计信息文件成功")

def calculate_permission_frequency(json_file, permission_frequency, frequencyfilename ,allfilename):
    all_permission_list = []
    with open(json_file, 'r') as f:
        data = json.load(f)
    for s_data in data:
        for key,value in s_data.items():
            for s_permission in value:
                    if s_permission not in permission_frequency:
                        permission_frequency[s_permission] = 1
                    else:
                        permission_frequency[s_permission] = permission_frequency[s_permission] + 1
    sorted_d = sorted(permission_frequency.items(), key=lambda x: x[1]) # 对权限频次进行升序排序
    # 遍历列表获取所有的权限信息
    for s in sorted_d:
        all_permission_list.append(s[0])
    text_save(frequencyfilename, allfilename, sorted_d, all_permission_list)

if __name__ == "__main__":
    # permission统计
    permission_frequency = {}
    json_file = r'E:\experiment\samples\permission.json'
    frequencyfilename = r'E:\experiment\frequencydata\frequency_permission.txt'
    allfilename = r'E:\experiment\frequencydata\all_permission.json'
    calculate_permission_frequency(json_file, permission_frequency, frequencyfilename ,allfilename)

    # api统计
    # permission_frequency = {}
    # json_file = r'E:\pythonProject\Experiment\Test\update_api.json'
    # frequencyfilename = r'E:\pythonProject\Experiment\Test\frequency_api.txt'
    # allfilename = r'E:\pythonProject\Experiment\Test\all_api.json'
    # calculate_permission_frequency(json_file, permission_frequency, frequencyfilename, allfilename)

    # interface统计
    # permission_frequency = {}
    # json_file = r'E:\pythonProject\Experiment\Test\update_interface.json'
    # frequencyfilename = r'E:\pythonProject\Experiment\Test\frequency_interface.txt'
    # allfilename = r'E:\pythonProject\Experiment\Test\all_interface.json'
    # calculate_permission_frequency(json_file, permission_frequency, frequencyfilename, allfilename)

    # package统计
    # permission_frequency = {}
    # json_file = r'E:\pythonProject\Experiment\Test\update_package.json'
    # frequencyfilename = r'E:\pythonProject\Experiment\Test\frequency_package.txt'
    # allfilename = r'E:\pythonProject\Experiment\Test\all_package.json'
    # calculate_permission_frequency(json_file, permission_frequency, frequencyfilename, allfilename)

    # super统计
    # permission_frequency = {}
    # json_file = r'E:\pythonProject\Experiment\Test\update_super.json'
    # frequencyfilename = r'E:\pythonProject\Experiment\Test\frequency_super.txt'
    # allfilename = r'E:\pythonProject\Experiment\Test\all_super.json'
    # calculate_permission_frequency(json_file, permission_frequency, frequencyfilename, allfilename)

    # so统计
    # permission_frequency = {}
    # json_file = r'E:\pythonProject\Experiment\Test\update_so.json'
    # frequencyfilename = r'E:\pythonProject\Experiment\Test\frequency_so.txt'
    # allfilename = r'E:\pythonProject\Experiment\Test\all_so.json'
    # calculate_permission_frequency(json_file, permission_frequency, frequencyfilename, allfilename)