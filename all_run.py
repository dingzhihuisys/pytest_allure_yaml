# @dingzhihui   
# 2021/9/13   
# 6:36 下午   
# PyCharm
import os
import pytest
if __name__ == '__main__':
    pytest.main()
    os.system('allure generate ./temp -o ./report --clean')