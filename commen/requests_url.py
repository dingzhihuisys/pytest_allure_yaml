# @dingzhihui   
# 2021/5/31   
# 8:49 下午   
# PyCharm
import json

import requests


class SendRequestUrl:
    session = requests.session()

    def request_url(self, method, url, data, **kwargs):
        # print(method, url, data, **kwargs+"---------------")
        method = str(method).lower()
        if method == 'get':
            result = SendRequestUrl.session.request(method, url=url, params=data, **kwargs)
        else:
            # data = json.dumps(data)
            # print(data+"------")
            result = SendRequestUrl.session.request(method, url=url, data=data, **kwargs)
            # print(str(result.text)+"00000")
        return result.text


