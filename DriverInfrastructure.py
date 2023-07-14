import time
import pyautogui
import os
import pyperclip
import random
import xlrd

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from src.utilities.select_message_for_sending import select_random_msg, read_file_line_by_line

senders_file = xlrd.open_workbook("./assets/xls/50-pcs-2020-16.6.xlsx") 
senders_list = senders_file.sheet_by_index(0)
number_of_senders = senders_list.nrows

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

def login_to_gmail(driver, email, password, recovery_email):
    driver.get("https://www.google.com/accounts/Login")
    time.sleep(1)
    try:
        input_email = driver.find_element(by=By.XPATH, value="//input[@name='identifier']")
        email_next = driver.find_element(by=By.ID, value="identifierNext")
        time.sleep(1)
        input_email.send_keys(email)
        time.sleep(1)
        email_next.click()
        time.sleep(1)
        try:
            input_password = driver.find_element(by=By.NAME, value="Passwd")
            password_Next = driver.find_element(by=By.ID, value="passwordNext")
            time.sleep(1)
            input_password.send_keys(password)
            time.sleep(1)
            password_Next.click()
            time.sleep(1)
            with open("./assets/accounts/senders.txt", "a", encoding="utf-8") as senders:
                senders.write(email + "," + password + "," + recovery_email + "\n")
            try:
                confirm_recovery_email = driver.find_element(by=By.XPATH, value="//div[@data-challengeindex='2']")
                time.sleep(1)
                confirm_recovery_email.click()
                time.sleep(1)
                try:
                    input_recovery_email = driver.find_element(by=By.ID, value="knowledge-preregistered-email-response")
                    input_recovery_email.send_keys(recovery_email)
                    input_recovery_email.send_keys(Keys.ENTER)
                    time.sleep(1)
                    try:
                        not_now_button = driver.find_element(by=By.TAG_NAME, value="button")
                        not_now_button.click()
                        time.sleep(1)
                        with open("./assets/accounts/senders.txt", "a", encoding="utf-8") as senders:
                            senders.write(email + "," + password + "," + recovery_email + "\n")
                        # try:
                        #     driver.get("https://mail.google.com/mail/u/0/#inbox")
                        # except:
                        #     # print("Cannot find url 'mail.google.com!!!!!!!!!!!!'")
                        #     pass
                    except:
                        # try:
                        #     driver.get("https://mail.google.com/mail/u/0/#inbox")
                        # except:
                        #     # print("Cannot find url 'mail.google.com!!!!!!!!!!!!'")
                        #     pass
                        # # print("There is no 'Not now' button!")
                        pass
                except:
                    print("Cannot find element 'input_recovery_email'")
                    # try:
                    #     driver.get("https://mail.google.com/mail/u/0/#inbox")
                    # except:
                    #     # print("Cannot find url 'mail.google.com!!!!!!!!!!!!'")
                    #     pass
            except:
                # print("There is no element have ID 'knowledge-preregistered-email-response'")
                # try:
                #     driver.get("https://mail.google.com/mail/u/0/#inbox")
                # except:
                #     # print("Cannot find url 'mail.google.com!!!!!!!!!!!!'")
                #     pass
                pass
        except:
            time.sleep(1)
            print("This account was disabled!")
            with open("./assets/accounts/disabled.txt", "a", encoding="utf-8") as disabled_accs:
                disabled_accs_list = read_file_line_by_line("./assets/accounts/disabled.txt")
                if email + "\n" not in disabled_accs_list:
                    disabled_accs.write(email + "\n")
            # login_to_gmail(driver=relogin_driver, index=index)
            # try:
            #     driver.get("https://mail.google.com/mail/u/0/#inbox")
            # except:
            #     # print("Cannot find url 'mail.google.com!!!!!!!!!!!!'")
            #     pass
    except:
        # try:
        #     driver.get("https://mail.google.com/mail/u/0/#inbox")
        # except:
        #     # print("Cannot find url 'mail.google.com!!!!!!!!!!!!'")
        #     pass
        pass
    time.sleep(2)
    driver.close()


def main():
    for i in range(0, number_of_senders):
        email = senders_list.cell_value(i, 0)
        password = senders_list.cell_value(i, 1)
        recovery_email = senders_list.cell_value(i, 2)
        driver = driver_chrome_incognito()
        time.sleep(1)
        login_to_gmail(driver=driver, email=email, password=password, recovery_email=recovery_email)
        time.sleep(1)


if __name__ == '__main__':
    main()