import spacy

nlp = spacy.load("zh_core_web_sm")

with open(r'C:\\Users\\丁丁\\Desktop\\学生工作_新词组.txt', 'r') as file:
    # 读取文件内容
    contents = file.read()

# 将文件内容转换为列表
data_list = eval(contents)

total_pos_list = []
class_list = []

for my_set in data_list:
    pos_list = []
    for item in my_set:
        word = nlp(item)
        for token in word:
            # print(token.text)
            pos_list.append(token.pos_)

    total_pos_list.append(pos_list)
    if 'ADJ' in pos_list:
        class_list.append('utility node')
    elif 'VERB' in pos_list:
        class_list.append('decision node')
    else:
        class_list.append('chance node')


print(data_list)
print(total_pos_list)


with open(r'C:\\Users\\丁丁\\Desktop\\学生工作_分类.txt', 'w') as f:
    for item1, item2 in zip(data_list, class_list):
        f.write(str(item1) + ' ' + str(item2) + '\n')
