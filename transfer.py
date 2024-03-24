import os
import pandas as pd
import numpy as np
import spacy
import jieba
from collections import Counter
import csv
'''
input_folder = r'C:\\Users\\丁丁\\Desktop\\prepare'
output_folder = r'C:\\Users\\丁丁\\Desktop\\for R'

# 获取输入文件夹中的文件列表
file_list = os.listdir(input_folder)

for file_name in file_list:
    if file_name.endswith(".csv"):
        input_file = os.path.join(input_folder, file_name)
        output_file = os.path.join(output_folder, os.path.splitext(file_name)[0] + ".csv")

        df = pd.read_csv(r'C:\\Users\\丁丁\\Desktop\\node_list.csv')
        print(df)

        input = pd.read_csv(input_file)
        input = input.drop_duplicates(['节点名称'])
        print(input)

        merge_df = pd.merge(df, input, on="节点名称", how='inner')
        print(merge_df)

        C = np.column_stack((df, np.zeros(df.shape[0])))

        # 在矩阵 C 的第三列进行匹配判断
        for i in range(len(df)):

            if df.iloc[i,0] in list(input['节点名称']):
                C[i,5] = 1

        df = pd.DataFrame(C, columns=['节点名称', 'lon','lat','type','importance', 'existence'])
        df.to_csv(output_file, index=False, encoding='gbk')


df = pd.read_csv(r'C:\\Users\\丁丁\\Desktop\\2022年公开招聘社区工作者面试.csv')
print(df)
ref_answer = ''
ctr = 0
for i in range(len(df)):
    score = df.iloc[i, :][0]
    text = df.iloc[i, :][1]
    if score >= 50:
        ref_answer += text
        ctr += 1

print(ctr)

ref_answer = ref_answer.replace("嗯。","")
ref_answer = ref_answer.replace("嗯？","")
ref_answer = ref_answer.replace("嗯，","")
ref_answer = ref_answer.replace("嗯","")
ref_answer = ref_answer.replace("呃。","")
ref_answer = ref_answer.replace("呃？","")
ref_answer = ref_answer.replace("呃，","")
ref_answer = ref_answer.replace("呃","")
ref_answer = ref_answer.replace("啊。","")
ref_answer = ref_answer.replace("啊？","")
ref_answer = ref_answer.replace("啊，","")
ref_answer = ref_answer.replace("啊","")
ref_answer = ref_answer.replace("呢。","")
ref_answer = ref_answer.replace("呢？","")
ref_answer = ref_answer.replace("呢，","")
ref_answer = ref_answer.replace("呢","")

nlp = spacy.load("zh_core_web_sm")
sentence = nlp(ref_answer)
new_ref_answer = ""

for token in sentence:
    if token.pos_ != "SPACE" and token.is_stop == False:
        new_ref_answer += token.text

with open(r'C:\\Users\\丁丁\\Desktop\\参考答案.txt', "w+", encoding="utf-8") as f:
    print(ref_answer,file=f)

words = jieba.lcut(new_ref_answer)

word2dict = dict(Counter(words))
sorted_dict = dict(sorted(word2dict.items(), key=lambda x: x[1], reverse=True))

print(sorted_dict)
print(len(sorted_dict))
with open(r'C:\\Users\\丁丁\\Desktop\\nodes.txt', "w+", encoding="utf-8") as f:
    print(sorted_dict,file=f)
'''

df = pd.read_csv(r'C:\\Users\\丁丁\\Desktop\\2022年公开招聘社区工作者面试.csv')
output_folder = r'C:\\Users\\丁丁\\Desktop\\单人面试文本'

for i in range(len(df)):
    score = df.iloc[i, :][0]
    text = df.iloc[i, :][1]

    file_name = os.path.join(output_folder, f"{i + 1}.txt")

    with open(file_name, 'w') as txtfile:
        txtfile.write(text)

