"""
TODO: word_classesの値検証をしたほうがいい
"""
import MeCab

from wordcloud_morphological.const.wordclass import ALL


class MecabTextAnalyst:
    """
    mecabによって、テキストを形態素分析で単語に分解するクラス
    """
    def __init__(self, text, word_classes=None):
        self._mecab = MeCab.Tagger("-Ochasen")
        self.text = text
        self._first_node = self._mecab.parseToNode(text)
        self.word_classes = word_classes if word_classes else ALL

    def analyze_to_list(self):
        output = []
        node = self._first_node
        while node:
            if node.feature.split(',')[0] in self.word_classes:
                output.append(node.surface)
            node = node.next
        return output
