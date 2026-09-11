import shutil#文件复制工具
import pytest#自动化测试框架
import os#操作系统命令调用，路径处理
import webbrowser#自动打开浏览器
from conf.setting import REPORT_TYPE#从配置文件`conf/setting.py`读取报告类型变量，取值一般是`allure`或者`tm`

if __name__ == '__main__':

    if REPORT_TYPE == 'allure':
        pytest.main(
            ['-s', '-v', '--alluredir=./report/temp', './testcase', '--clean-alluredir',
             '--junitxml=./report/results.xml'])

        shutil.copy('./environment.xml', './report/temp')
        os.system(f'allure serve ./report/temp')

    elif REPORT_TYPE == 'tm':
        pytest.main(['-vs', '--pytest-tmreport-name=testReport.html', '--pytest-tmreport-path=./report/tmreport'])
        webbrowser.open_new_tab(os.getcwd() + '/report/tmreport/testReport.html')
