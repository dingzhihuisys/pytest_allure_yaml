# @dingzhihui   
# 2021/9/16   
# 2:03 下午   
# PyCharm
import json

import pytest
import requests

import testCase
from commen.requests_url import SendRequestUrl
from commen.yaml_url import YamlUrl


class TestMobileLogin:
    # 类变量
    session = requests.session()

    @pytest.mark.parametrize("getMobileLoginInfo", YamlUrl().read_mobile_login_yaml('get_mobile_login.yml'))
    def test_mobile_login(self, getMobileLoginInfo):
        print(str(getMobileLoginInfo)+"=============")
        method = getMobileLoginInfo['request']['method']
        url = getMobileLoginInfo['request']['url']
        data = getMobileLoginInfo['request']['data']
        header = {"Content-type": "application/x-www-form-urlencoded"}
        result = SendRequestUrl().request_url(method, url, data, headers=header)
        result = json.loads(result)
        print(result)


if __name__ == '__main__':
    pytest.main(['-vs', 'mobile_login.py'])
#     pytest.main()