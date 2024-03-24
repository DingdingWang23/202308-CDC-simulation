import numpy as np
from mittens import GloVe


coWindow = 3 # 共现窗口大小（半径）
tableSize = 7 # 共现矩阵维度
cooccurrence = np.zeros((tableSize, tableSize), "int64" )

def countCOOC(cooccurrence, window, coreIndex):
   # cooccurrence：当前共现矩阵
   # window：当前移动窗口数组
   # coreIndex：当前移动窗口数组中的窗口中心位置
   for index in range(len(window)):
       if index == coreIndex:
           continue
       else:
           cooccurrence[window[coreIndex]][window[index]] = cooccurrence[window[coreIndex]][window[index]] + 1
   return cooccurrence

data = [[1,2,1],[2,5,4,5,6,2],[3,3,4],[6,3,1]]

# 开始统计
flag = 0
for item in data:
   itemInt = [int(x) for x in item]
   for core in range(1, len(item)):
       if core <= coWindow + 1:
           # 左窗口不足
           window = itemInt[1:core + coWindow + 1]
           coreIndex = core - 1
           cooccurrence = countCOOC(cooccurrence, window, coreIndex)
       elif core >= len(item) - 1 - coWindow:
           # 右窗口不足
           window = itemInt[core - coWindow:(len(item))]
           coreIndex = coWindow
           cooccurrence = countCOOC(cooccurrence, window, coreIndex)
       else:
           # 左右均没有问题
           window = itemInt[core - coWindow:core + coWindow + 1]
           coreIndex = coWindow
           cooccurrence = countCOOC(cooccurrence, window, coreIndex)
   flag = flag + 1

print(flag)
print(cooccurrence)

# 初始化模型
vecLength=100           # 矩阵长度
max_iter=10         # 最大迭代次数
display_progress=1000   # 每次展示
glove_model = GloVe(n=vecLength, max_iter=max_iter, display_progress=display_progress)
# 模型训练与结果输出
embeddings = glove_model.fit(cooccurrence)

print(embeddings)