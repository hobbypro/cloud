import os
from morphological_tool.other.wordcloud_view import WordCloudDefaultView


def test_save_file_correctly(tmpdir):
    file = tmpdir.join('test.png')
    wcv = WordCloudDefaultView(['test', 'test2', 'test3'])
    wcv.to_file(file.strpath)
    assert os.path.exists(str(file))
