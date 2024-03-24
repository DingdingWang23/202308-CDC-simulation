# -*- coding: utf-8 -*-

import os
import csv
import numpy as np
import matplotlib.pyplot as plt

# 延安精神 - \\report
data_dir = r"C:\\Users\\丁丁\\Desktop\\延安精神_report\\"
table_dir = r"C:\\Users\\丁丁\\Desktop\\延安精神_report_table\\"
history_dir = r"C:\\Users\\丁丁\\Desktop\\延安精神_report_history\\"
book_dir = r"C:\\Users\\丁丁\\Desktop\\延安精神_report_book\\"
other_perspective_dir = r"C:\\Users\\丁丁\\Desktop\\延安精神_report_other_perspectives\\"
total_score_dir = r"C:\\Users\\丁丁\\Desktop\\延安精神_report_total_score\\"
ability_dir = r"C:\\Users\\丁丁\\Desktop\\七项能力\\"

output_root = r"C:\\Users\\丁丁\\Desktop\\report_output\\"

data_dirs = os.listdir(data_dir)
ipt0 = []

for dir in data_dirs:

    print(dir)
    group, id = dir.split('.')[0].split('_')
    output_file = output_root + "{}_{}.md".format(group, id)

    markdown_content = """

# 个人发言内容总结

第{}组 第{}位发言人
**报告说明**：全体老师的发言内容主要涉及五个主题，分别为*（1）对于延安精神的理解；（2）干部队伍建设；（3）教学、科研及学生工作；（4）行政办公室、财务、规划、信息技术及法务工作；（5）医院建设。*本报告对个人发言中这五个主题的内容分别进行了抽取和简要分析。

[toc]

## 主题一：延安精神

本部分抽取了个人发言中与延安精神有关的内容。首先，根据延安精神的内涵分三个角度（*为人民服务、实事求是、自力更生艰苦奋斗*）概括了发言的主旨（对延安精神的理解）和关于联系实际的内容；其次，提取了发言中的史实和著作；此外，针对老师们提及的其他角度（*干部作风、道路自信、组织纪律、创新、民主集中制、政治站位、团队建设、调研和征求意见、联系群众、理想信念、学习的重要性、基层工作的重要性*）也作了概括。

<center>表1.1 对于延安精神的理解（精神内涵）</center>
""".format(group,id)

    with open(output_file, 'w') as f:
        f.write(markdown_content)

    with open(table_dir+dir, 'r', encoding='utf-8') as f:
        table = f.read()
        print(table)

    lines = table.split("\n")
    title = "|角度|对延安精神的理解|联系实际的内容|"
    new_line = "|---|---|---|"
    table = title+"\n"+new_line+"\n"+lines[0]+"\n"+lines[1]+"\n"+lines[2]+"\n"
    print(table)

    with open(output_file, 'a') as f:
        f.write(table)

    markdown_content = """
<center>表1.2 提到的史实和著作</center>
"""
    with open(output_file, 'a') as f:
        f.write(markdown_content)

    with open(history_dir+"history_"+dir, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        history = []
        for item in lines:
            history.append(item.strip())
        history = "".join(history)

    with open(book_dir+"book_"+dir, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        book = []
        for item in lines:
            book.append(item.strip())
        book = "".join(book)

    title = "|来源|内容|"
    new_line = "|---|---|"
    new_table = title + "\n" + new_line + "\n" + "|史实|"+ history + "|\n" + "|著作|"+ book + "|\n"
    print(new_table)

    with open(output_file, 'a') as f:
        f.write(new_table)

    markdown_content = """
对于延安精神的理解（老师们重点提及的其他方面）包括：
"""
    with open(output_file, 'a') as f:
        f.write(markdown_content)
    with open(other_perspective_dir+"other_perspectives_"+dir, 'r', encoding='utf-8') as f:
        other_perspective = f.read()
    with open(output_file, 'a') as f:
        f.write(other_perspective)


    with open(total_score_dir +"total_score_"+dir, 'r', encoding='utf-8') as f:
        total_score = f.read().strip()
        print(total_score)

    ipt0.append((group, id, float(total_score)/12))


# 干部队伍建设_Rplot
ipt1 = []
data_dir = r"D:\\干部队伍建设_Rplot\\"

output_root = r"C:\\Users\\丁丁\\Desktop\\report_output\\"
data_dirs = os.listdir(data_dir)

for dir in data_dirs:
    group, id = dir.split('.')[0].split('_')
    output_file = output_root + "{}_{}.md".format(group, id)

    markdown_content = """
## 主题二：干部队伍建设

本部分抽取了个人发言中与干部队伍建设有关的内容。首先，根据全体老师的发言内容，梳理了老师们所提及的干部队伍建设的*工作目标、工作基础/条件、工作措施*；同时，根据与延安精神的相关性、与高质量发展的相关性、老师们提及的频率等，参考因果/依赖关系分析的结果，识别了重要性较高/较低的目标、基础/条件与措施；此外，针对是否提及领导干部的七项能力（*政治能力、调查研究能力、科学决策能力、改革攻坚能力、应急处突能力、群众工作能力、抓落实能力*）进行了统计。

<center class="half">
    <img src="干部队伍建设_Rplot/{}_{}.png"/>
</center>
<center style="font-size:12px">图2.1 干部队伍建设的工作目标（蓝色）、工作基础/条件（黄色）与工作措施（红色）（深色-重要性较高；浅色-重要性较低；灰色-未提及）</center>

""".format(group, id, group, id)

    with open(output_file, 'a') as f:
        f.write(markdown_content)

# read node type
node_dict = {}
node_dict_low = {}
node_dict_high = {}
with open(r"C:\\Users\\丁丁\\Desktop\\node_干部队伍建设_1002.csv", 'r', encoding="utf-8") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        node, _1, _2, type, _3 = row
        node_dict[node] = type
        if type in ['u', 'd', 'c']:
            node_dict_low[node] = type
        else:
            node_dict_high[node] = type

node_dir = r"C:\\Users\\丁丁\\Desktop\\干部队伍建设_node_output\\"
node_dirs = os.listdir(node_dir)

for dir in node_dirs:
    print(dir)
    if dir.split('.')[1] != 'tsv':
        continue
    _1, _2, group, id = dir.split('.')[0].split('_')
    output_file = output_root + "{}_{}.md".format(group, id)
    with open(node_dir + dir, 'r', encoding="utf-8") as f:
        nodes = f.read().strip().split('\n')
        print("nodes",nodes)
        if len(nodes) > 1:
            nodes = [node.split('  ')[1] for node in nodes]

        nodes = [node for node in nodes if node != ""]
        nodes = [node for node in nodes if node in node_dict.keys()]
        nodes = list(set(nodes))

    ## 目标
    markdown_content = """
发言中提及的干部队伍建设的工作目标有：
"""
    with open(output_file, 'a') as f:
        f.write(markdown_content)

    for node in nodes:
        if node_dict[node] == 'U':
            markdown_content = """
- {}
""".format(node)
        else:
            markdown_content = ""
        with open(output_file, 'a') as f:
            f.write(markdown_content)

    for node in nodes:
        if node_dict[node] == 'u':
            markdown_content = """
- {}
""".format(node)
        else:
            markdown_content = ""
        with open(output_file, 'a') as f:
            f.write(markdown_content)
    ## 工作基础
    markdown_content = """
发言中提及的干部队伍建设的工作基础/条件有：
"""
    with open(output_file, 'a') as f:
        f.write(markdown_content)

    for node in nodes:
        if node_dict[node] == 'C':
            markdown_content = """
- {}
""".format(node)
        else:
            markdown_content = ""
        with open(output_file, 'a') as f:
            f.write(markdown_content)

    for node in nodes:
        if node_dict[node] == 'c':
            markdown_content = """
- {}
""".format(node)
        else:
            markdown_content = ""
        with open(output_file, 'a') as f:
            f.write(markdown_content)

    ## 措施
    markdown_content = """
发言中提及的干部队伍建设的工作措施有：
"""
    with open(output_file, 'a') as f:
        f.write(markdown_content)

    for node in nodes:
        if node_dict[node] == 'D':
            markdown_content = """
- {}
""".format(node)
        else:
            markdown_content = ""
        with open(output_file, 'a') as f:
            f.write(markdown_content)

    for node in nodes:
        if node_dict[node] == 'd':
            markdown_content = """
- {}
""".format(node)
        else:
            markdown_content = ""
        with open(output_file, 'a') as f:
            f.write(markdown_content)

## 工作能力
    markdown_content = """
发言中提及的工作能力有：
"""
    with open(output_file, 'a') as f:
        f.write(markdown_content)

    with open(ability_dir+dir.replace("all_sentence_","").replace(".tsv",".txt"), 'r', encoding='gbk') as f:
        ability = f.read()
        print(ability.split("提到的能力包括："))
        print(len(ability.split("提到的能力包括：")))
        ability = ability.split("提到的能力包括：")[1]
        print(ability)

    with open(output_file, 'a') as f:
        f.write(ability)

    tmp = 0
    for node in nodes:
        if node in node_dict_high.keys():
            tmp += 2
        if node in node_dict_low.keys():
            tmp += 1
    ipt1.append((group, id, tmp / (len(node_dict_high.keys()) * 2 + len(node_dict_low.keys()))))

##################

# 教学+科研+学生思政和活动_Rplot
ipt2 = []
data_dir = r"D:\\教学+科研+学生思政和活动_Rplot\\"

output_root = r"C:\\Users\\丁丁\\Desktop\\report_output\\"
data_dirs = os.listdir(data_dir)

for dir in data_dirs:
    group, id = dir.split('.')[0].split('_')
    output_file = output_root + "{}_{}.md".format(group, id)

    markdown_content = """
## 主题三：教学、科研及学生工作

本部分抽取了个人发言中与教学、科研及学生工作有关的内容。首先，根据全体老师的发言内容，梳理了老师们所提及的教学、科研及学生工作的*工作目标、工作基础/条件、工作措施*；同时，根据与延安精神的相关性、与高质量发展的相关性、老师们提及的频率等，参考因果/依赖关系分析的结果，识别了重要性较高/较低的目标、基础/条件与措施。

<center class="half">
    <img src="教学+科研+学生思政和活动_Rplot/{}_{}.png"/>
</center>
<center style="font-size:12px">图2.1 教学、科研及学生工作的工作目标（蓝色）、工作基础/条件（黄色）与工作措施（红色）（深色-重要性较高；浅色-重要性较低；灰色-未提及）</center>

""".format(group, id, group, id)

    with open(output_file, 'a') as f:
        f.write(markdown_content)

# read node type
node_dict = {}
node_dict_low = {}
node_dict_high = {}
with open(r"C:\\Users\\丁丁\\Desktop\\node_教学+科研+学生思政和活动_1003.csv", 'r', encoding="utf-8") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        node, _1, _2, type, _3 = row
        node_dict[node] = type
        if type in ['u', 'd', 'c']:
            node_dict_low[node] = type
        else:
            node_dict_high[node] = type

node_dir = r"C:\\Users\\丁丁\\Desktop\\教学+科研+学生思政和活动_node_output\\"
node_dirs = os.listdir(node_dir)

for dir in node_dirs:
    print(dir)
    if dir.split('.')[1] != 'tsv':
        continue
    _1, _2, group, id = dir.split('.')[0].split('_')
    output_file = output_root + "{}_{}.md".format(group, id)
    with open(node_dir + dir, 'r', encoding="utf-8") as f:
        nodes = f.read().strip().split('\n')
        print("nodes",nodes)
        if len(nodes) > 1:
            nodes = [node.split('  ')[1] for node in nodes]

        nodes = [node for node in nodes if node != ""]
        nodes = [node for node in nodes if node in node_dict.keys()]
        nodes = list(set(nodes))

    ## 目标
    markdown_content = """
发言中提及的教学、科研及学生工作的工作目标有：
"""
    with open(output_file, 'a') as f:
        f.write(markdown_content)

    for node in nodes:
        if node_dict[node] == 'U':
            markdown_content = """
- {}
""".format(node)
        else:
            markdown_content = ""
        with open(output_file, 'a') as f:
            f.write(markdown_content)

    for node in nodes:
        if node_dict[node] == 'u':
            markdown_content = """
- {}
""".format(node)
        else:
            markdown_content = ""
        with open(output_file, 'a') as f:
            f.write(markdown_content)
    ## 工作基础
    markdown_content = """
发言中提及的教学、科研及学生工作的工作基础/条件有：
"""
    with open(output_file, 'a') as f:
        f.write(markdown_content)

    for node in nodes:
        if node_dict[node] == 'C':
            markdown_content = """
- {}
""".format(node)
        else:
            markdown_content = ""
        with open(output_file, 'a') as f:
            f.write(markdown_content)

    for node in nodes:
        if node_dict[node] == 'c':
            markdown_content = """
- {}
""".format(node)
        else:
            markdown_content = ""
        with open(output_file, 'a') as f:
            f.write(markdown_content)

    ## 措施
    markdown_content = """
发言中提及的教学、科研及学生工作的工作措施有：
"""
    with open(output_file, 'a') as f:
        f.write(markdown_content)

    for node in nodes:
        if node_dict[node] == 'D':
            markdown_content = """
- {}
""".format(node)
        else:
            markdown_content = ""
        with open(output_file, 'a') as f:
            f.write(markdown_content)

    for node in nodes:
        if node_dict[node] == 'd':
            markdown_content = """
- {}
""".format(node)
        else:
            markdown_content = ""
        with open(output_file, 'a') as f:
            f.write(markdown_content)

    tmp = 0
    for node in nodes:
        if node in node_dict_high.keys():
            tmp += 2
        if node in node_dict_low.keys():
            tmp += 1
    ipt2.append((group, id, tmp / (len(node_dict_high.keys()) * 2 + len(node_dict_low.keys()))))


#########################

# 行政办公室、财务、规划、信息技术、法务_Rplot
ipt3 = []
data_dir = r"D:\\行政办公室、财务、规划、信息技术、法务_Rplot\\"

output_root = r"C:\\Users\\丁丁\\Desktop\\report_output\\"
data_dirs = os.listdir(data_dir)

for dir in data_dirs:
    group, id = dir.split('.')[0].split('_')
    output_file = output_root + "{}_{}.md".format(group, id)

    markdown_content = """
## 主题四：行政办公室、财务、规划、信息技术及法务工作

本部分抽取了个人发言中与行政办公室、财务、规划、信息技术及法务工作有关的内容。首先，根据全体老师的发言内容，梳理了老师们所提及的行政办公室、财务、规划、信息技术及法务工作的*工作目标、工作基础/条件、工作措施*；同时，根据与延安精神的相关性、与高质量发展的相关性、老师们提及的频率等，参考因果/依赖关系分析的结果，识别了重要性较高/较低的目标、基础/条件与措施。

<center class="half">
    <img src="行政办公室、财务、规划、信息技术、法务_Rplot/{}_{}.png"/>
</center>
<center style="font-size:12px">图2.1 行政办公室、财务、规划、信息技术及法务工作的工作目标（蓝色）、工作基础/条件（黄色）与工作措施（红色）（深色-重要性较高；浅色-重要性较低；灰色-未提及）</center>

""".format(group, id, group, id)

    with open(output_file, 'a') as f:
        f.write(markdown_content)

# read node type
node_dict = {}
node_dict_low = {}
node_dict_high = {}
with open(r"C:\\Users\\丁丁\\Desktop\\node_行政办公室、财务、规划、信息技术、法务_1002.csv", 'r', encoding="utf-8") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        node, _1, _2, type, _3 = row
        node_dict[node] = type
        if type in ['u', 'd', 'c']:
            node_dict_low[node] = type
        else:
            node_dict_high[node] = type

node_dir = r"C:\\Users\\丁丁\\Desktop\\行政办公室、财务、规划、信息技术、法务_node_output\\"
node_dirs = os.listdir(node_dir)

for dir in node_dirs:
    print(dir)
    if dir.split('.')[1] != 'tsv':
        continue
    _1, _2, group, id = dir.split('.')[0].split('_')
    output_file = output_root + "{}_{}.md".format(group, id)
    with open(node_dir + dir, 'r', encoding="utf-8") as f:
        nodes = f.read().strip().split('\n')
        print("nodes",nodes)
        if len(nodes) > 1:
            nodes = [node.split('  ')[1] for node in nodes]

        nodes = [node for node in nodes if node != ""]
        nodes = [node for node in nodes if node in node_dict.keys()]
        nodes = list(set(nodes))

    ## 目标
    markdown_content = """
发言中提及的行政办公室、财务、规划、信息技术及法务工作的工作目标有：
"""
    with open(output_file, 'a') as f:
        f.write(markdown_content)

    for node in nodes:
        if node_dict[node] == 'U':
            markdown_content = """
- {}
""".format(node)
        else:
            markdown_content = ""
        with open(output_file, 'a') as f:
            f.write(markdown_content)

    for node in nodes:
        if node_dict[node] == 'u':
            markdown_content = """
- {}
""".format(node)
        else:
            markdown_content = ""
        with open(output_file, 'a') as f:
            f.write(markdown_content)
    ## 工作基础
    markdown_content = """
发言中提及的行政办公室、财务、规划、信息技术及法务工作的工作基础/条件有：
"""
    with open(output_file, 'a') as f:
        f.write(markdown_content)

    for node in nodes:
        if node_dict[node] == 'C':
            markdown_content = """
- {}
""".format(node)
        else:
            markdown_content = ""
        with open(output_file, 'a') as f:
            f.write(markdown_content)

    for node in nodes:
        if node_dict[node] == 'c':
            markdown_content = """
- {}
""".format(node)
        else:
            markdown_content = ""
        with open(output_file, 'a') as f:
            f.write(markdown_content)

    ## 措施
    markdown_content = """
发言中提及的行政办公室、财务、规划、信息技术及法务工作的工作措施有：
"""
    with open(output_file, 'a') as f:
        f.write(markdown_content)

    for node in nodes:
        if node_dict[node] == 'D':
            markdown_content = """
- {}
""".format(node)
        else:
            markdown_content = ""
        with open(output_file, 'a') as f:
            f.write(markdown_content)

    for node in nodes:
        if node_dict[node] == 'd':
            markdown_content = """
- {}
""".format(node)
        else:
            markdown_content = ""
        with open(output_file, 'a') as f:
            f.write(markdown_content)

    tmp = 0
    for node in nodes:
        if node in node_dict_high.keys():
            tmp += 2
        if node in node_dict_low.keys():
            tmp += 1
    ipt3.append((group, id, tmp / (len(node_dict_high.keys()) * 2 + len(node_dict_low.keys()))))

###############################

# 医院建设_Rplot
ipt4 = []
data_dir = r"D:\\医院建设_Rplot\\"

output_root = r"C:\\Users\\丁丁\\Desktop\\report_output\\"
data_dirs = os.listdir(data_dir)

for dir in data_dirs:
    group, id = dir.split('.')[0].split('_')
    output_file = output_root + "{}_{}.md".format(group, id)

    markdown_content = """
## 主题五：医院建设

本部分抽取了个人发言中与医院建设有关的内容。首先，根据全体老师的发言内容，梳理了老师们所提及的医院建设的*工作目标、工作基础/条件、工作措施*；同时，根据与延安精神的相关性、与高质量发展的相关性、老师们提及的频率等，参考因果/依赖关系分析的结果，识别了重要性较高/较低的目标、基础/条件与措施。

<center class="half">
    <img src="医院建设_Rplot/{}_{}.png"/>
</center>
<center style="font-size:12px">图2.1 医院建设的工作目标（蓝色）、工作基础/条件（黄色）与工作措施（红色）（深色-重要性较高；浅色-重要性较低；灰色-未提及）</center>

""".format(group, id, group, id)

    with open(output_file, 'a') as f:
        f.write(markdown_content)

# read node type
node_dict = {}
node_dict_low = {}
node_dict_high = {}
with open(r"C:\\Users\\丁丁\\Desktop\\node_医院建设_1002.csv", 'r', encoding="utf-8") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        node, _1, _2, type, _3 = row
        node_dict[node] = type
        if type in ['u', 'd', 'c']:
            node_dict_low[node] = type
        else:
            node_dict_high[node] = type

node_dir = r"C:\\Users\\丁丁\\Desktop\\医院建设_node_output\\"
node_dirs = os.listdir(node_dir)

for dir in node_dirs:
    print(dir)
    if dir.split('.')[1] != 'tsv':
        continue
    _1, _2, group, id = dir.split('.')[0].split('_')
    output_file = output_root + "{}_{}.md".format(group, id)
    with open(node_dir + dir, 'r', encoding="utf-8") as f:
        nodes = f.read().strip().split('\n')
        print("nodes",nodes)
        if len(nodes) > 1:
            nodes = [node.split('  ')[1] for node in nodes]

        nodes = [node for node in nodes if node != ""]
        nodes = [node for node in nodes if node in node_dict.keys()]
        nodes = list(set(nodes))

    ## 目标
    markdown_content = """
发言中提及的医院建设的工作目标有：
"""
    with open(output_file, 'a') as f:
        f.write(markdown_content)

    for node in nodes:
        if node_dict[node] == 'U':
            markdown_content = """
- {}
""".format(node)
        else:
            markdown_content = ""
        with open(output_file, 'a') as f:
            f.write(markdown_content)

    for node in nodes:
        if node_dict[node] == 'u':
            markdown_content = """
- {}
""".format(node)
        else:
            markdown_content = ""
        with open(output_file, 'a') as f:
            f.write(markdown_content)
    ## 工作基础
    markdown_content = """
发言中提及的医院建设的工作基础/条件有：
"""
    with open(output_file, 'a') as f:
        f.write(markdown_content)

    for node in nodes:
        if node_dict[node] == 'C':
            markdown_content = """
- {}
""".format(node)
        else:
            markdown_content = ""
        with open(output_file, 'a') as f:
            f.write(markdown_content)

    for node in nodes:
        if node_dict[node] == 'c':
            markdown_content = """
- {}
""".format(node)
        else:
            markdown_content = ""
        with open(output_file, 'a') as f:
            f.write(markdown_content)

    ## 措施
    markdown_content = """
发言中提及的医院建设的工作措施有：
"""
    with open(output_file, 'a') as f:
        f.write(markdown_content)

    for node in nodes:
        if node_dict[node] == 'D':
            markdown_content = """
- {}
""".format(node)
        else:
            markdown_content = ""
        with open(output_file, 'a') as f:
            f.write(markdown_content)

    for node in nodes:
        if node_dict[node] == 'd':
            markdown_content = """
- {}
""".format(node)
        else:
            markdown_content = ""
        with open(output_file, 'a') as f:
            f.write(markdown_content)

    tmp = 0
    for node in nodes:
        if node in node_dict_high.keys():
            tmp += 2
        if node in node_dict_low.keys():
            tmp += 1
    ipt4.append((group, id, tmp / (len(node_dict_high.keys()) * 2 + len(node_dict_low.keys()))))

#########
output_root = r"C:\\Users\\丁丁\\Desktop\\report_output\\"
data_dirs = os.listdir(output_root)
s1 = []
s2 = []
s3 = []
s4 = []
s5 = []
for i, dir in enumerate(data_dirs):
    if len(dir.split('.')) < 2:
        continue
    if dir.split('.')[1] != 'md':
        continue
    group, id = dir.split('.')[0].split('_')

    flag = 0
    for ipt in ipt0:
        if group == ipt[0] and id == ipt[1]:
            s1.append(ipt[2])
            flag = 1
    if flag == 0:
        s1.append(0)

    flag = 0
    for ipt in ipt1:
        if group == ipt[0] and id == ipt[1]:
            s2.append(ipt[2])
            flag = 1
    if flag == 0:
        s2.append(0)

    flag = 0
    for ipt in ipt2:
        if group == ipt[0] and id == ipt[1]:
            s3.append(ipt[2])
            flag = 1
    if flag == 0:
        s3.append(0)

    flag = 0
    for ipt in ipt3:
        if group == ipt[0] and id == ipt[1]:
            s4.append(ipt[2])
            flag = 1
    if flag == 0:
        s4.append(0)

    flag = 0
    for ipt in ipt4:
        if group == ipt[0] and id == ipt[1]:
            s5.append(ipt[2])
            flag = 1
    if flag == 0:
        s5.append(0)

radar_avg = [
    np.mean(np.array(s1)),
    np.mean(np.array(s2)),
    np.mean(np.array(s3)),
    np.mean(np.array(s4)),
    np.mean(np.array(s5)),
    np.mean(np.array(s1))
]

output_root = r"C:\\Users\\丁丁\\Desktop\\report_output\\"
data_dirs = os.listdir(output_root)
i = -1
for dir in data_dirs:
    if len(dir.split('.')) < 2:
        continue
    if dir.split('.')[1] != 'md':
        continue
    i += 1
    group, id = dir.split('.')[0].split('_')

    radar_axes = ["ax1", "ax2", "ax3", "ax4", "ax5"]
    radar_values = [
        s1[i],
        s2[i],
        s3[i],
        s4[i],
        s5[i],
    ]

    num_axes = len(radar_axes)
    angles = np.linspace(0, 2 * np.pi, num_axes, endpoint=False).tolist()
    angles += angles[:1]  # Repeat the first angle to close the plot
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection': 'polar'})

    radar_values += radar_values[:1]
    ax.fill(angles, radar_values, alpha=0.25)
    ax.plot(angles, radar_values, marker='o')

    ax.fill(angles, radar_avg, alpha=0.25)
    ax.plot(angles, radar_avg, marker='o')

    # ax.plot(angles, radar_max, marker='o')

    ax.set_rmax(1)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(radar_axes)
    ax.yaxis.grid(True)

    plt.savefig(r"C:\\Users\\丁丁\\Desktop\\report_output\\radar\\{}_{}.png".format(group, id))



#####
output_root = r"C:\\Users\\丁丁\\Desktop\\report_output\\"
data_dirs = os.listdir(output_root)
for dir in data_dirs:
    if len(dir.split('.')) < 2:
        continue
    if dir.split('.')[1] != 'md':
        continue
    group, id = dir.split('.')[0].split('_')
    output_file = output_root + "{}_{}.md".format(group, id)

    markdown_content = """
# 总结

本部分以雷达图的形式，可视化地总结了个人发言在延安精神、干部队伍建设、教学、科研及学生工作、行政办公室、财务、规划、信息技术及法务工作、医院建设五个主题的内容覆盖情况；以推理模式图、搜索模式图的形式，可视化地总结了个人发言在后四个主题的推理模式和搜索模式。

在第一个主题(延安精神)下，雷达图展示的是对于延安精神内涵和重要角度的覆盖、运用实例支撑论述、联系工作实际的综合评分。

在后四个主题下，雷达图展示的是对于重要性较高和重要性较低节点的加权覆盖比例(重要性较高与较低节点的权重比为 2:1)。此处为涵盖了各主题的工作目标、工作基础/条件、工作措施的综合评分。


<center class="half">
    <img src="radar/{}_{}.png" />
</center>
<center style="font-size:12px">图6.1 各主题的内容覆盖情况</center>


""".format(group,id)

    with open(output_file, 'a') as f:
        f.write(markdown_content)

#####

for dir in data_dirs:
    if len(dir.split('.')) < 2:
        continue
    if dir.split('.')[1] != 'md':
        continue
    group, id = dir.split('.')[0].split('_')
    output_file = output_root + "{}_{}.md".format(group, id)

    markdown_content = """

推理模式图展示的是在后四个主题的推理模式，即根据四种推理模式（三段论、关系推理、归纳推理、溯因推理）的原理，统计得到的发言内容中各种推理模式的出现次数。推理模式图展示了思考的过程（思维链）。

<center class="half">
    <img src="reasoning_pattern/{}_{}.png" />
</center>
<center style="font-size:12px">图6.2 四种推理模式（三段论、关系推理、归纳推理、溯因推理）在后四个主题（干部队伍建设、教学、科研及学生工作、行政办公室、财务、规划、信息技术及法务工作、医院建设）中的出现频率</center>


    """.format(group, id)

    with open(output_file, 'a') as f:
        f.write(markdown_content)

for dir in data_dirs:
    if len(dir.split('.')) < 2:
        continue
    if dir.split('.')[1] != 'md':
        continue
    group, id = dir.split('.')[0].split('_')
    output_file = output_root + "{}_{}.md".format(group, id)

    markdown_content = """

搜索模式图展示的是在后四个主题的搜索模式，即基于网络搜索的思想，分析得到的发言内容中的重复访问和向内/向外搜索倾向。重复访问倾向控制回到上一个点的概率；向内搜索倾向/广度优先搜索倾向控制访问与当前节点接近的点的概率；向外搜索倾向/深度优先搜索倾向控制访问远离当前节点的点的概率。

<center class="half">
    <img src="search_pattern/{}_{}.png" />
</center>
<center style="font-size:12px">图6.3 三种搜索模式（重复访问、向外搜索、向内搜索）在后四个主题（干部队伍建设、教学、科研及学生工作、行政办公室、财务、规划、信息技术及法务工作、医院建设）中的出现比例</center>


    """.format(group, id)

    with open(output_file, 'a') as f:
        f.write(markdown_content)
