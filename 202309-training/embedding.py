import spacy
import os
from docx import Document
import jieba
from collections import Counter
import pandas as pd
from gensim.models import word2vec
import numpy as np
from mittens import GloVe
from scipy.spatial.distance import cosine
from sklearn.decomposition import PCA
import matplotlib
from matplotlib import pyplot
import gensim
import math


'''
with open(r'C:\\Users\\丁丁\\Desktop\\node_list.txt', 'r') as file:
    # 读取文件内容
    contents = file.read()

data_list = eval(contents)
node_list = []
for item in data_list:
    node_list.append(item[0])

with open(r'C:\\Users\\丁丁\\Desktop\\多元组词典_manual.txt', 'r', encoding='UTF-8') as file:
    # 读取文件内容
    contents = file.readlines()

for item in contents:
    new_item = item.replace('\n','')
    node_list.append(new_item)

print(node_list)
print(len(node_list))


with open(r'C:\\Users\\丁丁\\Desktop\\node_list_full.txt', 'r', encoding='UTF-8') as file:
    # 读取文件内容
    contents = file.read()

data_list = eval(contents)
print(data_list)
print(len(data_list))

nlp = spacy.load("zh_core_web_sm")
pos_dict ={}
output_node_list = []

for item in data_list:
    word = nlp(item)
    flag = 1
    for token in word:
        print(token.text)
        print(token.pos_)
        if token.pos_ in pos_dict.keys():
            pos_dict[token.pos_] += 1
        else:
            pos_dict[token.pos_] = 1
        if token.pos_ != "NOUN" and token.pos_ != "PROPN" and token.pos_ != "VERB" and token.pos_ != "ADJ":
            flag = 0
    if flag ==1:
        output_node_list.append(item)

print(pos_dict)

f = open(r'C:\\Users\\丁丁\\Desktop\\node_list_pos.txt', "w")
print(output_node_list, file=f)
f.close()
'''

# 定义文件夹路径
folder_path = r'C:\\Users\\丁丁\\Desktop\\干部培训测评\\转录_09192255'

# 获取文件夹中的所有docx文件
file_names = [file_name for file_name in os.listdir(folder_path) if file_name.endswith('.docx')]

# 读取每个文件的内容并存储为字符串
file_contents = []
for file_name in file_names:
    file_path = os.path.join(folder_path, file_name)
    document = Document(file_path)
    content = ''
    for paragraph in document.paragraphs:
        content += paragraph.text + '\n'
    file_contents.append(content)

total_corpus = []


for file_content in file_contents:
    group_dict = [[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

    sentences = file_content.split("\n\n")
    new_sentences = []
    for sentence in sentences:
        if "说话人" in sentence:
            new_sentences.append(sentence)
    sentences = new_sentences
    for sentence in sentences:
        try:
            said = sentence.split("\n")[1]
        except IndexError:
            said = ""
        #print(sentence)


        if "说话人 10" in sentence:
            group_dict[9].append(said)
        elif "说话人 11" in sentence:
            group_dict[10].append(said)
        elif "说话人 12" in sentence:
            group_dict[11].append(said)
        elif "说话人 13" in sentence:
            group_dict[12].append(said)
        elif "说话人 14" in sentence:
            group_dict[13].append(said)
        elif "说话人 1" in sentence:
            group_dict[0].append(said)
        elif "说话人 2" in sentence:
            group_dict[1].append(said)
        elif "说话人 3" in sentence:
            group_dict[2].append(said)
        elif "说话人 4" in sentence:
            group_dict[3].append(said)
        elif "说话人 5" in sentence:
            group_dict[4].append(said)
        elif "说话人 6" in sentence:
            group_dict[5].append(said)
        elif "说话人 7" in sentence:
            group_dict[6].append(said)
        elif "说话人 8" in sentence:
            group_dict[7].append(said)
        elif "说话人 9" in sentence:
            group_dict[8].append(said)


    for i in range(len(group_dict)):
        if group_dict[i] != []:
            total_corpus.append(group_dict[i])

total_said = []
for person_said in total_corpus:
    total_said += person_said
print(total_said)
print(len(total_said))

with open(r'C:\\Users\\丁丁\\Desktop\\干部培训测评\\node_list_single.txt', 'r', encoding='UTF-8') as file:
    # 读取文件内容
    contents = file.read()

# 将文件内容转换为列表
data_list = eval(contents)

model = gensim.models.KeyedVectors.load_word2vec_format(r"F:\\单人面试\\sgns.wiki.bigram", encoding='utf-8')

with open(r'C:\\Users\\丁丁\\Desktop\\干部培训测评\\筛选后单元组.txt', 'r', encoding='UTF-8') as file:
    # 读取文件内容
    contents = file.read()
data = eval(contents)
key2count_original = {t[0]: t[1] for t in data}

key2count = {}
key2idx = {}
key2vec = {}

ctr = 0
for item in data_list:
    key2count[item] = key2count_original[item]
    key2idx[item] = ctr
    if item in model.index_to_key:
        key2vec[item] = model[item]
    else:
        key2vec[item] = np.zeros(300)

    ctr += 1

print(key2count)
print(key2idx)


print(key2vec)
vec_list = list(key2vec.values())
print(len(vec_list))


corpus = []

for paragraph in total_said:
    phrases = jieba.lcut(paragraph)

    common_elements = [item for item in phrases if item in data_list]
    print(common_elements)
    if len(common_elements) > 0:
        corpus.append(common_elements)

print(len(corpus))
print(corpus)

model2 = word2vec.Word2Vec(corpus, min_count=1)

list = ["延安","延安精神","学校","院系","发展","干部","队伍","教学","科研","学生","工作"]


f = open(r'C:\\Users\\丁丁\\Desktop\\sim_words.txt', "w")
print("******word2vec****", file=f)
for item in list:
    sims = model2.wv.most_similar(item,topn=20)
    print(sims, file=f)

print("******预训练****", file=f)
for item in list:
    sims_output = []
    if item in model.index_to_key:
        for word in key2idx.keys():
            if word in model.index_to_key:
                sim = model.similarity(item,word)
                if sim > 0.5:
                    sims_output.append(word)

    else:
        sims_output = ['Nah']
    print(sims_output, file=f)
f.close()


'''
data = []
for line in corpus:
    line_data = []
    for word in line:
        line_data.append(key2idx[word])
    data.append(line_data)

print(data)
print(len(data))


coWindow = 5 # 共现窗口大小（半径）
tableSize = 3284 # 共现矩阵维度
cooccurrence = np.zeros((tableSize, tableSize), "int64" )

def countCOOC(cooccurrence, window, coreIndex):
   # cooccurrence：当前共现矩阵
   # window：当前移动窗口数组
   # coreIndex：当前移动窗口数组中的窗口中心位置
   for index in range(len(window)):
       if index == coreIndex:
           continue
       else:
           cooccurrence[window[coreIndex]][window[index]] += 1

   return cooccurrence


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

vec_list = list(key2vec.values())
print(len(vec_list))

for i in range(len(cooccurrence)):
    for j in range(len(cooccurrence)):
        cooccurrence[i][j] = math.sqrt(cooccurrence[i][j])
        #print(vec_list[i])
        #print(vec_list[j])
        cooccurrence[i][j] = (1 - cosine(vec_list[i], vec_list[j])) * cooccurrence[i][j]
    print(i,"轮")

# 初始化模型
vecLength=100           # 矩阵长度
max_iter=100         # 最大迭代次数
display_progress=1000   # 每次展示
glove_model = GloVe(n=vecLength, max_iter=max_iter, display_progress=display_progress)
# 模型训练与结果输出
embeddings = glove_model.fit(cooccurrence)

vec1 = embeddings[key2idx["清华"]]
vec2 = embeddings[key2idx["北大"]]
vec3 = embeddings[key2idx["电子系"]]
vec4 = embeddings[key2idx["电子"]]
vec5 = embeddings[key2idx["延安"]]

print(vec1)
print(vec2)
print(vec3)
print(vec4)
print(vec5)

sim12 = 1 - cosine(vec1, vec2)
sim23 = 1 - cosine(vec3, vec2)
sim34 = 1 - cosine(vec3, vec4)

print(sim12,sim23,sim34)

items = key2idx.items()

f = open(r'C:\\Users\\丁丁\\Desktop\\key2vec.txt', "w")

for item in list(items):
    key = item[0]
    print(key, file=f)
    idx = item[1]
    vec = embeddings[idx]
    print(vec, file=f)
    print("\n", file=f)
f.close()


X = np.array(embeddings)
X = pd.DataFrame(X)

# Y= np.array(vec_list)
# Y = pd.DataFrame(Y)
pca = PCA(n_components=2)
result = pca.fit_transform(X)

matplotlib.rcParams['font.sans-serif'] = ['SimSun']
# 可视化展示
pyplot.scatter(result[:, 0], result[:, 1])
words = list(key2idx.keys())
for i, word in enumerate(words):
    pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))
pyplot.show()

'''
'''
model = word2vec.Word2Vec(corpus, min_count=1)
print(model.wv["干部"])
sims = model.wv.most_similar("电子系",topn=10)
sims = model.wv.most_similar("孩子",topn=10)
sims = model.wv.most_similar("数字化",topn=10)
print(sims)
'''