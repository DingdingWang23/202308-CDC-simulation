import os
import csv
import pandas as pd
#####

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.expand_frame_repr', False)

df = pd.read_csv(r"C:\\Users\\丁丁\\Desktop\\深圳演练\\df.csv", encoding="gbk")
input = pd.read_csv(r"C:\\Users\\丁丁\\Desktop\\深圳演练\\node.csv",encoding="gbk")

merge_df = pd.merge(df, input, left_on='from', right_on='name', how='inner')
merge_df = pd.merge(merge_df, input, left_on='to', right_on='name', how='inner')

c_list = input.loc[input['type'] == 'c', 'name'].tolist()
d_list = input.loc[input['type'] == 'd', 'name'].tolist()

merge_df = merge_df.drop(columns=['name_x', 'lon_x', 'lat_x', 'name_y', 'lon_y', 'lat_y'])
merge_df.rename(columns={'type_x': 'from_type', 'type_y': 'to_type'}, inplace=True)

c_c_df = merge_df.loc[(merge_df['from_type'] == 'c') & (merge_df['to_type'] == 'c'), ['from', 'to']].copy()
c_c_list = [tuple(row) for index, row in c_c_df .iterrows()]
print(len(c_c_list))

d_others_df = merge_df.loc[(merge_df['from_type'] == 'd') , ['from', 'to']].copy()
d_others_list = [tuple(row) for index, row in d_others_df .iterrows()]
print(len(d_others_list))

c_d_df = merge_df.loc[(merge_df['from_type'] == 'c') & (merge_df['to_type'] == 'd'), ['from', 'to']].copy()
c_d_list = [tuple(row) for index, row in c_d_df .iterrows()]
print(len(c_d_list))

notd_others_df = merge_df.loc[(merge_df['from_type'] != 'd') , ['from', 'to']].copy()
notd_others_list = [tuple(row) for index, row in notd_others_df .iterrows()]
print(len(notd_others_list))

all_list = d_others_list+notd_others_list

# 定义输入文件夹路径
input_folder = r"C:\Users\丁丁\Desktop\深圳演练\new_arc"

# 定义输出文件夹路径
output_folder = r"C:\Users\丁丁\Desktop\深圳演练\arc_output"

# 确保输出文件夹存在，如果不存在则创建
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历输入文件夹中的每个文件
for filename in os.listdir(input_folder):
    # 构建完整的输入文件路径
    input_filepath = os.path.join(input_folder, filename)

    # 构建对应的输出文件路径
    output_filepath = os.path.join(output_folder, filename.replace("all_sentence_","").replace(".tsv",".csv"))

    # 打开输入文件并读取内容
    with open(input_filepath, 'r', encoding='utf-8') as infile:
        reader = csv.reader(infile, delimiter='\t')

        # 打开输出文件并写入内容
        with open(output_filepath, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)

            # 写入标题行
            # writer.writerow(next(reader))

            # 写入剩余的行
            for row in reader:
                print(row)
                if tuple(row) in all_list:
                    print("in!")
                    writer.writerow(row)


output_folder = r"C:\Users\丁丁\Desktop\深圳演练\arc_output_c_c"

for filename in os.listdir(input_folder):
    # 构建完整的输入文件路径
    input_filepath = os.path.join(input_folder, filename)

    # 构建对应的输出文件路径
    output_filepath = os.path.join(output_folder, filename.replace("all_sentence_","").replace(".tsv",".csv"))

    # 打开输入文件并读取内容
    with open(input_filepath, 'r', encoding='utf-8') as infile:
        reader = csv.reader(infile, delimiter='\t')

        # 打开输出文件并写入内容
        with open(output_filepath, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)

            # 写入标题行
            # writer.writerow(next(reader))

            # 写入剩余的行
            for row in reader:
                print(row)
                if tuple(row) in c_c_list:
                    print("c_c!")
                    writer.writerow(row)

output_folder = r"C:\Users\丁丁\Desktop\深圳演练\arc_output_d_others"

for filename in os.listdir(input_folder):
    # 构建完整的输入文件路径
    input_filepath = os.path.join(input_folder, filename)

    # 构建对应的输出文件路径
    output_filepath = os.path.join(output_folder, filename.replace("all_sentence_","").replace(".tsv",".csv"))

    # 打开输入文件并读取内容
    with open(input_filepath, 'r', encoding='utf-8') as infile:
        reader = csv.reader(infile, delimiter='\t')

        # 打开输出文件并写入内容
        with open(output_filepath, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)

            # 写入标题行
            # writer.writerow(next(reader))

            # 写入剩余的行
            for row in reader:
                print(row)
                if tuple(row) in d_others_list:
                    writer.writerow(row)
                    print("d_others!")

output_folder = r"C:\Users\丁丁\Desktop\深圳演练\arc_output_c_d"

for filename in os.listdir(input_folder):
    # 构建完整的输入文件路径
    input_filepath = os.path.join(input_folder, filename)

    # 构建对应的输出文件路径
    output_filepath = os.path.join(output_folder, filename.replace("all_sentence_","").replace(".tsv",".csv"))

    # 打开输入文件并读取内容
    with open(input_filepath, 'r', encoding='utf-8') as infile:
        reader = csv.reader(infile, delimiter='\t')

        # 打开输出文件并写入内容
        with open(output_filepath, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)

            # 写入标题行
            # writer.writerow(next(reader))

            # 写入剩余的行
            for row in reader:
                print(row)
                if tuple(row) in c_d_list:
                    writer.writerow(row)
                    print("c_d!")