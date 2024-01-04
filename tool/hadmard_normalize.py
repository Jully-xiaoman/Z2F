import scipy.io as scio
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from scipy import sparse
#import scipy.io as scio
# 封装归一化函数
def Normalize(filename,normalize_file_list):
    i=0
    for per_file in filename:
        feature=scio.loadmat(per_file)['permission']
        scaler = MinMaxScaler()
        m1 = scaler.fit(feature)
        m1 = scaler.transform(feature)
        # 筛选替换
        m = np.where(m1 < 0.96, 0, m1)
        m2 = np.where(m >= 0.96 ,1, m)
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

def Normalize_1(filename,normalize_file_list):
    i=0
    for per_file in filename:
        feature=scio.loadmat(per_file)['permission']
        feature_final = feature.dot(feature.T)
        scaler = MinMaxScaler()
        m1 = scaler.fit(feature_final)
        m1 = scaler.transform(feature_final)
        # 筛选替换
        m = np.where(m1 < 0.96, 0, m1)
        m2 = np.where(m >= 0.96 ,1, m)
        scio.savemat(normalize_file_list[i], {"permission": m2})
        print(f"{normalize_file_list[i]}已处理结束")
        i=i+1

def softmax(x):
    # 计算每行的最大值
    row_max = np.max(x)
    # 每行元素都需要减去对应的最大值，否则求exp(x)会溢出，导致inf情况
    x = x - row_max
    # 计算e的指数次幂
    x_exp = np.exp(x)
    x_sum = np.sum(x_exp)
    s = x_exp / x_sum
    return s

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
    # filename=[r"E:\experiment\sub_datasets\dataset7\Hadmard\graph1.mat",
    #           r"E:\experiment\sub_datasets\dataset7\Hadmard\graph2.mat",
    #           r"E:\experiment\sub_datasets\dataset7\Hadmard\graph3.mat",
    #           r"E:\experiment\sub_datasets\dataset7\Hadmard\graph4.mat",
    #           r"E:\experiment\sub_datasets\dataset7\Hadmard\graph5.mat",
    #           r"E:\experiment\sub_datasets\dataset7\Hadmard\path1.mat",
    #           r"E:\experiment\sub_datasets\dataset7\Hadmard\path2.mat",
    #           r"E:\experiment\sub_datasets\dataset7\Hadmard\path3.mat",
    #           r"E:\experiment\sub_datasets\dataset7\Hadmard\path4.mat",
    #           r"E:\experiment\sub_datasets\dataset7\Hadmard\path5.mat",
    #           r"E:\experiment\sub_datasets\dataset7\Hadmard\path6.mat",
    #           r"E:\experiment\sub_datasets\dataset7\Hadmard\path7.mat",
    #           ]
    # Hadmard(feature_matrix_path, relation_matrix_path, filename)

    #filename = [r"E:\experiment\testdata\dataset1\Hadmard\path1.mat"]
    #normalize_file_list = [r"E:\experiment\testdata\dataset1\Normalize\test.mat"]
    # normalize_file_list=[r"E:\experiment\sub_datasets\dataset7\Normalize\graph1.mat",
    #                       r"E:\experiment\sub_datasets\dataset7\Normalize\graph2.mat",
    #                       r"E:\experiment\sub_datasets\dataset7\Normalize\graph3.mat",
    #                       r"E:\experiment\sub_datasets\dataset7\Normalize\graph4.mat",
    #                       r"E:\experiment\sub_datasets\dataset7\Normalize\graph5.mat",
    #                      r"E:\experiment\sub_datasets\dataset7\Normalize\path1.mat",
    #                      r"E:\experiment\sub_datasets\dataset7\Normalize\path2.mat",
    #                      r"E:\experiment\sub_datasets\dataset7\Normalize\path3.mat",
    #                      r"E:\experiment\sub_datasets\dataset7\Normalize\path4.mat",
    #                      r"E:\experiment\sub_datasets\dataset7\Normalize\path5.mat",
    #                      r"E:\experiment\sub_datasets\dataset7\Normalize\path6.mat",
    #                      r"E:\experiment\sub_datasets\dataset7\Normalize\path7.mat"
    #                     ]
    #Normalize(filename, normalize_file_list)

    # data = np.array([0.9409,0.8917,0.9401,0.9562,0.8839,0.9481,0.5323,0.9724,0.7424,0.9202,0.8743,0.9341])
    # data_n = softmax(data)
    # print(data_n)
    # print()
    # print(sorted(data_n))
    # print()
    # print(sorted(data_n)[5:])
    # print("再次SOFTMAX")
    # data_n_last = softmax(sorted(data_n)[5:])
    # print(data_n_last)

    filename = [r"E:\experiment\sub_datasets\dataset1\dataset1_mat\dataset1_feature.mat",
                r"E:\experiment\sub_datasets\dataset2\dataset2_mat\dataset2_feature.mat",
                r"E:\experiment\sub_datasets\dataset3\dataset3_mat\dataset3_feature.mat",
                r"E:\experiment\sub_datasets\dataset4\dataset4_mat\dataset4_feature.mat",
                r"E:\experiment\sub_datasets\dataset5\dataset5_mat\dataset5_feature.mat",
                r"E:\experiment\sub_datasets\dataset6\dataset6_mat\dataset6_feature.mat",
                r"E:\experiment\sub_datasets\dataset7\dataset7_mat\dataset7_feature.mat"]

    normalize_file_list = [r"E:\experiment\Ablationdata\dataset1.mat",
                           r"E:\experiment\Ablationdata\dataset2.mat",
                           r"E:\experiment\Ablationdata\dataset3.mat",
                           r"E:\experiment\Ablationdata\dataset4.mat",
                           r"E:\experiment\Ablationdata\dataset5.mat",
                           r"E:\experiment\Ablationdata\dataset6.mat",
                           r"E:\experiment\Ablationdata\dataset7.mat"]
    Normalize_1(filename, normalize_file_list)