# -*- coding: utf-8 -*-
import os
import jieba
from fuzzywuzzy import fuzz
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
import re

input_folder = r"C:\\Users\\丁丁\\Desktop\\医院建设"


with open(r'C:\\Users\\丁丁\\Desktop\\node_list_single.txt', 'r', encoding='UTF-8') as file:
    contents = file.read()

node_list = eval(contents)
print(node_list)

said_all =[]
total_corpus = ""

for filename in os.listdir(input_folder):
    if filename.endswith(".txt"):
        filepath = os.path.join(input_folder, filename)

        with open(filepath, 'r', encoding='gbk') as file:
            content = file.read()

        paragraphs = content.split("\n")
        content = "\n".join(paragraphs)

        said_all.append(content)
        total_corpus += content


print(said_all)
print(len(said_all))
print(total_corpus)


word2count_all_person = []
word2count_total = {}

words_all_person = []
words_all_semi_sentences = []

for said in said_all:

    word2count_per_person = {}
    words_per_person = []

    phrases = jieba.lcut(said)
    for word in phrases:
        if word in node_list:
            words_per_person.append(word)

            if word not in word2count_total.keys():
                word2count_total[word] = 1
            else:
                word2count_total[word] += 1

            if word not in word2count_per_person.keys():
                word2count_per_person[word] = 1
            else:
                word2count_per_person[word] += 1

    word2count_all_person.append(word2count_per_person)
    words_all_person.append(words_per_person)

sorted_dict = dict(sorted(word2count_total.items(), key=lambda x: x[1], reverse=True))
print("以下是word2count_all_person")
print(word2count_all_person)
print("以下是words_all_person")
print(words_all_person)
print("sorted_dict")
print(sorted_dict)

words_all_semi_sentences = []

for said in said_all:
    semi_sentences = re.split(r'(?<=[。！？，\n])', said)

    for semi_sentence in semi_sentences:
        words_per_semi_sentences = []
        phrases = jieba.lcut(semi_sentence)
        for word in phrases:
            if word in node_list:
                words_per_semi_sentences.append(word)

        if words_per_semi_sentences != []:
            words_all_semi_sentences.append(words_per_semi_sentences)

print("以下是words_all_semi_sentences")
print(words_all_semi_sentences)
print(len(words_all_semi_sentences))

new_words_all_semi_sentences = []
for list in words_all_semi_sentences:
    if len(list) > 1:
        new_words_all_semi_sentences.append(list)

words_all_semi_sentences = new_words_all_semi_sentences

print(words_all_semi_sentences)
print(len(words_all_semi_sentences))
words_all_semi_sentences = words_all_semi_sentences


Encoder=TransactionEncoder()
encoded_data=Encoder.fit_transform(words_all_semi_sentences)
df=pd.DataFrame(encoded_data,columns=Encoder.columns_)
print(df)


frequent_items= apriori(df, min_support=0.0006, use_colnames=True, max_len=3).sort_values(by='support', ascending=False)
print(frequent_items)

ass_rule=association_rules(frequent_items, metric='confidence', min_threshold =0.6)
ass_rule.sort_values(by ='leverage', ascending = False, inplace =True)

# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
# pd.set_option('display.width', None)
# pd.set_option('display.max_colwidth', -1)

print(ass_rule)
print(type(ass_rule))


words_list = []
set_list = []


for i in range(len(ass_rule)):
    word_1 = ass_rule.iloc[i, 0]
    word_2 = ass_rule.iloc[i, 1]

    support_1 = ass_rule.iloc[i, 2]
    support_2 = ass_rule.iloc[i, 3]

    my_words = word_1.union(word_2)
    words = set(my_words)
    set_list.append(words)
    add = 1

    for previous_words in words_list:
        if len(previous_words & words) >= 2:
            add = 0
        elif len(previous_words & words) == 1 and support_1 > 0.01 and support_2 > 0.01:
            add = 0
    if add == 1:
        words_list.append(words)


for i in range(len(ass_rule)):
    word_1 = ass_rule.iloc[i, 0]
    word_2 = ass_rule.iloc[i, 1]

    my_words = word_1.union(word_2)
    words = set(my_words)
    set_list.append(words)

to_convert = []

for my_set in set_list:
    count_concept = 0
    count_example = 0
    for item in my_set:
        if word2count_total[item] ==1:
            count_example += 1
        elif word2count_total[item] > 1:
            count_concept += 1
    if count_example > 0 and count_concept > 0:
        print(my_set)
        to_convert.append(my_set)

example2concept = {}

for item in to_convert:
    if len(item) ==2:
        for word in item:
            if word2count_total[word] > 1:
                concept = word

        for word in item:
            if word2count_total[word] == 1:
                example2concept[word] = concept

    if len(item) == 3:
        max_count = 0
        for word in item:
            if word2count_total[word] > max_count:
                max_count = word2count_total[word]

        for word in item:
            if word2count_total[word] == max_count:
                concept = word

        for word in item:
            if word2count_total[word] == 1:
                example2concept[word] = concept

new_words_all_semi_sentences = []

for semi_sentence in words_all_semi_sentences:
    new_semi_sentences = []
    for word in semi_sentence:
        if word in example2concept.keys():
            new_semi_sentences.append(example2concept[word])
        else:
            new_semi_sentences.append(word)
    new_words_all_semi_sentences.append(new_semi_sentences)

words_all_semi_sentences = new_words_all_semi_sentences
print(words_all_semi_sentences)
print(len(words_all_semi_sentences))

f = open(r'C:\\Users\\丁丁\\Desktop\\医院建设_旧词组.txt', "w")
print(words_list, file=f)
f.close()

print("*********以下是替换掉例子后重新提词组**********")

Encoder=TransactionEncoder()
encoded_data=Encoder.fit_transform(words_all_semi_sentences)
df=pd.DataFrame(encoded_data,columns=Encoder.columns_)
print(df)


frequent_items= apriori(df, min_support=0.0006, use_colnames=True, max_len=3).sort_values(by='support', ascending=False)
print(frequent_items)

ass_rule=association_rules(frequent_items, metric='confidence', min_threshold =0.6)
ass_rule.sort_values(by ='leverage', ascending = False, inplace =True)

# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
# pd.set_option('display.width', None)
# pd.set_option('display.max_colwidth', -1)

print(ass_rule)
print(type(ass_rule))


words_list = []
set_list = []


for i in range(len(ass_rule)):
    word_1 = ass_rule.iloc[i, 0]
    word_2 = ass_rule.iloc[i, 1]


    support_1 = ass_rule.iloc[i, 2]
    support_2 = ass_rule.iloc[i, 3]

    my_words = word_1.union(word_2)
    words = set(my_words)
    set_list.append(words)
    add = 1

    for previous_words in words_list:
        if len(previous_words & words) >= 2:
            add = 0
        elif len(previous_words & words) == 1 and support_1 > 0.01 and support_2 > 0.01:
            add = 0
    if add == 1:
        words_list.append(words)


f = open(r'C:\\Users\\丁丁\\Desktop\\医院建设_新词组.txt', "w")
print(words_list, file=f)
f.close()
