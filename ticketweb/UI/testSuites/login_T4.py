from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import unittest


def fireFoxHeadless():
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.set_headless()
    driver = webdriver.Firefox(options=fireFoxOptions)
    return driver


def chromeHeadless():
    options = webdriver.ChromeOptions()
    options.set_headless()
# options.add_argument(‘--headless‘)
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
    return driver


def loginT4(driver,
            userName="alamMaster@ticketweb.com",
            password="111111",
            login_url='\
            https://ticketweb.com.tweb.twqa1.websys.tmcs/web-client/login.tw'):
    # driver = fireFoxHeadless()
    driver.get(login_url)
    driver.find_element_by_xpath("\
    	//*[@id=\"userName\"]").send_keys(userName)
    driver.find_element_by_xpath("\
    	//*[@id=\"password\"]").send_keys(password)
    driver.find_element_by_xpath("\
    	//*[@id=\"signIn\"]/span").click()
    time.sleep(5)
    return driver


def is_login_sucess(driver):
    try:
        text = driver.find_element_by_id("signOutId").text
        # print(text)
        driver.save_screenshot("./screenshot/is_login_sucess.png")
        return True
    except:
        return False


class Login(unittest.TestCase):

    def setUp(self):
        self.driver = fireFoxHeadless()
        # self.driver.implicitly_wait(30)

    def test_01(self):
        loginT4(self.driver)
        result = is_login_sucess(self.driver)
        self.driver.save_screenshot("./screenshot/T4_login.png")
        self.assertTrue(result)

    def test_02_invalid_user(self):
        loginT4(self.driver, userName="alamError@ticketweb.com")
        result = is_login_sucess(self.driver)
        self.driver.save_screenshot("./screenshot/T4_login_invalid_user.png")
        self.assertFalse(result)

    def test_03_invalid_password(self):
        loginT4(self.driver, password="222222")
        result = is_login_sucess(self.driver)
        self.driver.save_screenshot(
            "./screenshot/T4_login_invalid_password.png")
        self.assertFalse(result)

    def test_04_highUser(self):
        loginT4(self.driver, userName="alamH@ticketweb.com")
        result = is_login_sucess(self.driver)
        self.driver.save_screenshot("./screenshot/T4_login_highUser.png")
        self.assertTrue(result)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
