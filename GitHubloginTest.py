from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

# Create variables for login credentials.
username = "mimrancomsats"
password = "Lohari13"


DRIVER_LOCATION = "/usr/bin/chromedriver" 
BINARY_LOCATION = "/usr/bin/google-chrome" 

chrome_options = webdriver.ChromeOptions()

chrome_options.binary_location = BINARY_LOCATION
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(executable_path=DRIVER_LOCATION, options=chrome_options) 

# Launch the browser and open the github URL in your web driver.
driver.get("https://github.com/login")

# Find the username/email field and send the username to the input field.
uname = driver.find_element("id", "login_field") 
uname.send_keys(username)

# Find the password input field and send the password to the input field.
pword = driver.find_element("id", "password") 
pword.send_keys(password)

# Click sign in button to login the website.
driver.find_element("name", "commit").click()
# Wait for login process to complete. 
WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)
# Verify that the login was successful.
error_message = "Incorrect username or password."
# Retrieve any errors found. 
errors = driver.find_elements(By.CLASS_NAME, "flash-error")

# When errors are found, the login will fail. 
if any(error_message in e.text for e in errors): 
    print("[!] Login failed")
else:
    print("[+] Login successful")
    
# Close the driver
driver.close()
driver.quit()
