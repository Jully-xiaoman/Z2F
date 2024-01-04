import json
import numpy as np
import scipy.io as scio
import scipy.sparse
from scipy import sparse
# 该函数用于打标矩阵
# 先构造矩阵，行×列，其中行就是app应用程序的个数，列就是统计出的实体的个数
# 构造的矩阵应该是全0矩阵。
# 一个app一个app进行打标，读取一个app的实体信息后，若这个实体信息在总的矩阵里，就把第几个位置打标为1，
# 先把权限的做出来
# 提取信息，然后打标
def read_info(apkname,data2):
    allindex = []
    value = list(apkname.values())[0]
    for v in value:
       if v in data2:
        index = data2.index(v)
        allindex.append(index)
    return allindex

# 需要一个参数控制M的行数
def marking(allindex , raw, M):
    for i in allindex:
        M[raw , i] = 1
    return M


if __name__ == "__main__":
    # permission打标
    # json_file1 = r'E:\experiment\samples\permission.json'
    # json_file2 = r"E:\experiment\frequencydata\count_permission.json"
    # permission_mat = r"E:\experiment\matrix\matrix_permission.npz"
    # with open(json_file1, 'r', encoding='utf-8') as f1:
    #     data1 = json.load(f1)
    # with open(json_file2, 'r', encoding='utf-8') as f2:
    #     data2 = json.load(f2)
    # appnum = len(data1)
    # entitynum = len(data2)
    # M = np.zeros((appnum, entitynum))
    # raw = 0
    # for i1 in data1:
    #         allindex = read_info(i1, data2)
    #         M = marking(allindex, raw, M)
    #         print("第"+str(raw)+"个apk已打标完毕")
    #         raw = raw +1
    # M_sp= scipy.sparse.csr_matrix(M)
    # sparse.save_npz(permission_mat, M_sp)  # 保存稀疏矩阵
    # #scio.savemat(permission_mat, {'permission': M})
    # print("permission矩阵已打标结束")

    # interface打标
    # json_file1 = r'E:\experiment\samples\interface.json'
    # json_file2 = r"E:\experiment\frequencydata\count_interface.json"
    # permission_mat = r"E:\experiment\matrix\matrix_interface.npz"
    # with open(json_file1, 'r', encoding='utf-8') as f1:
    #     data1 = json.load(f1)
    # with open(json_file2, 'r', encoding='utf-8') as f2:
    #     data2 = json.load(f2)
    # appnum = len(data1)
    # entitynum = len(data2)
    # M = np.zeros((appnum, entitynum))
    # raw = 0
    # for i1 in data1:
    #     allindex = read_info(i1, data2)
    #     M = marking(allindex, raw, M)
    #     print("第" + str(raw) + "个apk已打标完毕")
    #     raw = raw + 1
    # M_sp= scipy.sparse.csr_matrix(M)
    # sparse.save_npz(permission_mat, M_sp)  # 保存稀疏矩阵
    # # scio.savemat(permission_mat, {'permission': M_sp})
    # print("interface矩阵已打标结束")

    # package打标
    # json_file1 = r'E:\experiment\samples\package.json'
    # json_file2 = r"E:\experiment\frequencydata\count_package.json"
    # permission_mat = r"E:\experiment\matrix\matrix_package.npz"
    # with open(json_file1, 'r', encoding='utf-8') as f1:
    #     data1 = json.load(f1)
    # with open(json_file2, 'r', encoding='utf-8') as f2:
    #     data2 = json.load(f2)
    # appnum = len(data1)
    # entitynum = len(data2)
    # M = np.zeros((appnum, entitynum))
    # raw = 0
    # for i1 in data1:
    #     allindex = read_info(i1, data2)
    #     M = marking(allindex, raw, M)
    #     print("第" + str(raw) + "个apk已打标完毕")
    #     raw = raw + 1
    # M_sp = scipy.sparse.csr_matrix(M)
    # sparse.save_npz(permission_mat, M_sp)  # 保存稀疏矩阵
    # # scio.savemat(permission_mat, {'permission': M})
    # print("package矩阵已打标结束")

    # super打标
    # json_file1 = r'E:\experiment\samples\super.json'
    # json_file2 = r"E:\experiment\frequencydata\count_super.json"
    # permission_mat = r"E:\experiment\matrix\matrix_super.npz"
    # with open(json_file1, 'r', encoding='utf-8') as f1:
    #     data1 = json.load(f1)
    # with open(json_file2, 'r', encoding='utf-8') as f2:
    #     data2 = json.load(f2)
    # appnum = len(data1)
    # entitynum = len(data2)
    # M = np.zeros((appnum, entitynum))
    # raw = 0
    # for i1 in data1:
    #     allindex = read_info(i1, data2)
    #     M = marking(allindex, raw, M)
    #     print("第" + str(raw) + "个apk已打标完毕")
    #     raw = raw + 1
    # M_sp = scipy.sparse.csr_matrix(M)
    # sparse.save_npz(permission_mat, M_sp)  # 保存稀疏矩阵
    # #scio.savemat(permission_mat, {'permission': M})
    # print("super矩阵已打标结束")

    # api打标
    json_file1 = r'E:\experiment\samples\api.json'
    json_file2 = r"E:\experiment\frequencydata\count_api.json"
    permission_mat = r"E:\experiment\matrix\matrix_api_mal.npz"
    with open(json_file1, 'r', encoding='utf-8') as f1:
        data1 = json.load(f1)[7239:]
    with open(json_file2, 'r', encoding='utf-8') as f2:
        data2 = json.load(f2)
    appnum = len(data1)
    entitynum = len(data2)
    M = np.zeros((appnum, entitynum),dtype='float16')
    raw = 0
    for i1 in data1:
        allindex = read_info(i1, data2)
        M = marking(allindex, raw, M)
        print("第" + str(raw) + "个apk已打标完毕")
        raw = raw + 1
    M_sp = scipy.sparse.csr_matrix(M)
    sparse.save_npz(permission_mat, M_sp)  # 保存稀疏矩阵
    # scio.savemat(permission_mat, {'permission': M})
    print("api矩阵已打标结束")

    # so打标
    # json_file1 = r'E:\experiment\samples\so.json'
    # json_file2 = r"E:\experiment\frequencydata\count_so.json"
    # permission_mat = r"E:\experiment\matrix\matrix_so.npz"
    # with open(json_file1, 'r', encoding='utf-8') as f1:
    #     data1 = json.load(f1)
    # with open(json_file2, 'r', encoding='utf-8') as f2:
    #     data2 = json.load(f2)
    # appnum = len(data1)
    # entitynum = len(data2)
    # M = np.zeros((appnum, entitynum))
    # raw = 0
    # for i1 in data1:
    #     allindex = read_info(i1, data2)
    #     M = marking(allindex, raw, M)
    #     print("第" + str(raw) + "个apk已打标完毕")
    #     raw = raw + 1
    # M_sp = scipy.sparse.csr_matrix(M)
    # sparse.save_npz(permission_mat, M_sp)  # 保存稀疏矩阵
    # # scio.savemat(permission_mat, {'permission': M})
    # print("so矩阵已打标结束")


    # filename = r"E:\experiment\matrix\matrix_permission.mat"
    # data = scio.loadmat(filename)["permission"]
    # print("hahah")