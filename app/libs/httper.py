import requests

class HTTP:
    def get(self, url, return_json=True ):
        """
        :param url:
        :param return_json: 设置返回数据是否是json格式
        :return:
        """
        r = requests.get(url)
        """
        1.遵循RESTful
        2.返回json
        """
        if r.status_code != '200':
            return {} if return_json else ''
        return r.json() if return_json else r.text # python三元表达式

        # if r.status_code == '200':
        #     if return_json:
        #         return r.json()
        #     else:
        #         return r.text
        # else:
        #     if return_json:
        #         return {}
        #     else:
        #         return ''
