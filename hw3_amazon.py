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

#Amazon logo
driver.find_element(By.CSS_SELECTOR,'.a-icon.a-icon-logo')
#your name field
driver.find_element(By.CSS_SELECTOR,'#ap_customer_name')
#Email field
driver.find_element(By.CSS_SELECTOR,'#ap_email')
#password field
driver.find_element(By.CSS_SELECTOR,'#ap_password')
#RE-enter password
driver.find_element(By.CSS_SELECTOR,'#ap_password_check')
#creat account
driver.find_element(By.CSS_SELECTOR,'h1.a-spacing-small')
#Passwords must be at least 6 characters
driver.find_element(By.CSS_SELECTOR,'#ap_password_context_message_section')
#continue
driver.find_element(By.CSS_SELECTOR,'#continue')
#Conditions of Use
driver.find_element(By.CSS_SELECTOR,"[href*='condition_of_use']")
# Privacy Notice
driver.find_element(By.CSS_SELECTOR,"[href*='ap_register_notification_privacy_notice']")
#Sign in
driver.find_element(By.CSS_SELECTOR,'.a-link-emphasis')