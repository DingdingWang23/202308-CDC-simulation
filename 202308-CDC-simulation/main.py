import jieba.analyse
import csv
import numpy as np
import pandas as pd
import gensim
from gensim.models import word2vec
from sklearn.decomposition import PCA
import matplotlib
from matplotlib import pyplot

model = gensim.models.KeyedVectors.load_word2vec_format(r"D:\\考试星项目\\sgns.wiki.bigram", encoding='utf-8')
filename = r'C:/Users/丁丁/Desktop/其他事务/备课/2023暑期-卫健委培训/node0822.csv'

vector_list = []
result_name = []
result_title = []
word2vec = {}

names = []
titles = []
names_titles = []

with open(filename, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        names.append(row[0])
        titles.append(row[1])
        names_titles.append([row[0], row[1]])

unique_title = list(set(titles))

for phrase in names_titles:
    words_name = jieba.lcut(phrase[0])
    result_name.append(words_name)
    vector_name = []
    for word in words_name:
        if word in model.index_to_key:
            vector_name.append(model[word])

    if not vector_name:
        vector_name = [np.zeros(300)]

    vector_name_mean = np.mean(vector_name, axis=0)

    words_title = jieba.lcut(phrase[1])
    result_title.append(words_title)
    vector_title = []
    for word in words_title:
        if word in model.index_to_key:
            vector_title.append(model[word])

    if not vector_title:
        vector_title = [np.zeros(300)]

    vector_title_mean = np.mean(vector_title, axis=0)

    vector_mean = 3*vector_title_mean+7*vector_name_mean

    vector_list.append(vector_mean)
    word2vec[phrase[0]] = vector_mean

title_embedding = []
title2vec = {}

other_title = ['病毒','城市','大学生运动会','抗病毒药物','密切接触者','社区管控','特殊人群','卫健专家','疫苗','舆情']
merged_title = unique_title+other_title

for phrase in merged_title:
    words = jieba.lcut(phrase)
    vector = []
    for word in words:
        if word in model.index_to_key:
            vector.append(model[word])

    if not vector:
        vector = [np.zeros(300)]
    if phrase in unique_title:
        vector_mean = 10*np.mean(vector, axis=0)
    else:
        vector_mean = 3 * np.mean(vector, axis=0)

    title_embedding.append(vector_mean)
    title2vec[phrase] = vector_mean

# 基于2d PCA拟合数据
X = np.array(vector_list)
Y = np.array(title_embedding)
X = pd.DataFrame(X)
Y = pd.DataFrame(Y)
combined = pd.concat([X, Y], axis=0)
pca = PCA(n_components=2)
result = pca.fit_transform(combined)

title_result = result[(len(names)):]
result = result[:(len(names))]

print("title2vec",title2vec)
print("title列表",merged_title)
print("title_result",title_result)

df_title = pd.DataFrame({'name': merged_title, 'lon': title_result.T[0], 'lat': title_result.T[1]})
filename = r'C:/Users/丁丁/Desktop/其他事务/备课/2023暑期-卫健委培训/title0822.csv'
with open(filename, 'w', newline='', encoding='utf-8-sig') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['name', 'lon', 'lat'])  # 写入标题行
    for name, lon, lat in zip(merged_title, title_result.T[0], title_result.T[1]):
        writer.writerow([name, lon, lat])  # 写入数据行


df = pd.DataFrame({'name': names, 'lon': result.T[0], 'lat': result.T[1]})
filename = r'C:/Users/丁丁/Desktop/其他事务/备课/2023暑期-卫健委培训/output0822.csv'
with open(filename, 'w', newline='', encoding='utf-8-sig') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['name', 'lon', 'lat'])  # 写入标题行
    for name, lon, lat in zip(names, result.T[0], result.T[1]):
        writer.writerow([name, lon, lat])  # 写入数据行


matplotlib.rcParams['font.sans-serif'] = ['SimSun']
# 可视化展示
pyplot.scatter(result[:, 0], result[:, 1])
words = list(word2vec.keys())
for i, word in enumerate(words):
    pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))
pyplot.show()




















