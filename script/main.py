import sys
import os
import shutil
import time
import pytest

# https://reqres.in/api-docs/#/
# https://httpbin.org/#/
# https://allurereport.org/docs/install-for-windows/

if __name__ == "__main__":
    report_dir = r'..\Reports'
    allure_dir = os.path.join(report_dir, 'allure-results')
    allure_dir = os.path.abspath(allure_dir)
    report_dir = os.path.abspath(report_dir)

    # 添加 common 模块所在的路径到 sys.path，否则pytest在终端运行时找不到common模块
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

    shutil.rmtree(allure_dir, True)
    pytest.main(["--reruns=0", "--reruns-delay=2", '--alluredir', allure_dir])
    os.system(f'allure generate "{allure_dir}" --clean --single-file --lang en --name "API Testing" -o "{report_dir}"')
    # os.system(f'allure open "{report_dir}"')
