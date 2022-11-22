import time
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By

from captcha_pass.captcha_bypass import capcha_bypass

class VisaBot():
    def __init__(self):
        # for linux server
        # self.display = Display(visible=0, size=(800, 600))
        # self.display.start()

        opts = uc.ChromeOptions()
        opts.add_argument('--proxy-server=193.23.50.186:10289')
        self.driver = uc.Chrome(options=opts)
        self.auth_link = None
        print('bot started to work')

    def get_book_link(self):
        website = 'https://visa.vfsglobal.com/blr/en/pol/book-an-appointment'

        # checking ip
        website1 = 'https://2ip.ru'
        self.driver.get(website)
        time.sleep(20)
        print('get vfsglobal.com')
        book_now = self.driver.find_element(By.CLASS_NAME, 'lets-get-started').get_attribute('href')
        self.auth_link = book_now
        self.driver.get(book_now)
        time.sleep(30)

    def auth(self):
        mail = 'artem.yevtukhovich.91@bk.ru'
        psd = 'Megapolis77@'
        login = self.driver.find_element(By.NAME,'EmailId')
        login.send_keys(mail)
        password = self.driver.find_element(By.NAME,'Password')
        password.send_keys(psd)
        capcha_bypass(self.driver,self.auth_link, '193.23.50.186:10289')
        self.driver.find_element(By.ID,'btnSubmit').click()
        time.sleep(20)

    def logout(self):
        logout_action = self.driver.find_element(By.XPATH,'//*[@id="logoutForm"]/a')
        self.driver.get(logout_action.get_attribute('href'))
        print('logout from account')


    def quite(self):
        self.driver.close()
        # for linux server
        # self.display.stop()


