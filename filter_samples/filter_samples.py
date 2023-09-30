import json

# 优势在于从json文件层面把废物样本信息给剔除了，而不是从系统层面把文件删除。


# 该函数用于删除废物样本
# file1是所有实体打标文件
# file2是需要删除的样本名称文件
# final是最终的样本数据文件
# 需要删除7次

def delete_trashsample(file1,file2,final):
    final_samples = []
    with open(file1, 'r') as f:
        data = json.load(f)
    with open(file2, 'r') as f:
        data2 = json.load(f)
    for s in data:
      name = list(s.keys())[0]
      if name not in data2:
            final_samples.append(s)
    print("最终样本长度为：",len(final_samples))
    with open(final, 'w') as f:
        json.dump(final_samples, f)
    print("样本已清理完毕")

if __name__ == "__main__":
    # api进行废物样本删除
    # file1 = r"E:\pythonProject\Experiment\Test\data_api.json" # 融合文件名
    # file2 = r"E:\pythonProject\Experiment\Test\check_no_smali.json"# 没有smali的废物样本文件名
    # final = r"E:\pythonProject\Experiment\Test\update_api.json" # 经过去重的保留样本文件名
    # delete_trashsample(file1, file2, final)

    # permission进行废物样本删除
    # file1 = r"E:\pythonProject\Experiment\Test\data_permission.json"  # 融合文件名
    # file2 = r"E:\pythonProject\Experiment\Test\check_no_smali.json"  # 没有smali的废物样本文件名
    # final = r"E:\pythonProject\Experiment\Test\update_permission.json"  # 经过去重的保留样本文件名
    # delete_trashsample(file1, file2, final)

    # data_permission_permissiontype.json进行废物样本删除
    # file1 = r"E:\pythonProject\Experiment\Test\data_permission_permissiontype.json"  # 融合文件名
    # file2 = r"E:\pythonProject\Experiment\Test\check_no_smali.json"  # 没有smali的废物样本文件名
    # final = r"E:\pythonProject\Experiment\Test\update_permission_permissiontype.json"  # 经过去重的保留样本文件名
    # delete_trashsample(file1, file2, final)

    # data_package.json进行废物样本删除
    # file1 = r"E:\pythonProject\Experiment\Test\data_package.json"  # 融合文件名
    # file2 = r"E:\pythonProject\Experiment\Test\check_no_smali.json"  # 没有smali的废物样本文件名
    # final = r"E:\pythonProject\Experiment\Test\update_package.json"  # 经过去重的保留样本文件名
    # delete_trashsample(file1, file2, final)

    # data_so.json进行废物样本删除
    # file1 = r"E:\pythonProject\Experiment\Test\data_so.json"  # 融合文件名
    # file2 = r"E:\pythonProject\Experiment\Test\check_no_smali.json"  # 没有smali的废物样本文件名
    # final = r"E:\pythonProject\Experiment\Test\update_so.json"  # 经过去重的保留样本文件名
    # delete_trashsample(file1, file2, final)

    # data_super.json进行废物样本删除
    # file1 = r"E:\pythonProject\Experiment\Test\data_super.json"  # 融合文件名
    # file2 = r"E:\pythonProject\Experiment\Test\check_no_smali.json"  # 没有smali的废物样本文件名
    # final = r"E:\pythonProject\Experiment\Test\update_super.json"  # 经过去重的保留样本文件名
    # delete_trashsample(file1, file2, final)

    # data_interface.json进行废物样本删除
    file1 = r"E:\pythonProject\Experiment\Test\data_interface.json"  # 融合文件名
    file2 = r"E:\pythonProject\Experiment\Test\check_no_smali.json"  # 没有smali的废物样本文件名
    final = r"E:\pythonProject\Experiment\Test\update_interface.json"  # 经过去重的保留样本文件名
    delete_trashsample(file1, file2, final)

