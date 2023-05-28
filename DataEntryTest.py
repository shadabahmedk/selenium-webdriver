from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
chrome_options = webdriver.ChromeOptions()

DRIVER_LOCATION = "/usr/bin/chromedriver" 
BINARY_LOCATION = "/usr/bin/google-chrome" 

chrome_options.binary_location = BINARY_LOCATION
chrome_options.add_argument('--headless')

browser = webdriver.Chrome(executable_path=DRIVER_LOCATION, options=chrome_options) 

browser.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/register")

browser.implicitly_wait(0.5)
time.sleep(5)
first_name = browser.find_element(By.ID, "input-firstname")
#print(first_name.text)
first_name.send_keys("FirstName")
last_name = browser.find_element(By.ID, "input-lastname")
telephone = browser.find_element(By.ID, "input-telephone")
email = browser.find_element(By.ID, "input-email")


last_name.send_keys("LastName")
email.send_keys("your-email@example.com")
telephone.send_keys("+351999888777")

password = browser.find_element(By.ID, "input-password")
password_confirm = browser.find_element(By.ID, "input-confirm")
password.send_keys("123456")
password_confirm.send_keys("123456")
newsletter = browser.find_element(By.XPATH, value="//label[@for='input-newsletter-yes']")
newsletter.click()
terms = browser.find_element(By.XPATH, value="//label[@for='input-agree']")
terms.click()


continue_button = browser.find_element(By.XPATH, value="//input[@value='Continue']")
continue_button.click()
print(browser.title)
assert browser.title == "Your Account Has Been Created!"
