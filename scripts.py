"""
status code 200,401,301
content-type http headers
content-type = text/html （默认值）
视图函数返回的本质是一个Response对象
web返回的本质都是字符串，可以是json格式的字符串
response = make_response("<html></html>",301)
response.headers = headers
"""
@app.route('/hello')
def hello():

    headers = {
        'content-type':'text/plain',
        'location':'http://www.bing.com'
    }


    return "<html></html>",301,headers # 这种方式常用,相对于使用make_response