# -*- coding: utf-8 -*-
import os
import jieba
from fuzzywuzzy import fuzz
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
import re

input_folder = r"C:\\Users\\丁丁\\Desktop\\学生工作"
output_folder = r"C:\\Users\\丁丁\\Desktop\\学生工作_output"

topic_1 = ['解放思想', '实事求是', '自力更生', '延安', '延安精神', '党校', '井冈山', '长征', '王明', '鲁艺', '中央党校', '遵义会议', '张闻天', '陕北', '张思德', '蒋南翔', '任弼时', '毛岸英', '整风运动', '青年干部', '杨家岭', '团中央', '革命圣地', '崔军', '人民大学', '青委', '延安地区', '瑞金', '先进事迹', '叶飞', '秋收起义', '上级指示', '警卫员', '留苏', '国统区', '张冲']
topic_2 = ['学校', '附小', '小学', '学堂', '中学', '高中', '高年级', '幼儿园', '医学院校','院系', '师生', '高校', '学科', '清华大学', '党校', '北大', '校内', '人才培养', '校医院', '附小', '文科', '学习班', '开班', '又红又专', '学科建设', '育人', '工程学院', '研究生院', '鲁艺', '本科生', '校办', '本科', '校领导', '工科', '博士生', '一流大学', '中央党校', '培训班', '法学院', '招生', '经管', '党建', '科室', '师资', '教学科研', '团委', '科研经费', '系主任', '办学', '课程标准', '意见建议', '学系', '附院', '科研项目', '留校', '扩招', '仪器设备', '领导班子', '职能部门', '教研', '机械系', '科研工作', '同济', '财务部门', '医学院', '开学', '机构编制', '专科', '育才', '地学', '理工科', '住校', '校园网', '校外', '学分', '博士后', '工学', '中西医', '美院', '审计工作', '电子系', '水利系', '英语课', '基础教育', '党政', '整风运动', '青年干部', '处级', '信息产业部', '中文系', '根本任务', '天文系', '本科毕业', '工作部门', '社科', '无纸化', '校企', '培养人才', '专业学位', '雕塑系', '经济法', '院办', '高等教育', '生命科学', '医学中心', '建院', '专业课', '青年教师', '市属', '人文学院', '高年级', '档案库', '口腔科', '临床医学', '美术学院', '招新', '组织部门', '药学院', '试点工作', '落实政策', '国防科技', '激励机制', 'QS', '人民大学', '体制改革', '生物科学', '医学生', '住院医师', '中层干部', '地质系', '学部委员', '延安地区', '体育部', '治校', '基础性', '轮训', '研究班', '必修课', '课程设计', '指导组', '思想战线', '自动化系', '计算机系', '交叉学科', '会计专业', '理科生', '社会科学', '科技领域', '社会科学界', '管理学', '研究型', '师资队伍', '上海交大', '复旦', '浙江大学', '科研课题', '清华北大', '浙大', '课题组', '国家教委', '化学工程', '学生处', '教师队伍', '妇产', '对口', '学府', '校团委', '择优', '教育经费', '听课', '学工', '师生员工', '测评', '基金委', '中办', '公费医疗', '院务', '社区卫生', '科主任', '中医科', '引进人才', '科研机构', '留苏', '新课程', '数学课', '数学系', '计算中心', '电教', '高等学校', '科技人才', '高考', '教育体制', '教务处', '城乡规划', '中国大学', '北医', '医学院校', '课文', '书本费', '科技成果', '医工', '教学方法','发展']
topic_3 = ['干部', '辅导员', '干部队伍', '党校', '班子', '学习班', '财务处', '党员', '党委', '又红又专', '组长', '群众路线', '组织部', '鲁艺', '校领导', '中央党校', '培训班', '军训', '党建', '外事', '党支部', '干事', '团委', '张思德', '职工', '中组部', '领导班子', '职能部门', '蒋南翔', '副职', '机构编制', '班主任', '办实事', '审计工作', '党政', '党务', '整风运动', '青年干部', '处级', '老同志', '根本任务', '工作部门', '武装部', '院办', '贯彻落实', '班子成员', '纪委', '团中央', '青年教师', '共产党员', '保卫处', '组织部门', '军官', '试点工作', '落实政策', '崔军', '中层干部', '中宣部', '青委', '宣传部长', '延安地区', '工会主席', '工作部', '体育部', '轮训', '研究班', '无产', '副处长', '指导组', '靠边站', '思想战线', '先进事迹', '师资队伍', '工农兵', '国家机关', '预决算', '学生处', '教导员', '教师队伍', '对口', '校团委', '巡视组', '副组长', '学工', '师生员工', '教育部党组', '现场会', '中办', '保密工作', '上级指示', '转业', '警卫员', '留苏', '科技人才', '纪委书记', '教务处', '德才兼备', '老干部','干部']
topic_4 = ['科研', '教学', '学科', '课程', '人才培养', '文科', '教师', '学习班', '开班', '学科建设', '育人', '上课', '讲课', '招生', '经管', '军训', '师资', '教学科研', '课程标准', '科研项目', '教研', '课堂', '授课', '科研工作', '理工科', '住校', '校外', '英语课', '基础教育', '根本任务', '社科', '校企', '培养人才', '专业学位', '科学素养', '专业课', '青年教师', '临床医学', '生物科学', '人学', '专业知识', '复习', '教室', '治校', '必修课', '课程设计', '会计专业', '理科生', '社会科学', '实践性', '师资队伍', '科研课题', '名师', '健全人格', '教师队伍', '理疗', '教具', '听课', '基金委', '院务', '科研机构', '新课程', '课后', '数学课', '电教', '科技人才', '教育体制', '教务处', '德才兼备', '课本', '课文', '医工', '教学方法']
topic_5 = ['科研', '信息化', '教学', '高质量', '创新', '学科', '实验室', '人才', '人才培养', '专项', '学术', '课题', '又红又专', '卓越', '群众路线', '学科建设', '育人', '军工', '研究生院', '校办', '博士生', '一流大学', '经管', '党建', '科室', '师资', '教学科研', '创业精神', '科研经费', '科研项目', '仪器设备', '专业化', '诊疗', '职能部门', '教研', '科研工作', '共建', '财务部门', '抓手', '地学', '理工科', '创新性', '运维', '管理中心', '信息技术', '专业性', '博士后', '中西医', '审计工作', '防控', '电子系', '水利系', '基础教育', '开拓创新', '根本任务', '天文系', '专家组', '工作部门', '社科', '定点医院', '校企', '培养人才', '专业学位', '科技部', '项目管理', '高等教育', '科学素养', '生命科学', '医学中心', '专业课', '高水平', '产业化', '先进性', '高素质', '青年教师', '人文学院', '档案库', '口腔科', '临床医学', '智能化', '组织部门', '试点工作', '技术难题', '国防科技', '激励机制', '生物科学', '技术创新', '毕业设计', '最前沿', '专业知识', '绩效', '基础性', '轮训', '服务性', '课程设计', '思想战线', '自动化系', '计算机系', '交叉学科', '会计专业', '社会科学', '科技领域', '社会科学界', '研究型', '实践性', '先进事迹', '师资队伍', '差旅', '上海交大', '浙江大学', '科研课题', '清华北大', '浙大', '课题组', '中科院', '国家教委', '化学工程', '学生处', '健全人格', '教师队伍', '妇产', '理疗', '互补性', '对口', '合规性', '教具', '测评', '基金委', '院务', '工程化', '科工', '社区卫生', '退耕还林', '引进人才', '放射科', '科研机构', '新课程', '计算中心', '电教', '科技司', '科技人才', '德才兼备', '城乡规划', '国土资源', '医学院校', '高标准', '科技成果', '医工']
topic_6 = ['学生', '同学', '师生', '家长', '教师', '本科生', '入学', '住校', '校外', '英语课', '大学生', '高年级', '医学生', '必修课', '理科生', '师生员工', '课后', '工作']

text_1 = '延安精神是实事求是、理论联系实际的精神，全心全意为人民服务的精神和自力更生艰苦奋斗的精神。'
text_2 = '学校院系高质量发展。'
text_3 = '干部队伍建设。'
text_4 = '高校的教育教学。'
text_5 = '学科建设和科研水平。'
text_6 = '学生工作。'

score = {}

with open(r'C:\\Users\\丁丁\\Desktop\\干部培训测评\\node_list_single.txt', 'r', encoding='UTF-8') as file:
    contents = file.read()

node_list = eval(contents)

said_all =[]

for filename in os.listdir(input_folder):
    if filename.endswith(".txt"):
        filepath = os.path.join(input_folder, filename)

        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()

        paragraphs = content.split("  ")
        output_paragraphs =[]
        for paragraph in paragraphs:
            phrases = jieba.lcut(paragraph)

            common_elements = [item for item in phrases if item in topic_6]
            print(common_elements)

            score[paragraph] = (len(common_elements)+1)*fuzz.ratio(paragraph, text_6)

            if score[paragraph] >= 0:
                output_paragraphs.append(paragraph)

        said_per_person = "\n".join(output_paragraphs)
        said_all.append(said_per_person)


        output_filepath = os.path.join(output_folder, filename)
        with open(output_filepath, 'w', encoding='utf-8') as file:
            print(output_paragraphs, file=file)

print(said_all)
print(len(said_all))


word2count_all_person = []
word2count_total = {}

words_all_person = []
words_all_semi_sentences = []

for said in said_all:

    word2count_per_person = {}
    words_per_person = []

    phrases = jieba.lcut(said)
    for word in phrases:
        if word in node_list:

            words_per_person.append(word)

            if word not in word2count_total.keys():
                word2count_total[word] = 1
            else:
                word2count_total[word] += 1

            if word not in word2count_per_person.keys():
                word2count_per_person[word] = 1
            else:
                word2count_per_person[word] += 1

    word2count_all_person.append(word2count_per_person)
    words_all_person.append(words_per_person)

sorted_dict = dict(sorted(word2count_total.items(), key=lambda x: x[1], reverse=True))

sorted_dict_2 = dict(sorted(score.items(), key=lambda x: x[1], reverse=True))


words_all_semi_sentences = []

for said in said_all:

    semi_sentences = re.split(r'(?<=[。！？，])', said)

    for semi_sentence in semi_sentences:

        words_per_semi_sentences = []

        phrases = jieba.lcut(semi_sentence)
        for word in phrases:
            if word in node_list:
                words_per_semi_sentences.append(word)

        if words_per_semi_sentences != []:
            words_all_semi_sentences.append(words_per_semi_sentences)

print(words_all_semi_sentences)
print(len(words_all_semi_sentences))


Encoder=TransactionEncoder()
encoded_data=Encoder.fit_transform(words_all_semi_sentences)
df=pd.DataFrame(encoded_data,columns=Encoder.columns_)
print(df)


frequent_items= apriori(df, min_support=0.001, use_colnames=True, max_len=3).sort_values(by='support', ascending=False)
print(frequent_items)

ass_rule=association_rules(frequent_items, metric='confidence', min_threshold =0.6)
ass_rule.sort_values(by ='leverage', ascending = False, inplace =True)

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)

print(ass_rule)
print(type(ass_rule))


words_list = []
set_list = []


for i in range(len(ass_rule)):
    word_1 = ass_rule.iloc[i, 0]
    word_2 = ass_rule.iloc[i, 1]


    support_1 = ass_rule.iloc[i, 2]
    support_2 = ass_rule.iloc[i, 3]

    my_words = word_1.union(word_2)
    words = set(my_words)
    set_list.append(words)
    add = 1

    for previous_words in words_list:
        if len(previous_words & words) >= 2:
            add = 0
        elif len(previous_words & words) == 1 and support_1 > 0.01 and support_2 > 0.01:
            add = 0
    if add == 1:
        words_list.append(words)

'''
f = open(r'C:\\Users\\丁丁\\Desktop\\延安精神_关联分析.txt', "w")
print(ass_rule,file=f)
f.close()

f = open(r'C:\\Users\\丁丁\\Desktop\\延安精神_词组.txt', "w")
print(words_list,file=f)
f.close()
'''

for i in range(len(ass_rule)):
    word_1 = ass_rule.iloc[i, 0]
    word_2 = ass_rule.iloc[i, 1]

    my_words = word_1.union(word_2)
    words = set(my_words)
    set_list.append(words)

to_convert = []

for my_set in set_list:
    count_concept = 0
    count_example = 0
    for item in my_set:
        if word2count_total[item] ==1:
            count_example += 1
        elif word2count_total[item] > 1:
            count_concept += 1
    if count_example > 0 and count_concept > 0:
        print(my_set)
        to_convert.append(my_set)

example2concept = {}

for item in to_convert:
    if len(item) ==2:
        for word in item:
            if word2count_total[word] > 1:
                concept = word

        for word in item:
            if word2count_total[word] == 1:
                example2concept[word] = concept

    if len(item) == 3:
        max_count = 0
        for word in item:
            if word2count_total[word] > max_count:
                max_count = word2count_total[word]

        for word in item:
            if word2count_total[word] == max_count:
                concept = word

        for word in item:
            if word2count_total[word] == 1:
                example2concept[word] = concept

new_words_all_semi_sentences = []

for semi_sentence in words_all_semi_sentences:
    new_semi_sentences = []
    for word in semi_sentence:
        if word in example2concept.keys():
            new_semi_sentences.append(example2concept[word])
        else:
            new_semi_sentences.append(word)
    new_words_all_semi_sentences.append(new_semi_sentences)

words_all_semi_sentences = new_words_all_semi_sentences
print(words_all_semi_sentences)
print(len(words_all_semi_sentences))

print("*********以下是替换掉例子后重新提词组**********")

Encoder=TransactionEncoder()
encoded_data=Encoder.fit_transform(words_all_semi_sentences)
df=pd.DataFrame(encoded_data,columns=Encoder.columns_)
print(df)


frequent_items= apriori(df, min_support=0.001, use_colnames=True, max_len=3).sort_values(by='support', ascending=False)
print(frequent_items)

ass_rule=association_rules(frequent_items, metric='confidence', min_threshold =0.6)
ass_rule.sort_values(by ='leverage', ascending = False, inplace =True)

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)

print(ass_rule)
print(type(ass_rule))


words_list = []
set_list = []


for i in range(len(ass_rule)):
    word_1 = ass_rule.iloc[i, 0]
    word_2 = ass_rule.iloc[i, 1]


    support_1 = ass_rule.iloc[i, 2]
    support_2 = ass_rule.iloc[i, 3]

    my_words = word_1.union(word_2)
    words = set(my_words)
    set_list.append(words)
    add = 1

    for previous_words in words_list:
        if len(previous_words & words) >= 2:
            add = 0
        elif len(previous_words & words) == 1 and support_1 > 0.01 and support_2 > 0.01:
            add = 0
    if add == 1:
        words_list.append(words)

'''
f = open(r'C:\\Users\\丁丁\\Desktop\\延安精神_新关联分析.txt', "w")
print(ass_rule,file=f)
f.close()
'''
f = open(r'C:\\Users\\丁丁\\Desktop\\学生工作_新词组.txt', "w")
print(words_list,file=f)
f.close()