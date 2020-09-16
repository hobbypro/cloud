import MeCab


class MecabAnalyst:
    TARGET_WROD_CLASSes = ['動詞', '名詞', '副詞', '形容詞']

    def __init__(self):
        self.mecab = MeCab.Tagger("-Ochasen -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd/")

    def analyze(self, text):
        output = []
        node = self.mecab.parseToNode(text)
        while node:
            if node.feature.split(',')[0] in self.TARGET_WROD_CLASSes:
                output.append(node.surface)
            node = node.next
        return output
