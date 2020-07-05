from selenium import webdriver
import re
from PageLocators.login_page_locators import LoginPageLocator as loc
from Common.basepage import BasePage
from aip import AipOcr
from PIL import Image
from Common import dir_config
import time

""" 你的 APPID AK SK """
config = {
    "appId": '20367335',
    "apiKey": 'wfXUvEBDyQT87der31X0i6L6',
    "secretKey": 'WeCD7QoGG4oIRrZrWFAv1Gaig05KqbM4'
}

client = AipOcr(**config)


class LoginPage(BasePage):

    def login(self, username, password, code):
        doc = '登录页面_登录操作'
        self.wait_eleVisible(loc.username_ele, doc=doc)
        self.input_text(loc.username_ele, username, doc=doc)
        self.wait_eleVisible(loc.password_ele, doc=doc)
        self.input_text(loc.password_ele, password, doc=doc)
        self.wait_eleVisible(loc.code_ele, doc=doc)
        self.input_text(loc.code_ele, code, doc=doc)
        # time.sleep(10)
        self.wait_eleVisible(loc.click_button, doc=doc)
        self.click_element(loc.click_button, doc=doc)

    def get_code_error_msg(self):
        doc = '登录页面'
        self.wait_eleVisible(loc.error_msg_ele, doc=doc)
        return self.get_text(loc.error_msg_ele, doc=doc)
        #获取错误提示信息
        # WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.error_msg_ele))
        # return self.driver.find_element(*loc.error_msg_ele).text

    def clear_username_input(self):
        doc = '登录页面'
        self.wait_eleVisible(loc.username_ele, doc=doc)
        self.clear_input(loc.username_ele, doc=doc)
        # WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.username_ele))
        # self.driver.find_element(*loc.username_ele).clear()

    def clear_password_input(self):
        doc = '登录页面'
        self.wait_eleVisible(loc.password_ele, doc=doc)
        self.clear_input(loc.password_ele, doc=doc)
        # WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.password_ele))
        # self.driver.find_element(*loc.password_ele).clear()

    def clear_code_input(self):
        doc = '登录页面'
        self.wait_eleVisible(loc.code_ele, doc=doc)
        self.clear_input(loc.code_ele, doc=doc)
        # WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.code_ele))
        # self.driver.find_element(*loc.code_ele).clear()

    def code_image_to_text(self, file_name=None):
        if file_name == None:
            file_name = dir_config.code_picture_dir + "/code.png"
            # file_name = 'F:\DMP_test\code.png'
        self.driver.save_screenshot(file_name)
        code_element = self.driver.find_element_by_id('authImg')
        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width'] + left
        height = code_element.size['height'] + top
        im = Image.open(file_name)
        img = im.crop((left, top, right, height))
        img.save(file_name)
        img = Image.open(file_name)
        # 模式L”为灰色图像
        img = img.convert('L')
        img.save(file_name)
        text = self.get_image_str(file_name)
        code_text = (re.findall(r'[a-zA-Z0-9]', text))
        text = ''.join(code_text)
        return text
        # if text is None:
        #     time.sleep(0.5)
        #     self.driver.refresh()
        #     time.sleep(0.5)
        #     self.code_image_to_text()
        # elif len(text) == 4:
        #     return text
        # else:
        #     time.sleep(0.5)
        #     self.driver.refresh()
        #     time.sleep(0.5)
        #     self.code_image_to_text()


    """ 读取图片 """
    def get_file_content(self, image_path):
        with open(image_path, 'rb') as fp:
            return fp.read()

    def get_image_str(self, image_path):
        image = self.get_file_content(image_path)
        """ 调用通用文字识别, 图片参数为本地图片 """
        result = client.basicGeneral(image)

    #结果拼接返回输出
        if 'words_result' in result:
            return ''.join([w['words'] for w in result['words_result']])






if __name__ == '__main__':

    driver = webdriver.Firefox()
    driver.get('http://127.0.0.1:7001/dmp')
    a = LoginPage(driver)
    code = a.code_image_to_text()
    a.login('lixiao', 'FU123456', code)
    driver.quit()
