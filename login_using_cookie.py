import time
import time
import pyperclip
import pickle

from email.parser import Parser
from email.message import EmailMessage

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.utilities.constants import PROXY_IP, PROXY_PORT, RECIPIENT_ADDRESS, SMTP_SERVER, SMTP_INTERVAL, POP3_SERVER, POP3_INTERVAL
from src.utilities.select_message_for_sending import select_random_msg, read_file_line_by_line, update_file

# Set up the Chrome driver with a user profile
def login(profile, email, password, recovery_email, profile_dir):
    from undetected_chromedriver import Chrome, ChromeOptions
    chrome_options = ChromeOptions()
    chrome_options.add_argument(f"--user-data-dir={profile_dir}")
    driver = Chrome(options=chrome_options)

    # Navigate to the Google login page
    driver.get("https://accounts.google.com/")
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "identifier")))
        input_email = driver.find_element(by=By.XPATH, value="//input[@name='identifier']")
        email_next = driver.find_element(by=By.ID, value="identifierNext")
        input_email.send_keys(email)
        email_next.click()
        time.sleep(2)
        try:
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "Passwd")))
            input_password = driver.find_element(by=By.NAME, value="Passwd")
            password_Next = driver.find_element(by=By.ID, value="passwordNext")
            ActionChains(driver=driver).move_to_element(input_password).click().send_keys(password).perform()
            ActionChains(driver=driver).move_to_element(password_Next).click().perform()
            time.sleep(2)
            try:
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@data-challengetype='12']")))
                confirm_recovery_email = driver.find_element(by=By.XPATH, value="//div[@data-challengetype='12']")
                confirm_recovery_email.click()
                time.sleep(2)
                try:
                    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "knowledge-preregistered-email-response")))
                    input_recovery_email = driver.find_element(by=By.ID, value="knowledge-preregistered-email-response")
                    input_recovery_email.send_keys(recovery_email)
                    input_recovery_email.send_keys(Keys.ENTER)
                    time.sleep(2)
                    try:
                        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "button")))
                        not_now_button = driver.find_element(by=By.TAG_NAME, value="button")
                        not_now_button.click()
                        time.sleep(2)
                    except:
                        pass
                except:
                    pass
            except:
                # try:
                #     WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, "//span[@jsname='V67aGc']")))
                #     update_file(url_senders, disable_index)
                #     with open(url_disabled, "a", encoding="utf-8") as disabled:
                #         disabled.write(email)
                # except:
                #     pass
                pass
        except:
            # update_file(url_senders, disable_index)
            # with open(url_disabled, "a", encoding="utf-8") as disabled:
            #     disabled.write(email)
            pass
    except:
        # update_file(url_senders, disable_index)
        # with open(url_disabled, "a", encoding="utf-8") as disabled:
        #     disabled.write(email)
        pass

    time.sleep(10)
    # Save the profile for later use
    driver.quit()


def main():
    senders = read_file_line_by_line("./assets/txt/senders.txt")
    num_senders = len(senders)
    for i in range(0, num_senders):
        profile_name = "Profile " + format(i + 1)
        profile_dir = f"C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\User Data\\{profile_name}"
        email = senders[i].split(",")[0].strip()
        password = senders[i].split(",")[1].strip()
        recovery = senders[i].split(",")[2].strip()
        print(profile_dir)
        login(profile=profile_name, email=email, password=password, recovery_email=recovery, profile_dir=profile_dir)


if __name__ == "__main__":
    main()