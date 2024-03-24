import os
from docx import Document
import jieba
from collections import Counter
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# 定义文件夹路径
folder_path = r'C:\\Users\\丁丁\\Desktop\\转录_09192255'

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


folder_path = r'C:\\Users\\丁丁\\Desktop\\每个人讲的话'
os.makedirs(folder_path, exist_ok=True)

# 将列表中的每个元素输出到txt文件
for i, item in enumerate(total_corpus):
    file_path = os.path.join(folder_path, f'file{i+1}.txt')  # txt文件路径
    with open(file_path, 'w') as file:
        for sentence in item:
            file.write(sentence+"\n")

print(len(total_corpus))



total_sentences = []

for paragraph in total_said:
    sentences = paragraph.split("。")
    total_sentences += sentences

new_total_sentences = []
for item in total_sentences:
    if item != "":
        new_total_sentences.append(item)

total_sentences = new_total_sentences

print(total_sentences)



total_str = ''

for speaker in total_corpus:
    for sentence in speaker:
        total_str += sentence

stopwords = set()
with open(r'C:\\Users\\丁丁\\Desktop\\群组资源分配\\code\\stopword.txt', 'r', encoding='utf-8') as f:
    for line in f:
        stopwords.add(line.strip())

# 分词并去掉停用词
def tokenize(text):
    seg_list = jieba.cut(text)
    return [word for word in seg_list if word not in stopwords]

# 统计词频
def count_words(text):
    words = tokenize(text)
    counter = Counter(words).most_common()
    return counter

counter = count_words(total_str)
counter = counter[1:]
print(counter)

f = open(r'C:\\Users\\丁丁\\Desktop\\单元组词典.txt', "w")
print(counter,file=f)
f.close()



with open(r'C:\\Users\\丁丁\\Desktop\\单元组词典.txt', 'r') as file:
    # 读取文件内容
    contents = file.read()

# 将文件内容转换为列表
data_list = eval(contents)
half_filtered_list = [item for item in data_list if item[1] >= 3]
filtered_list = [item for item in half_filtered_list if item[1] <= 20]

list2dict = dict(filtered_list)
print(filtered_list)
print(len(filtered_list))

total_phrases = []

for sentence in total_sentences:
    phrases = jieba.lcut(sentence)
    new_phrases = []
    for phrase in phrases:
        if phrase in list2dict.keys():
            new_phrases.append(phrase)
    total_phrases.append(new_phrases)

print("*******")
print(total_phrases)
print(len(total_phrases))


Encoder=TransactionEncoder()
encoded_data=Encoder.fit_transform(total_phrases)
df=pd.DataFrame(encoded_data,columns=Encoder.columns_)
print(df)

frequent_items= apriori(df, min_support=0.001, use_colnames=True, max_len=None).sort_values(by='support', ascending=False)
print(frequent_items)

ass_rule=association_rules(frequent_items, metric='confidence', min_threshold =0.6)
ass_rule.sort_values(by ='leverage', ascending = False, inplace =True)

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)

print(ass_rule)
print(type(ass_rule))

f = open(r'C:\\Users\\丁丁\\Desktop\\多元组词典.txt', "w")
print(ass_rule,file=f)
f.close()

