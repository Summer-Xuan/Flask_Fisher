
def is_isbn_or_key(word):
    """
    :param word: 搜索词
    :return: 返回搜索关键词的类型（isbn或者关键词）
    判断搜索词的类型
    """
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('_','')
    if '_' in short_word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key