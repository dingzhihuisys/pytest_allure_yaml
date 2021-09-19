# @dingzhihui   
# 2021/6/1   
# 2:44 下午   
# PyCharm
import os
import yaml
class YamlUrl:
    # 获取get_login.yaml内容
    def read_login_yaml(self, yaml_name):
        # 反序列化 ：yaml转dict格式
        with open('/Users/dingzhihui/dzh_test/PycharmProjects/hq_pytest_allure/testCase/test_hq_passport/'+yaml_name, mode='r', encoding='utf-8')as f:
            # print(os.getcwd()+'/'+yaml_name)
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value

    # 写入get_login.yaml内容
    def write_token_yaml(self, yaml_name):
        with open('/Users/dingzhihui/dzh_test/PycharmProjects/hq_pytest_allure/commen/yaml_url.py', mode='r', encoding='utf-8')as f:
            # print(os.getcwd()+'/'+yaml_name)
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value

    # 获取get_mobile_login.yaml内容
    def read_mobile_login_yaml(self, yaml_name):
        # 反序列化 ：yaml转dict格式
        with open('/Users/dingzhihui/dzh_test/PycharmProjects/hq_pytest_allure/testCase/test_mobile_member/'+yaml_name, mode='r', encoding='utf-8')as f:
            # print(os.getcwd()+'/'+yaml_name)
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value