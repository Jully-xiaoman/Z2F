import scipy.io as scio
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from scipy import sparse
import torch.nn.functional as nn
import sys  # 导入sys模块
sys.setrecursionlimit(3000)  # 将默认的递归深度修改为3000
# 先给每个特征降维
# 然后合并特征
def label(start, end, filename):
    raw = 0
    label = np.zeros(2000)
    benign = [0,1,2,3,4,5]
    mal = [6,7,8,9,10,11]
    while raw<start:
        label[raw] = benign[raw % 6]
        raw =raw+1
    while raw>=start and raw <end:
        label[raw] =mal[raw % 6]
        raw =raw+1
    label_ = label.T
    print(label_)
    print(len(label_))
    dl = pd.DataFrame(label_)
    dl.to_csv(filename, index=False, header=False)
    print("打标文件已保存")

# npz文件转csv文件
def n2c(filenamen, filenamec):
    m_feature = sparse.load_npz(filenamen)
    m_featire_dense =np.asarray(m_feature.todense())
    df = pd.DataFrame(m_featire_dense)
    df.to_csv(filenamec,index= False, header= False)
    print(f'{filenamec}文件已保存')

if __name__ == "__main__":
    # 生成打标文件
    # start = 1000
    # end = 2000
    # filename = r"E:\experiment\sub_datasets\dataset1\dataset1_csv\label1.csv"
    # label(start, end, filename)

    # 生成每个实体的csv文件
    # 读入npz,保存为csv
    # filenamen = r"E:\experiment\sub_datasets\dataset7\matrix_super_7.npz"
    # filenamec = r"E:\experiment\sub_datasets\dataset7\dataset7_csv\super_7.csv"
    # n2c(filenamen, filenamec)

    # 降维
    df_feature = pd.read_csv(r'/sub_datasets/dataset8/dataset8_csv/super_8.csv', header=None) # csv文件
    df_label = pd.read_csv(r'/sub_datasets/dataset8/dataset8_csv/label8.csv', header=None) # 标签文件
    permission_mat = r"E:\experiment\sub_datasets\dataset8\dataset8_mat\lda_super_8.mat" # 降维后的mat文件
    x, y = df_feature.iloc[:, :].values, df_label.iloc[:, :].values.ravel()
    sc = MinMaxScaler()
    x_std = sc.fit_transform(x)
    lda = LDA(n_components=10)
    x_train_lda = lda.fit_transform(x_std, y)
    print(x_train_lda)
    scio.savemat(permission_mat, {'permission': x_train_lda})
    print("特征矩阵已降维完毕")
