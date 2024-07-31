import pickle
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import sys
import random

chrome_options = Options()

chrome_options.add_experimental_option(
    "prefs", {"profile.default_content_setting_values.notifications": 1}
)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

# chrome_options.add_extension("proxy.zip")
browser1 = webdriver.Chrome(
    executable_path="./driver/chromedriver-win64/chromedriver.exe", options=chrome_options)

# 2. Mở thử một trang web 
browser1.get(r"https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fwww.google.com%3Fhl%3Den-US&ec=GAlA8wE&hl=en&flowName=GlifWebSignIn&flowEntry=AddSession&dsh=S890486865%3A1722182912233738&ddm=0")
sleep(random.randint(2, 4))


emailInput = browser1.find_element(By.XPATH, '//input[@type="email"]')

emailInput.send_keys("q2rh5we@gmail.com")
sleep(random.randint(2, 4))


nextButton = browser1.find_element(By.XPATH, '//div[@id="identifierNext"]/div/button')
nextButton.click()
sleep(random.randint(1, 3))

try:
    redMess = browser1.find_element(By.XPATH, '//div[contains(@aria-live, "assertive")]/div[@class]')
    print(redMess.text)
except:
    browser1.back()

browser1.close()
browser1.quit()