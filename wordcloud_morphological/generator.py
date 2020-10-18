from wordcloud import WordCloud
import matplotlib.pyplot as plt


class WordCloudGenerator:
    def __init__(self):
        self.morphological_analyst = None
        self.sources = set()

    def generate(self):
        words = []
        for source in self.sources:
            words.extend(self.morphological_analyst.analyze(source.pull()))
        text = WORDCLOUD_DELIMITER.join(words)
        wordcloud = WordCloud(font_path="System/Library/Fonts/ヒラギノ角ゴシック W4.ttc",
                              background_color="black").generate(text)
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.show()

    def set_morphological_analyst(self, morphological_analyst):
        self.morphological_analyst = morphological_analyst

    def add_source(self, source):
        self.sources.add(source)


if __name__ == '__main__':
    from cloud.morphological_analysts.mecab import MecabAnalyst
    from cloud.analsis_source.tweets import SearchedRecentTweetsSource

    generator = WordCloudGenerator()
    generator.set_morphological_analyst(MecabAnalyst())
    generator.add_source(SearchedRecentTweetsSource("ネットプロテクションズ"))
    generator.generate()
