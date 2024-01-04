import scipy.io as scio
import numpy as np

# 生成模型需要的cites文件
if __name__ == "__main__":

    # 处理为.cites文件
    # data = scio.loadmat(r'E:\experiment\testdata\dataset1\Normalize\test3.mat')["permission"]
    # self = np.eye(len(data))
    # datanew = data-self
    # fout = open(r'E:\experiment\testdata\dataset1\model_data\test3.cites',"w")
    # for i in range(len(data)):
    #     line = datanew[i].tolist()
    #     col = 0
    #     for s in line:
    #         col = col + 1
    #         if s == 1:
    #              fout.write(str(i) +" " +str(col-1)+"\n")
    # print(".cites已结束处理")
    #

    # 处理为.contents文件
    feature = scio.loadmat(r'E:\experiment\testdata\dataset1\dataset1_mat\dataset1_feature.mat')["permission"]
    fout = open(r'E:\experiment\testdata\dataset1\model_data\feature3.0.content', "w")
   # benign_label = ["benign1","benign2","benign3","benign4","benign5","benign6"]
    benign_label = ["benign1", "benign2", "benign3"]
   # mal_label = ["mal1","mal2","mal3","mal4","mal5","mal6"]
    mal_label = ["mal1", "mal2", "mal3"]
    for i in range(len(feature)):
        line = feature[i].tolist()
        fout.write(str(i) + " ")
        for num in line:
            fout.write(str(num) + " ")
        if i < 999:
            label = benign_label[i % 3]
            fout.write(label)
        else:
            label = mal_label[(i-999) % 3]
            fout.write(label)
        fout.write("\n")
    print(".content已结束处理")

