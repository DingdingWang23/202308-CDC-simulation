# -*- coding: utf-8 -*-

import os
import zhipuai
import random

zhipuai.api_key = "2853e15e35c0be35f3435ec9b0127d08.RKdVy3NNCRzIIVo9"

'''
  说明：
  add: 事件流开启
  error: 平台服务或者模型异常，响应的异常事件
  interrupted: 中断事件，例如：触发敏感词
  finish: 数据接收完毕，关闭事件流
'''

def output(content, group, id, output_dir = r'C:\\Users\\丁丁\\Desktop\\table_2\\'):
    file = output_dir + str(group)+"_"+str(id)+".txt"
    with open(file, 'a') as f:
        f.write(content)
        f.write("\n")

# 测试记忆是否消失了
def mytest(
        text="",
        group=0,
        id=0,
        unique_id = ""
):
    prompt = [
        {"role": "user",
         "content": text},
    ]

    response = zhipuai.model_api.sse_invoke(
        model="chatglm_pro",
        prompt=prompt,
        top_p=0.7,
        temperature=0.1,
        incremental=False,
        request_id=unique_id

    )


    for event in response.events():
        if event.event == "add":
            pass
        elif event.event == "error" or event.event == "interrupted":
            print(event.data)
        elif event.event == "finish":
            print(event.data)
        else:
            print(event.data)

# 搜索与延安精神相关的学校场景
def sse_invoke_yanan1_1(
        text="",
        group=0,
        id=0,
        unique_id=""
):
    prompt = [
        {"role": "user",
         "content": "你将看到一段文本，从“服务人民”、“实事求是”、“自力更生，艰苦奋斗”的角度搜索文本，如果文本中提及该角度，用表格罗列提及该角度的原文亮点，并列出提及该角度的联系实际工作内容；如果没有提及，对文本中未提及的角度，务必直接在表格中说明“未提及”。文本：---"},
    ]
    assert text != ""
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
    output_dir = r'C:\\Users\\丁丁\\Desktop\\table_1\\'
    for event in response.events():
        if event.event == "add":
            # print(event.data)
            pass
        elif event.event == "error" or event.event == "interrupted":
            print(event.data)
            # output(event.data, group=group, id=id, output_dir=output_dir)
        elif event.event == "finish":
            print(event.data)
            # output(event.data, group=group, id=id, output_dir=output_dir)
            # print(event.meta)
        else:
            print(event.data)
            # output(event.data, group=group, id=id, output_dir=output_dir)

# 搜索与延安精神相关的学校的具体工作
def sse_invoke_yanan1_2(
        text="",
        group=0,
        id=0,
        unique_id=""
):
    prompt = [
        {"role": "user",
         "content": "你将看到一段文本，从“服务人民”、“实事求是”、“自力更生，艰苦奋斗”的角度搜索文本，如果文本中提及该角度，用表格罗列提及该角度的原文主旨，并列出提及该角度的联系实际工作内容；如果没有提及，对文本中未提及的角度，务必直接在表格中说明“未提及”。文本：---"},
    ]
    assert text != ""
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
    output_dir = r'C:\\Users\\丁丁\\Desktop\\table_2\\'
    for event in response.events():
        if event.event == "add":
            # print(event.data)
            pass
        elif event.event == "error" or event.event == "interrupted":
            print(event.data)
            # output(event.data, group=group, id=id, output_dir=output_dir)
        elif event.event == "finish":
            print(event.data)
            # output(event.data, group=group, id=id, output_dir=output_dir)
            # print(event.meta)
        else:
            print(event.data)
            # output(event.data, group=group, id=id, output_dir=output_dir)


def sse_invoke_yanan2(
        text="",
        group=0,
        id=0,
        unique_id=""
):
    prompt = [
        {"role": "user",
         "content": "你将看到一段文本，请在原文中搜索关于“团队建设”的内容，并输出搜索到的原文。文本：---"},
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
    output_dir = r'C:\\Users\\丁丁\\Desktop\\table_1\\'
    for event in response.events():
        if event.event == "add":
            # print(event.data)
            pass
        elif event.event == "error" or event.event == "interrupted":
            print(event.data)
            output(event.data, group=group, id=id, output_dir=output_dir)
        elif event.event == "finish":
            print(event.data)
            output(event.data, group=group, id=id, output_dir=output_dir)
            # print(event.meta)
        else:
            print(event.data)
            output(event.data, group=group, id=id, output_dir=output_dir)

# 搜索文本中全部具体事例，包括延安时期/历史上的清华精神/学校的当下实际
def sse_invoke_yanan3(
        text="",
        group=0,
        id=0,
        unique_id=""
):
    prompt = [
        {"role": "user",
         "content": "你将看到一段文本，请根据原文内容，抽取文本中提到的结合实际工作的具体事例，包括历史上的事例和当下现实中的事例。文本：---"},
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
    output_dir = r'C:\\Users\\丁丁\\Desktop\\table_1\\'
    for event in response.events():
        if event.event == "add":
            # print(event.data)
            pass
        elif event.event == "error" or event.event == "interrupted":
            print(event.data)
            output(event.data, group=group, id=id, output_dir=output_dir)
        elif event.event == "finish":
            print(event.data)
            output(event.data, group=group, id=id, output_dir=output_dir)
            # print(event.meta)
        else:
            print(event.data)
            output(event.data, group=group, id=id, output_dir=output_dir)

# 抽取文本中的著作
def sse_invoke_yanan3_1(
        text="",
        group=0,
        id=0,
        unique_id=""
):
    prompt = [
        {"role": "user",
         "content": "你将看到一段文本，抽取原文中精确提及的著作。文本：---"},
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
    output_dir = r'C:\\Users\\丁丁\\Desktop\\table_1\\'
    for event in response.events():
        if event.event == "add":
            # print(event.data)
            pass
        elif event.event == "error" or event.event == "interrupted":
            print(event.data)
            output(event.data, group=group, id=id, output_dir=output_dir)
        elif event.event == "finish":
            print(event.data)
            output(event.data, group=group, id=id, output_dir=output_dir)
            # print(event.meta)
        else:
            print(event.data)
            output(event.data, group=group, id=id, output_dir=output_dir)


def sse_invoke_yanan3_2(
        text="",
        group=0,
        id=0,
        unique_id=""
):
    prompt = [
        {"role": "user",
         "content": "你将看到一段文本，请根据原文内容，抽取文本中明确提及的延安时期的具体历史事例。文本：---"},
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
    output_dir = r'C:\\Users\\丁丁\\Desktop\\table_1\\'
    for event in response.events():
        if event.event == "add":
            # print(event.data)
            pass
        elif event.event == "error" or event.event == "interrupted":
            print(event.data)
            output(event.data, group=group, id=id, output_dir=output_dir)
        elif event.event == "finish":
            print(event.data)
            output(event.data, group=group, id=id, output_dir=output_dir)
            # print(event.meta)
        else:
            print(event.data)
            output(event.data, group=group, id=id, output_dir=output_dir)

# 主题分类+1.2的表格输出，需要改prompt
def test(
        text="",
        group=0,
        id=0,
        unique_id=""
):
    prompt = [
        {"role": "user",
         "content": "你将看到一段文本，请根据原文内容，从“干部作风”、“道路自信”、“组织纪律”、“创新发展”、“民主集中制”、“政治站位”、“团队建设”、“调研和征求意见”、“联系群众”、“理想信念”、“学习的重要性”、“马克思主义中国化”、“基层工作的重要性”这些主题中选择一个与文本最接近的主题。文本：---"},
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
    output_dir = r'C:\\Users\\丁丁\\Desktop\\table_1\\'
    for event in response.events():
        if event.event == "add":
            # print(event.data)
            pass
        elif event.event == "error" or event.event == "interrupted":
            print(event.data)
            output(event.data, group=group, id=id, output_dir=output_dir)
        elif event.event == "finish":
            print(event.data)
            output(event.data, group=group, id=id, output_dir=output_dir)
            # print(event.meta)
        else:
            print(event.data)
            output(event.data, group=group, id=id, output_dir=output_dir)


# 语料的分类
def test_3(
        text="",
        group=0,
        id=0,
        unique_id=""
):
    prompt = [
        {"role": "user",
         "content": "你将看到一段文本，请根据原文内容，从“干部队伍建设”、“教学”、“科研”、“行政办公室、财务、规划、信息技术、法务“、“学生思政和活动”、“医院建设”这些主题中选择一个与文本最接近的主题，并给接近程度打分。文本：---"},
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
    output_dir = r'C:\\Users\\丁丁\\Desktop\\table_1\\'
    for event in response.events():
        if event.event == "add":
            # print(event.data)
            pass
        elif event.event == "error" or event.event == "interrupted":
            print(event.data)
            output(event.data, group=group, id=id, output_dir=output_dir)
        elif event.event == "finish":
            print(event.data)
            output(event.data, group=group, id=id, output_dir=output_dir)
            # print(event.meta)
        else:
            print(event.data)
            output(event.data, group=group, id=id, output_dir=output_dir)


def corpus_classification(
        text="",
        group=0,
        id=0,
        unique_id=""
):
    prompt = [
        {"role": "user",
         "content": "你将看到一段文本，请根据原文内容，从“干部队伍建设”、“教学”、“科研”、“行政办公室、财务、规划、信息技术、法务“、“学生思政和活动”、“医院建设”这些主题中选择一个与文本最接近的主题，并给接近程度打分。文本：---"},
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
    output_dir = r'C:\\Users\\丁丁\\Desktop\\table_1\\'
    output = ""
    for event in response.events():
        if event.event == "add":
            # print(event.data)
            pass
        elif event.event == "error" or event.event == "interrupted":
            print(event.data)
            output = event.data
            output(event.data, group=group, id=id, output_dir=output_dir)
        elif event.event == "finish":
            print(event.data)
            output = event.data
            output(event.data, group=group, id=id, output_dir=output_dir)
            # print(event.meta)
        else:
            print(event.data)
            output = event.data
            output(event.data, group=group, id=id, output_dir=output_dir)
    return output


def perspective_classification(
        text="",
        group=0,
        id=0,
        unique_id=""
):
    prompt = [
        {"role": "user",
         "content": "你将看到一段文本，请根据原文内容，从“干部作风”、“道路自信”、“组织纪律”、“创新发展”、“民主集中制”、“政治站位”、“团队建设”、“调研和征求意见”、“联系群众”、“理想信念”、“学习的重要性”、“马克思主义中国化”、“基层工作的重要性”这些主题中选择一个与文本最接近的主题，并给接近程度打分。文本：---"},
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
    output_dir = r'C:\\Users\\丁丁\\Desktop\\table_1\\'
    output = ""
    for event in response.events():
        if event.event == "add":
            # print(event.data)
            pass
        elif event.event == "error" or event.event == "interrupted":
            print(event.data)
            output = event.data
            output(event.data, group=group, id=id, output_dir=output_dir)
        elif event.event == "finish":
            print(event.data)
            output = event.data
            output(event.data, group=group, id=id, output_dir=output_dir)
            # print(event.meta)
        else:
            print(event.data)
            output = event.data
            output(event.data, group=group, id=id, output_dir=output_dir)
    return output


# 改后的主题分类
def test_2(
        text="",
        group=0,
        id=0,
        unique_id=""
):
    prompt = [
        {"role": "user",
         "content": "你将看到一段文本，请根据原文内容，从“干部作风”、“道路自信”、“组织纪律”、“创新发展”、“民主集中制”、“政治站位”、“团队建设”、“调研和征求意见”、“联系群众”、“理想信念”、“学习的重要性”、“马克思主义中国化”、“基层工作的重要性”这些主题中选择一个与文本最接近的主题，并给接近程度打分。文本：---"},
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
    output_dir = r'C:\\Users\\丁丁\\Desktop\\table_1\\'
    for event in response.events():
        if event.event == "add":
            # print(event.data)
            pass
        elif event.event == "error" or event.event == "interrupted":
            print(event.data)
            output(event.data, group=group, id=id, output_dir=output_dir)
        elif event.event == "finish":
            print(event.data)
            output(event.data, group=group, id=id, output_dir=output_dir)
            # print(event.meta)
        else:
            print(event.data)
            output(event.data, group=group, id=id, output_dir=output_dir)


# 文本分割
def scan(
        text="",
        group=0,
        id=0,
        unique_id=""
):
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

    # print response data
    output_dir = r'C:\\Users\\丁丁\\Desktop\\table_1\\'
    for event in response.events():
        if event.event == "add":
            # print(event.data)
            pass
        elif event.event == "error" or event.event == "interrupted":
            print(event.data)
            output(event.data, group=group, id=id, output_dir=output_dir)
        elif event.event == "finish":
            print(event.data)
            output(event.data, group=group, id=id, output_dir=output_dir)
            # print(event.meta)
        else:
            print(event.data)
            output(event.data, group=group, id=id, output_dir=output_dir)


def test_1(
        text="",
        group=0,
        id=0,
        unique_id = ""
):
    prompt = [
        {"role": "user",
         "content": "你将看到一些事例，请将每个事例分为“延安精神的事例”“历史上的清华精神的事例”“当下学校实际工作的事例”中的一类。文本：---"},
    ]
    prompt_add_text = prompt
    prompt_add_text[0]["content"] = prompt_add_text[0]["content"] + text

    response = zhipuai.model_api.sse_invoke(
        model="chatglm_pro",
        prompt=prompt_add_text,
        top_p=0.7,
        temperature=0.1,
        incremental=False,
        request_id = unique_id
    )

    # print response data
    output_dir = r'C:\\Users\\丁丁\\Desktop\table_1\\'
    for event in response.events():
        if event.event == "add":
            # print(event.data)
            pass
        elif event.event == "error" or event.event == "interrupted":
            print(event.data)
            output(event.data, group=group, id=id, output_dir=output_dir)
        elif event.event == "finish":
            print(event.data)
            output(event.data, group=group, id=id, output_dir=output_dir)
            # print(event.meta)
        else:
            print(event.data)
            output(event.data, group=group, id=id, output_dir=output_dir)


def sse_invoke_yanan1_1_refinement(
        text="",
        group=0,
        id=0,
        unique_id=""
):
    prompt = [
        {"role": "user",
         "content": "你将看到一段文本，从“服务人民”、“实事求是”、“自力更生，艰苦奋斗”的角度搜索文本，如果文本中提及该角度，用表格罗列提及该角度的原文亮点，并列出提及该角度的联系实际工作内容，只输出一行；如果没有提及，对文本中未提及的角度，务必直接在表格中说明“未提及”。文本：---"},
    ]
    assert text != ""
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
    output_dir = r'C:\\Users\\丁丁\\Desktop\\table_1\\'
    for event in response.events():
        if event.event == "add":
            # print(event.data)
            pass
        elif event.event == "error" or event.event == "interrupted":
            print(event.data)
            output(event.data, group=group, id=id, output_dir=output_dir)
        elif event.event == "finish":
            print(event.data)
            output(event.data, group=group, id=id, output_dir=output_dir)
            # print(event.meta)
        else:
            print(event.data)
            output(event.data, group=group, id=id, output_dir=output_dir)

'''
data_dir = r"C:\\Users\\丁丁\\Desktop\\每个人讲的话_掐头去尾版\\"
data_dirs = os.listdir(data_dir)


dir_topic_1 = r"C:\\Users\\丁丁\\Desktop\\干部队伍建设\\"
dir_topic_2 = r"C:\\Users\\丁丁\\Desktop\\教学\\"
dir_topic_3 = r"C:\\Users\\丁丁\\Desktop\\科研\\"
dir_topic_4 = r"C:\\Users\\丁丁\\Desktop\\行政办公室、财务、规划、信息技术、法务\\"
dir_topic_5 = r"C:\\Users\\丁丁\\Desktop\\学生思政和活动\\"
dir_topic_6 = r"C:\\Users\\丁丁\\Desktop\\医院建设\\"
'''

for dir in data_dirs:
    print(dir)
    group, id = dir.split('.')[0].split('_')
    data_file = data_dir + dir
    if group != "05" or id != "1":
        continue

    with open(data_file, 'r', encoding='gbk') as f:
        '''
        text = f.readlines()
        # text = text.replace("【","")
        # text = text.replace("】", "")
        new_text = []
        for line in text:
            if line != "\n":
                new_text.append(line.rstrip("\n"))
        print(text)
        print(new_text)
        # new_text = [item for item in text if item != "\n"]
        print(len(text)-text.count("\n"))
        content = "".join(new_text)
        # content = "\n".join(new_text)
        '''
        content = f.read()
        print(content)

    '''
    for item in text:
        if item != "\n":
            # random_int = random.randint(1, 1000000)
            unique_id = str(group) + str(id)

            get_output = corpus_classification(text=item, group=group, id=id, unique_id=unique_id)
            if "“干部队伍建设”" in get_output and ("6 分" in get_output or "7 分" in get_output or "8 分" in get_output or "9 分" in get_output or "10 分" in get_output or "6/10" in get_output or "7/10" in get_output or "8/10" in get_output or "9/10" in get_output):
                output_file = dir_topic_1 + str(group) + "_" + str(id) + ".txt"
                with open(output_file, 'a') as f:
                    f.write(item)
                    f.write("\n")
            if "“教学”" in get_output and ("6 分" in get_output or "7 分" in get_output or "8 分" in get_output or "9 分" in get_output or "10 分" in get_output or "6/10" in get_output or "7/10" in get_output or "8/10" in get_output or "9/10" in get_output):
                output_file = dir_topic_2 + str(group) + "_" + str(id) + ".txt"
                with open(output_file, 'a') as f:
                    f.write(item)
                    f.write("\n")
            if "“科研”" in get_output and ("6 分" in get_output or "7 分" in get_output or "8 分" in get_output or "9 分" in get_output or "10 分" 



# 你将看到一段文本，请根据原文内容，抽取文本中提到的著作和领导讲话。文本：---
# 你将看到一段文本，抽取原文中提到的著作。文本：---
# 你将看到一段文本，请抽取原文中提到的著作；如果原文未提及任何著作，请输出“未提及”。文本：---

# 你将看到一段文本，请根据原文内容，抽取文本中提及的结合延安时期史实的具体事例。文本：---
# 你将看到一段文本，请根据原文内容，抽取文本中提及的延安时期的具体历史事例。文本：---

# 你将看到一段文本，请根据原文内容，从“干部作风”、“团队建设”、“道路自信”、“从严治党”、“组织纪律”、“实事求是”、“理性乐观”、“激励措施”、“创新发展”、“终身学习”、“民主集中制”、“政治站位”、“调研和征求意见”、“跨部门交流”、“联系群众”这些主题中选择一个与文本最接近的主题。文本：---
# 你将看到一段文本，请根据原文内容，从“干部作风”、“道路自信”、“组织纪律”、“创新发展”、“民主集中制”、“政治站位”、“团队建设”、“调研和征求意见”、“联系群众”、“理想信念”、“学习的重要性”、“马克思主义中国化”、“基层工作的重要性”这些主题中选择一个与文本最接近的主题。文本：---

# text ="而且还有一个就是说起那个群众工作，反正我自己刚上任俩月，虽然还满脑袋包，天天在忙活一些事的时候，但是我大概就在一周前，我安排了一个我跟所有我们系的职员每个人谈话半小时，我觉得效果特别好。就这个超乎我的想象，就是我个人感觉还是真的是要听到大家的声音，了解他的具体的问题，其实每个人还都有自己的设想，都有一些好的观察到的工作当中的问题，也有一些建议。所以我现在这个他们他聊完之后，我就好多事情我都列成列出来，都后面想去解决，所以我个人也是感觉这些东西还是很重要的，作为一个干部来说，对，嗯，你是受那个主题教育的启发。"

# test_3(text=text, group=0, id=0, unique_id="0501")


# text ="而且这个点从咱们说结合到学校工作来讲，就因为我现在在院系干这个党委书记，实际上马上回去，紧挨着周四一场，周五一场，就要给研究生新生上党课，就要给本科生新生上党课，所以这个对我来说是非常现实的一个培训的帮助就是我有很多的东西之前理解的不够好，或者说有很多那个你其实也企图要启发学生，但那个地方因为你没有掌握那个第一手的史料或者一些影像或者怎么样，那种冲击力是不够的。"

# get_output = corpus_classification(text=text, group=0, id=0, unique_id="0505")
# print(get_output)
