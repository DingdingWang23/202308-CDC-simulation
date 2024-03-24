import os
import pandas as pd
import csv
import numpy as np
import os
import collections
import math

'''
input_folder = r"C:\\Users\\丁丁\\Desktop\\物资集团测评\\1130\\group 1\\group_id_node_output"
output_folder = r'C:\\Users\\丁丁\\Desktop\\物资集团测评\\1130\\group 1\\utility_merge'
shuchu_folder = r'C:\\Users\\丁丁\\Desktop\\物资集团测评\\1130\\group 1\\utility_merge_新'
plot_1_folder = r'C:\\Users\\丁丁\\Desktop\\物资集团测评\\1130\\group 1\\plot_1'
'''
'''
for filename in os.listdir(input_folder):

    if filename.endswith('.tsv'): 
        input_filepath = os.path.join(input_folder, filename)
        output_filepath = os.path.join(input_folder, os.path.splitext(filename)[0] + ".csv")

        node_list = []

        with open(input_filepath, 'r', encoding='UTF-8') as file:
            contents = file.read()
            contents = contents.split("\n")
            for line in contents:
                words = line.strip()
                if len(words)>1:
                    node_list.append(words)

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

        df = pd.read_csv(r"C:\\Users\\丁丁\\Desktop\\物资集团测评\\1130\\group 1\\utility_node.csv",encoding="gbk")
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
                C[i, 5] = 1

        df = pd.DataFrame(C, columns=['name', 'lon','lat', 'type', 'class', 'existence'])
        df.to_csv(output_file, index=False, encoding='gbk')


file_list = os.listdir(output_folder)

for file_name in file_list:
    if file_name.endswith(".csv"):
        input_file = os.path.join(output_folder, file_name)
        output_filepath = os.path.join(shuchu_folder, file_name)

        df = pd.read_csv(input_file, encoding="gbk")
        df.loc[df['existence'] != 1, 'type'] = 'N'
        df.to_csv(output_filepath, index=False, encoding='gbk')
'''
'''
file_list = os.listdir(input_folder)

for file_name in file_list:
    if file_name.endswith(".csv"):
        input_file = os.path.join(input_folder, file_name)
        output_file = os.path.join(plot_1_folder, os.path.splitext(file_name)[0].replace("all_sentence_", "") + ".csv")

        df = pd.read_csv(r"C:\\Users\\丁丁\\Desktop\\物资集团测评\\1130\\group 5\\node.csv", encoding="gbk")
        # print(df)

        input = pd.read_csv(input_file,encoding="utf-8")
        # input = input.drop_duplicates(['name'])
        print(input)

        name2type = {}
        for i in range(len(df)):
            name2type[df.iloc[i,0]]=df.iloc[i,3]

        print(name2type)

        merge_df = np.column_stack((input, np.zeros(input.shape[0])))

        for i in range(len(input)):
            merge_df[i, 1] = name2type[input.iloc[i,0]]

        merge_df = pd.DataFrame(merge_df, columns=['name', 'type'])

        # merge_df = pd.merge(input, df, on="name", how='inner')
        print(merge_df)

        merge_df.to_csv(output_file, index=False, encoding='gbk')
'''

node_file = r"C:\\Users\\丁丁\\Desktop\\物资集团测评\\1130\\group 1\\node.csv"

df = pd.read_csv(node_file,encoding="gbk")
#print(df)
num_node = len(df)
print(num_node)
nodes= df['name']
# print(nodes)
# print(len(nodes))
my_list = []

input_folder=r"C:\\Users\\丁丁\\Desktop\\物资集团测评\\1130\\group 1\\group_id_node_output_dropdup"
file_list = os.listdir(input_folder)

for file_name in file_list:
    if file_name.endswith(".tsv"):
        input_file = os.path.join(input_folder, file_name)

        with open(input_file,"r",encoding="utf-8") as f:
            id_nodes = f.readlines()
            for item in id_nodes:
                if item not in my_list:
                    my_list.append(item)
            # print(len(my_list))
            #print(my_list)

num_node_true=len(my_list)
print(num_node_true)
dict={}

for item in nodes:
    flag = 0
    print(item+"\n")
    print(my_list)
    if item+"\n" in my_list:
        dict[item]=1
        flag = 1
    if flag==0:
        dict[item] = 0
print("dict=",dict)

df_file = r"C:\\Users\\丁丁\\Desktop\\物资集团测评\\1130\\group 1\\df.csv"
df = pd.read_csv(df_file,encoding="gbk")
# print(df)
start_list=df['from']
end_list=df['to']
start_end=pd.concat([start_list,end_list],axis=0,ignore_index=False)
# print(start_end)
# print(len(start_end))
count = collections.Counter(start_end)

sorted_dict = sorted(count.items(), key=lambda x: x[1], reverse=True)

top_30_percent = sorted_dict[:math.ceil(num_node*0.3)]
sum = 0
for i in range(len(top_30_percent)):
    value = top_30_percent[i][1]
    # print(value)
    sum+= value
average = sum/len(top_30_percent)
print(average)