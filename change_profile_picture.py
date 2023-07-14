import time
import pyautogui
import os
import pyperclip
import random

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


current_dir = os.path.dirname(os.path.abspath(__file__))

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
        profile_picture = driver.find_element(by=By.XPATH, value="//div[@class='wMR7G oGaYYd']")
        profile_picture.click()
        time.sleep(5)
        try:
            driver.switch_to.frame(1)
            time.sleep(1)
            picture_edit = driver.find_element(by=By.XPATH, value="//img[@class='EEKrSc xUNOSc']")
            time.sleep(1)
            picture_edit.click()
            time.sleep(3)
            try:
                from_computer = driver.find_element(by=By.XPATH, value="//button[@jsname='zf3vf']")
                from_computer.click()
                time.sleep(3)
                try:
                    upload_button = driver.find_element(by=By.XPATH, value="//button[@jsname='NBieKd']")
                    upload_button.click()
                    time.sleep(2)
                    pictures_pass = "./assets/profile_picture/profile_pictures"
                    pictures_names = os.listdir(pictures_pass)
                    picture = pictures_names[random.randrange(0, len(pictures_names))]
                    image_path = os.path.join(current_dir, 'assets\profile_picture\profile_pictures', picture)
                    pyautogui.write(image_path)
                    time.sleep(1)
                    pyautogui.press("enter")
                    time.sleep(4)
                    try:
                        next_button = driver.find_element(by=By.XPATH, value="//button[@jsname='yTKzd']")
                        next_button.click()
                        time.sleep(1)
                        try:
                            save_button = driver.find_element(by=By.XPATH, value="//button[@jsname='WCwAu']")
                            save_button.click()
                            print("-------------------------------------------------------")
                            print("Changed profile picture")
                        except:
                            pass
                    except:
                        pass
                except:
                    pass
            except:
                pass
        except:
            print("err")
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

if __name__ == '__main__':
    main()