from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from extension import proxies
from VPN import get_all_ports
from time import sleep

website = 'https://2ip.ru'

proxy_list = get_all_ports()

chrome_options = webdriver.ChromeOptions()

for proxy in proxy_list:
    proxies_extension = proxies(proxy['login'], proxy['password'], proxy['ip'], proxy['port'])
    chrome_options.add_extension(proxies_extension)
    #chrome_options.add_argument("--headless=chrome")
    chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    chrome.get(website)
    sleep(10)
    chrome.close()