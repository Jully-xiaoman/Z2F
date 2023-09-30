import scipy.io as scio
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from scipy import sparse

# 封装归一化函数
def Normalize(filename,normalize_file_list):
    i=0
    for per_file in filename:
        feature=scio.loadmat(per_file)['permission']
        scaler = MinMaxScaler()
        m1 = scaler.fit(feature)
        m1 = scaler.transform(feature)
        # 筛选替换
        m = np.where(m1 < 0.1, 0, m1)
        m2 = np.where(m >= 0.1 ,1, m)
        scio.savemat(normalize_file_list[i], {"permission": m2})
        print(f"{normalize_file_list[i]}已处理结束")
        i=i+1

def Hadmard(feature_matrix_path,relation_matrix_path,filename):
    # 实现特征矩阵的点乘
    m=scio.loadmat(feature_matrix_path)['permission']
    m1=np.dot(m,m.T)
    # 分别与7个关系矩阵相乘
    i=0
    for per_file in relation_matrix_path:
        r = sparse.load_npz(per_file).todense()
        m = m1 * r
        scio.savemat(filename[i], {"permission":m})
        i=i+1
        print("hadmard计算已完毕")
if __name__ == '__main__':
    # feature_matrix_path=r"E:\experiment\sub_datasets\dataset7\dataset7_mat\dataset7_feature.mat"
    # relation_matrix_path=[r"E:\experiment\sub_datasets\dataset7\meta\graph1.npz",
    #                       r"E:\experiment\sub_datasets\dataset7\meta\graph2.npz",
    #                       r"E:\experiment\sub_datasets\dataset7\meta\graph3.npz",
    #                       r"E:\experiment\sub_datasets\dataset7\meta\graph4.npz",
    #                       r"E:\experiment\sub_datasets\dataset7\meta\graph5.npz",
    #                       r"E:\experiment\sub_datasets\dataset7\meta\path1.npz",
    #                       r"E:\experiment\sub_datasets\dataset7\meta\path2.npz",
    #                       r"E:\experiment\sub_datasets\dataset7\meta\path3.npz",
    #                       r"E:\experiment\sub_datasets\dataset7\meta\path4.npz",
    #                       r"E:\experiment\sub_datasets\dataset7\meta\path5.npz",
    #                       r"E:\experiment\sub_datasets\dataset7\meta\path6.npz",
    #                       r"E:\experiment\sub_datasets\dataset7\meta\path7.npz",]
    filename=[r"E:\experiment\sub_datasets\dataset7\Hadmard\graph1.mat",
              r"E:\experiment\sub_datasets\dataset7\Hadmard\graph2.mat",
              r"E:\experiment\sub_datasets\dataset7\Hadmard\graph3.mat",
              r"E:\experiment\sub_datasets\dataset7\Hadmard\graph4.mat",
              r"E:\experiment\sub_datasets\dataset7\Hadmard\graph5.mat",
              r"E:\experiment\sub_datasets\dataset7\Hadmard\path1.mat",
              r"E:\experiment\sub_datasets\dataset7\Hadmard\path2.mat",
              r"E:\experiment\sub_datasets\dataset7\Hadmard\path3.mat",
              r"E:\experiment\sub_datasets\dataset7\Hadmard\path4.mat",
              r"E:\experiment\sub_datasets\dataset7\Hadmard\path5.mat",
              r"E:\experiment\sub_datasets\dataset7\Hadmard\path6.mat",
              r"E:\experiment\sub_datasets\dataset7\Hadmard\path7.mat",
              ]
    # Hadmard(feature_matrix_path, relation_matrix_path, filename)

    normalize_file_list=[r"E:\experiment\sub_datasets\dataset7\Normalize\graph1.mat",
                          r"E:\experiment\sub_datasets\dataset7\Normalize\graph2.mat",
                          r"E:\experiment\sub_datasets\dataset7\Normalize\graph3.mat",
                          r"E:\experiment\sub_datasets\dataset7\Normalize\graph4.mat",
                          r"E:\experiment\sub_datasets\dataset7\Normalize\graph5.mat",
                         r"E:\experiment\sub_datasets\dataset7\Normalize\path1.mat",
                         r"E:\experiment\sub_datasets\dataset7\Normalize\path2.mat",
                         r"E:\experiment\sub_datasets\dataset7\Normalize\path3.mat",
                         r"E:\experiment\sub_datasets\dataset7\Normalize\path4.mat",
                         r"E:\experiment\sub_datasets\dataset7\Normalize\path5.mat",
                         r"E:\experiment\sub_datasets\dataset7\Normalize\path6.mat",
                         r"E:\experiment\sub_datasets\dataset7\Normalize\path7.mat"
                         ]
    Normalize(filename, normalize_file_list)

