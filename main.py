import undetected_chromedriver as uc
from time import sleep

PROXY = "109.248.7.95:10305"
chrome_options = uc.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % PROXY)

if __name__ == '__main__' :
    driver = uc.Chrome(options = chrome_options)
    driver.get('https://2ip.ru/')
    sleep(15)
    driver.close()