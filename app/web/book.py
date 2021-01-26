from flask import jsonify
from helper import is_isbn_or_key
from yushu_book import YuShuBook
from . import web

""" Blueprint 两个参数：蓝图名， 蓝图所在的模块名"""

@web.route('/book/search/<q>/<page>')
def search(q, page):
    """
    :param q: 普通关键字 or isbn
    :param page:
    :return:
    视图函数简洁易懂
    """
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    return jsonify(result)
    # return json.dumps(result), 200, {'content-type':'application/json'}