# @dingzhihui   
# 2021/9/20   
# 9:31 下午   
# PyCharm
import json

import pytest
import requests

import testCase
from commen.DateEncoder import DateEncoder
from commen.requests_url import SendRequestUrl
from commen.yaml_url import YamlUrl


class TestBossEatType:
    # 类变量
    session = requests.session()

    @pytest.mark.parametrize("getBossEatTypeInfo", YamlUrl().read_boss_sales_trend_yaml('get_boss_eat_type.yml'))
    def test_boss_eat_type(self, getBossEatTypeInfo):
        print(str(getBossEatTypeInfo) + "=============")
        data = getBossEatTypeInfo['request']
        method = getBossEatTypeInfo['request']['method']
        url = getBossEatTypeInfo['request']['url']
        header = {"Content-type": "application/x-www-form-urlencoded"}
        result = SendRequestUrl().request_url(method, url, json.dumps(data, cls=DateEncoder), headers=header)
        # result = json.loads(result)
        print(result)


if __name__ == '__main__':
    pytest.main(['-vs', 'test_boss_eat_type.py'])