# -*- coding: utf-8 -*-

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import csv

matplotlib.rcParams['font.family'] = 'SimHei'
matplotlib.rcParams['font.sans-serif'] = 'SimHei'

data_dir = r"C:\\Users\\丁丁\\Desktop\\深圳演练\\每个人讲的话\\"
data_dirs = os.listdir(data_dir)
whole_plot_dir=r"C:\\Users\\丁丁\\Desktop\\深圳演练\\plot\\"
chance_plot_dir=r"C:\\Users\\丁丁\\Desktop\\深圳演练\\chance_plot\\"
chance_node_dir=r"C:\\Users\\丁丁\\Desktop\\深圳演练\\chance_node_dropdup\\"
score_1_1_dir=r"C:\\Users\\丁丁\\Desktop\\深圳演练\\1_1_score\\"
uncertainty_node_dir=r"C:\\Users\\丁丁\\Desktop\\深圳演练\\uncertainty_node_dropdup\\"
score_1_2_dir=r"C:\\Users\\丁丁\\Desktop\\深圳演练\\1_2_score\\"
c_c_dir=r"C:\\Users\\丁丁\\Desktop\\深圳演练\\c_c_dropdup\\"
score_1_3_dir=r"C:\\Users\\丁丁\\Desktop\\深圳演练\\1_3_score\\"
reasoning_chain_dir=r"C:\\Users\\丁丁\\Desktop\\深圳演练\\推理链条\\"
score_1_4_dir=r"C:\\Users\\丁丁\\Desktop\\深圳演练\\1_4_score\\"
reasoning_pattern_dir=r"C:\\Users\\丁丁\\Desktop\\深圳演练\\reasoning_图\\"
score_1_5_dir=r"C:\\Users\\丁丁\\Desktop\\深圳演练\\1_5_score\\"
utility_plot_dir=r"C:\\Users\\丁丁\\Desktop\\深圳演练\\utility_plot\\"
utility_node_dir=r"C:\\Users\\丁丁\\Desktop\\深圳演练\\utility_node_dropdup\\"
score_2_1_dir=r"C:\\Users\\丁丁\\Desktop\\深圳演练\\2_1_score\\"
d_others_dir=r"C:\\Users\\丁丁\\Desktop\\深圳演练\\d_others_dropdup\\"
score_2_2_dir=r"C:\\Users\\丁丁\\Desktop\\深圳演练\\2_2_score\\"
c_d_dir=r"C:\\Users\\丁丁\\Desktop\\深圳演练\\c_d_dropdup\\"
score_2_3_dir=r"C:\\Users\\丁丁\\Desktop\\深圳演练\\2_3_score\\"

output_root = r"C:\\Users\\丁丁\\Desktop\\深圳演练\\report_output\\"
ipt0 = []
ipt1 = []
ipt2 = []
ipt3 = []
ipt4 = []
ipt5 = []
ipt6 = []
ipt7=[]
max_ipt0 = 38
max_ipt1 = 10
max_ipt2 = 5
max_ipt3 = 45
max_ipt4 = 11
max_ipt5 = 3
max_ipt6 = 8
max_ipt7 = 7

for dir in data_dirs:
    id = dir.split('.')[0]
    output_file = output_root + "{}.md".format(id)

    markdown_content = """
### 情报分析能力评估报告

#### 导语

> 本报告讨论了参与者在应急演练过程中，在信息考量全面性、风险识别能力、态势研判能力、思考深入程度、推理模式、价值考量全面性、后果研判能力、信息利用能力八个方面的表现。本部分以雷达图的形式，可视化地总结了参与者在八个方面的得分。

<center class="half">
    <img src="radar/{}.png" style="zoom: 100%;" />
</center>
<center style="font-size:12px">雷达图（蓝色为当前参与者的表现，桔色为所有人的平均表现）</center>


> 信息考量全面性：评估参与者获取对决策有帮助的信息的能力。
> 
> 风险识别能力：评估参与者判断信息概率分布或变化范围的能力。
> 
> 态势研判能力：评估参与者对信息间关系的把握能力。
> 
> 思考深入程度：评估参与者的推理链条长度和质量。
> 
> 推理模式：评估参与者使用四种推理方法的频率。
> 
> 价值考量全面性：评估参与者全面考量演练中的重要价值的能力。
> 
> 后果研判能力：评估参与者推断各个决策可能导致的后果的能力。
> 
> 信息利用能力：评估参与者利用信息提升决策的预期效果（并降低决策的不确定程度）的能力。

""".format(id, id)

    with open(output_file, 'a') as f:
        f.write(markdown_content)

    markdown_content = """
参与者本人提及的关键信息、价值和方案分别由语义空间中的黄色、蓝色和粉色表示表示。

<center class="half">
    <img src="plot/{}.png" style="zoom: 100%;" />
</center>
<center style="font-size:12px">信息、方案、价值的覆盖情况</center>

""".format(id, id)

    with open(output_file, 'a') as f:
        f.write(markdown_content)

    markdown_content = """
> 接下来，本报告从风险研判能力、应急处置能力两个方面展开，对八项能力的评估方法分别进行介绍，展示参与者在各项能力上的表现。

#### 1 风险研判能力

> 本环节评估参与者的风险研判能力，风险研判能力涉及两个方面：对当前情况的认识和对未来态势的预测。本环节通过参与者考察的信息数量、信息包含的风险（概率分布或变化范围）评估参与者对当前情况的认识能力；通过参与者对未知信息的判断（对信息间关系的把握）、推理链条的长度和质量、推理模式评估参与者对未来态势的预测能力。

##### 1.1 信息考量全面性

> 参与者在进行应急场景下的情报分析时，首先需要准确且全面地识别该场景下对决策有帮助的信息源，这一环节是后续风险分析和决策支持的基础。本环节统计参与者提及的信息源数量，判断参与者提及的信息源的可获取性和准确性。

<center class="half">
    <img src="utility_plot/{}.png" style="zoom: 100%;" />
</center>
<center style="font-size:12px">图1.1 信息考量全面性</center>

""".format(id, id)

    with open(output_file, 'a') as f:
        f.write(markdown_content)

    markdown_content = """
提到的信息列表包括：
"""
    with open(output_file, 'a') as f:
        f.write(markdown_content)

    ctr=0
    with open(chance_node_dir + dir, 'r', encoding="utf-8") as f:
        nodes = f.read().strip().split('\n')
        # print(nodes)

    for node in nodes:
        if node != "":
            ctr += 1
            markdown_content = """
- {}
""".format(node)
            with open(output_file, 'a') as f:
                f.write(markdown_content)
                # print(markdown_content)

    if ctr == 0:
        markdown_content = """
- 无
"""
        with open(output_file, 'a') as f:
            f.write(markdown_content)
            # print(markdown_content)

    # print("ctr", ctr)

    with open(score_1_1_dir + dir, 'r', encoding='utf-8') as f:
        score_1_1 = f.read().strip()

    ipt0.append((id, float(score_1_1) / max_ipt0))

    markdown_content = """
##### 1.2 风险识别能力

> 在应急场景下，参与者需要重点考察信息包含的风险，即概率分布或可能的取值范围。本环节统计参与者提及的信息源的概率分布或取值范围，判断参与者的风险识别能力。

<center class="half">
    <img src="chance_plot/{}.png" style="zoom: 100%;" />
</center>
<center style="font-size:12px">图1.2 风险识别能力</center>

""".format(id, id)

    with open(output_file, 'a') as f:
        f.write(markdown_content)

    markdown_content = """
提到的包含不确定性的信息包括：
"""
    with open(output_file, 'a') as f:
        f.write(markdown_content)

    with open(uncertainty_node_dir + dir, 'r', encoding="utf-8") as f:
        nodes = f.read().strip().split('\n')
        # print("nodes", nodes)

    ctr = 0
    for node in nodes:
        if node != "":
            ctr += 1
            markdown_content = """
- {}
""".format(node)

            with open(output_file, 'a') as f:
                f.write(markdown_content)

    if ctr == 0:
        markdown_content = """
- 无
"""
        with open(output_file, 'a') as f:
            f.write(markdown_content)

    with open(score_1_2_dir + dir, 'r', encoding='utf-8') as f:
        score_1_2 = f.read().strip()

    ipt1.append((id, float(score_1_2) / max_ipt1))


    markdown_content = """
##### 1.3 态势研判能力

> 参与者基于对信息间关系的考察，通过已知信息推断（未来的）未知信息（可能的取值或概率分布），体现对态势的研判能力。本环节统计参与者提及的信息间定性和定量关系的数量和准确性，考察上述关系对参与者推断（未来的）未知信息的支持作用。

""".format(id, id)

    with open(output_file, 'a') as f:
        f.write(markdown_content)

    markdown_content = """
提到的未知信息的支持关系包括：
"""
    with open(output_file, 'a') as f:
        f.write(markdown_content)

    with open(c_c_dir + dir, 'r', encoding="utf-8") as f:
        arcs = f.read().strip().split('\n')
        print("arcs", arcs)

    ctr = 0
    for arc in arcs:
        if arc != "":
            ctr += 1
            markdown_content = """
- {}
""".format(arc)

            with open(output_file, 'a') as f:
                f.write(markdown_content)

    if ctr == 0:
        markdown_content = """
- 无
"""
        with open(output_file, 'a') as f:
            f.write(markdown_content)

    with open(score_1_3_dir + dir, 'r', encoding='utf-8') as f:
        score_1_3 = f.read().strip()

    ipt2.append((id, float(score_1_3) / max_ipt2))


    markdown_content = """
##### 1.4 思考深入程度

> 参与者通过上述关系判断推断未知信息（未来态势），在此过程中形成推理链条。推理链条的长度和链条中的累计信息量反应参与者的思考深入程度。本环节考察参与者推理链条的长度和累计信息量。

""".format(id, id)

    with open(output_file, 'a') as f:
        f.write(markdown_content)

    markdown_content = """
推理链条列表：
"""
    with open(output_file, 'a') as f:
        f.write(markdown_content)

    with open(reasoning_chain_dir + dir, 'r', encoding="utf-8") as f:
        arcs = f.read().strip().split('\n')
        # print("nodes", nodes)

    ctr = 0
    for arc in arcs:
        if arc != "":
            ctr += 1
            markdown_content = """
- {}
""".format(arc)

            with open(output_file, 'a') as f:
                f.write(markdown_content)

    if ctr == 0:
        markdown_content = """
- 无
"""
        with open(output_file, 'a') as f:
            f.write(markdown_content)

    with open(score_1_4_dir + dir, 'r', encoding='utf-8') as f:
        score_1_4 = f.read().strip()

    ipt3.append((id, float(score_1_4) / max_ipt3))

    markdown_content = """
##### 1.5 推理模式

> 根据四种推理模式（三段论、关系推理、归纳推理、溯因推理）的原理，统计参与者的发言内容中各种推理模式的出现次数。推理模式图展示了思考的过程（思维链）。

<center class="half">
    <img src="reasoning_图/{}.png" style="zoom: 100%;" />
</center>
<center style="font-size:12px">图1.5 推理模式</center>

""".format(id, id)

    with open(output_file, 'a') as f:
        f.write(markdown_content)

    with open(score_1_5_dir + dir, 'r', encoding='utf-8') as f:
        score_1_5 = f.read().strip()

    ipt4.append((id, float(score_1_5) / max_ipt4))

    markdown_content = """
#### 2 应急处置能力

> 本环节评估参与者的应急处置能力，应急处置能力涉及两个方面：对重要价值的判断和对决策方案的考察。本环节通过参与者考察的价值数量评估参与者对重要价值的判断能力；通过参与者提及的信息对决策的支持作用、对决策导致的可能后果的研判评估参与者对方案的考察能力。

##### 2.1 价值考量全面性

> 在应急处置环节，指导现场决策和情报支持的核心是对（决策影响的）重要价值的判断。本环节统计参与者提及的价值数量，判断参与者对应急场景下重要价值的判断能力。

<center class="half">
    <img src="utility_plot/{}.png" style="zoom: 25%;" />
</center>
<center style="font-size:12px">图2.1 价值考量全面性</center>

""".format(id, id)

    with open(output_file, 'a') as f:
        f.write(markdown_content)

    markdown_content = """
提到的价值列表包括：
"""
    with open(output_file, 'a') as f:
        f.write(markdown_content)

    with open(utility_node_dir + dir, 'r', encoding="utf-8") as f:
        nodes = f.read().strip().split('\n')
        # print("nodes", nodes)

    ctr = 0
    for node in nodes:
        if node != "":
            ctr += 1
            markdown_content = """
- {}
""".format(node)

            with open(output_file, 'a') as f:
                f.write(markdown_content)

    if ctr == 0:
        markdown_content = """
- 无
"""
        with open(output_file, 'a') as f:
            f.write(markdown_content)

    with open(score_2_1_dir + dir, 'r', encoding='utf-8') as f:
        score_2_1 = f.read().strip()

    ipt5.append((id, float(score_2_1) / max_ipt5))

    markdown_content = """
##### 2.2 后果研判能力

> 参与者在评估决策方案时，需全面分析其导致的可能后果和包含的风险（后果的不确定性）。对于每个决策方案，参与者需明确其可能影响的信息、价值和其他决策，并考察后果的不确定程度（如最坏可能性）。本环节统计参与者提及的决策对其他因素的影响的表述。

""".format(id, id)

    with open(output_file, 'a') as f:
        f.write(markdown_content)

    markdown_content = """
提到的各决策的可能后果包括：
"""
    with open(output_file, 'a') as f:
        f.write(markdown_content)

    with open(d_others_dir + dir, 'r', encoding="utf-8") as f:
        arcs = f.read().strip().split('\n')
        # print("nodes", nodes)

    ctr = 0
    for arc in arcs:
        if arc != "":
            ctr += 1
            markdown_content = """
- {}
""".format(arc)

            with open(output_file, 'a') as f:
                f.write(markdown_content)

    if ctr == 0:
        markdown_content = """
- 无
"""
        with open(output_file, 'a') as f:
            f.write(markdown_content)

    with open(score_2_2_dir + dir, 'r', encoding='utf-8') as f:
        score_2_2 = f.read().strip()

    ipt6.append((id, float(score_2_2) / max_ipt6))

    markdown_content = """
##### 2.3 信息利用能力

> 参与者基于已知或未知（需推断）信息进行决策，信息提升决策的预期效果，并降低决策的不确定性程度。本环节统计参与者提及的信息对决策的支持作用。

""".format(id, id)

    with open(output_file, 'a') as f:
        f.write(markdown_content)

    markdown_content = """
提到的信息对决策的支持作用包括： 
"""
    with open(output_file, 'a') as f:
        f.write(markdown_content)

    with open(c_d_dir + dir, 'r', encoding="utf-8") as f:
        arcs = f.read().strip().split('\n')
        # print("nodes", nodes)

    ctr = 0
    for arc in arcs:
        if arc!="":
            ctr += 1
            markdown_content = """
- {}
""".format(arc)

            with open(output_file, 'a') as f:
                f.write(markdown_content)

    if ctr == 0:
        markdown_content = """
- 无
"""
        with open(output_file, 'a') as f:
            f.write(markdown_content)

    with open(score_2_3_dir + dir, 'r', encoding='utf-8') as f:
        score_2_3 = f.read().strip()

    ipt7.append((id, float(score_2_3) / max_ipt7))


output_root = r"C:\\Users\\丁丁\\Desktop\\深圳演练\\report_output\\"
data_dirs = os.listdir(output_root)
s1 = []
s2 = []
s3 = []
s4 = []
s5 = []
s6 = []
s7 = []
s8 = []

for i, dir in enumerate(data_dirs):
    if len(dir.split('.')) < 1:
        continue
    id = dir.split('.')[0]

    flag = 0
    for ipt in ipt0:
        if id == ipt[0]:
            s1.append(ipt[1])
            flag = 1
    if flag == 0:
        s1.append(0)

    flag = 0
    for ipt in ipt1:
        if id == ipt[0]:
            s2.append(ipt[1])
            flag = 1
    if flag == 0:
        s2.append(0)

    flag = 0
    for ipt in ipt2:
        if id == ipt[0]:
            s3.append(ipt[1])
            flag = 1
    if flag == 0:
        s3.append(0)

    flag = 0
    for ipt in ipt3:
        if id == ipt[0]:
            s4.append(ipt[1])
            flag = 1
    if flag == 0:
        s4.append(0)

    flag = 0
    for ipt in ipt4:
        if id == ipt[0]:
            s5.append(ipt[1])
            flag = 1
    if flag == 0:
        s5.append(0)

    flag = 0
    for ipt in ipt5:
        if id == ipt[0]:
            s6.append(ipt[1])
            flag = 1
    if flag == 0:
        s6.append(0)

    flag = 0
    for ipt in ipt6:
        if id == ipt[0]:
            s7.append(ipt[1])
            flag = 1
    if flag == 0:
        s7.append(0)

    flag = 0
    for ipt in ipt7:
        if id == ipt[0]:
            s8.append(ipt[1])
            flag = 1
    if flag == 0:
        s8.append(0)

radar_avg = [
    np.mean(np.array(s1)),
    np.mean(np.array(s2)),
    np.mean(np.array(s3)),
    np.mean(np.array(s4)),
    np.mean(np.array(s5)),
    np.mean(np.array(s6)),
    np.mean(np.array(s7)),
    np.mean(np.array(s8)),
    np.mean(np.array(s1))
]
print(radar_avg)

output_root = r"C:\\Users\\丁丁\\Desktop\\深圳演练\\report_output\\"
data_dirs = os.listdir(output_root)
i = -1
for dir in data_dirs:
    if len(dir.split('.')) < 1:
        continue

    i += 1
    id = dir.split('.')[0]
    if len(id)>2:
        continue

    radar_axes = ["信息考量全面性","风险识别能力","态势研判能力","思考深入程度","推理模式","价值考量全面性","后果研判能力","信息利用能力"]
    radar_values = [
        s1[i],
        s2[i],
        s3[i],
        s4[i],
        s5[i],
        s6[i],
        s7[i],
        s8[i],
    ]
    print(radar_values)

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

    plt.savefig(r"C:\\Users\\丁丁\\Desktop\\深圳演练\\report_output\\radar\\{}.png".format(id))


with open(r"C:\\Users\\丁丁\\Desktop\\output.csv", 'a', newline='', encoding='utf-8-sig') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', "信息考量全面性","风险识别能力","态势研判能力","思考深入程度","推理模式","价值考量全面性","后果研判能力","信息利用能力"])
    for dir in data_dirs:
        id = dir.split('.')[0]
        ability_1 = []
        ability_2 = []
        ability_3 = []
        ability_4 = []
        ability_5 = []
        ability_6 = []
        ability_7 = []
        ability_8 = []
        for ipt in ipt0:
            if id == ipt[0]:
                ability_1.append(ipt[1])
        for ipt in ipt1:
            if id == ipt[0]:
                ability_2.append(ipt[1])
        for ipt in ipt2:
            if id == ipt[0]:
                ability_3.append(ipt[1])
        for ipt in ipt3:
            if id == ipt[0]:
                ability_4.append(ipt[1])
        for ipt in ipt4:
            if id == ipt[0]:
                ability_5.append(ipt[1])
        for ipt in ipt5:
            if id == ipt[0]:
                ability_6.append(ipt[1])
        for ipt in ipt6:
            if id == ipt[0]:
                ability_7.append(ipt[1])
        for ipt in ipt7:
            if id == ipt[0]:
                ability_8.append(ipt[1])

        writer.writerow([id, ability_1,ability_2,ability_3,ability_4,ability_5,ability_6,ability_7,ability_8])


