import os
import shutil

os.system('pytest --alluredir=allure-results')
os.system('allure generate allure-results --clean -o allure-reports')
os.popen('allure open allure-reports')

shutil.rmtree('allure-results')