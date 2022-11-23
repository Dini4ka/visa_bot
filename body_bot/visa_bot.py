import time
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from captcha_pass.captcha_bypass import capcha_bypass
from get_data import proxy


class VisaBot:
    def __init__(self, proxy, data):
        # for linux server
        # self.display = Display(visible=0, size=(800, 600))
        # self.display.start()
        self.proxy = proxy
        self.data = data
        opts = uc.ChromeOptions()
        opts.add_argument(f'--proxy-server={self.proxy}')
        self.driver = uc.Chrome(options=opts)
        self.auth_link = None
        print('bot started to work')

    def get_new_data(self, data):
        self.data = data
        print('new data was get')


    def get_book_link(self):
        website = 'https://visa.vfsglobal.com/blr/ru/pol/book-an-appointment'

        # checking ip
        website1 = 'https://2ip.ru'
        self.driver.get(website)
        time.sleep(20)
        print('get vfsglobal.com')
        book_now = self.driver.find_element(By.CLASS_NAME, 'lets-get-started').get_attribute('href')
        self.auth_link = book_now
        self.driver.get(book_now)
        while self.driver.title == 'Just a moment...':
            time.sleep(5)
            self.driver.get(book_now)
            time.sleep(5)

    def auth(self):
        print(self.driver.title)
        mail = self.data['mail']
        psd = self.data['password']
        login = self.driver.find_element(By.NAME, 'EmailId')
        login.send_keys(mail)
        password = self.driver.find_element(By.NAME, 'Password')
        password.send_keys(psd)
        try:
            capcha_bypass(self.driver, self.auth_link, self.proxy)
            while self.driver.title == 'Just a moment...':
                self.driver.refresh()
                time.sleep(5)
        except:
            self.driver.refresh()
            time.sleep(10)
            mail = self.data['mail']
            psd = self.data['password']
            login = self.driver.find_element(By.NAME, 'EmailId')
            login.send_keys(mail)
            password = self.driver.find_element(By.NAME, 'Password')
            password.send_keys(psd)
            capcha_bypass(self.driver, self.auth_link, self.proxy)
            while self.driver.title == 'Just a moment...':
                self.driver.refresh()
                time.sleep(5)
        self.driver.find_element(By.ID, 'btnSubmit').click()
        time.sleep(15)
        while self.driver.title == 'Just a moment...':
            self.driver.refresh()
            time.sleep(5)
        while str(self.driver.title) == 'VFS : Registered Login':
            login = self.driver.find_element(By.NAME, 'EmailId')
            login.send_keys(mail)
            password = self.driver.find_element(By.NAME, 'Password')
            password.send_keys(psd)
            try:
                capcha_bypass(self.driver, self.auth_link, self.proxy)
                while self.driver.title == 'Just a moment...':
                    self.driver.refresh()
                    time.sleep(5)
            except:
                self.driver.refresh()
                time.sleep(10)
                mail = self.data['mail']
                psd = self.data['password']
                login = self.driver.find_element(By.NAME, 'EmailId')
                login.send_keys(mail)
                password = self.driver.find_element(By.NAME, 'Password')
                password.send_keys(psd)
                capcha_bypass(self.driver, self.auth_link, self.proxy)
                sleep(5)
                while self.driver.title == 'Just a moment...':
                    self.driver.refresh()
                    time.sleep(5)
            self.driver.find_element(By.ID, 'btnSubmit').click()
            time.sleep(10)
            while self.driver.title == 'Just a moment...':
                self.driver.refresh()

    def put_data(self,personal_documents):
        registration_for_submition = self.driver.find_elements(By.CLASS_NAME,'inactive-link')[0].find_element(By.TAG_NAME,'a').get_attribute('href')
        print(registration_for_submition)
        self.driver.get(registration_for_submition)
        time.sleep(5)
        while self.driver.title == 'Just a moment...':
            self.driver.refresh()
            time.sleep(5)
        while self.driver.title == 'VFS : Registered Login':
            auth()
        select_city = Select(self.driver.find_element(By.ID,'LocationId'))
        select_city.select_by_value('635')
        select_visa = Select(self.driver.find_element(By.ID,'VisaCategoryId'))
        select_visa.select_by_value('1101')
        self.driver.find_element(By.ID,'btnContinue').click()
        time.sleep(5)
        while self.driver.title == 'Just a moment...':
            self.driver.refresh()
            time.sleep(5)


    def logout(self):
        time.sleep(10)
        self.driver.execute_script('document.getElementById("logoutForm").submit()')
        time.sleep(5)
        while self.driver.title == 'Just a moment...':
            self.driver.refresh()
        print('logout from account')

    def quite(self):
        self.driver.close()
        print('Bot stopped')
        # for linux server
        # self.display.stop()

# if __name__ == '__main__':
#     a = VisaBot(proxy[0], {'mail': 'sabayda96@bk.ru', 'password': 'Megapolis77@'})
#     a.get_book_link()
#     a.auth()
#     a.logout()
#     a.quite()
