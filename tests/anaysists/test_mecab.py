from wordcloud_morphological.const.wordclass import VERB
from wordcloud_morphological.text_analysts.mecab import MecabTextAnalyst


def test_base_case():
    text_data = '私はおいしいカレーをいつも食べる'
    instance = MecabTextAnalyst(text_data)
    expected = ['私', 'おいしい', 'カレー', 'いつも', '食べる']
    assert instance.analyze_to_list() == expected


def test_twice_words():
    text_data = '猫と猫の喧嘩は激しい'
    instance = MecabTextAnalyst(text_data)
    expected = ['猫', '猫', '喧嘩', '激しい']
    assert instance.analyze_to_list() == expected


def test_only_one_wordclass():
    text_data = '私はおいしいカレーをいつも食べる'
    word_classes = [VERB]
    instance = MecabTextAnalyst(text_data, word_classes)
    expected = ['食べる']
    assert instance.analyze_to_list() == expected
