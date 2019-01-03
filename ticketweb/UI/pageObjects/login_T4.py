import sys
sys.path.append("..")
from framework.base_page import BasePage


class LoginPage(BasePage):
    findMethod = "xpath"
    input_userName = "//*[@id=\"userName\"]"
    input_passWord = "//*[@id=\"password\"]"
    button_login = "//*[@id=\"signIn\"]/span"

    def type_login_userName(self, text):
        self.type(self.findMethod, self.input_userName, text)

    def type_login_passWord(self, text):
        self.type(self.findMethod, self.input_passWord, text)

    def submit_btn(self):
        self.click(self.findMethod, self.button_login)


if __name__ == '__main__':
    from selenium import webdriver
    import sys
    sys.path.append("..")
    from framework.browser_engine import BrowserEngine

    driver = webdriver.Chrome()
    b = BrowserEngine(driver)
    # b.open_browser(driver)
    b.type_login_userName("alamMaster@ticketweb.com")
    b.type_login_passWord("111111")
    b.submit_btn()
