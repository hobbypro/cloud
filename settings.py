from pathlib import Path


# share
BASE_DIR = Path(__file__).parent

# wordcloud-morphological
WORDCLOUD_OUTPUT_DIR = Path.joinpath(BASE_DIR, 'var', 'wordclouds')
WORDCLOUD_DELIMITER = ' '
