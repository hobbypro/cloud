from pathlib import Path


def default_font_path():
    return str(Path(__file__).parent.parent.parent.joinpath('lib', 'fonts', 'ヒラギノ角ゴシック W6.ttc'))

