# 1）在run_main.py中执行../test_cases/test1.py
"""import os


os.system('python ../test_cases/test1.py')"""

# 2）main调用（此时未引入pytest）
"""import os
from test_cases.test2 import TestOne


def main():
    o = TestOne()
    o.test_get_inventory()
    o.test_post_order()
    o.test_get_store_order()


if __name__ == '__main__':
    main()
    print(os.path.abspath(__file__))"""

# 3）main调用（引入pytest）
"""import pytest
import os

if __name__ == '__main__':
    pytest.main(['-vs', '../test_cases/test_swagger1.py', '--clean-alluredir', '--alluredir', '../output/report/allure_data'])
    os.system('allure generate ../output/report/allure_data -o ../output/report/allure_report --clean')
    # os.system('allure open ../output/report/allure_report')"""

# 4）main调用（测试文件为类）
import pytest
import os
import subprocess


if __name__ == '__main__':
    pytest.main(['-vs', '../test_cases/test_swagger_allure.py', '--clean-alluredir','--alluredir', '../output/report/allure_data'])
    # print(os.getcwd())
    subprocess.run("call " + "copy ..\\output\\environment.properties ..\\output\\report\\allure_data\\", shell=True)   # 仅支持win
    os.system('allure generate ../output/report/allure_data -o ../output/report/allure_report --clean')
