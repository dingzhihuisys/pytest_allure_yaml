# @dingzhihui   
# 2021/9/20   
# 1:03 下午   
# PyCharm
import json

import pytest
import requests

import testCase
from commen.DateEncoder import DateEncoder
from commen.requests_url import SendRequestUrl
from commen.yaml_url import YamlUrl


class TestBossApi:
    # 类变量
    session = requests.session()

    @pytest.mark.parametrize("getBossKpiInfo", YamlUrl().read_boss_api_yaml('get_boss_api.yml'))
    def test_boss_api(self, getBossKpiInfo):
        print(str(getBossKpiInfo)+"=============")
        data = getBossKpiInfo['request']
        method = getBossKpiInfo['request']['method']
        url = getBossKpiInfo['request']['url']
        header = {"Content-type": "application/x-www-form-urlencoded"}
        result = SendRequestUrl().request_url(method, url, json.dumps(data, cls=DateEncoder), headers=header)
        # result = json.loads(result)
        print(result)


if __name__ == '__main__':
    pytest.main(['-vs', 'test_boss_kpi.py'])
# #     pytest.main()