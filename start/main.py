from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from extension import proxies
from VPN import get_port
from time import sleep

username = 'iharmikhailovich1341'
password = 'e8c14a'
endpoint = '109.248.7.195'
port = '10181'
website = 'https://2ip.ru'

chrome_options = webdriver.ChromeOptions()

proxies_extension = proxies(username, password, endpoint, port)

chrome_options.add_extension(proxies_extension)
#chrome_options.add_argument("--headless=chrome")


chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
chrome.get(website)
sleep(10)
chrome.close()