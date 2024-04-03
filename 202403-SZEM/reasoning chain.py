import csv
import os

# 定义输入文件夹路径
input_folder = r"C:\Users\丁丁\Desktop\深圳演练\arc_output"

# 定义输出文件夹路径
output_folder = r"C:\Users\丁丁\Desktop\深圳演练\推理链条"
tuple_list = []

def build_adjacency_list(edges):
    adjacency_list = {}
    for edge in edges:
        if len(edge) != 2:
            print("注意！")
            continue
        u, v = edge
        if u not in adjacency_list:
            adjacency_list[u] = []
        if v not in adjacency_list:
            adjacency_list[v] = []
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)
    return adjacency_list


def dfs(node, adjacency_list, visited, connected_component):
    visited.add(node)
    connected_component.add(node)

    if node in adjacency_list:
        for neighbor in adjacency_list[node]:
            if neighbor not in visited:
                dfs(neighbor, adjacency_list, visited, connected_component)


def find_connected_components(adjacency_list):
    visited = set()
    connected_components = []

    for node in adjacency_list:
        if node not in visited:
            connected_component = set()
            dfs(node, adjacency_list, visited, connected_component)
            connected_components.append(connected_component)

    return connected_components

# 遍历输入文件夹中的每个文件
for filename in os.listdir(input_folder):
    # 构建完整的输入文件路径
    input_filepath = os.path.join(input_folder, filename)

    # 构建对应的输出文件路径
    output_filepath = os.path.join(output_folder, filename)

    # 打开输入文件并读取内容
    with open(input_filepath, 'r', encoding='utf-8') as infile:
        csv_reader = csv.reader(infile)

        # next(csv_reader)
        tuple_list=[]
        # 将每一行转换为元组并添加到列表中
        for row in csv_reader:
            # 将字符串列表转换为元组
            row_tuple = tuple(row)
            # 将元组添加到列表中
            tuple_list.append(row_tuple)

            adjacency_list = build_adjacency_list(tuple_list)

            # 找出所有连接的图的元素
            connected_components = find_connected_components(adjacency_list)

            component_filepath = os.path.join(output_folder, filename.replace(".csv",".txt"))

            # 打开输出文件并写入内容
            with open(component_filepath, 'w', newline='', encoding='utf-8') as outfile:
                for item in connected_components:
                    outfile.write(str(item))
                    outfile.write("\n")

# 所有文件处理完成
print(f"All files have been processed and saved to {output_folder}")
