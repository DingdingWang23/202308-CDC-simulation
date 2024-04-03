import re
import jieba
import jieba.posseg as pseg


class CausalityExtractor:
    def __init__(self):
        # 定义确定性和不确定性词语
        self.certain_causal_words = ['导致', '因为', '所以', '造成']
        self.uncertain_causal_words = ['可能', '或许', '假如', '有可能']
        # 预加载词典
        jieba.load_userdict(self.certain_causal_words + self.uncertain_causal_words)

    def classify_causality(self, sentence):
        """
        分类因果关系的确定性
        """
        words = pseg.cut(sentence)
        for word, flag in words:
            if word in self.certain_causal_words:
                return 'Certain'
            elif word in self.uncertain_causal_words:
                return 'Uncertain'
        return 'Unknown'

    def extract_causality(self, sentence):
        """
        抽取因果关系并分类其确定性
        """
        classification = self.classify_causality(sentence)
        return {'sentence': sentence, 'classification': classification}


# 示例
if __name__ == '__main__':
    extractor = CausalityExtractor()
    sentences = [
        '因为昨夜下大雨，所以街道积水严重。',
        '可能会下雨，所以带上伞。',
        '如果天气好，我们就去爬山。',
        '由于地震，许多建筑物倒塌。'
    ]

    for sentence in sentences:
        result = extractor.extract_causality(sentence)
        print(f"Sentence: {result['sentence']}\nClassification: {result['classification']}\n")

x