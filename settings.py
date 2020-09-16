from pathlib import Path


# share
BASE_DIR = Path(__file__).parent

# cloud
WORDCLOUD_OUTPUT_DIR = Path.joinpath(BASE_DIR, 'var', 'wordclouds')
WORDCLOUD_DELIMITER = ' '


# twitter analsis_source settings
LIMIT_PULL_TWEETs = 1000


try:
    from .secret_settings import *
except ImportError:
    pass
