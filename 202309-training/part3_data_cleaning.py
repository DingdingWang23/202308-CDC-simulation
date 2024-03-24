import os
import re

input_folder = r'C:\\Users\\丁丁\\Desktop\\医院建设'
input_folder2 = r'C:\\Users\\丁丁\\Desktop\\医院建设_node_output'
output_folder = r'C:\\Users\\丁丁\\Desktop\\医院建设_for_reasoning'

for filename in os.listdir(input_folder):

    if filename.endswith('.txt'):
        input_filepath = os.path.join(input_folder, filename)
        print(filename)

        with open(input_filepath, 'r') as file:
            contents = file.read()
            paragraphs = contents.split("\n")
            paragraphs = [x for x in paragraphs if len(x) > 1]
            print(paragraphs)

            sentence_id = 1
            paragraph_id = 1
            sentence2paragraph = {}
            for paragraph in paragraphs:
                sentences = re.split(r"[。？：]", paragraph)
                sentences = [x for x in sentences if len(x) > 1]
                print(sentences)
                print(len(sentences))

                for i in range(len(sentences)):
                    sentence2paragraph[sentence_id+i] = paragraph_id
                sentence_id += len(sentences)
                paragraph_id += 1
        print(sentence2paragraph)

        input_filepath2 = os.path.join(input_folder2, "all_sentence_" + os.path.splitext(filename)[0] + ".tsv")
        paragraph_list = []
        node_list = []
        with open(input_filepath2, 'r', encoding='UTF-8') as file:
            contents = file.read()
            contents = contents.split("\n")
            for line in contents:
                words = line.split('  ')
                if len(words) > 1:
                    paragraph_list.append(sentence2paragraph[int(words[0])])
                    node_list.append(words[1])

        output_filepath = os.path.join(output_folder, filename)
        with open(output_filepath, 'w', encoding='utf-8') as file:
            for i in range(len(node_list)):

                line = str(paragraph_list[i]) + '\t' + str(node_list[i]) + '\n'

                file.write(line)

