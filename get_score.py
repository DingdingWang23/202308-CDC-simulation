import os

# 输入文件夹路径
input_folder_path = r"C:\\Users\\丁丁\\Desktop\\深圳演练\\c_d_dropdup\\"
# 输出文件夹路径
output_folder_path = r"C:\\Users\\丁丁\\Desktop\\深圳演练\\2_3_score\\"

# 遍历输入文件夹中的所有文件
for filename in os.listdir(input_folder_path):
    # 检查文件扩展名是否为.txt
    if filename.endswith('.txt'):
        # 构建完整的文件路径
        file_path = os.path.join(input_folder_path, filename)
        # 计算文件行数
        with open(file_path, 'r', encoding='utf-8') as txtfile:
            # 读取所有行
            lines = txtfile.readlines()
            # 行数即为列表长度
            line_count = len(lines)

        # 创建输出文件名（这里我们直接在原文件名后加上 "_linecount"）
        output_filename = os.path.splitext(filename)[0] + '.txt'
        # 构建输出文件的完整路径
        output_path = os.path.join(output_folder_path, output_filename)
        # 将行数写入到输出文件
        with open(output_path, 'w', encoding='utf-8') as outputfile:
            outputfile.write(str(line_count))