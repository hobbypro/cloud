from morphological_tool.analysts.mecab import MecabAnalyst


def analyze_to_words(text, analyst_name='mecab'):
    analysts = {'mecab': MecabAnalyst}
    if analysts not in analysts:
        raise ValueError(f'the analyst does not exist: analyst_name: {analyst_name}')
    analyst = analysts[analyst_name](text)
    return analyst.to_words()
