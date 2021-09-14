# @dingzhihui   
# 2021/5/31   
# 8:38 下午   
# PyCharm
import json

import pytest
import requests

import testCase
from commen.requests_url import SendRequestUrl
from commen.yaml_url import YamlUrl


class TestPassport:
    # 类变量
    session = requests.session()

    @pytest.mark.parametrize("getLoginInfo", YamlUrl().read_login_yaml('get_login.yml'))
    def test_passport(self, getLoginInfo):
        print(str(getLoginInfo)+"=============")
        method = getLoginInfo['request']['method']
        url = getLoginInfo['request']['url']
        data = getLoginInfo['request']['data']
        header = {"Content-type": "application/x-www-form-urlencoded"}
        result = SendRequestUrl().request_url(method, url, data, headers=header)
        result = json.loads(result)
        print(result)


if __name__ == '__main__':
    # pytest.main(['-vs', 'test_login.py'])
    pytest.main()