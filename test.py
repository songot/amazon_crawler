from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import selenium
import time
import pandas as pd
import os
import re

data = pd.read_csv('store_credentials.csv', header=0, sep=';', index_col=False)
email = data.Email[0]
pswrd= data.Password[0]

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome('env/bin/chromedriver',options=chrome_options)


scrape_url = "https://sellercentral.amazon.com/signin"
driver.get(scrape_url)
time.sleep(2)

try:
    username = driver.find_element_by_name("email")
    password =  driver.find_element_by_name("password")
    username.send_keys(email)
    password.send_keys(pswrd)
    driver.find_element_by_xpath("//input[@id='signInSubmit']").click()
    time.sleep(5)
    try:
        onetimepass = driver.find_element_by_name("otpCode")
        os.system('rm -f output.txt')
        os.system('echo "./cook_otp\nexit" | script output.txt') 
        with open("output.txt","r") as f:
            data = f.read()
            found = re.findall(r"(?<=com: ).*(?= \()",data,re.M)
            otp = found[0]
            print(otp)
            onetimepass.send_keys(otp)   
        driver.find_element_by_xpath("//input[@id='auth-signin-button']").click()
        time.sleep(5)
        driver.find_element_by_partial_link_text("Unshipped").click()
        time.sleep(5)

        print(driver.page_source)
    except selenium.common.exceptions.NoSuchElementException:
        print(driver.page_source)
except selenium.common.exceptions.WebDriverException:
    print(driver.page_source)
