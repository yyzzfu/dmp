from selenium.webdriver.common.by import By


class HomePageLocator:

    #退出按钮
    logout_ele = (By.XPATH,  '//*[@id="toolbar"]//span[text()="退出"]')
    #展开我的资产按钮
    open_my_asset_ele = (By.XPATH, '//div[@node-id="010300"]/span[2]')
    #办公资产采购
    asset_offoice_buy = (By.XPATH, '//*[@node-id="010301"]//span[text()="办公资产采购"]')
