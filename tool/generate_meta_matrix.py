import scipy.io as scio
import numpy as np
from scipy import sparse
# 需要补充生成元图的函数
def get_Matrix(dataFileb, resMatrix):
    # d = sparse.load_npz(dataFileb)['permission']
    d = sparse.load_npz(dataFileb)
    res=np.dot(d,d.T)
    print(res) # 依旧是稀疏矩阵
    #res_new =res.todense()
    #scio.savemat(resMatrix, {'permission':res})
    sparse.save_npz(resMatrix, res)
    print("元结构稀疏矩阵已生成")


def get_Matrix_v2(dataFileb, dataFilem):
        # d = scio.loadmat(dataFileb)['permission']
        d = sparse.load_npz(dataFileb)
        # d1 = scio.loadmat(dataFilem)['permission']
        d1 = sparse.load_npz(dataFilem)
        res = np.dot(d, d1.T)
        return res


def get_Matrix_v3(dataFileb, dataFilem):
    # d = scio.loadmat(dataFileb)['permission']
    # d1 = scio.loadmat(dataFilem)['permission']
    d = sparse.load_npz(dataFileb)
    d1 = sparse.load_npz(dataFilem)
    res = d * d1
    return res


if __name__ == "__main__":
    # api
    # dataFileb = r"E:\experiment\sub_datasets\dataset1\matrix_api_1.npz"
    # resMatrix = r"E:\experiment\sub_datasets\dataset1\meta\path1.npz"
    # get_Matrix(dataFileb, resMatrix)

    # interface
    # dataFileb = r"E:\experiment\sub_datasets\dataset1\matrix_interface_1.npz"
    # resMatrix = r"E:\experiment\sub_datasets\dataset1\meta\path2.npz"
    # get_Matrix(dataFileb, resMatrix)

    # package
    # dataFileb = r"E:\experiment\sub_datasets\dataset1\matrix_package_1.npz"
    # resMatrix = r"E:\experiment\sub_datasets\dataset1\meta\path3.npz"
    # get_Matrix(dataFileb, resMatrix)

    # permission
    # dataFileb = r"E:\experiment\sub_datasets\dataset1\matrix_permission_1.npz"
    # resMatrix = r"E:\experiment\sub_datasets\dataset1\meta\path4.npz"
    # get_Matrix(dataFileb, resMatrix)

    # so
    # dataFileb = r"E:\experiment\sub_datasets\dataset1\matrix_so_1.npz"
    # resMatrix = r"E:\experiment\sub_datasets\dataset1\meta\path5.npz"
    # get_Matrix(dataFileb, resMatrix)

    # super
    # dataFileb = r"E:\experiment\sub_datasets\dataset1\matrix_super_1.npz"
    # resMatrix = r"E:\experiment\sub_datasets\dataset1\meta\path6.npz"
    # get_Matrix(dataFileb, resMatrix)

    # permission-permissiontype
    # dataFileb = r"E:\experiment\sub_datasets\dataset1\matrix_permission_1.npz"
    # dataFilem = r"E:\experiment\sub_datasets\dataset1\matrix_permissiontype_1.npz"
    # resMatrix = r"E:\experiment\sub_datasets\dataset1\meta\path7.npz"
    # mid1 = get_Matrix_v2(dataFileb, dataFilem)
    # res = np.dot(mid1, mid1.T)
    # sparse.save_npz(resMatrix, res)
    # print("元结构稀疏矩阵已生成")


    # graph1 [7,1]
    dataFileb = r"E:\experiment\sub_datasets\dataset1\meta\path7.npz"
    dataFilem = r"E:\experiment\sub_datasets\dataset1\meta\path1.npz"
    M=get_Matrix_v3(dataFileb, dataFilem)
    resMatrix = r"E:\experiment\sub_datasets\dataset1\meta\graph1.npz"
    sparse.save_npz(resMatrix, M)
    print("元图稀疏矩阵已生成")


    # graph2 [7,2]
    dataFileb = r"E:\experiment\sub_datasets\dataset1\meta\path7.npz"
    dataFilem = r"E:\experiment\sub_datasets\dataset1\meta\path2.npz"
    M = get_Matrix_v3(dataFileb, dataFilem)
    resMatrix = r"E:\experiment\sub_datasets\dataset1\meta\graph2.npz"
    sparse.save_npz(resMatrix, M)
    print("元图稀疏矩阵已生成")

    # graph3 [7,3]
    dataFileb = r"E:\experiment\sub_datasets\dataset1\meta\path7.npz"
    dataFilem = r"E:\experiment\sub_datasets\dataset1\meta\path3.npz"
    M = get_Matrix_v3(dataFileb, dataFilem)
    resMatrix = r"E:\experiment\sub_datasets\dataset1\meta\graph3.npz"
    sparse.save_npz(resMatrix, M)
    print("元图稀疏矩阵已生成")

    # graph4 [5,6]
    dataFileb = r"E:\experiment\sub_datasets\dataset1\meta\path5.npz"
    dataFilem = r"E:\experiment\sub_datasets\dataset1\meta\path6.npz"
    M = get_Matrix_v3(dataFileb, dataFilem)
    resMatrix = r"E:\experiment\sub_datasets\dataset1\meta\graph4.npz"
    sparse.save_npz(resMatrix, M)
    print("元图稀疏矩阵已生成")

    # graph5 [5,2]
    dataFileb = r"E:\experiment\sub_datasets\dataset1\meta\path5.npz"
    dataFilem = r"E:\experiment\sub_datasets\dataset1\meta\path2.npz"
    M = get_Matrix_v3(dataFileb, dataFilem)
    resMatrix = r"E:\experiment\sub_datasets\dataset1\meta\graph5.npz"
    sparse.save_npz(resMatrix, M)
    print("元图稀疏矩阵已生成")

