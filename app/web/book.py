from flask import jsonify, request
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from . import web
from app.forms.book import SearchForm

""" Blueprint 两个参数：蓝图名， 蓝图所在的模块名"""

@web.route('/book/search/')
def search(q, page):
    """
    :param q: 普通关键字 or isbn
    :param page:
    :return:
    ?q=金庸&page=1
    """
    # Request(直接从flask中导入request) Response(导入make_response())
    #
    # 例：查询参数args POST参数 remote ip
    isbn_or_key = is_isbn_or_key(q)

    # q,page为不可变字典 request.args.to_dict()-->将不可变字典转为可变字典
    # q = request.args['q']
    # page = request.args['page']
    # 验证层
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q, page)
        return jsonify(result)
    else:
        return jsonify(form.errors)
    # return json.dumps(result), 200, {'content-type':'application/json'}