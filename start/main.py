import undetected_chromedriver as uc
from VPN import *
from time import sleep

if __name__ == '__main__':
    data = get_port()
    PROXY = f'http://{data["login"]}:{data["password"]}@{data["ip"]}:{data["port"]}'
    print(PROXY)
    chrome_options = uc.ChromeOptions()
    chrome_options.add_argument('--proxy-server=%s' % PROXY)
    driver = uc.Chrome(options=chrome_options)
    driver.get('https://www.whatismyip.com/')
    sleep(10)
    driver.close()
