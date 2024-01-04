import numpy as np
import scipy.io as scio
from scipy import sparse
#>>> np.concatenate((a,b),axis=1)  #axis=1表示对应行的数组进行拼接
if __name__ == "__main__":
    # 权限
    filename1 = scio.loadmat(r"/sub_datasets/dataset8/dataset8_mat/lda_permission_8.mat")['permission']
    # 权限类型
    filename2 = scio.loadmat(r"/sub_datasets/dataset8/dataset8_mat/lda_permissiontype_8.mat")['permission']
    # api
    # filename3 = scio.loadmat(r"E:\experiment\sub_datasets\dataset7\dataset7_mat\lda_api_7.mat")['permission']
    # package
    filename4 = scio.loadmat(r"/sub_datasets/dataset8/dataset8_mat/lda_package_8.mat")['permission']
    # interface
    # filename5 = scio.loadmat(r"E:\experiment\sub_datasets\dataset7\dataset7_mat\lda_interface_7.mat")['permission']
    # super
    filename6 = scio.loadmat(r"/sub_datasets/dataset8/dataset8_mat/lda_super_8.mat")['permission']
    # so
    filename7 = scio.loadmat(r"/sub_datasets/dataset8/dataset8_mat/lda_so_8.mat")['permission']

    # M = np.concatenate((filename1,filename2,filename3,filename4,filename5,filename6,filename7), axis=1)
    M = np.concatenate((filename1, filename2,  filename4,  filename6, filename7), axis=1)

    # 保存为特征矩阵
    features_mat = r"E:\experiment\sub_datasets\dataset8\dataset8_mat\dataset8_feature.mat"
    scio.savemat(features_mat, {'permission': M})
    print("特征矩阵已合并结束")

    # # 权限：
    # filename1 = sparse.load_npz(r'E:\experiment\matrix\matrix_permission_new.npz')
    # # 权限类型
    # filename2 = sparse.load_npz(r'E:\experiment\matrix\matrix_permissiontype_new.npz')
    # # api
    # filename3 = sparse.load_npz(r'E:\experiment\matrix\matrix_permissiontype_new.npz')