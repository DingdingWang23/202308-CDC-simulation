import os


# 获取指定目录下的所有tsv文件
def get_files(directory):
    file_list = []
    for filename in os.listdir(directory):
        if filename.endswith(".tsv"):
            file_list.append(os.path.join(directory, filename))
    return file_list


# 合并相同group_id的tsv文件

def merge_tsvfiles(file_list):
    merged_data = {}
    for filepath in file_list:
        group = os.path.splitext(os.path.basename(filepath))[0].split('_')[2]
        id = os.path.splitext(os.path.basename(filepath))[0].split('_')[3]
        group_id = group+"_"+id
        print(group_id)

        with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                print(line.strip())
                word = line.strip().split('  ')[1]
                if group_id in merged_data:
                    merged_data[group_id].add(word)
                else:
                    merged_data[group_id] = {word}
            print("merged_data", merged_data)
            print("merged_data", merged_data)

            output_path = r"C:\\Users\\丁丁\\Desktop\\物资集团测评\\1130\\group 5\\group_id_node_output_dropdup\\"
            # 生成合并后的新tsv文件
            with open(output_path+group_id+".tsv", 'w', encoding='utf-8') as f:
                
                # for group_id, words in merged_data.items():
                    # for word in words:
                        # f.write(f"{word}\n")
                
                for word in merged_data[group_id]:
                    f.write(f"{word}\n")


'''
def merge_tsvfiles(file_list):
    merged_data = {}

    for filepath in file_list:
        group = os.path.splitext(os.path.basename(filepath))[0].split('_')[2]
        id = os.path.splitext(os.path.basename(filepath))[0].split('_')[3]
        group_id = group + "_" + id
        print(group_id)

        with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                word = line.strip().split('  ')[1]
                if group_id in merged_data:
                    merged_data[group_id].append(word)
                else:
                    merged_data[group_id] = [word]

        output_path = r"C:\\Users\\丁丁\\Desktop\\物资集团测评\\1130\\group 5\\group_id_node_output\\"

        # Generate the merged TSV file
        with open(output_path + group_id + ".tsv", 'w', encoding='utf-8') as f:
            for word in merged_data[group_id]:
                f.write(f"{word}\n")
'''
# 指定tsv文件所在的目录
directory = r"C:\\Users\\丁丁\\Desktop\\物资集团测评\\1130\\group 5\\node_output"

# 获取该目录下的所有tsv文件
file_list = get_files(directory)
print("file_list", file_list)

# 合并并生成新的tsv文件
merge_tsvfiles(file_list)
