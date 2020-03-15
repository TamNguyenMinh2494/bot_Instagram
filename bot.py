import time
from selenium import webdriver

chrome_dir = 'C:/Program Files (x86)/Google/Chrome/chromedriver'

class Bot():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.base_url = 'https://instagram.com/'
        self.nav_url = 'https://instagram.com/{}/'
        self.driver = webdriver.Chrome(chrome_dir)
        self.login()
    def login(self):
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_name("username").send_keys(self.username)
        self.driver.find_element_by_name("password").send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]').click()
    def nav_user(self, user):
        self.driver.get(self.nav_url.format(user))

if __name__ == '__main__':
    bot = Bot('user', 'password')
    bot.nav_user('sontungmtp')