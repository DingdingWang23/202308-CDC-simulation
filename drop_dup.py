import os
import pandas as pd

# 目标文件夹路径
target_folder = r"C:\\Users\\丁丁\\Desktop\\深圳演练\\node_output_去掉编号\\"
output_folder = r"C:\\Users\\丁丁\\Desktop\\深圳演练\\node_output_dropdup_去掉编号\\"

# 获取文件夹中的所有文件
file_list = os.listdir(target_folder)

# 遍历所有文件
for file in file_list:
    # 构建完整的文件路径
    file_path = os.path.join(target_folder, file)

    # 检查文件扩展名是否为.tsv
    if file.endswith('.tsv'):
        # 读取TSV文件
        df = pd.read_csv(file_path, sep='\t', encoding='utf-8')

        # 删除重复行
        df_unique = df.drop_duplicates()

        # 构建输出文件的路径，将.tsv替换为.txt
        txt_file_path = output_folder+file.replace('.tsv','') + '.txt'
        print(txt_file_path)

        # 将处理后的DataFrame保存为文本文件，不带索引
        with open(txt_file_path, 'w', encoding='utf-8') as file_out:
            # 如果DataFrame有多列，使用to_string保留列结构
            file_out.write(df_unique.to_string(header=True, index=False).replace(" ",""))

print("转换完成！")