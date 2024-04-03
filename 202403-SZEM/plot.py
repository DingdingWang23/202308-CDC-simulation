import jieba.analyse
import csv
import numpy as np
import pandas as pd
import gensim
from gensim.models import word2vec
from sklearn.decomposition import PCA
import matplotlib
from matplotlib import pyplot
from sklearn.manifold import MDS
import os
import pandas as pd

model = gensim.models.KeyedVectors.load_word2vec_format(r"F:\\单人面试\\sgns.wiki.bigram", encoding='utf-8')

filename = r'C:\\Users\\丁丁\\Desktop\\深圳演练\\node_name_title.csv'

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


vector_list = []
my_word2vec = {}

result_name = []
result_title = []
# word2vec = {}

for tuple in names_titles:
    words_name = jieba.lcut(tuple[0])
    result_name.append(words_name)
    vector_name = []
    for word in words_name:
        if word in model.index_to_key:
            vector_name.append(model[word])

    if not vector_name:
        vector_name = [np.zeros(300)]

    vector_name_mean = np.mean(vector_name, axis=0)

    words_title = jieba.lcut(tuple[1])
    result_title.append(words_title)
    vector_title = []
    for word in words_title:
        if word in model.index_to_key:
            vector_title.append(model[word])

    if not vector_title:
        vector_title = [np.zeros(300)]

    vector_title_mean = np.mean(vector_title, axis=0)

    vector_mean = 0.3 * vector_title_mean + 0.7 * vector_name_mean
    '''
    if np.all(vector_title == 0):
        vector_mean = 3 * vector_title_mean
    else:
        vector_mean = 3 * vector_title_mean + 7 * vector_name_mean
    '''

    vector_list.append(vector_mean)
    my_word2vec[tuple[0]] = vector_mean


X = np.array(vector_list)
X = pd.DataFrame(X)
pca = PCA(n_components=2)
result = pca.fit_transform(X)


# 计算MDS映射
# mds = MDS(n_components=2, dissimilarity='precomputed')
# result = mds.fit_transform(X)


# mds = MDS(n_components=2,random_state=0)
# result = mds.fit_transform(X)


df = pd.DataFrame({'name': names, 'lon': result.T[0], 'lat': result.T[1]})

filename = r'C:\\Users\\丁丁\\Desktop\\深圳演练\\node.csv'

with open(filename, 'w', newline='', encoding='utf-8-sig') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['name', 'lon', 'lat'])
    for name, lon, lat in zip(names, result.T[0], result.T[1]):
        writer.writerow([name, lon, lat])


matplotlib.rcParams['font.sans-serif'] = ['SimSun']

pyplot.scatter(result[:, 0], result[:, 1])
words = list(my_word2vec.keys())
for i, word in enumerate(words):
    pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))
pyplot.show()

