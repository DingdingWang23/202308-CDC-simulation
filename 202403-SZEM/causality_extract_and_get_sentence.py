import re, jieba
import jieba.posseg as pseg
import pyltp
from pyltp import SentenceSplitter
import spacy
from fuzzywuzzy import fuzz
import gensim
from gensim.models import word2vec
import numpy as np
from scipy import spatial
import time
import os


class CausalityExractor():
    def __init__(self):
        pass

    '''1由果溯因配套式'''
    def ruler1(self, sentence):
        '''
        conm2:〈[之]所以,是因为〉、〈[之]所以,由于〉、 <[之]所以,缘于〉
        conm2_model:<Conj>{Effect},<Conj>{Cause}
        '''
        datas = list()
        word_pairs =[['之?所以', '是因为'], ['之?所以', '由于'], ['之?所以', '缘于'], ['的原因', '第一']]
        for word in word_pairs:
            pattern = re.compile(r'\s?(%s)/[p|c]+\s(.*)(%s)/[p|c]+\s(.*)' % (word[0], word[1]))
            result = pattern.findall(sentence)
            data = dict()
            if result:
                data['tag'] = result[0][0] + '-' + result[0][2]
                data['cause'] = result[0][3]
                data['effect'] = result[0][1]
                datas.append(data)
        if datas:
            return datas[0]
        else:
            return {}
    '''2由因到果配套式'''
    def ruler2(self, sentence):
        '''
        conm1:〈因为,从而〉、〈因为,为此〉、〈既[然],所以〉、〈因为,为此〉、〈由于,为此〉、〈只有|除非,才〉、〈由于,以至[于]>、〈既[然],却>、
        〈如果,那么|则〉、<由于,从而〉、<既[然],就〉、〈既[然],因此〉、〈如果,就〉、〈只要,就〉〈因为,所以〉、 <由于,于是〉、〈因为,因此〉、
         <由于,故〉、 〈因为,以致[于]〉、〈因为,因而〉、〈由于,因此〉、<因为,于是〉、〈由于,致使〉、〈因为,致使〉、〈由于,以致[于] >
         〈因为,故〉、〈因[为],以至[于]>,〈由于,所以〉、〈因为,故而〉、〈由于,因而〉
        conm1_model:<Conj>{Cause}, <Conj>{Effect}
        '''
        datas = list()
        word_pairs =[['因为', '从而'], ['因为', '为此'], ['既然?', '所以'],
                    ['因为', '为此'], ['由于', '为此'], ['除非', '才'],
                    ['只有', '才'], ['由于', '以至于?'], ['既然?', '却'],
                    ['如果', '那么'], ['如果', '则'], ['由于', '从而'],
                    ['既然?', '就'], ['既然?', '因此'], ['如果', '就'],
                    ['只要', '就'], ['因为', '所以'], ['由于', '于是'],
                    ['因为', '因此'], ['由于', '故'], ['因为', '以致于?'],
                    ['因为', '以致'], ['因为', '因而'], ['由于', '因此'],
                    ['因为', '于是'], ['由于', '致使'], ['因为', '致使'],
                    ['由于', '以致于?'], ['因为', '故'], ['因为?', '以至于?'],
                    ['由于', '所以'], ['因为', '故而'], ['由于', '因而'],['只有', '才能']]

        for word in word_pairs:
            pattern = re.compile(r'\s?(%s)/[p|c]+\s(.*)(%s)/[p|c]+\s(.*)' % (word[0], word[1]))
            result = pattern.findall(sentence)
            data = dict()
            if result:
                data['tag'] = result[0][0] + '-' + result[0][2]
                data['cause'] = result[0][1]
                data['effect'] = result[0][3]
                datas.append(data)
        if datas:
            return datas[0]
        else:
            return {}
    '''3由因到果居中式明确'''
    def ruler3(self, sentence):
        '''
        cons2:于是、所以、故、致使、以致[于]、因此、以至[于]、从而、因而
        cons2_model:{Cause},<Conj...>{Effect}
        '''

        pattern = re.compile(r'(.*)[,，]+.*(于是|所以|故|致使|以致于|因此|以至于|从而|因而|以此|以使|以促进|以更好)/[p|c]+\s(.*)')
        result = pattern.findall(sentence)
        data = dict()
        if result:
            data['tag'] = result[0][1]
            data['cause'] = result[0][0]
            data['effect'] = result[0][2]
        return data
    '''4由因到果居中式精确'''
    def ruler4(self, sentence):
        '''
        verb1:牵动、导向、使动、导致、勾起、指引、使、予以、产生、促成、造成、引导、造就、促使、酿成、
            引发、渗透、促进、引起、诱导、引来、促发、引致、诱发、推进、诱致、推动、招致、影响、致使、滋生、归于、
            使得、决定、攸关、令人、引出、浸染、挟带、触发、关系、渗入、诱惑、波及、诱使
        verb1_model:{Cause},<Verb|Adverb...>{Effect}
        # 删掉“作用”、“引入”
        '''
        pattern = re.compile(r'(.*)\s+(牵动|已致|导向|使动|导致|勾起|指引|使|予以|产生|促成|造成|引导|造就|促使|酿成|引发|渗透|促进|引起|诱导|引来|促发|引致|诱发|推进|诱致|推动|招致|影响|致使|以使|滋生|归于|使得|决定|攸关|令人|引出|浸染|挟带|触发|关系|渗入|诱惑|波及|诱使)/[d|v]+\s(.*)')
        result = pattern.findall(sentence)
        data = dict()
        if result:
            data['tag'] = result[0][1]
            data['cause'] = result[0][0]
            data['effect'] = result[0][2]
        return data
    '''5由因到果前端式模糊'''
    def ruler5(self, sentence):
        '''
        prep:为了、依据、为、按照、因[为]、按、依赖、照、比、凭借、由于
        prep_model:<Prep...>{Cause},{Effect}
        '''
        pattern = re.compile(r'\s?(既然|如果|只要|通过|根据|依据|按照|因为|因|按|依赖|凭借|由于|)/[p|c]+\s(.*)[,，]+(.*)')
        result = pattern.findall(sentence)

        data = dict()
        if result:
            data['tag'] = result[0][0]
            data['cause'] = result[0][1]
            data['effect'] = result[0][2]

        return data

    '''6由因到果居中式模糊'''
    def ruler6(self, sentence):
        '''
        adverb:以免、以便、为此、才
        adverb_model:{Cause},<Verb|Adverb...>{Effect}
        '''
        pattern = re.compile(r'(.*)[,，]?.*(需要|可以|有助于|以免|以便|为此|才)\s?(.*)')
        result = pattern.findall(sentence)
        data = dict()
        if result:
            data['tag'] = result[0][1]
            data['cause'] = result[0][0]
            data['effect'] = result[0][2]
        return data

    '''7由因到果前端式精确'''
    def ruler7(self, sentence):
        '''
        cons1:既[然]、因[为]、如果、由于、只要
        cons1_model:<Conj...>{Cause},{Effect}
        '''
        pattern = re.compile(r'\s?(既然|因|因为|如果|由于|只要)\s?(.*)[,，]+(.*)')
        result = pattern.findall(sentence)
        data = dict()
        if result:
            data['tag'] = result[0][0]
            data['cause'] = result[0][1]
            data['effect'] = result[0][2]
        return data
    '''8由果溯因居中式模糊'''
    def ruler8(self, sentence):
        '''
        3
        verb2:根源于、取决、来源于、出于、取决于、缘于、在于、出自、起源于、来自、发源于、发自、源于、根源于、立足[于]
        verb2_model:{Effect}<Prep...>{Cause}
        '''

        pattern = re.compile(r'(.*)(根源于|取决|来源于|出于|取决于|缘于|在于|出自|起源于|来自|发源于|发自|源于|根源于|立足|立足于)\s?(.*)')
        result = pattern.findall(sentence)
        data = dict()
        if result:
            data['tag'] = result[0][1]
            data['cause'] = result[0][2]
            data['effect'] = result[0][0]
        return data
    '''9由果溯因居端式精确'''
    def ruler9(self, sentence):
        '''
        cons3:因为、由于
        cons3_model:{Effect}<Conj...>{Cause}
        '''
        pattern = re.compile(r'(.*)是?\s?(因为|由于)/[p|c]+\s(.*)')
        result = pattern.findall(sentence)
        data = dict()
        if result:
            data['tag'] = result[0][1]
            data['cause'] = result[0][2]
            data['effect'] = result[0][0]

        return data

    '''抽取主函数'''
    def extract_triples(self, sentence):
        infos = list()
        if self.ruler1(sentence):
            infos.append(self.ruler1(sentence))
        elif self.ruler2(sentence):
            infos.append(self.ruler2(sentence))
        elif self.ruler3(sentence):
            infos.append(self.ruler3(sentence))
        elif self.ruler4(sentence):
            infos.append(self.ruler4(sentence))
        elif self.ruler5(sentence):
            infos.append(self.ruler5(sentence))
        elif self.ruler6(sentence):
            infos.append(self.ruler6(sentence))
        elif self.ruler7(sentence):
            infos.append(self.ruler7(sentence))
        elif self.ruler8(sentence):
            infos.append(self.ruler8(sentence))
        elif self.ruler9(sentence):
            infos.append(self.ruler9(sentence))

        return infos

    '''抽取主控函数'''
    def extract_main(self, content):
        sentences = self.process_content(content)
        datas = list()
        for sentence in sentences:
            subsents = self.fined_sentence(sentence)
            subsents.append(sentence)
            for sent in subsents:
                sent = ' '.join([word.word + '/' + word.flag for word in pseg.cut(sent)])
                result = self.extract_triples(sent)
                if result:
                    for data in result:
                        if data['tag'] and data['cause'] and data['effect']:
                            datas.append(data)
        return datas

    '''文章分句处理'''
    def process_content(self, content):
        return [sentence for sentence in SentenceSplitter.split(content) if sentence]

    '''切分最小句'''
    def fined_sentence(self, sentence):
        return re.split(r'[？！，；]', sentence)


def test(input_file,output_file):

    cause_list = []
    effect_list = []
    f = open(input_file, encoding='utf-8')
    f=f.readlines()
    f = ''.join(f)

    sentences = re.split(r"[。？：]", f)
    sentence_list = []

    for i, sentence in enumerate(sentences):
        sentence = sentence.strip()
        if sentence:
            sentence_list.append(sentence)

    extractor = CausalityExractor()

    file = open(output_file, 'w+')

    ctr = 0
    id_list = []
    for sentence in sentence_list:
        datas = extractor.extract_main(sentence)
        ctr += 1
        for data in datas:
            if datas:
                id_list.append(ctr)
            # print(ctr,file=file)
            # print('cause', ''.join([word.split('/')[0] for word in data['cause'].split(' ') if word.split('/')[0]]), file=file)
            cause_list.append(''.join([word.split('/')[0] for word in data['cause'].split(' ') if word.split('/')[0]]))
            # print('tag', data['tag'], file=file)
            # print('effect', ''.join([word.split('/')[0] for word in data['effect'].split(' ') if word.split('/')[0]]), file=file)
            effect_list.append(''.join([word.split('/')[0] for word in data['effect'].split(' ') if word.split('/')[0]]))

    file.close()
    return cause_list,effect_list,id_list


def fuzzy_match(sentences, list):

    max_phrase_list = []

    for sentence in sentences:
        sentence = nlp(sentence)
        new_sentence = ""

        for token in sentence:
            if token.pos_ != "SPACE" and token.is_stop == False:
                new_sentence = new_sentence + token.text

        similarities = []
        sentence = new_sentence

        for phrase in list:
            sim = fuzz.ratio(sentence,phrase)

            similarities.append((phrase, sim))

        sorted_similarities = sorted(similarities, key=lambda x: x[1], reverse=True)

        max_phrase_list.append(sorted_similarities[0][0])
        max_phrase_list.append(sorted_similarities[1][0])
        max_phrase_list.append(sorted_similarities[2][0])
        max_phrase_list.append(sorted_similarities[3][0])
        max_phrase_list.append(sorted_similarities[4][0])
        max_phrase_list.append(sorted_similarities[5][0])
        max_phrase_list.append(sorted_similarities[6][0])
        max_phrase_list.append(sorted_similarities[7][0])
        max_phrase_list.append(sorted_similarities[8][0])
        max_phrase_list.append(sorted_similarities[9][0])


    return max_phrase_list

nlp = spacy.load("zh_core_web_sm")

f = open(r"C:\\Users\\丁丁\\Desktop\\深圳演练\\nodelist.txt",encoding='utf-8')

node_list = []
for line in f.readlines():
    line = line.replace("\n", "")
    node_list.append(line)


input_folder = r"C:\Users\丁丁\Desktop\深圳演练\每个人讲的话"
output_folder_1 = r"C:\Users\丁丁\Desktop\深圳演练\因果对输出"
output_folder_2 = r"C:\Users\丁丁\Desktop\深圳演练\所有句子输出"

output_folder = r"C:\Users\丁丁\Desktop\深圳演练\output"

# 获取输入文件夹中的文件列表
file_list = os.listdir(input_folder)


for file_name in file_list:
    if file_name.endswith(".txt"):
        # 读取数据
        with open(os.path.join(input_folder, file_name), "r", encoding="utf-8") as f:
            data = f.read()
        if data == "":
            data = "此处应该有一句话。"

        input_file_path = os.path.join(input_folder, file_name)
        output_file_name = "causality_output_" + file_name
        output_file_path = os.path.join(output_folder, output_file_name)

        cause_list, effect_list, id_list = test(input_file_path, output_file_path)
        print("cause_list",cause_list)

        # 将文本分割为句子
        sentences = re.split(r"[。？：]", data)
        sentence_list = []
        for i, sentence in enumerate(sentences):
            sentence = sentence.strip()
            if sentence:
                sentence_list.append(sentence)

        # 其他操作...
        print(len(sentence_list))
        ctr = 0

        second_list = []
        total_sub_sentences = []

        for sentence in sentence_list:
            ctr += 1
            sub_sentences = re.split(r"，", sentence)
            total_sub_sentences += sub_sentences
            for sub_sentence in sub_sentences:
                second_list.append(ctr)
        print(second_list)
        print(total_sub_sentences)

        cause_phrase = fuzzy_match(cause_list, node_list)
        effect_phrase = fuzzy_match(effect_list, node_list)
        sentence_phrase = fuzzy_match(total_sub_sentences, node_list)

        # 生成输出文件路径
        base_name = os.path.splitext(file_name)[0]
        causality_output_file = os.path.join(output_folder_1, "causality_pair_" + base_name + ".tsv")
        all_sentence_output_file = os.path.join(output_folder_2, "all_sentence_" + base_name + ".tsv")


        # 打开输出文件并进行写入操作
        with open(causality_output_file, "w+", encoding="utf-8") as f:
            for i in range(2 * len(cause_phrase)):
                if (i % 20 == 0) or (i % 20 == 1) or (i % 20 == 2) or (i % 20 == 3) or (i % 20 == 4) or (
                        i % 20 == 5) or (i % 20 == 6) or (i % 20 == 7) or (i % 20 == 8) or (i % 20 == 9):
                    print(id_list[(i // 20)], "\t", cause_list[(i // 20)], "\t", cause_phrase[
                        ((i // 20) * 10 + (i % 20))], file=f)
                else:
                    print(id_list[(i // 20)], "\t", effect_list[(i // 20)], "\t", effect_phrase[
                        ((i // 20) * 10 + (i % 20) - 10)], file=f)

        with open(all_sentence_output_file, "w+", encoding="utf-8") as f:
            for i in range(len(sentence_phrase)):
                print(second_list[(i // 10)], "\t", total_sub_sentences[(i // 10)], "\t", sentence_phrase[i],
                      file=f)
