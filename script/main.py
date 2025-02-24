import sys
import os
import pytest

# https://reqres.in/api-docs/#/
# https://httpbin.org/#/
# https://allurereport.org/docs/install-for-windows/

if __name__ == "__main__":
    report_dir = r'..\Reports'
    allure_dir = os.path.join(report_dir, 'allure-results')
    report_dir = os.path.abspath(os.path.join(report_dir, 'allure-report'))
    allure_dir = os.path.abspath(allure_dir)

    # 添加 common 模块所在的路径到 sys.path，否则pytest在终端运行时找不到common模块
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

    pytest.main(["--reruns=0", "--reruns-delay=2", '--alluredir', allure_dir])
    os.system(f'allure generate "{allure_dir}" '
              f'--report-dir "{report_dir}" '
              f'--name "API Testing" '
              f'--clean --single-file --lang en')
