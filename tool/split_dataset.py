from scipy import sparse
import numpy as np
from scipy import sparse
import scipy

# 先分割
# 再合并
# 再保存

if __name__ == "__main__":
    dataset= sparse.load_npz(r'/sub_datasets/dataset8/matrix_api_benign_8.npz')
    dataset1 = sparse.load_npz(r'/sub_datasets/dataset8/matrix_api_mal_8.npz')
    permission_mat = r'E:\experiment\sub_datasets\dataset8\matrix_api_8.npz'
    samples_benign = dataset.todense()
    samples_benign_ = dataset1.todense()
    # samples_mal = dataset.todense()[14238: ,]
    m2 = np.asarray(samples_benign)
    m3 = np.asarray(samples_benign_)
    # m3 = np.asarray(samples_mal)
    m4 = np.vstack((m2,m3))
    M_sp = scipy.sparse.csr_matrix(m4)
    sparse.save_npz(permission_mat, M_sp)  # 保存稀疏矩阵
    print("permission矩阵已打标结束")