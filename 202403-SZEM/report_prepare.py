import os
import pandas as pd
import csv

# 目标文件夹路径

input_folder = r"C:\\Users\\丁丁\\Desktop\\深圳演练\\uncertainty_node\\"
output_folder = r"C:\\Users\\丁丁\\Desktop\\深圳演练\\uncertainty_node_dropdup\\"


for filename in os.listdir(input_folder):
    # 检查文件扩展名是否为.tsv
    if filename.endswith('.tsv'):
        # 构建完整的文件路径
        file_path = os.path.join(input_folder, filename)
        # 读取文件
        with open(file_path, 'r', encoding='utf-8') as tsvfile:
            # 创建输出文件名（更改扩展名为.txt）
            output_filename = os.path.splitext(filename)[0].replace("uncertainty_","") + '.txt'
            # 构建输出文件的完整路径
            output_path = os.path.join(output_folder, output_filename)
            # 写入处理过的数据
            with open(output_path, 'w', encoding='utf-8') as txtfile:
                word_list = []
                for line in tsvfile:
                    # 使用制表符分割每行，并获取分割后的列表
                    parts = line.split(' ')
                    my_parts=[]
                    for part in parts:
                        if part !="":
                            my_parts.append(part)

                    if len(my_parts) > 1 and my_parts[1] not in word_list:
                        # 写入第一个制表符后的内容
                        txtfile.write(my_parts[1])
                        word_list.append(my_parts[1])

# 输入文件夹路径
input_folder = r"C:\\Users\\丁丁\\Desktop\\深圳演练\\arc_output_c_c\\"
# 输出文件夹路径
output_folder = r"C:\\Users\\丁丁\\Desktop\\深圳演练\\c_c_dropdup\\"

# 遍历输入文件夹中的所有文件
for filename in os.listdir(input_folder):
    # 检查文件扩展名是否为.csv
    if filename.endswith('.csv'):
        # 构建完整的文件路径
        file_path = os.path.join(input_folder, filename)
        # 读取CSV文件
        with open(file_path, 'r', encoding='utf-8') as csvfile:
            # 创建输出文件名（更改扩展名为.txt）
            output_filename = os.path.splitext(filename)[0].replace("all_sentence_","") + '.txt'
            # 构建输出文件的完整路径
            output_path = os.path.join(output_folder, output_filename)
            # 写入处理过的数据
            with open(output_path, 'w', encoding='utf-8') as txtfile:
                csv_reader = csv.reader(csvfile)  # 创建csv.reader对象
                arc_list=[]
                for row in csv_reader:
                    # 检查行是否至少有两个元素
                    if len(row) >= 2 and (row[0] + '\t' + row[1]) not in arc_list:
                        # 使用制表符分隔前两个元素
                        txtfile.write(row[0] + '\t' + row[1])
                        # 添加换行符以保持格式
                        txtfile.write('\n')
                        arc_list.append((row[0] + '\t' + row[1]))

input_folder = r"C:\\Users\\丁丁\\Desktop\\深圳演练\\node_output_去掉编号\\"
output_folder = r"C:\\Users\\丁丁\\Desktop\\深圳演练\\chance_node_dropdup\\"
chance_df = pd.read_csv(r"C:\\Users\\丁丁\\Desktop\\深圳演练\\chance_node.csv",encoding="gbk")


for filename in os.listdir(input_folder):
    # 检查文件扩展名是否为.tsv
    if filename.endswith('.tsv'):
        # 构建完整的文件路径
        file_path = os.path.join(input_folder, filename)
        # 读取文件
        with open(file_path, 'r', encoding='utf-8') as tsvfile:
            # 创建输出文件名（更改扩展名为.txt）
            output_filename = os.path.splitext(filename)[0].replace("all_sentence_","") + '.txt'
            # 构建输出文件的完整路径
            output_path = os.path.join(output_folder, output_filename)
            output_path = output_path.replace("all_sentence_", "")
            # 写入处理过的数据
            with open(output_path, 'w', encoding='utf-8') as txtfile:
                word_list=[]
                for line in tsvfile:
                    if line.strip() in chance_df['name'].values and line.strip() not in word_list:
                        txtfile.write(line.strip())
                        txtfile.write('\n')
                        word_list.append(line.strip())

input_folder = r"C:\\Users\\丁丁\\Desktop\\深圳演练\\node_output_去掉编号\\"
output_folder = r"C:\\Users\\丁丁\\Desktop\\深圳演练\\utility_node_dropdup\\"
utility_df = pd.read_csv(r"C:\\Users\\丁丁\\Desktop\\深圳演练\\utility_node.csv",encoding="gbk")

for filename in os.listdir(input_folder):
    # 检查文件扩展名是否为.tsv
    if filename.endswith('.tsv'):
        # 构建完整的文件路径
        file_path = os.path.join(input_folder, filename)
        # 读取文件
        with open(file_path, 'r', encoding='utf-8') as tsvfile:
            # 创建输出文件名（更改扩展名为.txt）
            output_filename = os.path.splitext(filename)[0].replace("all_sentence_","") + '.txt'
            # 构建输出文件的完整路径
            output_path = os.path.join(output_folder, output_filename)
            output_path=output_path.replace("all_sentence_","")
            # 写入处理过的数据
            with open(output_path, 'w', encoding='utf-8') as txtfile:
                word_list = []
                for line in tsvfile:
                    if line.strip() in utility_df['name'].values and line.strip() not in word_list:
                        txtfile.write(line.strip())
                        txtfile.write('\n')
                        word_list.append(line.strip())

# 输入文件夹路径
input_folder = r"C:\\Users\\丁丁\\Desktop\\深圳演练\\arc_output_d_others\\"
# 输出文件夹路径
output_folder = r"C:\\Users\\丁丁\\Desktop\\深圳演练\\d_others_dropdup\\"

# 遍历输入文件夹中的所有文件
for filename in os.listdir(input_folder):
    # 检查文件扩展名是否为.csv
    if filename.endswith('.csv'):
        # 构建完整的文件路径
        file_path = os.path.join(input_folder, filename)
        # 读取CSV文件
        with open(file_path, 'r', encoding='utf-8') as csvfile:
            # 创建输出文件名（更改扩展名为.txt）
            output_filename = os.path.splitext(filename)[0].replace("all_sentence_","") + '.txt'
            # 构建输出文件的完整路径
            output_path = os.path.join(output_folder, output_filename)
            # 写入处理过的数据
            with open(output_path, 'w', encoding='utf-8') as txtfile:
                csv_reader = csv.reader(csvfile)  # 创建csv.reader对象
                arc_list=[]
                for row in csv_reader:
                    # 检查行是否至少有两个元素
                    if len(row) >= 2 and (row[0] + '\t' + row[1]) not in arc_list:
                        # 使用制表符分隔前两个元素
                        txtfile.write(row[0] + '\t' + row[1])
                        # 添加换行符以保持格式
                        txtfile.write('\n')
                        arc_list.append((row[0] + '\t' + row[1]))

# 输入文件夹路径
input_folder = r"C:\\Users\\丁丁\\Desktop\\深圳演练\\arc_output_c_d\\"
# 输出文件夹路径
output_folder = r"C:\\Users\\丁丁\\Desktop\\深圳演练\\c_d_dropdup\\"

# 遍历输入文件夹中的所有文件
for filename in os.listdir(input_folder):
    # 检查文件扩展名是否为.csv
    if filename.endswith('.csv'):
        # 构建完整的文件路径
        file_path = os.path.join(input_folder, filename)
        # 读取CSV文件
        with open(file_path, 'r', encoding='utf-8') as csvfile:
            # 创建输出文件名（更改扩展名为.txt）
            output_filename = os.path.splitext(filename)[0].replace("all_sentence_","") + '.txt'
            # 构建输出文件的完整路径
            output_path = os.path.join(output_folder, output_filename)
            # 写入处理过的数据
            with open(output_path, 'w', encoding='utf-8') as txtfile:
                csv_reader = csv.reader(csvfile)  # 创建csv.reader对象
                arc_list=[]
                for row in csv_reader:
                    # 检查行是否至少有两个元素
                    if len(row) >= 2 and (row[0] + '\t' + row[1]) not in arc_list:
                        # 使用制表符分隔前两个元素
                        txtfile.write(row[0] + '\t' + row[1])
                        # 添加换行符以保持格式
                        txtfile.write('\n')
                        arc_list.append((row[0] + '\t' + row[1]))