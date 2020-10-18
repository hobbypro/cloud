from wordcloud import WordCloud
from matplotlib import pyplot as plt

from morphological_tool.other.utils import default_font_path


class WordCloudDefaultView:
    def __init__(self, words):
        self._words = words
        self.wordcloud = self._default_wordcloud()

    @staticmethod
    def _default_wordcloud():
        return WordCloud(
            font_path=default_font_path()
        )

    def _generate_wordcloud(self):
        return self.wordcloud.generate(' '.join(self._words))

    def show(self):
        wc = self._generate_wordcloud()
        plt.imshow(wc)
        plt.show()

    def to_file(self, path):
        self._generate_wordcloud().to_file(path)
