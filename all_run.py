# @dingzhihui   
# 2021/9/13   
# 6:36 下午   
# PyCharm
import os
import pytest

if __name__ == '__main__':
    pytest.main()
    # os.system('allure generate ../report/tmp -o ../report/allure_raw --clean')


"""
#allure生成报告的几种命令
1、生成测试报告数据
pytest test_food.py --alluredir ../report/tmp
2、测试报告在线预览
allure serve  ../report/tmp
3、测试报告本地静态数据生成
allure generate ../report/tmp -o ../report/html --clean

4、执行以test开头的测试用例
pytest -k"test"  --alluredir ../report/tmep  

"""