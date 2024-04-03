import os


def extract_before_uncertainties(sentence, uncertainty_words):
    # 将句子分解为多个分句
    sentences = sentence.split('。')

    # 存储提取的内容
    extracted = []

    # 对于每个分句，检查是否包含不确定性词汇
    for s in sentences:
        for word in uncertainty_words:
            if word in s:
                # 提取不确定性词汇前面的部分
                before_word = s.split(word)[0]
                extracted.append(before_word)

    return extracted


# 更新后的不确定词列表
uncertainty_words = ['可能', '不确定性', '的风险','概率']

# 输入和输出文件夹路径（请根据您的需求修改这些路径）
input_folder = r"C:\Users\丁丁\Desktop\深圳演练\每个人讲的话"
output_folder = r"C:\Users\丁丁\Desktop\深圳演练\每个人的不确定性节点"

# 确保输出文件夹存在
os.makedirs(output_folder, exist_ok=True)

# 遍历输入文件夹中的所有txt文件
for filename in os.listdir(input_folder):
    if filename.endswith(".txt"):
        # 构建输入和输出文件的完整路径
        input_file_path = os.path.join(input_folder, filename)
        output_file_path = os.path.join(output_folder, filename)

        # 读取文件内容
        with open(input_file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # 提取内容
        extracted_content = extract_before_uncertainties(content, uncertainty_words)

        # 将提取的内容写入到输出文件
        with open(output_file_path, 'w', encoding='utf-8') as file:
            for line in extracted_content:
                file.write(line + '\n')