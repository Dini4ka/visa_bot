import time
from pyvirtualdisplay import Display
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By


class VisaBot():
    def __init__(self):
        self.display = Display(visible=0, size=(800, 600))
        self.display.start()
        opts = uc.ChromeOptions()
        #opts.headless = True
        opts.add_argument('--proxy-server=193.23.50.245:10109')
        self.driver = uc.Chrome(options=opts)
        print('bot started to work')

    def get_book_link(self):
        website = 'https://visa.vfsglobal.com/blr/en/pol/book-an-appointment'
        website1 = 'https://2ip.ru'
        self.driver.get(website)
        time.sleep(15)
        print('get vfsglobal.com')
        book_now = self.driver.find_element(By.CLASS_NAME, 'lets-get-started').get_attribute('href')
        self.driver.get(book_now)
        time.sleep(30)

    def check_connection(self):
        page_source = self.driver.page_source
        print(page_source)

    def quite(self):
        self.driver.close()
        self.display.stop()


if __name__ == '__main__':
    bot = VisaBot()
    bot.get_book_link()
    bot.check_connection()
    bot.quite()


# launch stuff inside virtual display here
