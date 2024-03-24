import os
import pandas as pd
import csv
import numpy as np
import os


# input_folder = r'C:\\Users\\丁丁\\Desktop\\干部队伍建设_node_output'
output_folder = r'C:\\Users\\丁丁\\Desktop\\医院建设_merge'
shuchu_folder = r'C:\\Users\\丁丁\\Desktop\\医院建设_merge_新'

'''
for filename in os.listdir(input_folder):

    if filename.endswith('.tsv'): 
        input_filepath = os.path.join(input_folder, filename)
        output_filepath = os.path.join(output_folder, os.path.splitext(filename)[0] + ".csv")

        node_list = []

        with open(input_filepath, 'r', encoding='UTF-8') as file:
            contents = file.read()
            contents = contents.split("\n")
            for line in contents:
                words = line.split('  ')
                if len(words) > 1:
                    node_list.append(words[1])

            print("*******",node_list)


            with open(output_filepath, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)

                # 写入标题行
                writer.writerow(['name'])

                # 遍历列表，将每个元素写入新的一行
                for item in node_list:
                    writer.writerow([item])

'''
'''
file_list = os.listdir(input_folder)

for file_name in file_list:
    if file_name.endswith(".csv"):
        input_file = os.path.join(input_folder, file_name)
        output_file = os.path.join(output_folder, os.path.splitext(file_name)[0].replace("all_sentence_", "") + ".csv")

        df = pd.read_csv(r"C:\\Users\\丁丁\\Desktop\\node_干部队伍建设_1002.csv")
        print(df)

        input = pd.read_csv(input_file)
        input = input.drop_duplicates(['name'])
        print(input)

        merge_df = pd.merge(df, input, on="name", how='inner')
        print(merge_df)

        C = np.column_stack((df, np.zeros(df.shape[0])))

        # 在矩阵 C 的第三列进行匹配判断
        for i in range(len(df)):

            if df.iloc[i,0] in list(input['name']):
                C[i, 4] = 1

        df = pd.DataFrame(C, columns=['name', 'lon','lat','type','existence'])
        df.to_csv(output_file, index=False, encoding='gbk')


'''
file_list = os.listdir(output_folder)

for file_name in file_list:
    if file_name.endswith(".csv"):
        input_file = os.path.join(output_folder, file_name)
        output_filepath = os.path.join(shuchu_folder, file_name)

        df = pd.read_csv(input_file, encoding="gbk")
        df.loc[df['existence'] != 1, 'type'] = 'N'
        df.to_csv(output_filepath, index=False, encoding='gbk')
