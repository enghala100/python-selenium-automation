from xml.etree.ElementPath import xpath_tokenizer

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

#amazon logo
driver.find_element(By.XPATH,"//i[@class='a-icon a-icon-logo']")
#Email field
driver.find_element(By.ID,'ap_email')
#Continue button
driver.find_element(By.ID,'continue')
#Conditions of use link
driver.find_element(By.XPATH,"//a[text()='Conditions of Use']")
#Privacy Notice link
driver.find_element(By.XPATH,"//a[text()='Privacy Notice']")
#Need help link
driver.find_element(By.XPATH,"//span[@class='a-expander-prompt']")
#Forgot your password link
driver.find_element(By.ID,'auth-fpp-link-bottom')
#Other issues with Sign-In link
driver.find_element(By.ID,'ap-other-signin-issues-link')
#Create your Amazon account button
driver.find_element(By.ID,'createAccountSubmit')