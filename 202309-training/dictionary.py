import gensim
from gensim.models import word2vec
from scipy.spatial.distance import cosine
import numpy as np
import spacy
'''
model = gensim.models.KeyedVectors.load_word2vec_format(r"F:\\考试星项目\\sgns.wiki.bigram", encoding='utf-8')

with open(r'C:\\Users\\丁丁\\Desktop\\单元组词典.txt', 'r') as file:
    # 读取文件内容
    contents = file.read()

# 将文件内容转换为列表
data_list = eval(contents)
print(len(data_list))

filtered_list = [item for item in data_list if item[1] <= 3]

ctr = 0
vec_list = []
IsUseful = [0]*len(filtered_list)

for item in filtered_list:
    if item[0] in model.index_to_key:
        vec_list.append(model[item[0]])
    else:
        vec_list.append(np.zeros(300))

for i in range(len(vec_list)):
    if i >= 1 and (i <= len(filtered_list)-2):
        if filtered_list[i][0] in model.index_to_key:
            previous_sim = 1 - cosine(vec_list[i], vec_list[i-1])
            next_sim = 1 - cosine(vec_list[i], vec_list[i + 1])
            if previous_sim > 0.5 or next_sim > 0.5:
                IsUseful[i] = 1

print(IsUseful)
print(len(IsUseful))
print(len(filtered_list))

total_list = [item for item in data_list if item[1] > 3]
for i in range(len(filtered_list)):
    if IsUseful[i] == 1:
        total_list.append(filtered_list[i])

print(total_list)
print(len(total_list))

f = open(r'C:\\Users\\丁丁\\Desktop\\筛选后单元组.txt', "w")
print(total_list, file=f)
f.close()
'''
nlp = spacy.load("zh_core_web_sm")

with open(r'C:\\Users\\丁丁\\Desktop\\筛选后单元组.txt', 'r', encoding='UTF-8') as file:
    # 读取文件内容
    contents = file.read()

data_list = eval(contents)

node_list = []
to_be_decided = []

for item in data_list:
    if len(item[0]) == 1:
        to_be_decided.append(item)
    else:
        word = nlp(item[0])
        flag = 0
        for token in word:
            if token.pos_ == "NUM" or token.is_stop == 1:
                flag = 1
        if flag == 0:
            node_list.append(item)
        else:
            to_be_decided.append(item)

f = open(r'C:\\Users\\丁丁\\Desktop\\node_list.txt', "w")
print(node_list, file=f)
f.close()
print(len(node_list))

f = open(r'C:\\Users\\丁丁\\Desktop\\to_be_decided.txt', "w")
print(to_be_decided, file=f)
f.close()
print(len(to_be_decided))