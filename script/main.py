import os
import shutil
import time
import pytest

# https://reqres.in/api-docs/#/
# https://httpbin.org/#/


if __name__ == "__main__":
    allure_dir = '../Reports/allure-results'
    report_dir = os.path.join("../Reports", time.strftime(r'%Y%m%d%H%M%S', time.localtime()).__str__())
    allure_dir = os.path.abspath(allure_dir)
    report_dir = os.path.abspath(report_dir)

    shutil.rmtree(allure_dir, True)
    pytest.main(["--reruns=0", "--reruns-delay=1", '--alluredir', allure_dir])
    os.system(f'allure generate "{allure_dir}" --clean --single-file --lang en --name "API Testing" -o "{report_dir}"')
    os.system(f'allure open "{report_dir}"')

