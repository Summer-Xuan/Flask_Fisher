from flask import Flask, make_response
# from config import DEBUG


app = Flask(__name__)
app.config.from_object('config') # flask导入文件
# print(app.config['DEBUG']) #app.config['DEBUG']字典子类

@app.route('/book/search/<q>/<page>')
def search():
    """
    q&isbn:普通关键字和isbn
    page：start count

    """
    isbn_or_key = 'key'
    if len(q) == 13 and q.isdigit():
        isbn_or_key = 'isbn'
    short_q = q.replace('_','')
    if '_' in q and len(short_q) == 10 and short_q.isdigit():
        isbn_or_key = 'isbn'




if __name__ == '__main__':
    # 生产环境 nginx+uwsgi(web服务器)
    app.run(host='0.0.0.0', debug=app.config['DEBUG']) # 可以指定端口port=81