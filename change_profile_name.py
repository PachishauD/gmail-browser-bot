import time
import pyautogui
import pyperclip

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from src.utilities.select_message_for_sending import select_random_msg

def set_clipboard(text):
    pyperclip.copy(text)


def driver_chrome_incognito():
    from undetected_chromedriver import Chrome, ChromeOptions
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument("--log-level=OFF")
    chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
    driver = Chrome(options=chrome_options, version_main = 114)

    #driver.get("https://www.google.com")
    # print("----------------------------------------------------------------------------------------------")
    return driver

def login_to_gmail(driver):
    driver.get("https://google.com/accounts/Login")
    time.sleep(1)
    try:
        input_email = driver.find_element(by=By.XPATH, value="//input[@name='identifier']")
        email_next = driver.find_element(by=By.ID, value="identifierNext")
        time.sleep(1)
        input_email.send_keys("emmanuelbamaiyi9098@gmail.com")
        time.sleep(1)
        email_next.click()
        time.sleep(1)
        try:
            input_password = driver.find_element(by=By.NAME, value="Passwd")
            password_Next = driver.find_element(by=By.ID, value="passwordNext")
            time.sleep(1)
            input_password.send_keys("Wxpnsoxzqmhi")
            time.sleep(1)
            password_Next.click()
            time.sleep(1)
            try:
                confirm_recovery_email = driver.find_element(by=By.XPATH, value="//div[@data-challengeindex='2']")
                time.sleep(1)
                confirm_recovery_email.click()
                time.sleep(1)
                try:
                    input_recovery_email = driver.find_element(by=By.ID, value="knowledge-preregistered-email-response")
                    input_recovery_email.send_keys("maqbarariieu645991@kaishime.com")
                    input_recovery_email.send_keys(Keys.ENTER)
                    time.sleep(1)
                    try:
                        not_now_button = driver.find_element(by=By.TAG_NAME, value="button")
                        not_now_button.click()
                        time.sleep(1)
                    except:
                        print("There is no 'Not now' button!")
                except:
                    print("Cannot find element 'input_recovery_email'")
            except:
                print("There is no element have ID 'knowledge-preregistered-email-response'")
        except:
            print("There is no element named 'Passwd'")
    except:
        pass
    time.sleep(1)
    driver.get("https://aboutme.google.com")
    return driver

def change_profile_name(driver):
    time.sleep(1)
    # profile_picture = driver.find_element(by=By.XPATH, value="//div[@class='wMR7G oGaYYd']")
    try:
        profile_name = driver.find_element(by=By.XPATH, value="//div[@class='bJCr1d']")
        profile_name.click()
        time.sleep(5)
        try:
            name_edit = driver.find_element(by=By.XPATH, value="//button[@aria-label='Edit Name']")
            name_edit.click()
            time.sleep(1)
            try:
                first_name = driver.find_element(by=By.ID, value="i6")
                first_name.send_keys(Keys.CONTROL + "a")
                time.sleep(1)
                string_first_name = select_random_msg("./assets/txt/femail names.txt").strip().capitalize()
                first_name.send_keys(string_first_name)
                try:
                    last_name = driver.find_element(by=By.ID, value="i11")
                    last_name.send_keys(Keys.CONTROL + "a")
                    time.sleep(1)
                    string_last_name = select_random_msg("./assets/txt/femail names.txt").strip().capitalize()
                    last_name.send_keys(string_last_name)
                    try:
                        save_button = driver.find_element(by=By.XPATH, value="//div[@jsname='Ob2vef']")
                        save_button.click()
                        print("-------------------------------------------------------")
                        print("Profile name changed!")
                    except:
                        pass
                except:
                    pass
            except:
                pass
        except:
            pass
    except:
        pass
    time.sleep(1000)

    

def main():
    driver = driver_chrome_incognito()
    time.sleep(1)
    gmail_driver = login_to_gmail(driver)
    time.sleep(1)
    change_profile_name(gmail_driver)

# sender_driver = send_mail(gmail_driver)
# time.sleep(5)
# read_driver = watch_unread_gmails(sender_driver)
# time.sleep(5)
# sign_out_driver = sign_out(read_driver)
# time.sleep(5)
# sign_out_driver.close()
# time.sleep(1000)

if __name__ == '__main__':
    main()