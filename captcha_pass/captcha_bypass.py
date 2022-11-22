from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

capcha_bypass_id = '138.201.188.166'


def capcha_bypass(driver, website, proxy):
    print('bypassing capcha...')

    # API key on rucaptcha.com
    API = 'b26c1cfaf4386620ee694aacc0e24897'

    # Identify of captcha
    data_sitekey = driver.find_element(By.CLASS_NAME, 'g-recaptcha').get_attribute('data-sitekey')

    # Request for solution proxy
    reqst = 'http://rucaptcha.com/in.php?key=' + API + '&method=userrecaptcha&googlekey=' + str(
        data_sitekey) + '&pageurl=' + website
    captcha = str(requests.post(reqst, data={f'proxy': {proxy}, 'proxytype': 'HHTPS'}).content)
    print(captcha)
    captcha_id = captcha.split('|')[1][:-1]
    time.sleep(15)

    # Getting answer for our request
    res = 'http://rucaptcha.com/res.php?key=' + API + '&action=get&id=' + captcha_id
    result = requests.get(res).content
    if result != b'CAPCHA_NOT_READY':  # Checking answer
        print(result)
        responce = str(result).split('|')[1][:-1]
    else:
        print(result)
        while result == b'CAPCHA_NOT_READY':  # Updating every 10 seconds waiting captcha will be rdy
            time.sleep(10)
            result = requests.get(res).content
            print(result)
        result = requests.get(res).content
        responce = str(result).split('|')[1][:-1]  # Captcha solution!

    # Changing html page
    driver.execute_script('var element=document.getElementById("g-recaptcha-response"); '
                          'element.style.display="";')
    driver.execute_script("""document.getElementById("g-recaptcha-response").innerHTML = arguments[0]""", responce)
    driver.execute_script('var element=document.getElementById("g-recaptcha-response"); '
                          'element.style.display="none";')
    print('CAPCHA was passed')
