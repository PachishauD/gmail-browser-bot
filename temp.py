from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Chrome driver with a user profile
chrome_options = Options()
chrome_options.add_argument("--user-data-dir=profile")
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the Google login page
driver.get("https://accounts.google.com/")

# Find the email input field, enter your email, and click the "Next" button
email_input = driver.find_element(by=By.ID, value="identifierId")
email_input.send_keys("your_email@gmail.com")
next_button = driver.find_element(by=By.ID, value="identifierNext")
next_button.click()

# Wait for the password input field to appear and enter your password
password_input = driver.find_element_by_name("password")
password_input.send_keys("your_password")

# Click the "Next" button to log in
password_next_button = driver.find_element(by=By.ID, value="passwordNext")
password_next_button.click()

# Wait for the login process to complete and verify that you are logged in
driver.implicitly_wait(10)  # Wait for 10 seconds
assert "My Account" in driver.title

# Save the profile for later use
driver.quit()