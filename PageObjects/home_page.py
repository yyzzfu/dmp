from Common.basepage import BasePage
from PageLocators.home_page_locators import HomePageLocator as loc
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Common import login

class HomePage(BasePage):

    def is_exist_logout_ele(self):
        #如果元素存在，则返回Ture
        try:
            doc = '首页'
            self.wait_eleVisible(loc.logout_ele, doc=doc)
            # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.logout_ele))
            return True
        except:
            return False

    def get_home_page_title(self):
        doc = '首页'
        return self.get_title(doc=doc)

    # def open_myAsset(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.open_my_asset_ele))
        self.driver.find_element(*loc.open_my_asset_ele).click()

    # def click_assetOfficeBuy(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.asset_offoice_buy))
        self.driver.find_element(*loc.asset_offoice_buy).click()


    #判断元素是否存在，存在则返回true，不存在则返回false
    def is_exist_ele(self, locator):
        try:
            # doc = '首页'
            self.wait_eleVisible(locator, times=3)
            # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.logout_ele))
            return True
        except:
            return False


    # 进入我的资产--办公资产采购
    def access_to_office_assets_buy(self):
        #1.展开--个人：判断是否已展开，未展开则点击，已展开则不进行点击

            #如果--》个人，已展开，则存在person_open_tag_ele元素
        person_open_tag_ele = (By.XPATH, '//div[@node-id="010000"]//span[@class="tree-icon tree-folder tree-folder-open"]')

            #展开--》个人，按钮元素定位
        person_open_button = (By.XPATH, '//*[@id="treeul"]//div[@node-id="010000"]/span[1]')
        # 展开--》我的资产，按钮元素定位
        my_assets_open_button = (By.XPATH, '//*[@id="treeul"]//div[@node-id="010300"]/span[2]')
        # 如果--》我的资产，已展开，则存在my_assets_open_tag_ele元素
        my_assets_open_tag_ele = (
        By.XPATH, '//div[@node-id="010300"]//span[@class="tree-icon tree-folder tree-folder-open"]')
        #办公资产采购定位元素
        office_assets_buy = (By.XPATH, '//div[@ node-id="010301"]//span[text()="办公资产采购"]')
        if self.is_exist_ele(person_open_tag_ele):
            doc = '我的资产展开'
            self.wait_eleVisible(my_assets_open_button)
            self.click_element(my_assets_open_button, doc=doc)
            if self.is_exist_ele(my_assets_open_tag_ele):
                doc = '点击办公资产采购'
                self.wait_eleVisible(office_assets_buy)
                self.click_element(office_assets_buy, doc=doc)
            else:
                doc = '我的资产展开'
                self.wait_eleVisible(my_assets_open_button)
                self.click_element(my_assets_open_button, doc=doc)
                doc = '点击办公资产采购'
                self.wait_eleVisible(office_assets_buy)
                self.click_element(office_assets_buy, doc=doc)
        else:
            doc = '个人展开'
            self.click_element(person_open_button, doc=doc)
            if self.is_exist_ele(my_assets_open_tag_ele):
                doc = '点击办公资产采购'
                self.click_element(office_assets_buy, doc=doc)
            else:
                doc = '我的资产展开'
                self.click_element(my_assets_open_button, doc=doc)
                doc = '点击办公资产采购'
                self.click_element(office_assets_buy, doc=doc)
        iframe = '010301'
        self.switch_iframe(iframe)
        office_assets_buy_apply = (By.XPATH, '//*[@id="tb"]//span[text()="办公资产采购申请"]')
        doc = '办公资产采购申请入口页面'
        self.wait_eleVisible(office_assets_buy_apply)
        js = 'setTimeout(function(){document.getElementsByClassName("easyui-linkbutton l-btn")[1].click()},1000)'
        self.execute_js(js, doc=doc)

        # self.wait_eleVisible(office_assets_buy_apply)
        # self.click_element(office_assets_buy_apply, doc=doc)
        time.sleep(1.5)
        self.switch_to_new_window()
        #请购部门下拉按钮定位元素
        apply_department_ele = (By.XPATH, './/*[@id="fwjl"]/tbody/tr[1]/td[2]/span/span/span[1]')
        doc = '展开请购部门下拉框'
        self.wait_eleVisible(apply_department_ele)
        self.click_element(apply_department_ele, doc=doc)
        #销售一部定位元素
        sale_one = (By.XPATH, '//div[@node-id="1034"]//span[text()="销售一部"]')
        doc = '选择部门'
        self.wait_eleVisible(sale_one)
        self.click_element(sale_one, doc=doc)


        #2.展开--我的资产：判断是否已展开，未展开则点击，已展开则不进行点击
            # 如果--》我的资产，已展开，则存在my_assets_open_tag_ele元素
        my_assets_open_tag_ele = (By.XPATH, '//div[@node-id="010300"]//span[@class="tree-icon tree-folder tree-folder-open"]')

            # 展开--》我的资产，按钮元素定位
        my_assets_open_button = (By.XPATH, '//*[@id="treeul"]//div[@node-id="010300"]/span[2]')
        # doc = '首页--我的资产展开按钮元素'
        # if not self.is_exist_ele(my_assets_open_tag_ele):
        #     self.click_element(my_assets_open_button, doc=doc)

    #3.点击--办公资产采购

    #4.切换iframe到新打开的页面

    #进入我的资产--项目设备采购


if __name__ == '__main__':

    driver = webdriver.Firefox()
    driver.get('http://127.0.0.1:7001/dmp')
    hp = HomePage(driver)
    login.login_sucess(driver)
    hp.access_to_office_assets_buy()





    '''
    person_open_tag_ele = (By.XPATH, '//div[@node-id="010000"]//span[@class="tree-icon tree-folder tree-folder-open"]')
    # ele = WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(person_open_tag_ele))
    time.sleep(1)
    ele = WebDriverWait(driver, 10).until(EC.visibility_of(driver.find_element(*person_open_tag_ele)))
    print(ele)
    print('----------------')
    time.sleep(1)
    my_assets_open_tag_ele = (By.XPATH, '//div[@node-id="010300"]//span[@class="tree-icon tree-folder tree-folder-open"]')
    # ele = WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(my_assets_open_tag_ele))
    ele = WebDriverWait(driver, 10).until(EC.visibility_of(driver.find_element(*my_assets_open_tag_ele)))
    print(ele)
    '''
