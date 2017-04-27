# -*- coding: utf-8-*-
import os
import unittest
from appium import webdriver
from time import sleep
class DemoTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = '2a22cee'
        #可以在这里进行相关参数配置
        desired_caps['appPackage'] = ''
        desired_caps['appActivity'] = ''
        #此处可配置Appium服务的地址，本例的服务端为本机
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
    def tearDown(self):
        self.driver.quit()
    def test_login(self):
        #首次打开app的时候一般都会有广告展示，我们等待5s
        sleep(10)
        #通过点击底部菜单“资产”跳转打登录界面
        self.driver.find_element_by_id(id_="tab_center_layout").click()
        #输入用户名及密码进行登录操作
        #第一步就是把这些元素都找到
        el_username = self.driver.find_element_by_id(id_="userName")
        self.driver.find_element_by_id(id_="tab_center_layout").click()
        el_username.clear()
        el_username.click()
        el_username.send_keys("xxxxx")
        el_username.is_selected()
        el_username.is_displayed()
        el_username.is_enabled()
        el_username.text
        el_password = self.driver.find_element_by_id(id_="userPwd")
        #找到之后就是对这些元素进行对应的动作，例如输入 、点击 等等
        #el_username.send_keys("13716983483")
        sleep(3)
        na = self.driver.find_elements_by_name(name="请输入手机号/黄金卡号")
        for i in na:
            i.click()
            i.send_keys("13716983483")
        el_password.send_keys("qwer1234")
        sleep(4)
        #当然你也可以这么写 self.driver.find_element_by_id(id_="userPwd").send_keys("naonao0314")
        #点击登录按钮
        self.driver.find_element_by_id(id_="submitbtn").click()
        sleep(5)
        #我们需要检查下是否登录成功，就是我们用例中的预期结果验证
        try:
            self.driver.find_element_by_id(id_="member_id2")
            actual = True
        except:
            actual = False
        self.assertEquals(actual,True,"登录失败！")
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(DemoTests)
    unittest.TextTestRunner(verbosity=2).run(suite)



