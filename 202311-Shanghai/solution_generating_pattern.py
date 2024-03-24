import os
import pandas as pd
import csv
import gensim
from gensim.models import word2vec
import jieba
import numpy as np
from scipy.spatial.distance import cosine

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.expand_frame_repr', False)

with open(r"C:\\Users\\丁丁\\Desktop\\物资集团测评\\1130\\group 4\\chance_node.txt", 'r', encoding='UTF-8') as file:
    lines = file.readlines()
    chance_node = []
    for item in lines:
        line = item.strip()
        chance_node.append(line)

with open(r"C:\\Users\\丁丁\\Desktop\\物资集团测评\\1130\\group 4\\utility_node.txt", 'r', encoding='UTF-8') as file:
    lines = file.readlines()
    utility_node = []
    for item in lines:
        line = item.strip()
        utility_node.append(line)

with open(r"C:\\Users\\丁丁\\Desktop\\物资集团测评\\1130\\group 4\\decision_node.txt", 'r', encoding='UTF-8') as file:
    lines = file.readlines()
    decision_node = []
    for item in lines:
        line = item.strip()
        decision_node.append(line)

df = pd.read_csv(r"C:\\Users\\丁丁\\Desktop\\物资集团测评\\1130\\group 4\\df.csv", encoding="gbk")
input = pd.read_csv(r"C:\\Users\\丁丁\\Desktop\\物资集团测评\\1130\\group 4\\node.csv", encoding="gbk")

merge_df = pd.merge(df, input, left_on='from', right_on='name', how='inner')
merge_df = pd.merge(merge_df, input, left_on='to', right_on='name', how='inner')
print(merge_df)

c_list = input.loc[input['type'] == 'C', 'name'].tolist()
u_list = input.loc[input['type'] == 'U', 'name'].tolist()
d_list = input.loc[input['type'] == 'D', 'name'].tolist()

merge_df = merge_df.drop(columns=['name_x', 'lon_x', 'lat_x', 'class_x', 'name_y', 'lon_y', 'lat_y', 'class_y'])
merge_df.rename(columns={'type_x': 'from_type', 'type_y': 'to_type'}, inplace=True)
print(merge_df)

u_d_df = merge_df.loc[(merge_df['from_type'] == 'U') & (merge_df['to_type'] == 'D'), ['from', 'to']].copy()
u_d_list = [tuple(row) for index, row in u_d_df .iterrows()]
print(u_d_list)

d_u_df = merge_df.loc[(merge_df['from_type'] == 'D') & (merge_df['to_type'] == 'U'), ['from', 'to']].copy()
d_u_list = [tuple(row) for index, row in d_u_df .iterrows()]
print(d_u_list)
print(d_u_df)

model = gensim.models.KeyedVectors.load_word2vec_format(r"F:\\单人面试\\sgns.wiki.bigram", encoding='utf-8')


def pattern1(corpus_list, u_list,d_list,u_d_list,d_u_list,window_size):
    count=0
    arc=[]
    num_arc=[]

    if len(corpus_list)<window_size:
        window_size = len(corpus_list)

    for i in range(len(corpus_list)-window_size+1):
        current_window=corpus_list[i:i+window_size]
        # print(current_window)
        for j in range(i,i+window_size):
            for k in range(j,i+window_size):
                if corpus_list[j] in u_list and corpus_list[k] in d_list and (corpus_list[j], corpus_list[k]) in u_d_list and (corpus_list[j],corpus_list[k]) not in arc and (corpus_list[k],corpus_list[j]) not in arc:
                    count +=1
                    arc.append((corpus_list[j], corpus_list[k]))
                    num_arc.append((j,k))
                elif corpus_list[j] in d_list and corpus_list[k] in u_list and (corpus_list[j], corpus_list[k]) in d_u_list and (corpus_list[j],corpus_list[k]) not in arc and (corpus_list[k],corpus_list[j]) not in arc:
                    count +=1
                    arc.append((corpus_list[j], corpus_list[k]))
                    num_arc.append((j, k))

    return count, arc,num_arc

def sim_between_phrases(phrase_1,phrase_2):
    words_1 = jieba.lcut(phrase_1)
    words_2 = jieba.lcut(phrase_2)
    vector_1 = []
    vector_2 = []
    for word in words_1:
        if word in model.index_to_key:
            vector_1.append(model[word])
    for word in words_2:
        if word in model.index_to_key:
            vector_2.append(model[word])
    if not vector_1:
        vector_1 = [np.zeros(300)]
    if not vector_2:
        vector_2 = [np.zeros(300)]

    vector_1_mean = np.mean(vector_1, axis=0)
    vector_2_mean = np.mean(vector_2, axis=0)
    sim = 1- cosine(vector_1_mean,vector_2_mean)

    return sim

def distance_between_options(decision_node):
    option_pair_2_sim ={}
    for i in range(len(decision_node)):
        for j in range(i+1,len(decision_node)):
            tuple = (decision_node[i],decision_node[j])
            option_pair_2_sim[tuple]= sim_between_phrases(decision_node[i],decision_node[j])
    return option_pair_2_sim

option_pair_2_sim= distance_between_options(decision_node)
print(option_pair_2_sim)

def pattern2(corpus_list,option_pair_2_sim,window_size,sim_threshold):
    count = 0
    pair = []
    num_pair = []

    if len(corpus_list) < window_size:
        window_size = len(corpus_list)

    for i in range(len(corpus_list) - window_size + 1):
        current_window = corpus_list[i:i + window_size]
        print(current_window)
        for j in range(i, i + window_size):
            for k in range(j+1, i + window_size):
                if (corpus_list[j], corpus_list[k]) in option_pair_2_sim.keys() and option_pair_2_sim[(corpus_list[j], corpus_list[k])]>sim_threshold and (corpus_list[j],corpus_list[k]) not in pair and (corpus_list[k],corpus_list[j]) not in pair:
                    count += 1
                    pair.append((corpus_list[j], corpus_list[k]))
                    num_pair.append((j, k))
                elif (corpus_list[k], corpus_list[j]) in option_pair_2_sim.keys() and option_pair_2_sim[(corpus_list[k], corpus_list[j])]>sim_threshold and (corpus_list[j],corpus_list[k]) not in pair and (corpus_list[k],corpus_list[j]) not in pair:
                    count += 1
                    pair.append((corpus_list[j], corpus_list[k]))
                    num_pair.append((j, k))

    return count, pair, num_pair

def max_distance(phrase_list):
    max_dist = 0

    for i in range(len(phrase_list)):
        for j in range(i,len(phrase_list)):
            phrase_1 = phrase_list[i]
            phrase_2 = phrase_list[j]

            words_1 = jieba.lcut(phrase_1)
            words_2 = jieba.lcut(phrase_2)
            vector_1 = []
            vector_2 = []
            for word in words_1:
                if word in model.index_to_key:
                    vector_1.append(model[word])
            for word in words_2:
                if word in model.index_to_key:
                    vector_2.append(model[word])
            if not vector_1:
                vector_1 = [np.zeros(300)]
            if not vector_2:
                vector_2 = [np.zeros(300)]

            vector_1_mean = np.mean(vector_1, axis=0)
            vector_2_mean = np.mean(vector_2, axis=0)

            vec_dist = vector_1_mean-vector_2_mean
            dist = np.linalg.norm(vec_dist)
            if dist>max_dist:
                max_dist=dist

    return max_dist

input_folder = r'C:\\Users\\丁丁\\Desktop\\物资集团测评\\1130\\group 4\\group_id_node_output_tsv\\'
output_folder_2_1_1 = r'C:\\Users\\丁丁\\Desktop\\物资集团测评\\1130\\group 4\\2_1_1_score\\'
output_folder_2_1_1_arc = r'C:\\Users\\丁丁\\Desktop\\物资集团测评\\1130\\group 4\\2_1_1_arc\\'
output_folder_2_1_2 = r'C:\\Users\\丁丁\\Desktop\\物资集团测评\\1130\\group 4\\2_1_2_score\\'
output_folder_2_1_2_pair = r'C:\\Users\\丁丁\\Desktop\\物资集团测评\\1130\\group 4\\2_1_2_pair\\'
output_folder_2_2 = r'C:\\Users\\丁丁\\Desktop\\物资集团测评\\1130\\group 4\\2_2_score\\'
output_folder_2_3 = r'C:\\Users\\丁丁\\Desktop\\物资集团测评\\1130\\group 4\\2_3_score\\'
output_folder_2_3_list = r'C:\\Users\\丁丁\\Desktop\\物资集团测评\\1130\\group 4\\2_3_list\\'

data_dirs = os.listdir(input_folder)

total_list = []
for dir in data_dirs:
    with open(input_folder+dir, 'r', encoding='UTF-8') as file:
        lines = file.readlines()
        corpus_list = []
        for item in lines:
            line = item.strip()
            corpus_list.append(line)
        my_list = list(set(corpus_list))
        total_list += my_list

print(total_list)

counter = {}
for item in total_list:
   if item in counter:
       counter[item] += 1
   else:
       counter[item] = 1
print(counter)

len_counter = len(counter)
counter_tuple_list = list(zip(counter.values(),counter.keys()))
n = int(len_counter*0.4)+1
sorted_counter = sorted(counter_tuple_list, reverse=False)
good_list = []
for i in range(n):
    good_list.append(sorted_counter[i][1])
print(good_list)
print(len(good_list))

for dir in data_dirs:
    print(dir)
    group, id = dir.split('.')[0].split('_')
    output_file_2_1_1 = output_folder_2_1_1 + dir
    output_file_2_1_1_arc = output_folder_2_1_1_arc + dir
    output_file_2_1_2 = output_folder_2_1_2 + dir
    output_file_2_1_2_pair = output_folder_2_1_2_pair + dir
    output_file_2_2 = output_folder_2_2 + dir
    output_file_2_3 = output_folder_2_3 + dir
    output_file_2_3_list = output_folder_2_3_list + dir
    total_list = []

    with open(input_folder + dir, 'r', encoding='UTF-8') as file:
        lines = file.readlines()
        corpus_list = []
        for item in lines:
            line = item.strip()
            corpus_list.append(line)
        # print(corpus_list)

        count_pattern_1 = pattern1(corpus_list, u_list,d_list,u_d_list,d_u_list,window_size=20)[0]
        print(count_pattern_1)
        arcs=pattern1(corpus_list, u_list,d_list,u_d_list,d_u_list,window_size=20)[1]
        with open(output_file_2_1_1, 'w', encoding='UTF-8') as file:
            file.write(str(count_pattern_1))
            file.write("\n")
        with open(output_file_2_1_1_arc, 'w', encoding='UTF-8') as file:
            for i in range(len(arcs)):
                file.write(str(arcs[i]))
                file.write("\n")

        count_pattern_2 = pattern2(corpus_list, option_pair_2_sim, window_size=10, sim_threshold=0.4)
        print(count_pattern_2[0])
        pairs = pattern2(corpus_list, option_pair_2_sim, window_size=10, sim_threshold=0.4)[1]
        with open(output_file_2_1_2, 'w', encoding='UTF-8') as file:
            file.write(str(count_pattern_2[0]))
            file.write("\n")
        with open(output_file_2_1_2_pair, 'w', encoding='UTF-8') as file:
            for i in range(len(pairs)):
                file.write(str(pairs[i]))
                file.write("\n")

        phrase_list = []
        for item in corpus_list:
            if item in decision_node:
                phrase_list.append(item)

        max_dist=max_distance(phrase_list)
        print(max_dist)
        print(phrase_list)
        with open(output_file_2_2, 'w', encoding='UTF-8') as file:
            file.write(str(max_dist))
            file.write("\n")

        unique_list =[]
        for item in corpus_list:
            if item in good_list:
                unique_list.append(item)
        unique_list=list(set(unique_list))
        print(unique_list)

        with open(output_file_2_3, 'w', encoding='UTF-8') as file:
            file.write(str(len(unique_list)))
            file.write("\n")

        with open(output_file_2_3_list, 'w', encoding='UTF-8') as file:
            for i in range(len(unique_list)):
                file.write(str(unique_list[i]))
                file.write("\n")

'''
corpus_list = ['培训后跟踪','有人文关怀','设置奖励和惩罚','设置奖励和惩罚','学员知识/业务水平提升','工种实操','业务概念介绍','游戏环节']
print(pattern1(corpus_list, u_list,d_list,u_d_list,d_u_list,window_size=2))
'''

'''
corpus_list = ['培训后跟踪','有人文关怀','设置奖励和惩罚','角色扮演','设置奖励和惩罚','学员知识/业务水平提升','工种实操','业务概念介绍','游戏环节']
print(pattern2(corpus_list,option_pair_2_sim,window_size=5,sim_threshold=0.4))
'''