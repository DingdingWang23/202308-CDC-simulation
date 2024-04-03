import re
import spacy
from fuzzywuzzy import fuzz
import os


f = open(r"C:\\Users\\丁丁\\Desktop\\深圳演练\\nodelist.txt",encoding='utf-8')

node_list = []
for line in f.readlines():
    line = line.replace("\n", "")
    node_list.append(line)

nlp = spacy.load("zh_core_web_sm")

def fuzzy_match(sentences, list):

    max_phrase_list = []

    for sentence in sentences:
        sentence = nlp(sentence)
        new_sentence = ""

        for token in sentence:
            if token.pos_ != "SPACE" and token.is_stop == False:
                new_sentence = new_sentence + token.text

        similarities = []
        sentence = new_sentence

        for phrase in list:
            sim = fuzz.ratio(sentence,phrase)

            similarities.append((phrase, sim))

        sorted_similarities = sorted(similarities, key=lambda x: x[1], reverse=True)

        max_phrase_list.append(sorted_similarities[0][0])
        max_phrase_list.append(sorted_similarities[1][0])
        max_phrase_list.append(sorted_similarities[2][0])
        max_phrase_list.append(sorted_similarities[3][0])
        max_phrase_list.append(sorted_similarities[4][0])
        max_phrase_list.append(sorted_similarities[5][0])
        max_phrase_list.append(sorted_similarities[6][0])
        max_phrase_list.append(sorted_similarities[7][0])
        max_phrase_list.append(sorted_similarities[8][0])
        max_phrase_list.append(sorted_similarities[9][0])


    return max_phrase_list

input_folder = r"C:\\Users\\丁丁\\Desktop\\深圳演练\\每个人讲的话"
output_folder = r"C:\\Users\\丁丁\\Desktop\\深圳演练\\all_sentence_output"


# 获取输入文件夹中的文件列表
file_list = os.listdir(input_folder)


for file_name in file_list:
    if file_name.endswith(".txt"):
        # 读取数据
        with open(os.path.join(input_folder, file_name), "r", encoding="utf-8") as f:
            data = f.read()
        if data == "":
            data = "此处应该有一句话。"

        input_file_path = os.path.join(input_folder, file_name)

        # 将文本分割为句子
        sentences = re.split(r"[。？：]", data)
        sentence_list = []
        for i, sentence in enumerate(sentences):
            sentence = sentence.strip()
            if sentence:
                sentence_list.append(sentence)

        # 其他操作...
        print(len(sentence_list))
        ctr = 0

        second_list = []
        total_sub_sentences = []

        for sentence in sentence_list:
            ctr += 1
            sub_sentences = re.split(r"，", sentence)
            total_sub_sentences += sub_sentences
            for sub_sentence in sub_sentences:
                second_list.append(ctr)
        print(second_list)
        print(total_sub_sentences)

        sentence_phrase = fuzzy_match(total_sub_sentences, node_list)
        # 生成输出文件路径
        base_name = os.path.splitext(file_name)[0]

        all_sentence_output_file = os.path.join(output_folder, "all_sentence_" + base_name + ".tsv")


        with open(all_sentence_output_file, "w+", encoding="utf-8") as f:
            for i in range(len(sentence_phrase)):
                print(second_list[(i // 10)], "\t", total_sub_sentences[(i // 10)], "\t", sentence_phrase[i],
                      file=f)
