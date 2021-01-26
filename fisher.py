from app import create_app

"""
Flask 核心对象：app
"""

app = create_app()



if __name__ == '__main__':
    # 生产环境 nginx+uwsgi(web服务器)
    app.run(host='0.0.0.0', debug=app.config['DEBUG']) # 可以指定端口port=81