import os
from docx import Document

#定义文件夹路径
folder_path = r'C:\\Users\\丁丁\\Desktop\\物资集团测评\\每组讲的话_原始'

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

print(file_contents)
total_corpus = []


for file_content in file_contents:
    group_dict = [[],[],[],[],[],[],[],[],[],[]]

    sentences = file_content.split("\n\n")
    print(sentences)
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
        print(sentence)

        if "说话人 10" in sentence:
            group_dict[9].append(said)
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
        elif "说话人 1" in sentence:
            group_dict[0].append(said)
    print(group_dict)


    for i in range(len(group_dict)):
        if group_dict[i] != []:
            total_corpus.append(group_dict[i])

total_said = []
for person_said in total_corpus:
    total_said += person_said
print(total_said)
print(len(total_said))

print(total_corpus)
print(len(total_corpus))

output_folder = r'C:\\Users\\丁丁\\Desktop\\物资集团测评\\每个人讲的话'

for index, item in enumerate(total_corpus):
   file_path = os.path.join(output_folder, f'{index+1}.txt')
   with open(file_path, 'w') as f:
       for sentence in item:
        f.write(sentence)
        f.write("\n")
