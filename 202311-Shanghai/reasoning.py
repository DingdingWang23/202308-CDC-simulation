import os
import pandas as pd
import csv

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.expand_frame_repr', False)

df = pd.read_csv(r"C:\\Users\\丁丁\\Desktop\\物资集团测评\\1130\\group 5\\df.csv", encoding="gbk")
input = pd.read_csv(r"C:\\Users\\丁丁\\Desktop\\物资集团测评\\1130\\group 5\\node.csv", encoding="gbk")

merge_df = pd.merge(df, input, left_on='from', right_on='name', how='inner')
merge_df = pd.merge(merge_df, input, left_on='to', right_on='name', how='inner')

c_list = input.loc[input['class'] == 'c', 'name'].tolist()
f_list = input.loc[input['class'] == 'f', 'name'].tolist()

merge_df = merge_df.drop(columns=['name_x', 'lon_x', 'lat_x', 'type_x', 'name_y', 'lon_y', 'lat_y', 'type_y'])
merge_df.rename(columns={'class_x': 'from_class', 'class_y': 'to_class'}, inplace=True)
# print(merge_df)

c_f_df = merge_df.loc[(merge_df['from_class'] == 'c') & (merge_df['to_class'] == 'f'), ['from', 'to']].copy()
c_f_list = [tuple(row) for index, row in c_f_df .iterrows()]
# print(c_f_list)

f_f_df = merge_df.loc[(merge_df['from_class'] == 'f') & (merge_df['to_class'] == 'f'), ['from', 'to']].copy()
f_f_list = [tuple(row) for index, row in f_f_df .iterrows()]
print(f_f_df)
print(f_f_list)
print(len(f_f_list))

c_c_df = merge_df.loc[(merge_df['from_class'] == 'c') & (merge_df['to_class'] == 'c'), ['from', 'to']].copy()
c_c_list = [tuple(row) for index, row in c_c_df .iterrows()]
# print(c_c_list)

f_c_df = merge_df.loc[(merge_df['from_class'] == 'f') & (merge_df['to_class'] == 'c'), ['from', 'to']].copy()
f_c_list = [tuple(row) for index, row in f_c_df .iterrows()]
# print(f_c_list)

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

def pattern1(corpus_list, c_f_list, f_f_list, c_list, f_list):
    flag = [0]* len(corpus_list)

    arc = []
    num_arc = []
    for i in range(len(corpus_list)):
        if corpus_list[i] in c_list:
            flag[i] = 2
            for j in range(i+1, len(corpus_list)):
                if corpus_list[j] in f_list and (corpus_list[i], corpus_list[j]) in c_f_list:
                    flag[j] = 1
                    arc.append((corpus_list[i], corpus_list[j]))
                    num_arc.append((i+1,j+1))

    for i in range(len(corpus_list)):
        if flag[i] == 1:
            for j in range(i-1):
                if corpus_list[j] in f_list and (corpus_list[j], corpus_list[i]) in f_f_list:
                    flag[j] = 1
                    arc.append((corpus_list[j], corpus_list[i]))
                    num_arc.append((j+1, i+1))
    return flag, arc, num_arc

def pattern2(corpus_list, arc_pattern_1, f_f_list, f_list):
    fact_list = []
    pos_dict = {}
    arc =[]
    num_arc =[]
    my_f_f_list = []
    num_my_f_f_list = []

    idx2word = {}
    for i in range(len(corpus_list)):
        idx2word[i + 1] = corpus_list[i]

    for i in range(len(corpus_list)):
        if corpus_list[i] in f_list:
            fact_list.append(corpus_list[i])
            pos_dict[len(fact_list)] = i+1
    for i in range(len(fact_list)):
        for j in range(i+1,len(fact_list)):
            if (fact_list[i], fact_list[j]) in f_f_list and (fact_list[i], fact_list[j]) not in arc_pattern_1:
                my_f_f_list.append((fact_list[i], fact_list[j]))
                num_my_f_f_list.append((pos_dict[i+1], pos_dict[j+1]))

    print(my_f_f_list)
    print(num_my_f_f_list)

    for i in range(len(num_my_f_f_list)):
        for j in range(i+1,len(num_my_f_f_list)):
            if num_my_f_f_list[i][1] == num_my_f_f_list[j][0]:
                num_arc.append((num_my_f_f_list[i][0], num_my_f_f_list[i][1], num_my_f_f_list[j][1]))
                arc.append((idx2word[num_my_f_f_list[i][0]], idx2word[num_my_f_f_list[i][1]], idx2word[num_my_f_f_list[j][1]]))

    return arc, num_arc

def pattern3(corpus_list, c_c_list, f_c_list, c_list, f_list):
    flag = [0] * len(corpus_list)
    arc = []
    num_arc=[]
    for i in range(len(corpus_list)):
        if corpus_list[i] in c_list:
            flag[i] = 2
            for j in range(i + 1, len(corpus_list)):
                if corpus_list[j] in c_list and (corpus_list[i], corpus_list[j]) in c_c_list:
                    flag[j] = 2
                    arc.append((corpus_list[i], corpus_list[j]))
                    num_arc.append((i+1, j+1))
    for i in range(len(corpus_list)):
        if flag[i] == 2:
            for j in range(i - 1):
                if corpus_list[j] in f_list and (corpus_list[j], corpus_list[i]) in f_c_list:
                    flag[j] = 1
                    arc.append((corpus_list[j], corpus_list[i]))
                    num_arc.append((j+1, i+1))
    return flag, arc,num_arc

def pattern4(corpus_list, c_f_list, f_f_list, c_list, f_list):
    flag = [0] * len(corpus_list)
    arc = []
    num_arc =[]
    for i in range(len(corpus_list)):
        if corpus_list[i] in f_list:
            flag[i] = 1
            for j in range(i + 1, len(corpus_list)):
                if corpus_list[j] in f_list and (corpus_list[j], corpus_list[i]) in f_f_list:
                    flag[j] = 1
                    arc.append((corpus_list[j], corpus_list[i]))
                    num_arc.append((j+1, i+1))
                elif corpus_list[j] in c_list and (corpus_list[j], corpus_list[i]) in c_f_list:
                    flag[j] = 2
                    arc.append((corpus_list[j], corpus_list[i]))
                    num_arc.append((j+1, i+1))
    return flag, arc, num_arc

def pattern5(corpus_list, c_f_list, f_f_list, f_list):
    flag = [0] * len(corpus_list)
    arc = []
    num_arc =[]
    for i in range(len(corpus_list)):
        if corpus_list[i] in f_list:
            flag[i] = 1
            parent_c = []
            for tuple in c_f_list:
                if corpus_list[i] == tuple[1]:
                    parent_c.append(tuple[0])
            for j in range(i+1, len(corpus_list)):
                if corpus_list[j] in f_list and (corpus_list[i], corpus_list[j]) not in f_f_list and (corpus_list[j], corpus_list[i]) not in f_f_list:
                    for c in parent_c:
                        if (c, corpus_list[j]) in c_f_list:
                            flag[j] = 1
                            arc.append((corpus_list[i], corpus_list[j]))
                            num_arc.append((i + 1, j + 1))

    return flag, arc, num_arc

input_folder = r'C:\\Users\\丁丁\\Desktop\\物资集团测评\\1130\\group 5\\for_reasoning\\'
output_file = r'C:\\Users\\丁丁\\Desktop\\物资集团测评\\1130\\group 5\\reasoning.csv'

with open(output_file, 'a', newline='', encoding='utf-8-sig') as csvfile:
    writer = csv.writer(csvfile)
    # writer.writerow(['id', 'group', 'pattern', 'value'])
    for filename in os.listdir(input_folder):

        if filename.endswith('.tsv'):
            print(filename)
            input_filepath = os.path.join(input_folder, filename)
            # output_filepath = os.path.join(output_folder, os.path.splitext(filename)[0] + ".csv")
            # ode_list = []
            count_pattern_1 = 0
            count_pattern_2 = 0
            count_pattern_3 = 0
            count_pattern_4 = 0
            count_pattern_5 = 0

            with open(input_filepath, 'r', encoding='UTF-8') as file:
                data = []
                lines = file.readlines()
                for line in lines:
                    line = line.strip().split('  ')
                    if len(line) > 1:
                        index = int(line[0]) - 1

                        value = line[1]
                        print("value",value)
                        while index >= len(data):
                            data.append([])
                            # print(data)
                        data[index].append(value)

            for paragraph in data:
                # print("pattern1")
                print(pattern1(paragraph, c_f_list, f_f_list, c_list, f_list))
                num_arc_1 = pattern1(paragraph, c_f_list, f_f_list, c_list, f_list)[2]
                arc_pattern_1 = pattern1(paragraph, c_f_list, f_f_list, c_list, f_list)[1]
                adjacency_list = build_adjacency_list(num_arc_1)
                connected_components = find_connected_components(adjacency_list)
                print(connected_components)
                print(len(connected_components))
                count_pattern_1 += len(connected_components)

                # print("pattern2")
                print(pattern2(paragraph, arc_pattern_1, f_f_list, f_list))
                num_arc_2 = pattern2(paragraph, arc_pattern_1, f_f_list, f_list)[1]
                adjacency_list = build_adjacency_list(num_arc_2)
                connected_components = find_connected_components(adjacency_list)
                print(connected_components)
                print(len(connected_components))
                count_pattern_2 += len(connected_components)

                # print("pattern3")
                print(pattern3(paragraph, c_c_list, f_c_list, c_list, f_list))
                num_arc_3 = pattern3(paragraph, c_c_list, f_c_list, c_list, f_list)[2]
                adjacency_list = build_adjacency_list(num_arc_3)
                connected_components = find_connected_components(adjacency_list)
                print(connected_components)
                print(len(connected_components))
                count_pattern_3 += len(connected_components)

                # print("pattern4")
                print(pattern4(paragraph, c_f_list, f_f_list, c_list, f_list))
                num_arc_4 = pattern4(paragraph, c_f_list, f_f_list, c_list, f_list)[2]
                adjacency_list = build_adjacency_list(num_arc_4)
                connected_components = find_connected_components(adjacency_list)
                print(connected_components)
                print(len(connected_components))
                count_pattern_4 += len(connected_components)

                # print("pattern5")
                print(pattern5(paragraph, c_f_list, f_f_list, f_list))
                num_arc_5 = pattern5(paragraph, c_f_list, f_f_list, f_list)[2]
                adjacency_list = build_adjacency_list(num_arc_5)
                connected_components = find_connected_components(adjacency_list)
                print(connected_components)
                print(len(connected_components))
                count_pattern_5 += len(connected_components)

            writer.writerow([filename.replace(".tsv", ""), 1, count_pattern_1])
            writer.writerow([filename.replace(".tsv", ""), 2, count_pattern_2])
            writer.writerow([filename.replace(".tsv", ""), 3, count_pattern_3])
            writer.writerow([filename.replace(".tsv", ""), 4, count_pattern_4])

'''
paragraph = ['明确研究方向','承接项目情况','期刊发表情况', '建设重点实验室']

print(pattern1(paragraph, c_f_list, f_f_list, c_list, f_list))
num_arc_1 = pattern1(paragraph, c_f_list, f_f_list, c_list, f_list)[2]
arc_pattern_1 = pattern1(paragraph, c_f_list, f_f_list, c_list, f_list)[1]
adjacency_list = build_adjacency_list(num_arc_1)
connected_components = find_connected_components(adjacency_list)
print(connected_components)
print(len(connected_components))

print(pattern2(paragraph, arc_pattern_1, f_f_list, f_list))
num_arc_2 = pattern2(paragraph, arc_pattern_1, f_f_list, f_list)[1]
adjacency_list = build_adjacency_list(num_arc_2)
connected_components = find_connected_components(adjacency_list)
print(connected_components)
print(len(connected_components))
'''