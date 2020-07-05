from PageObjects.login_page import LoginPage
from TestDatas import login_datas as LD
from selenium import webdriver


def login_sucess(driver):
    lg = LoginPage(driver)
    code = lg.code_image_to_text()
    lg.login(LD.sucess_data['username'], LD.sucess_data['password'], code)
    if lg.get_title() != '日常事务管理平台':
        lg.clear_username_input()
        lg.clear_password_input()
        lg.clear_code_input()
        login_sucess(driver)


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get('http://127.0.0.1:7001/dmp')
    login_sucess(driver)
