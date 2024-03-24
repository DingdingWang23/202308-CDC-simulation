# -*- coding: utf-8 -*-

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import csv

matplotlib.rcParams['font.family'] = 'SimHei'
matplotlib.rcParams['font.sans-serif'] = 'SimHei'

data_dir = r"C:\\Users\\丁丁\\Desktop\\物资集团测评\\1130\\group 5\\group_id_node_output_dropdup\\"
data_dirs = os.listdir(data_dir)
node_dir = r"C:\\Users\\丁丁\\Desktop\\物资集团测评\\1130\\group 5\\group_id_node_output_dropdup\\"
arc_2_1_1_dir = r"C:\\Users\\丁丁\\Desktop\\物资集团测评\\1130\\group 5\\2_1_1_arc\\"
pair_2_1_2_dir = r"C:\\Users\\丁丁\\Desktop\\物资集团测评\\1130\\group 5\\2_1_2_pair\\"
dist_dir = r"C:\\Users\\丁丁\\Desktop\\物资集团测评\\1130\\group 5\\2_2_score\\"
unique_dir = r"C:\\Users\\丁丁\\Desktop\\物资集团测评\\1130\\group 5\\2_3_list\\"
score_1_3_dir = r"C:\\Users\\丁丁\\Desktop\\物资集团测评\\1130\\group 5\\1_3_score\\"
score_2_1_1_dir = r"C:\\Users\\丁丁\\Desktop\\物资集团测评\\1130\\group 5\\2_1_1_score\\"
score_2_1_2_dir = r"C:\\Users\\丁丁\\Desktop\\物资集团测评\\1130\\group 5\\2_1_2_score\\"
score_2_2_dir = r"C:\\Users\\丁丁\\Desktop\\物资集团测评\\1130\\group 5\\2_2_score\\"
score_2_3_dir = r"C:\\Users\\丁丁\\Desktop\\物资集团测评\\1130\\group 5\\2_3_score\\"

output_root = r"D:\\group 5\\report_output\\"
ipt0 = []
ipt1=[]
ipt2=[]
ipt3=[]
ipt4=[]
ipt5=[]
ipt6=[]
max_ipt0 = 0
max_ipt1 = 0
max_ipt2 = 0
max_ipt3 = 0
max_ipt4 = 0
max_ipt5 = 0
max_ipt6 = 0


with open(r"C:\\Users\\丁丁\\Desktop\\物资集团测评\\1130\\group 5\\chance_node.txt", 'r', encoding='UTF-8') as file:
    lines = file.readlines()
    chance_node = []
    for item in lines:
        line = item.strip()
        chance_node.append(line)

with open(r"C:\\Users\\丁丁\\Desktop\\物资集团测评\\1130\\group 5\\utility_node.txt", 'r', encoding='UTF-8') as file:
    lines = file.readlines()
    utility_node = []
    for item in lines:
        line = item.strip()
        utility_node.append(line)

with open(r"C:\\Users\\丁丁\\Desktop\\物资集团测评\\1130\\group 5\\decision_node.txt", 'r', encoding='UTF-8') as file:
    lines = file.readlines()
    decision_node = []
    for item in lines:
        line = item.strip()
        decision_node.append(line)

max_dist=0
for dir in data_dirs:
    group, id = dir.split('.')[0].split('_')
    with open(dist_dir + dir, 'r', encoding='utf-8') as f:
        score_2_2 = f.read().strip()
        if float(score_2_2)>max_dist:
            max_dist=float(score_2_2)

for dir in data_dirs:
    group, id = dir.split('.')[0].split('_')
    output_file = output_root + "{}_{}.md".format(group, id)

    markdown_content = """
## 创新启发能力评估报告

### 导语

> 本报告概括了参与者所在小组的讨论内容，展示了参与者本人的表现总览，并进行了参与者表现的详细分析。通过对参与者在小组讨论中表现的综合分析，能够对其在价值考量全面性、信息考量全面性、推理方法、方案的创新性、基于价值的决策、方案间的联想、想象力七个方面的能力进行评估。以下的雷达图展示了参与者七项能力的整体情况，以及与全体参与者均值的比较。

<center class="half">
    <img src="radar/{}_{}.png" style="zoom: 100%;" />
</center>
<center style="font-size:12px">雷达图（蓝色为当前参与者的表现，桔色为所有人的平均表现）</center>

""".format(group, id, group, id)

    with open(output_file, 'a') as f:
        f.write(markdown_content)

    markdown_content = """

### 参与者所在小组的讨论内容


### 参与者本人的表现总览

> 参与者所在小组讨论的内容构成了下图所示的语义空间。参与者本人提及的关键信息、价值和方案分别由橙色、蓝色和红色表示。图中的连线表示参与者在讨论中的联想。

<center class="half">
    <img src="plot_2_result/{}_{}.png" style="zoom: 100%;" />
</center>
<center style="font-size:12px">信息、方案、价值的覆盖情况</center>

""".format(group, id, group, id)

    with open(output_file, 'a') as f:
        f.write(markdown_content)

    markdown_content = """
### 参与者表现的详细分析

> 接下来，本报告从问题解决能力、创造性思维两个方面展开，对七项能力的评估方法分别进行介绍，展示参与者在各项能力上的表现。

#### 1 问题解决能力

> 本环节评估参与者的问题解决能力，问题解决能力涉及三个方面：对问题域（problem space）的观察、理解和推理。

> 报告将通过参与者认识到的信息量和共情到的价值/痛点评估参与者对问题域的观察、理解能力；通过参与者在讨论过程中展示出的推理方式刻画参与者对问题域的推理能力。

##### 1.1 价值考量全面性

> 当参与者面对需要创新思维的问题时，他们首先需要准确且全面地理解问题所涉及的核心价值和关键痛点。在讨论过程中，参与者可能会提到多个不同的价值，即与问题相关的关键点和概念。这些价值的数量反映出参与者对问题中的价值和痛点理解的深度和广度。本环节通过评估参与者在讨论中提到的价值数量，衡量参与者对问题的全面认识程度。

<center class="half">
    <img src="utility_plot/{}_{}.png" style="zoom: 100%;" />
</center>
<center style="font-size:12px">图1.1 价值考量全面性</center>

""".format(group, id, group, id)

    with open(output_file, 'a') as f:
        f.write(markdown_content)

    markdown_content = """
如图所示，参与者提及的价值包括：
"""
    with open(output_file, 'a') as f:
        f.write(markdown_content)

    with open(node_dir + dir, 'r', encoding="utf-8") as f:
        nodes = f.read().strip().split('\n')
        # print("nodes", nodes)

    ctr = 0
    for node in nodes:
        if node in utility_node:
            ctr+=1
            markdown_content = """
- {}
""".format(node)
        else:
            markdown_content = ""
        with open(output_file, 'a') as f:
            f.write(markdown_content)
    if ctr ==0:
        markdown_content = """
- 无
"""
        with open(output_file, 'a') as f:
            f.write(markdown_content)

    print("ctr",ctr)
    ipt0.append((group, id, ctr / len(utility_node)))
    if float(ctr / len(utility_node))> max_ipt0:
        max_ipt0=float(ctr / len(utility_node))

    markdown_content = """
##### 1.2 信息考量全面性

> 在解决需要创新思维的问题时，参与者需要理解问题中的信息，并在问题域内进行有效思考、构建解决方案。讨论中提及的信息个数，即关键信息点或潜在解决方案的个数，能反映出参与者对问题信息的理解程度和全面性。本环节计算讨论中提到的信息个数，以评估参与者对问题的全面理解。

<center class="half">
    <img src="chance_plot/{}_{}.png" style="zoom: 100%;" />
</center>
<center style="font-size:12px">图1.2 信息考量全面性</center>

""".format(group, id, group, id)

    with open(output_file, 'a') as f:
        f.write(markdown_content)

    markdown_content = """
参与者提及的信息包括：
"""
    with open(output_file, 'a') as f:
        f.write(markdown_content)

    with open(node_dir + dir, 'r', encoding="utf-8") as f:
        nodes = f.read().strip().split('\n')
        # print("nodes", nodes)

    ctr =0
    for node in nodes:
        if node in chance_node:
            ctr+=1
            markdown_content = """
- {}
""".format(node)
        else:
            markdown_content = ""
        with open(output_file, 'a') as f:
            f.write(markdown_content)

    if ctr ==0:
        markdown_content = """
- 无
"""
        with open(output_file, 'a') as f:
            f.write(markdown_content)

    ipt1.append((group, id, ctr / len(chance_node)))
    if float(ctr / len(chance_node))> max_ipt1:
        max_ipt1=float(ctr / len(chance_node))
    print(len(chance_node))
    print(len(decision_node))
    print(len(utility_node))

    markdown_content = """
##### 1.3 推理方法

> 在解决问题的过程中，参与者通常运用四种主要推理模式：三段论、关系推理、归纳推理和溯因推理。这些推理模式帮助参与者深入分析和探索问题领域。为评估参与者的思维过程，本环节在参与者的讨论中跟踪并统计这四种推理模式各自出现的次数，以理解不同的逻辑思考方式连接不同的想法从而形成的完整思维链。此思维链，即推理模式图，展示思考问题的整个过程。

<center class="half">
    <img src="reasoning/{}_{}.png" style="zoom: 25%;" />
</center>
<center style="font-size:12px">图1.3 推理方法</center>

""".format(group, id, group, id)

    with open(output_file, 'a') as f:
        f.write(markdown_content)

    with open(score_1_3_dir + dir, 'r', encoding='utf-8') as f:
        score_1_3 = f.read().strip()

    ipt2.append((group, id, float(score_1_3)))
    if float(score_1_3)> max_ipt2:
        max_ipt2=float(score_1_3)

    markdown_content = """
#### 2 创造性思维

> 本环节评估参与者的创造性思维。创造性思维包括从问题域（problem space）到解决域（solution space）的启发和迁移、创新性方案生成的过程特点、创新性方案的质量。

##### 2.1 启发和迁移

> 本部分通过分析参与者在讨论中提及信息、价值观念和解决方案的顺序和频率，来评估他们在从问题分析（问题域）到解决方案生成（解决域）的过程中所采用的思维方式。

参与者对三类节点提及的顺序如下：

<center class="half">
    <img src="plot_1_result/{}_{}.png" style="zoom: 25%;" />
</center>
<center style="font-size:12px">图2.1.1 三类节点提及顺序</center>

""".format(group, id, group, id)

    with open(output_file, 'a') as f:
        f.write(markdown_content)

    markdown_content = """
参与者对三类节点提及的比例如下：

<center class="half">
    <img src="1_4_plot/{}_{}.png" style="zoom: 25%;" />
</center>
<center style="font-size:12px">图2.1.2 三类节点提及比例</center>

""".format(group, id, group, id)

    with open(output_file, 'a') as f:
        f.write(markdown_content)

    markdown_content = """
##### 2.2 方案的创新性

> 本部分通过基于计算得出的方案之间的最大语义距离，评估参与者针对需要创新思维的问题所提出的多个解决方案，来衡量方案的创新性。

<center class="half">
    <img src="decision_plot/{}_{}.png" style="zoom: 100%;" />
</center>
<center style="font-size:12px">图2.2 方案的创新性</center>

""".format(group, id, group, id)

    with open(output_file, 'a') as f:
        f.write(markdown_content)

    markdown_content = """
参与者提及的方案包括：
"""
    with open(output_file, 'a') as f:
        f.write(markdown_content)

    with open(node_dir + dir, 'r', encoding="utf-8") as f:
        nodes = f.read().strip().split('\n')
        # print("nodes", nodes)

    ctr = 0
    for node in nodes:
        if node in decision_node:
            ctr += 1
            markdown_content = """
- {}
""".format(node)
        else:
            markdown_content = ""
        with open(output_file, 'a') as f:
            f.write(markdown_content)
    if ctr ==0:
        markdown_content = """
- 无
"""
        with open(output_file, 'a') as f:
            f.write(markdown_content)

    markdown_content = """
参与者的决策节点间最大语义距离为：
""".format(group, id, group, id)

    with open(output_file, 'a') as f:
        f.write(markdown_content)

    with open(dist_dir + dir, 'r', encoding="utf-8") as f:
        dist = f.read()
        dist = round(float(dist)/max_dist*100,1)
        dist= str(dist)+"%"
        print(dist)

    markdown_content = """
- 与最大距离相比占{}
""".format(dist)

    with open(output_file, 'a') as f:
        f.write(markdown_content)

    with open(score_2_2_dir + dir, 'r', encoding='utf-8') as f:
        score_2_2 = f.read().strip()

    ipt3.append((group, id, round(0.5 * float(score_2_2)/max_dist + 0.5 * ctr / len(decision_node), 4)))
    if float(0.5 * float(score_2_2)/max_dist + 0.5 * ctr / len(decision_node))> max_ipt3:
        max_ipt3=float(.5 * float(score_2_2)/max_dist + 0.5 * ctr / len(decision_node))

    markdown_content = """
##### 2.3 创新性方案生成的过程特点

> 参与者在解决创新启发问题时，需要全面细致的提出可能的解决方案，这一过程被称为创新性方案的生成，即创造性地思考如何解决问题。不同参与者在创新性方案生成时会展现出不同的特点和方法，其中两类较为理想的思维模式：基于价值的决策和方案间的联想。

参与者出现基于价值的决策的节点对为：
""".format(group, id, group, id)

    with open(output_file, 'a') as f:
        f.write(markdown_content)

    with open(arc_2_1_1_dir + dir, 'r', encoding="utf-8") as f:
        arcs = f.readlines()

    for arc in arcs:
        markdown_content = """
- {}
""".format(arc)

        with open(output_file, 'a') as f:
            f.write(markdown_content)
    if len(arcs) ==0:
        markdown_content = """
- 无
"""
        with open(output_file, 'a') as f:
            f.write(markdown_content)

    with open(score_2_1_1_dir + dir, 'r', encoding='utf-8') as f:
        score_2_1_1 = f.read().strip()

    ipt4.append((group, id, float(score_2_1_1)))
    if float(score_2_1_1)> max_ipt4:
        max_ipt4=float(score_2_1_1)

    markdown_content = """
参与者出现方案间的联想的节点对为：
""".format(group, id, group, id)

    with open(output_file, 'a') as f:
        f.write(markdown_content)

    with open(pair_2_1_2_dir + dir, 'r', encoding="utf-8") as f:
        pairs = f.readlines()

    for pair in pairs:
        markdown_content = """
- {}
""".format(pair)

        with open(output_file, 'a') as f:
            f.write(markdown_content)
    if len(pairs) ==0:
        markdown_content = """
- 无
"""
        with open(output_file, 'a') as f:
            f.write(markdown_content)

    with open(score_2_1_2_dir + dir, 'r', encoding='utf-8') as f:
        score_2_1_2 = f.read().strip()

    ipt5.append((group, id, float(score_2_1_2)))
    if float(score_2_1_2)> max_ipt5:
        max_ipt5=float(score_2_1_2)

    markdown_content = """
##### 2.4 想象力

> 本部分通过生成独特想法的数量评估参与组合的想象力。参与者在思考问题时，他们会进行信息的收集、价值的分析，以及解决方案的构想和生成，当参与者提出独特且其他参与者未提到的想法时，可认为其展现了一定程度的想象力。评估依据是参与者提出的多少个其他人未曾提出的新颖和创造性的想法数量。

""".format(group, id, group, id)

    with open(output_file, 'a') as f:
        f.write(markdown_content)

    markdown_content = """
参与者的独特想法包括：
""".format(group, id, group, id)

    with open(output_file, 'a') as f:
        f.write(markdown_content)

    with open(unique_dir + dir, 'r', encoding="utf-8") as f:
        uniques = f.readlines()

    for unique in uniques:
        markdown_content = """
- {}
""".format(unique)

        with open(output_file, 'a') as f:
            f.write(markdown_content)

    if len(uniques) == 0:
        markdown_content = """
- 无
"""
        with open(output_file, 'a') as f:
            f.write(markdown_content)

    with open(score_2_3_dir + dir, 'r', encoding='utf-8') as f:
        score_2_3 = f.read().strip()

    ipt6.append((group, id, float(score_2_3)))
    if float(score_2_3)> max_ipt6:
        max_ipt6=float(score_2_3)

'''
s1 = []
s2 = []
s3 = []
s4 = []
s5 = []
s6 = []
s7 = []
ipt0_new=[]
ipt1_new=[]
ipt3_new=[]
ipt4_new=[]
ipt5_new=[]
ipt6_new=[]
ipt2_new=[]

for ipt in ipt0:
    print(max_ipt0)
    if max_ipt0>0:
        ipt_new = (ipt[0], ipt[1], float(ipt[2]) / max_ipt0)
        ipt = ipt_new
        ipt0_new.append(ipt_new)
    # print(ipt)
print(ipt0_new)
for ipt in ipt1:
    print(max_ipt1)
    if max_ipt1>0:
        ipt_new = (ipt[0], ipt[1], float(ipt[2]) / max_ipt1)
        ipt = ipt_new
        ipt1_new.append(ipt_new)
    # print(ipt)
print(ipt1_new)

for ipt in ipt2:
    print(max_ipt2)
    if max_ipt2>0:
        ipt_new = (ipt[0], ipt[1], float(ipt[2]) / max_ipt2)
        ipt = ipt_new
        ipt2_new.append(ipt_new)
    # print(ipt)
print(ipt2_new)
for ipt in ipt3:
    print(max_ipt3)
    if max_ipt3>0:
        ipt_new = (ipt[0], ipt[1], float(ipt[2]) / max_ipt3)
        ipt = ipt_new
        ipt3_new.append(ipt_new)
    # print(ipt)
print(ipt3_new)
for ipt in ipt4:
    print(max_ipt4)
    if max_ipt4>0:
        ipt_new = (ipt[0], ipt[1], float(ipt[2]) / max_ipt4)
        ipt = ipt_new
        ipt4_new.append(ipt_new)
    # print(ipt)
print(ipt4_new)
for ipt in ipt5:
    print(max_ipt5)
    if max_ipt5>0:
        ipt_new = (ipt[0], ipt[1], float(ipt[2]) / max_ipt5)
        ipt = ipt_new
        ipt5_new.append(ipt_new)
    # print(ipt)
print(ipt5_new)
for ipt in ipt6:
    print(max_ipt6)
    if max_ipt6>0:
        ipt_new = (ipt[0], ipt[1], float(ipt[2]) / max_ipt6)
        ipt = ipt_new
        ipt6_new.append(ipt_new)
    #print(ipt)
print(ipt6_new)

for dir in data_dirs:
    group, id = dir.split('.')[0].split('_')

    flag = 0
    for ipt in ipt0_new:
        if group == ipt[0] and id == ipt[1]:
            s1.append(ipt[2])
            flag = 1
    if flag == 0:
        s1.append(0)

    flag = 0
    for ipt in ipt1_new:
        if group == ipt[0] and id == ipt[1]:
            s2.append(ipt[2])
            flag = 1
    if flag == 0:
        s2.append(0)

    flag = 0
    for ipt in ipt2_new:
        if group == ipt[0] and id == ipt[1]:
            s3.append(ipt[2])
            flag = 1
    if flag == 0:
        s3.append(0)

    flag = 0
    for ipt in ipt3_new:
        if group == ipt[0] and id == ipt[1]:
            s4.append(ipt[2])
            flag = 1
    if flag == 0:
        s4.append(0)

    flag = 0
    for ipt in ipt4_new:
        if group == ipt[0] and id == ipt[1]:
            s5.append(ipt[2])
            flag = 1
    if flag == 0:
        s5.append(0)

    flag = 0
    for ipt in ipt5_new:
        if group == ipt[0] and id == ipt[1]:
            s6.append(ipt[2])
            flag = 1
    if flag == 0:
        s6.append(0)

    flag = 0
    for ipt in ipt6_new:
        if group == ipt[0] and id == ipt[1]:
            s7.append(ipt[2])
            flag = 1
    if flag == 0:
        s7.append(0)

radar_avg = [
    np.mean(np.array(s1)),
    np.mean(np.array(s2)),
    np.mean(np.array(s3)),
    np.mean(np.array(s4)),
    np.mean(np.array(s5)),
    np.mean(np.array(s6)),
    np.mean(np.array(s7)),
    np.mean(np.array(s1))
]

# data_dirs = os.listdir(output_root)
i = -1
for dir in data_dirs:
    if len(dir.split('.')) < 2:
        continue
    # if dir.split('.')[1] != 'md':
        # continue
    i += 1
    group, id = dir.split('.')[0].split('_')

    radar_axes = ["价值考量全面性", "信息考量全面性", "推理方法", "方案的创新性", "基于价值的决策", "方案间的联想", "想象力"]
    radar_values = [
        s1[i],
        s2[i],
        s3[i],
        s4[i],
        s5[i],
        s6[i],
        s7[i],
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

    plt.savefig(r"D:\\group 1\\report_output\\radar\\{}_{}.png".format(group, id))

for dir in data_dirs:
    if len(dir.split('.')) < 2:
        continue
    if dir.split('.')[1] != 'md':
        continue
    group, id = dir.split('.')[0].split('_')
    output_file = output_root + "{}_{}.md".format(group, id)

    markdown_content = """
#### 导语

本报告描述了参与者对语义空间的探索，即对信息、方案、价值的覆盖情况。

<center class="half">
    <img src="plot_2_result/{}_{}.png" />
</center>
<center style="font-size:12px">信息、方案、价值的覆盖情况</center>

""".format(group,id)

    # with open(output_file, 'a') as f:
        # f.write(markdown_content)

    markdown_content = """
- 价值考量全面性：评估个人在理解和共情问题中的价值和痛点方面的能力。

- 信息考量全面性：评估个人在认识问题所需的所有相关信息方面的能力。

- 推理方法：评估个人在使用不同的推理方法方面的能力。

- 基于价值的决策：评估个人在使用基于价值的决策方法来解决问题方面的能力。

- 方案间的联想：评估个人在联想和生成相关联的多个解决方案方面的能力。

- 方案的创新性：评估个人在创造新颖解决方案方面的能力。

- 想象力：评估个人在展现创造性思维和想象力方面的能力。

本报告讨论了参与者的发言全过程中，在价值考量全面性、信息考量全面性、推理方法、方案的创新性、基于价值的决策、方案间的联想、想象力七个方面的表现。本部分以雷达图的形式，可视化地总结了个人发言在七个方面的得分。

<center class="half">
    <img src="radar/{}_{}.png" />
</center>
<center style="font-size:12px">雷达图（蓝色为当前参与者的表现，桔色为所有人的平均表现）</center>

""".format(group, id)

    # with open(output_file, 'a') as f:
        # f.write(markdown_content)


with open(r"C:\\Users\\丁丁\\Desktop\\output.csv", 'a', newline='', encoding='utf-8-sig') as csvfile:
    writer = csv.writer(csvfile)
    # writer.writerow(['group', 'id', '价值考量全面性','信息考量全面性','推理方法','方案的创新性','基于价值的决策','方案间的联想','想象力'])
    for dir in data_dirs:
        group, id = dir.split('.')[0].split('_')
        ability_1 = []
        ability_2 = []
        ability_3 = []
        ability_4 = []
        ability_5 = []
        ability_6 = []
        ability_7 = []
        for ipt in ipt0_new:
            if group == ipt[0] and id == ipt[1]:
                ability_1.append(ipt[2])
        for ipt in ipt1_new:
            if group == ipt[0] and id == ipt[1]:
                ability_2.append(ipt[2])
        for ipt in ipt2_new:
            if group == ipt[0] and id == ipt[1]:
                ability_3.append(ipt[2])
        for ipt in ipt3_new:
            if group == ipt[0] and id == ipt[1]:
                ability_4.append(ipt[2])
        for ipt in ipt4_new:
            if group == ipt[0] and id == ipt[1]:
                ability_5.append(ipt[2])
        for ipt in ipt5_new:
            if group == ipt[0] and id == ipt[1]:
                ability_6.append(ipt[2])
        for ipt in ipt6_new:
            if group == ipt[0] and id == ipt[1]:
                ability_7.append(ipt[2])
                
        # writer.writerow([group, id, ability_1,ability_2,ability_3,ability_4,ability_5,ability_6,ability_7])
'''


