from selenium.webdriver.common.by import By


class LoginPageLocator:

    username_ele = (By.ID, 'j_username')
    password_ele = (By.ID, 'j_password')
    code_ele = (By.ID, 'vercode')
    click_button = (By.ID, 'submitBtn')
    error_msg_ele = (By.ID, 'error')
