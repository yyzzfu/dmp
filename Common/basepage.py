# 封装基本函数：执行日志、遗产处理、失败截图
# 所有页面的公共部分
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
from Common import dir_config
import time
from Common.my_log import MyLog


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.log = MyLog()

    # 等待元素可见
    def wait_eleVisible(self, locator, times=20, poll_frequency=0.5, doc=''):
        '''
        :param locator: 元素定位方式，元祖类型，如（BY.XPATH, XPTAH定位表达式）
        :param times: 最长等待时间
        :param poll_frequency: 多长时间查询一次
        :param doc: 操作的具体页面，doc的值传给except中的截图函数
        :return:
        '''
        self.log.info('{0}-->等待元素:{1}可见'.format(doc, locator))
        try:
            start = datetime.datetime.now()
            WebDriverWait(self.driver, times, poll_frequency).until(EC.visibility_of_element_located(locator))
            end = datetime.datetime.now()
            wait_times = (end - start).seconds
            self.log.info('{0}-->元素:{1}-->已可见，等待时长为{2}秒'.format(doc, locator, wait_times))
        except:
            self.log.error('等待元素可见失败！')
            # 截图
            self.save_screen_picture(doc)
            raise

    # 截图
    def save_screen_picture(self, doc):
        '''
        :param doc: 当前操作的页面，如登录页面
        :return: None
        '''
        # 图片名称：页面名称_操作名称_时间.png
        file_name = dir_config.screenshot_dir + \
                    "/{0}_{1}.png".format(doc, time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time())))
        try:
            self.driver.save_screenshot(file_name)
            self.log.info('截图成功，存放路径为：{}'.format(file_name))
        except:
            self.log.error('截图失败')
            raise

    # 等待元素存在
    def wait_elePresence(self):
        pass

    #判断元素是否不存在与DOM树里面或不可见
    def invisibility_of_ele(self, locator, times=5, poll_frequency=0.5, doc=''):
        try:
            WebDriverWait(self.driver, times, poll_frequency).until(EC.invisibility_of_element_located(locator))
            self.log.info('{0}元素{1}不存在'.format(doc, locator))
        except:
            self.log.error('元素{}存在'.format(locator))

    # 查找元素
    def get_element(self, locator, doc=''):
        try:
            return self.driver.find_element(*locator)
        except:
            self.log.error('查找元素失败')
            self.save_screen_picture(doc)
            raise

    # 点击操作
    def click_element(self, locator, doc=''):
        ele = self.get_element(locator)
        self.log.info('{0}-->点击元素:{1}'.format(doc, locator))
        try:
            ele.click()
        except:
            self.log.error('点击元素失败')
            self.save_screen_picture(doc)
            raise

    # 输入操作
    def input_text(self, locator, text, doc=''):
        ele = self.get_element(locator, doc)
        self.log.info('在{0}-->元素：{1}进行输入操作'.format(doc, locator))
        try:
            ele.send_keys(text)
            self.log.info('输入的值为-->{}'.format(text))
        except:
            self.log.error('输入失败')
            self.save_screen_picture(doc)
            raise

    # 获取元素的文本内容
    def get_text(self, locator, doc=''):
        ele = self.get_element(locator, doc)
        self.log.info('在{0}-->获取元素:{1}的文本内容'.format(doc, locator))
        try:
            self.log.info('获取到的元素文本内容为-->{}'.format(ele.text))
            return ele.text
        except:
            self.log.error('获取元素文本内容失败')
            self.save_screen_picture(doc)
            raise

    #清空输入框
    def clear_input(self, locator, doc=''):
        ele = self.get_element(locator, doc)
        try:
            self.log.info('在{0}-->清空元素(**输入框**)：{1}中的内容'.format(doc, locator))
            ele.clear()
        except:
            self.log.error('清空输入框失败')
            raise

    #获取title
    def get_title(self):
        self.log.info('获取页面的title')
        try:
            self.log.info('在页面获取到的title是-->{}'.format(self.driver.title))
            return self.driver.title
        except:
            self.log.error('获取页面的title失败！')

    # 获取元素的属性
    def get_element_attribute(self):
        pass

    # alert处理
    def alert_action(self, action='accept'):
        pass

    # iframe切换
    def switch_iframe(self, iframe_ele):
        try:
            self.driver.switch_to.frame(iframe_ele)
            self.log.info('已切换到{}iframe'.format(iframe_ele))
        except:
            self.log.error('切换iframe失败')

    #窗口切换--切换到最新的窗口
    def switch_to_new_window(self):
        self.log.info('切换到最新的窗口')
        try:
            self.all_h = self.driver.window_handles
            self.driver.switch_to.window(self.all_h[-1])
            self.log.info('已成功切换到最新的窗口！！！')
        except:
            self.log.error('切换到最新的窗口失败！！！')

    # 上传操作
    def upload_file(self):
        pass


    #执行JS
    def execute_js(self, js, doc=''):
        self.log.info('在{}通过js执行点击'.format(doc))
        try:
            self.driver.execute_script(js)
            self.log.info('在{}通过js执行点击-->成功！！！'.format(doc))
        except:
            self.log.error('在{}执行js点击失败'.format(doc))

# 滚动条处理