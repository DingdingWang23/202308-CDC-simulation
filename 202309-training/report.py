import os
import re
import zhipuai
import random


# zhipuai.api_key = "2853e15e35c0be35f3435ec9b0127d08.RKdVy3NNCRzIIVo9"

'''
data_dir = r"C:\\Users\\丁丁\\Desktop\\每个人讲的话_掐头去尾版\\"
data_dirs = os.listdir(data_dir)

output_dir = r'C:\\Users\\丁丁\\Desktop\\合并表格\\'
output_dirs = os.listdir(output_dir)

table_1_dir = r'C:\\Users\\丁丁\\Desktop\\table_1\\'
table_1_dirs = os.listdir(table_1_dir)
table_2_dir = r'C:\\Users\\丁丁\\Desktop\\table_2\\'

fenduan_dir = r"C:\\Users\\丁丁\\Desktop\\每个人讲的话_掐头去尾分段版\\"
fenduan_dirs = os.listdir(fenduan_dir)

fenduan_output_dir = r'C:\\Users\\丁丁\\Desktop\\分段结果\\'
fenduan_output_dirs = os.listdir(fenduan_output_dir)

zhenghe_dir = r'C:\\Users\\丁丁\\Desktop\\整合\\'
'''
'''
def analysis_1(input):

    keyword_list = []
    patterns_1 = [r"服务人民",r"为人民服务"]
    patterns_2 = [r"解放思想", r"实事求是"]
    patterns_3 = [r"自力更生", r"艰苦奋斗"]

    for pattern in patterns_1:
        if re.search(pattern, input):
            keyword_list.append("为人民服务")
    for pattern in patterns_2:
        if re.search(pattern, input):
            keyword_list.append("实事求是")
    for pattern in patterns_3:
        if re.search(pattern, input):
            keyword_list.append("自力更生艰苦奋斗")

    output = "；".join(keyword_list)
    if output == "":
        output = "无"

    return output
'''
'''
def output(content, group, id, output_dir = r'C:\\Users\\丁丁\\Desktop\\分段结果\\'):
    file = output_dir + str(group)+"_"+str(id)+".txt"
    with open(file, 'a') as f:
        f.write(content)
        f.write("\n")
'''
'''
def scan(output_file,text="",unique_id=""):
    prompt = [
        {"role": "user",
         "content": "你将看到一段文本，请基于连贯性进行文本分割，逐段输出原文。文本：---"},
    ]
    prompt_add_text = prompt
    prompt_add_text[0]["content"] = prompt_add_text[0]["content"] + text

    response = zhipuai.model_api.sse_invoke(
        model="chatglm_pro",
        prompt=prompt_add_text,
        top_p=0.7,
        temperature=0.1,
        incremental=False,
        request_id=unique_id
    )

    for event in response.events():
        if event.event == "add":

            pass
        elif event.event == "error" or event.event == "interrupted":
            with open(output_file, 'a') as f:
                f.write(event.data)
                f.write("\n")
            print(event.data)
        elif event.event == "finish":
            print(event.data)
            with open(output_file, 'a') as f:
                f.write(event.data)
                f.write("\n")
        else:
            print(event.data)
            with open(output_file, 'a') as f:
                f.write(event.data)
                f.write("\n")
'''
'''
def perspective_classification(
        text="",
        group=0,
        id=0,
        unique_id=""
):
    prompt = [
        {"role": "user",
         "content": "你将看到一段文本，请根据原文内容，从“干部作风”、“道路自信”、“组织纪律”、“创新”、“民主集中制”、“政治站位”、“团队建设”、“调研和征求意见”、“联系群众”、“理想信念”、“学习的重要性”、“基层工作的重要性”这些主题中选择一个与文本最接近的主题，并给接近程度打分。文本：---"},
    ]
    prompt_add_text = prompt
    prompt_add_text[0]["content"] = prompt_add_text[0]["content"] + text

    response = zhipuai.model_api.sse_invoke(
        model="chatglm_pro",
        prompt=prompt_add_text,
        top_p=0.7,
        temperature=0.1,
        incremental=False,
        request_id=unique_id
    )

    # print response data
    # output_dir = r'C:\\Users\\丁丁\\Desktop\\著作\\'
    output = ""
    for event in response.events():
        if event.event == "add":
            # print(event.data)
            pass
        elif event.event == "error" or event.event == "interrupted":
            print(event.data)
            output = event.data
            # output(event.data, group=group, id=id, output_dir=output_dir)
        elif event.event == "finish":
            print(event.data)
            output = event.data
            # output(event.data, group=group, id=id, output_dir=output_dir)
            # print(event.meta)
        else:
            print(event.data)
            output = event.data
            # output(event.data, group=group, id=id, output_dir=output_dir)
    return output
'''
'''
def ability_classification(
        text="",
        group=0,
        id=0,
        unique_id=""
):
    prompt = [
        {"role": "user",
         "content": "你将看到一段文本，请根据原文内容，从“政治能力”、“调查研究能力”、“科学决策能力”、“改革攻坚能力”、“应急处突能力”、“群众工作能力”、“抓落实能力”这些主题中选择一个与文本最接近的主题，并给接近程度打分。文本：---"},
    ]
    prompt_add_text = prompt
    prompt_add_text[0]["content"] = prompt_add_text[0]["content"] + text

    response = zhipuai.model_api.sse_invoke(
        model="chatglm_pro",
        prompt=prompt_add_text,
        top_p=0.7,
        temperature=0.1,
        incremental=False,
        request_id=unique_id
    )

    # print response data
    # output_dir = r'C:\\Users\\丁丁\\Desktop\\著作\\'
    output = ""
    for event in response.events():
        if event.event == "add":
            # print(event.data)
            pass
        elif event.event == "error" or event.event == "interrupted":
            print(event.data)
            output = event.data
            # output(event.data, group=group, id=id, output_dir=output_dir)
        elif event.event == "finish":
            print(event.data)
            output = event.data
            # output(event.data, group=group, id=id, output_dir=output_dir)
            # print(event.meta)
        else:
            print(event.data)
            output = event.data
            # output(event.data, group=group, id=id, output_dir=output_dir)
    return output
'''
'''
for dir in data_dirs:
    print(dir)
    group, id = dir.split('.')[0].split('_')
    data_file = data_dir + dir
    with open(data_file, 'r', encoding='gbk') as f:
        text = f.read()
    print(text)

    output = analysis_1(text)

    output_file = output_dir + str(group) + "_" + str(id) + ".txt"
    with open(output_file, 'a') as f:
        f.write("提到的延安精神包括：")
        f.write(output)
        f.write("\n")
'''
'''
for dir in data_dirs:
    print(dir)
    group, id = dir.split('.')[0].split('_')
    data_file = data_dir + dir
    with open(data_file, 'r', encoding='gbk') as f:
        text = f.read()
    print(text)
    paragraphs = text.split("\n")
    num_paragraph = len(paragraphs)
    outputs = []
    word_count = 0
    current_paragraph = ""
    for paragraph in paragraphs:
        current_paragraph += paragraph
        word_count = len(current_paragraph)
        if word_count > 1000:
            outputs.append(current_paragraph)
            current_paragraph = ""
            word_count = 0
    outputs.append(current_paragraph)
    new_num_paragraph = len(outputs)

    for i in range(new_num_paragraph):
        output_file = fenduan_dir + str(group) + "_" + str(id) + "_" + str(i+1) + ".txt"

        with open(output_file, 'a') as f:
            f.write(outputs[i])
            f.write("\n")
'''
'''
for dir in table_1_dirs:
    data_file = data_dir + dir
    output_file = output_dir + dir
    table_1_file = table_1_dir + dir
    table_2_file = table_2_dir + dir
    output_1 = []
    output_2 = []
    # print(dir)

    with open(table_1_file, 'r', encoding='gbk') as f:
        list = f.readlines()

        lines = list[2:]
        for line in lines:
            line = line.rstrip()
        # print(lines)
        for line in lines:
            # print("line",line)
            title = line.split("|")[1]
            point = line.split("|")[2]
            my_str = "|"+title+"|"+point+"|"
            # print("title",title)
            # print("point",point)
            output_1.append(my_str)


    with open(table_2_file, 'r', encoding='gbk') as f:
        list = f.readlines()

        lines = list[2:]
        for line in lines:
            line = line.rstrip()
        # print(lines)
        for line in lines:
            # print("line",line)
            title = line.split("|")[1]
            detail = line.split("|")[3]
            my_str = "|"+title+"|"+detail+"|"
            # print("title",title)
            # print("detail",detail)
            output_2.append(my_str)

    output_file = output_dir + dir
    with open(output_file, 'a') as f:
        f.write("对延安精神的理解：")
        f.write("\n")
        f.write("\n".join(output_1))
        f.write("\n")
        f.write("联系实际的内容：")
        f.write("\n")
        f.write("\n".join(output_2))
        f.write("\n")
'''
'''
for dir in fenduan_output_dirs:
    print(dir)

    group, id, num = dir.split('.')[0].split('_')

    input_file = fenduan_output_dir + dir
    with open(input_file, 'r', encoding='gbk') as f:
        text = f.read()

    data_file = zhenghe_dir + str(group) + "_" + str(id) + ".txt"

    with open(data_file, 'a') as f:
        f.write(text)
        f.write("\n")

'''
'''
data_dir = r"C:\\Users\\丁丁\\Desktop\\干部队伍建设\\"
data_dirs = os.listdir(data_dir)

output_dir = r'C:\\Users\\丁丁\\Desktop\\七项能力\\'
output_dirs = os.listdir(output_dir)
'''


'''
dir_topic_1 = r"C:\\Users\\丁丁\\Desktop\\干部作风\\"
dir_topic_1_dirs = os.listdir(dir_topic_1)
dir_topic_2 = r"C:\\Users\\丁丁\\Desktop\\道路自信\\"
dir_topic_2_dirs = os.listdir(dir_topic_2)
dir_topic_3 = r"C:\\Users\\丁丁\\Desktop\\组织纪律\\"
dir_topic_3_dirs = os.listdir(dir_topic_3)
dir_topic_4 = r"C:\\Users\\丁丁\\Desktop\\创新\\"
dir_topic_4_dirs = os.listdir(dir_topic_4)
dir_topic_5 = r"C:\\Users\\丁丁\\Desktop\\民主集中制\\"
dir_topic_5_dirs = os.listdir(dir_topic_5)
dir_topic_6 = r"C:\\Users\\丁丁\\Desktop\\政治站位\\"
dir_topic_6_dirs = os.listdir(dir_topic_6)
dir_topic_7 = r"C:\\Users\\丁丁\\Desktop\\团队建设\\"
dir_topic_7_dirs = os.listdir(dir_topic_7)
dir_topic_8 = r"C:\\Users\\丁丁\\Desktop\\调研和征求意见\\"
dir_topic_8_dirs = os.listdir(dir_topic_8)
dir_topic_9 = r"C:\\Users\\丁丁\\Desktop\\联系群众\\"
dir_topic_9_dirs = os.listdir(dir_topic_9)
dir_topic_10 = r"C:\\Users\\丁丁\\Desktop\\理想信念\\"
dir_topic_10_dirs = os.listdir(dir_topic_10)
dir_topic_11 = r"C:\\Users\\丁丁\\Desktop\\学习的重要性\\"
dir_topic_11_dirs = os.listdir(dir_topic_11)
dir_topic_12 = r"C:\\Users\\丁丁\\Desktop\\基层工作的重要性\\"
dir_topic_12_dirs = os.listdir(dir_topic_12)
print(dir_topic_12_dirs)
'''
'''
dir_topic_1 = r"C:\\Users\\丁丁\\Desktop\\政治能力\\"
dir_topic_1_dirs = os.listdir(dir_topic_1)
dir_topic_2 = r"C:\\Users\\丁丁\\Desktop\\调查研究能力\\"
dir_topic_2_dirs = os.listdir(dir_topic_2)
dir_topic_3 = r"C:\\Users\\丁丁\\Desktop\\科学决策能力\\"
dir_topic_3_dirs = os.listdir(dir_topic_3)
dir_topic_4 = r"C:\\Users\\丁丁\\Desktop\\改革攻坚能力\\"
dir_topic_4_dirs = os.listdir(dir_topic_4)
dir_topic_5 = r"C:\\Users\\丁丁\\Desktop\\应急处突能力\\"
dir_topic_5_dirs = os.listdir(dir_topic_5)
dir_topic_6 = r"C:\\Users\\丁丁\\Desktop\\群众工作能力\\"
dir_topic_6_dirs = os.listdir(dir_topic_6)
dir_topic_7 = r"C:\\Users\\丁丁\\Desktop\\抓落实能力\\"
dir_topic_7_dirs = os.listdir(dir_topic_7)
'''
'''
for dir in data_dirs:
    print(dir)
    group, id = dir.split('.')[0].split('_')
    data_file = data_dir + dir
    if group != "06" or id != "12":
        continue
    with open(data_file, 'r', encoding='gbk') as f:
        text = f.readlines()
        print(text)
        print(len(text) - text.count("\n"))

    for item in text:
        if item != "\n":
            # random_int = random.randint(1, 1000000)
            unique_id = str(group) + str(id)
            get_output = perspective_classification(text=item, group=group, id=id, unique_id=unique_id)
            if "最接近的主题是“干部作风”" in get_output and ("6 分" in get_output or "7 分" in get_output or "8 分" in get_output or "9 分" in get_output or "10 分" in get_output or "6/10" in get_output or "7/10" in get_output or "8/10" in get_output or "9/10" in get_output):
                output_file = dir_topic_1 + str(group) + "_" + str(id) + ".txt"
                with open(output_file, 'a') as f:
                    f.write(item)
                    f.write("\n")
            if "最接近的主题是“道路自信”" in get_output and ("6 分" in get_output or "7 分" in get_output or "8 分" in get_output or "9 分" in get_output or "10 分" in get_output or "6/10" in get_output or "7/10" in get_output or "8/10" in get_output or "9/10" in get_output):
                output_file = dir_topic_2 + str(group) + "_" + str(id) + ".txt"
                with open(output_file, 'a') as f:
                    f.write(item)
                    f.write("\n")
            if "最接近的主题是“组织纪律”" in get_output and ("6 分" in get_output or "7 分" in get_output or "8 分" in get_output or "9 分" in get_output or "10 分" in get_output or "6/10" in get_output or "7/10" in get_output or "8/10" in get_output or "9/10" in get_output):
                output_file = dir_topic_3 + str(group) + "_" + str(id) + ".txt"
                with open(output_file, 'a') as f:
                    f.write(item)
                    f.write("\n")
            if "最接近的主题是“创新”" in get_output and ("6 分" in get_output or "7 分" in get_output or "8 分" in get_output or "9 分" in get_output or "10 分" in get_output or "6/10" in get_output or "7/10" in get_output or "8/10" in get_output or "9/10" in get_output):
                output_file = dir_topic_4 + str(group) + "_" + str(id) + ".txt"
                with open(output_file, 'a') as f:
                    f.write(item)
                    f.write("\n")
            if "最接近的主题是“民主集中制”" in get_output and ("6 分" in get_output or "7 分" in get_output or "8 分" in get_output or "9 分" in get_output or "10 分" in get_output or "6/10" in get_output or "7/10" in get_output or "8/10" in get_output or "9/10" in get_output):
                output_file = dir_topic_5 + str(group) + "_" + str(id) + ".txt"
                with open(output_file, 'a') as f:
                    f.write(item)
                    f.write("\n")
            if "最接近的主题是“政治站位”" in get_output and ("6 分" in get_output or "7 分" in get_output or "8 分" in get_output or "9 分" in get_output or "10 分" in get_output or "6/10" in get_output or "7/10" in get_output or "8/10" in get_output or "9/10" in get_output):
                output_file = dir_topic_6 + str(group) + "_" + str(id) + ".txt"
                with open(output_file, 'a') as f:
                    f.write(item)
                    f.write("\n")
            if "最接近的主题是“团队建设”" in get_output and ("6 分" in get_output or "7 分" in get_output or "8 分" in get_output or "9 分" in get_output or "10 分" in get_output or "6/10" in get_output or "7/10" in get_output or "8/10" in get_output or "9/10" in get_output):
                output_file = dir_topic_7 + str(group) + "_" + str(id) + ".txt"
                with open(output_file, 'a') as f:
                    f.write(item)
                    f.write("\n")
            if "最接近的主题是“调研和征求意见”" in get_output and ("6 分" in get_output or "7 分" in get_output or "8 分" in get_output or "9 分" in get_output or "10 分" in get_output or "6/10" in get_output or "7/10" in get_output or "8/10" in get_output or "9/10" in get_output):
                output_file = dir_topic_8 + str(group) + "_" + str(id) + ".txt"
                with open(output_file, 'a') as f:
                    f.write(item)
                    f.write("\n")
            if "最接近的主题是“联系群众”" in get_output and ("6 分" in get_output or "7 分" in get_output or "8 分" in get_output or "9 分" in get_output or "10 分" in get_output or "6/10" in get_output or "7/10" in get_output or "8/10" in get_output or "9/10" in get_output):
                output_file = dir_topic_9 + str(group) + "_" + str(id) + ".txt"
                with open(output_file, 'a') as f:
                    f.write(item)
                    f.write("\n")
            if "最接近的主题是“理想信念”" in get_output and ("6 分" in get_output or "7 分" in get_output or "8 分" in get_output or "9 分" in get_output or "10 分" in get_output or "6/10" in get_output or "7/10" in get_output or "8/10" in get_output or "9/10" in get_output):
                output_file = dir_topic_10 + str(group) + "_" + str(id) + ".txt"
                with open(output_file, 'a') as f:
                    f.write(item)
                    f.write("\n")
            if "最接近的主题是“学习的重要性”" in get_output and ("6 分" in get_output or "7 分" in get_output or "8 分" in get_output or "9 分" in get_output or "10 分" in get_output or "6/10" in get_output or "7/10" in get_output or "8/10" in get_output or "9/10" in get_output):
                output_file = dir_topic_11 + str(group) + "_" + str(id) + ".txt"
                with open(output_file, 'a') as f:
                    f.write(item)
                    f.write("\n")
            if "最接近的主题是“基层工作的重要性”" in get_output and ("6 分" in get_output or "7 分" in get_output or "8 分" in get_output or "9 分" in get_output or "10 分" in get_output or "6/10" in get_output or "7/10" in get_output or "8/10" in get_output or "9/10" in get_output):
                output_file = dir_topic_12 + str(group) + "_" + str(id) + ".txt"
                with open(output_file, 'a') as f:
                    f.write(item)
                    f.write("\n")

'''
'''
for dir in data_dirs:
    print(dir)
    group, id = dir.split('.')[0].split('_')
    data_file = data_dir + dir
    if group != "06" or id != "10":
        continue
    with open(data_file, 'r', encoding='gbk') as f:
        text = f.readlines()
        print(text)
        print(len(text) - text.count("\n"))

    for item in text:
        if item != "\n":
            # random_int = random.randint(1, 1000000)
            unique_id = str(group) + str(id)
            get_output = ability_classification(text=item, group=group, id=id, unique_id=unique_id)
            if "最接近的主题是“政治能力”" in get_output and (
                    "6 分" in get_output or "7 分" in get_output or "8 分" in get_output or "9 分" in get_output or "10 分" in get_output or "6/10" in get_output or "7/10" in get_output or "8/10" in get_output or "9/10" in get_output):
                output_file = dir_topic_1 + str(group) + "_" + str(id) + ".txt"
                with open(output_file, 'a') as f:
                    f.write(item)
                    f.write("\n")
            if "最接近的主题是“调查研究能力”" in get_output and (
                    "6 分" in get_output or "7 分" in get_output or "8 分" in get_output or "9 分" in get_output or "10 分" in get_output or "6/10" in get_output or "7/10" in get_output or "8/10" in get_output or "9/10" in get_output):
                output_file = dir_topic_2 + str(group) + "_" + str(id) + ".txt"
                with open(output_file, 'a') as f:
                    f.write(item)
                    f.write("\n")
            if "最接近的主题是“科学决策能力”" in get_output and (
                    "6 分" in get_output or "7 分" in get_output or "8 分" in get_output or "9 分" in get_output or "10 分" in get_output or "6/10" in get_output or "7/10" in get_output or "8/10" in get_output or "9/10" in get_output):
                output_file = dir_topic_3 + str(group) + "_" + str(id) + ".txt"
                with open(output_file, 'a') as f:
                    f.write(item)
                    f.write("\n")
            if "最接近的主题是“改革攻坚能力”" in get_output and (
                    "6 分" in get_output or "7 分" in get_output or "8 分" in get_output or "9 分" in get_output or "10 分" in get_output or "6/10" in get_output or "7/10" in get_output or "8/10" in get_output or "9/10" in get_output):
                output_file = dir_topic_4 + str(group) + "_" + str(id) + ".txt"
                with open(output_file, 'a') as f:
                    f.write(item)
                    f.write("\n")
            if "最接近的主题是“应急处突能力”" in get_output and (
                    "6 分" in get_output or "7 分" in get_output or "8 分" in get_output or "9 分" in get_output or "10 分" in get_output or "6/10" in get_output or "7/10" in get_output or "8/10" in get_output or "9/10" in get_output):
                output_file = dir_topic_5 + str(group) + "_" + str(id) + ".txt"
                with open(output_file, 'a') as f:
                    f.write(item)
                    f.write("\n")
            if "最接近的主题是“群众工作能力”" in get_output and (
                    "6 分" in get_output or "7 分" in get_output or "8 分" in get_output or "9 分" in get_output or "10 分" in get_output or "6/10" in get_output or "7/10" in get_output or "8/10" in get_output or "9/10" in get_output):
                output_file = dir_topic_6 + str(group) + "_" + str(id) + ".txt"
                with open(output_file, 'a') as f:
                    f.write(item)
                    f.write("\n")
            if "最接近的主题是“抓落实能力”" in get_output and (
                    "6 分" in get_output or "7 分" in get_output or "8 分" in get_output or "9 分" in get_output or "10 分" in get_output or "6/10" in get_output or "7/10" in get_output or "8/10" in get_output or "9/10" in get_output):
                output_file = dir_topic_7 + str(group) + "_" + str(id) + ".txt"
                with open(output_file, 'a') as f:
                    f.write(item)
                    f.write("\n")

'''
'''

# “干部作风”、“道路自信”、“组织纪律”、“创新”、“民主集中制”、“政治站位”、“团队建设”、“调研和征求意见”、“联系群众”、“理想信念”、“学习的重要性”、“基层工作的重要性”
for dir in data_dirs:
    print(dir)
    points = []
    if dir in dir_topic_1_dirs:
        points.append("干部作风")
    if dir in dir_topic_2_dirs:
        points.append("道路自信")
    if dir in dir_topic_3_dirs:
        points.append("组织纪律")
    if dir in dir_topic_4_dirs:
        points.append("创新")
    if dir in dir_topic_5_dirs:
        points.append("民主集中制")
    if dir in dir_topic_6_dirs:
        points.append("政治站位")
    if dir in dir_topic_7_dirs:
        points.append("团队建设")
    if dir in dir_topic_8_dirs:
        points.append("调研和征求意见")
    if dir in dir_topic_9_dirs:
        points.append("联系群众")
    if dir in dir_topic_10_dirs:
        points.append("理想信念")
    if dir in dir_topic_11_dirs:
        points.append("学习的重要性")
    if dir in dir_topic_12_dirs:
        points.append("基层工作的重要性")
        print(dir in dir_topic_12_dirs)

    points = list(set(points))

    if len(points) > 0:
        output = "；".join(points)
    else:
        output = "无"

    output_file = output_dir + dir

    with open(output_file, 'a') as f:
        f.write("\n")
        f.write("与延安精神相关的其他角度包括：")
        f.write(output)
        f.write("\n")


'''


'''
# 政治能力、调查研究能力、科学决策能力、改革攻坚能力、应急处突能力、群众工作能力、抓落实能力
for dir in data_dirs:
    print(dir)
    points = []
    if dir in dir_topic_1_dirs:
        points.append("政治能力")
    if dir in dir_topic_2_dirs:
        points.append("调查研究能力")
    if dir in dir_topic_3_dirs:
        points.append("科学决策能力")
    if dir in dir_topic_4_dirs:
        points.append("改革攻坚能力")
    if dir in dir_topic_5_dirs:
        points.append("应急处突能力")
    if dir in dir_topic_6_dirs:
        points.append("群众工作能力")
    if dir in dir_topic_7_dirs:
        points.append("抓落实能力")


    points = list(set(points))

    if len(points) > 0:
        output = "；".join(points)
    else:
        output = "无"

    output_file = output_dir + dir

    with open(output_file, 'a') as f:
        f.write("\n")
        f.write("提到的能力包括：")
        f.write(output)
        f.write("\n")
'''
'''
input_folder = r"C:\\Users\\丁丁\\Desktop\\延安精神_report\\"
output_folder = r"C:\\Users\\丁丁\\Desktop\\延安精神_report_seperate\\"

for filename in os.listdir(input_folder):
    print(filename)
    input_filepath = os.path.join(input_folder, filename)
    with open(input_filepath, 'r', encoding='gbk') as file:
        lines = file.readlines()
        table_1 = lines[2:5]
        output_filepath_table_1 = os.path.join(output_folder, "table_1_" + filename)
        with open(output_filepath_table_1, 'w', encoding='utf-8') as f1:
            f1.write("\n".join(table_1))

        table_2 = lines[6:9]
        output_filepath_table_2 = os.path.join(output_folder, "table_2_" + filename)
        with open(output_filepath_table_2, 'w', encoding='utf-8') as f2:
            f2.write("\n".join(table_2))

        lines = lines[9:]
        print(lines)
        content = "".join(lines)
        content = content.split("提到了史实：")[1]
        history = content.split("提到了著作：")[0]
        output_filepath_history = os.path.join(output_folder, "history_" + filename)
        with open(output_filepath_history, 'w', encoding='utf-8') as f3:
            f3.write(history)

        book = content.split("提到了著作：")[1].split("与延安精神相关的其他角度包括：")[0]
        output_filepath_book = os.path.join(output_folder, "book_" + filename)
        with open(output_filepath_book, 'w', encoding='utf-8') as f4:
            f4.write(book)

        other_perspectives = content.split("提到了著作：")[1].split("与延安精神相关的其他角度包括：")[1].split("\n\n")[0]
        output_filepath_other_perspectives = os.path.join(output_folder, "other_perspectives_" + filename)
        with open(output_filepath_other_perspectives, 'w', encoding='utf-8') as f5:
            f5.write(other_perspectives)

        total_score = content.split("总得分：")[1]
        output_filepath_total_score = os.path.join(output_folder, "total_score_" + filename)
        with open(output_filepath_total_score, 'w', encoding='utf-8') as f6:
            f6.write(total_score)

        print(history)
        print(book)
        print(other_perspectives)
        print(total_score)

'''

input_folder_1 = r"C:\\Users\\丁丁\\Desktop\\延安精神_report_table_1\\"
input_folder_2 = r"C:\\Users\\丁丁\\Desktop\\延安精神_report_table_2\\"
output_folder = r"C:\\Users\\丁丁\\Desktop\\延安精神_report_table\\"

for filename in os.listdir(input_folder_1):
    print(filename)
    print(filename.replace("table_1_", ""))
    first =[]
    second =[]
    third = []

    input_filepath_1 = os.path.join(input_folder_1, filename)
    with open(input_filepath_1, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in [lines[0], lines[2], lines[4]]:
            word1 = line.split("|")
            word1 = word1[1:3]
            first.append(word1[0])
            second.append(word1[1])

    input_filepath_2 = os.path.join(input_folder_2, filename.replace("table_1_","table_2_"))
    with open(input_filepath_2, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in [lines[0], lines[2], lines[4]]:
            word2 = line.split("|")
            word2 = word2[1:3]
            third.append(word2[1])

    output_filepath = os.path.join(output_folder, filename.replace("table_1_",""))
    with open(output_filepath, 'w', encoding='utf-8') as file:
        for i in range(3):
            output_str = "|" + first[i] + "|" + second[i] + "|" + third[i] + "|"
            file.write(output_str)
            file.write("\n")



