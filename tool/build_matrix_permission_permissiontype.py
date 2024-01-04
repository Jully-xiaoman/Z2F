import json
import numpy as np
import scipy.io as scio
from scipy import sparse
import scipy
# 输入权限打标（仅仅是权限是否出现）矩阵，输入权限-权限类型json文件
# 输出权限-权限类型打标矩阵（出现的权限属于哪个权限组） 0-8对应 data3定义的危险权限组信息，9就是普通权限
def read_info(i1, data2, data3):
    flag = 0
    value0 = list(data2.values())[0]
    for i in i1:
        if i == 1:
            value = value0[flag]
            number = data3.index(value)
            # location = i1.tolist().index(i)
            location = i1.index(i)
            i1[location] = number
            flag = flag + 1
    return i1

# 这边直接堆叠就可以了
def marking(M, i, number):
    M[number, ] = i
    return M


if __name__ == "__main__":
    with open(r'E:\experiment\samples\permissiontype.json', 'r') as f: #权限-权限类型文件
        data2 = json.load(f)
    data3 = ['CALENDAR','CAMERA','CONTACTS','LOCATION','MICROPHONE','PHONE','SENSORS','SMS','STORAGE','Normal']
    matrix_file1 = r"E:\experiment\matrix\matrix_permission.npz" # 权限打标矩阵
    permissiontype_mat = r"E:\experiment\matrix\matrix_permission_permissiontype.npz"
    data1 = sparse.load_npz(matrix_file1).todense()
    # data1 = scio.loadmat(matrix_file1)["permission"]
    appnum = np.size(data1, 0)
    entitynum = np.size(data1, 1)
    M = np.zeros((appnum, entitynum))
    number = 0
    for i1 in data1:
         i1 = i1.tolist()[0]
         d2 = data2[number]
         i = read_info(i1, d2, data3)
         M = marking(M, i, number)
         print("第" + str(number) + "个apk已打标完毕")
         number = number+1
    M_sp = scipy.sparse.csr_matrix(M)
    sparse.save_npz(permissiontype_mat, M_sp)  # 保存稀疏矩阵
    # scio.savemat(permissiontype_mat, {'permission': M})
    print("permissiontype矩阵已打标结束")