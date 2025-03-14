from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')

driver.find_element(By.CSS_SELECTOR,"[data-test='@web/AccountLink']").click()
driver.find_element(By.XPATH,"//button[@data-test='accountNav-signIn']").click()
sleep(5)

# verification:
actual_text =driver.find_element(By.XPATH,"//*[text()='Sign into your Target account']").text
expected_text = 'Sign into your Target account'
assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'
print('Test case passed')

driver.find_element(By.XPATH,"//*[text()='Sign in with password']")