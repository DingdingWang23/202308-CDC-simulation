import pandas as pd
import os


input_folder = r"C:\\Users\\丁丁\\Desktop\\物资集团测评\\1130\\group 5\\group_id_node_output"
output_folder = r"C:\\Users\\丁丁\\Desktop\\物资集团测评\\1130\\group 5\\plot_2"

file_list = os.listdir(input_folder)

for file_name in file_list:
    if file_name.endswith(".csv"):
        input_file = os.path.join(input_folder, file_name)
        output_file = os.path.join(output_folder, os.path.splitext(file_name)[0] + ".csv")

        df = pd.read_csv(r"C:\\Users\\丁丁\\Desktop\\物资集团测评\\1130\\group 5\\df.csv", encoding="gbk")
        print(df)

        input = pd.read_csv(input_file,encoding="utf-8")
        print(input)
        node_list = input.iloc[:,0].tolist()
        print(node_list)

        # 检查ab两列是否都在list中，并保留满足条件的行
        df = df.loc[df['from'].isin(node_list) & df['to'].isin(node_list)]
        # 打印结果
        print(df)

        df.to_csv(output_file, index=False, encoding='gbk')



