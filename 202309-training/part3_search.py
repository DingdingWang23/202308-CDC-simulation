import heapq
import os
import pandas as pd
import csv

def dijkstra(nodes, edges, start_node):
    # 构建图的邻接字典
    graph = {}
    for node in nodes:
        graph[node] = []
    for edge in edges:
        source, target = edge
        weight = 1  # 这里默认边的权重都为1，如果是有权重的边，需要在edges中提供对应的权重
        graph[source].append((target, weight))
        graph[target].append((source, weight))

    # 初始化距离字典和堆
    distances = {node: float('inf') for node in nodes}
    distances[start_node] = 0
    heap = [(0, start_node)]

    while heap:
        current_distance, current_node = heapq.heappop(heap)

        # 如果当前节点已被处理过，跳过
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances

input_folder = r'C:\\Users\\丁丁\\Desktop\\医院建设_for_reasoning'
id2nodes = {}

for filename in os.listdir(input_folder):
    if filename.endswith('.txt'):
        print(filename)
        input_filepath = os.path.join(input_folder, filename)

        with open(input_filepath, 'r', encoding='UTF-8') as file:
            nodes = []
            lines = file.readlines()
            for line in lines:
                line = line.strip().split('\t')
                if len(line) > 1:
                    nodes.append(line[1])
            print(nodes)
            id2nodes[filename.replace(".txt","")] = nodes

print(id2nodes)

df = pd.read_csv(r"C:\\Users\\丁丁\\Desktop\\df_医院建设_1002.csv", encoding="gbk")
tuple_list = [tuple(row) for row in df.values.tolist()]

df = pd.read_csv(r"C:\\Users\\丁丁\\Desktop\\node_医院建设_1002.csv", encoding="utf-8")
print(df)
node_list = df.iloc[:, 0].tolist()

print(node_list)

output_folder_p = r'C:\\Users\\丁丁\\Desktop\\医院建设_p'
output_folder_q = r'C:\\Users\\丁丁\\Desktop\\医院建设_q'

search_output_file = r'C:\\Users\\丁丁\\Desktop\\search_1007.csv'

with open(search_output_file, 'a', newline='', encoding='utf-8-sig') as csvfile:
    writer = csv.writer(csvfile)
    # writer.writerow(['id', 'group', 'parameter', 'value'])
    for item in id2nodes:

        print(item)
        print(id2nodes[item])

        p_list = [0] * len(id2nodes[item])
        q_list = [0] * len(id2nodes[item])

        count_p = 0
        count_q_pos = 0
        count_q_neg = 0

        for i in range(1, len(p_list) - 1):
            if id2nodes[item][i - 1] == id2nodes[item][i + 1]:
                p_list[i] = 1
                count_p += 1

        for i in range(1, len(q_list) - 1):
            distances = dijkstra(node_list, tuple_list, id2nodes[item][i])
            prev = distances[id2nodes[item][i - 1]]
            nex = distances[id2nodes[item][i + 1]]

            distances_2 = dijkstra(node_list, tuple_list, id2nodes[item][i - 1])
            prev_nex = distances_2[id2nodes[item][i + 1]]
            print(prev, nex, prev_nex)
            if prev + nex == prev_nex:
                q_list[i] = 1
                count_q_pos += 1
            elif prev + nex > prev_nex:
                q_list[i] = -1
                count_q_neg += 1
        '''
        output_filepath_p = os.path.join(output_folder_p, item + ".csv")

        with open(output_filepath_p, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['p'])
            for item in p_list:
                writer.writerow([item])

        output_filepath_q = os.path.join(output_folder_q, item + ".csv")

        with open(output_filepath_q, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['q'])
        for item in q_list:
        writer.writerow([item])
        '''
        print(p_list)
        print(q_list)
        if len(p_list)>0:
            writer.writerow([item, '医院建设', '重复访问', count_p/len(p_list)])
            writer.writerow([item, '医院建设', '向外搜索', count_q_pos / len(q_list)])
            writer.writerow([item, '医院建设', '向内搜索', count_q_neg / len(q_list)])
        else:
            writer.writerow([item, '医院建设', '重复访问', 0])
            writer.writerow([item, '医院建设', '向外搜索', 0])
            writer.writerow([item, '医院建设', '向内搜索', 0])
