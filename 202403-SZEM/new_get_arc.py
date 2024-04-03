import os
import csv
import pandas as pd

# 定义输入文件夹路径
input_folder = r"C:\Users\丁丁\Desktop\深圳演练\node_output"

# 定义输出文件夹路径
output_folder = r"C:\Users\丁丁\Desktop\深圳演练\new_arc"

df = pd.read_csv(r"C:\\Users\\丁丁\\Desktop\\深圳演练\\df.csv", encoding="gbk")
input = pd.read_csv(r"C:\\Users\\丁丁\\Desktop\\深圳演练\\node.csv",encoding="gbk")

merge_df = pd.merge(df, input, left_on='from', right_on='name', how='inner')
merge_df = pd.merge(merge_df, input, left_on='to', right_on='name', how='inner')
merge_df = merge_df.drop(columns=['name_x', 'lon_x', 'lat_x', 'name_y', 'lon_y', 'lat_y'])
merge_df.rename(columns={'type_x': 'from_type', 'type_y': 'to_type'}, inplace=True)

d_others_df = merge_df.loc[(merge_df['from_type'] == 'd') , ['from', 'to']].copy()
d_others_list = [tuple(row) for index, row in d_others_df .iterrows()]
print(len(d_others_list))

notd_others_df = merge_df.loc[(merge_df['from_type'] != 'd') , ['from', 'to']].copy()
notd_others_list = [tuple(row) for index, row in notd_others_df .iterrows()]
print(len(notd_others_list))

word_pairs = d_others_list+notd_others_list
print(word_pairs)

# 确保输出文件夹存在，如果不存在则创建
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历输入文件夹中的每个文件
for filename in os.listdir(input_folder):
    # 构建完整的输入文件路径
    input_filepath = os.path.join(input_folder, filename)

    # 构建对应的输出文件路径
    output_filepath = os.path.join(output_folder, filename)

    # 打开输入文件并读取内容
    with open(input_filepath, 'r', encoding='utf-8') as infile:
        reader = csv.reader(infile, delimiter='\t')

        # 打开输出文件并准备写入内容
        with open(output_filepath, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile, delimiter='\t')

            # 初始化变量
            len = 0
            idx_list = []
            word_list = []

            # 逐行读取并处理
            for row in reader:
                len += 1

                words = row[0].split(" ")
                my_words = []
                for word in words:
                    if word != "":
                        my_words.append(word)
                idx_list.append(my_words[0])
                word_list.append(my_words[1])

            # 打印结果（可选）
            print(idx_list)
            print(word_list)

            # 创建arc列表
            arc = []
            for i in range(len):
                for j in range(i + 1, len):
                    if int(idx_list[j]) <= int(idx_list[i]) + 1 and (word_list[i], word_list[j]) in word_pairs:
                        arc.append((word_list[i], word_list[j]))

            # 打印arc列表（可选）
            print(arc)

            # 将arc列表写入输出文件
            for edge in arc:
                writer.writerow(edge)
