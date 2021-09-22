# @dingzhihui   
# 2021/9/20   
# 7:50 下午   
# PyCharm
import json

import pytest
import requests

import testCase
from commen.DateEncoder import DateEncoder
from commen.requests_url import SendRequestUrl
from commen.yaml_url import YamlUrl


class TestBossSalesTrend:
    # 类变量
    session = requests.session()

    @pytest.mark.parametrize("getBossSalesTrendInfo", YamlUrl().read_boss_sales_trend_yaml('get_boss_sales_trend.yml'))
    def test_boss_sales_trend(self, getBossSalesTrendInfo):
        print(str(getBossSalesTrendInfo) + "=============")
        data = getBossSalesTrendInfo['request']
        method = getBossSalesTrendInfo['request']['method']
        url = getBossSalesTrendInfo['request']['url']
        header = {"Content-type": "application/x-www-form-urlencoded"}
        result = SendRequestUrl().request_url(method, url, json.dumps(data, cls=DateEncoder), headers=header)
        # result = json.loads(result)
        print(result)


if __name__ == '__main__':
    pytest.main(['-vs', 'test_boss_sales_trend.py'])