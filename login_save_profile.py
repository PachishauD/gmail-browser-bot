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

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.utilities.select_message_for_sending import select_random_msg, read_file_line_by_line, update_file

# senders_file = xlrd.open_workbook("./assets/xls/50-pcs-2020-16.6.xlsx") 
# senders_list = senders_file.sheet_by_index(0)
# number_of_senders = senders_list.nrows
url_senders = "./assets/txt/senders.txt"
url_ricipients = "./assets/txt/recipients.txt"
url_links = "./assets/txt/links.txt"
url_message = "./assets/txt/First Msgs 300.txt"
url_reply_message = "./assets/txt/Reply Message 200 Eng.txt"
url_total_sent = "./assets/txt/total_sent.txt"
url_total_reply = "./assets/txt/total_reply.txt"
url_disabled = "./assets/accounts/disabled.txt"
url_recipients_backup = "./assets/txt/recipients_backup.txt"
current_dir = os.path.dirname(os.path.abspath(__file__))

def set_clipboard(text):
    pyperclip.copy(text)


def driver_chrome_incognito(profile_dir):
    from undetected_chromedriver import Chrome, ChromeOptions
    chrome_options = ChromeOptions()
    chrome_options.add_argument(f"--user-data-dir={profile_dir}")
    # chrome_options.add_argument("--incognito")
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument("--log-level=OFF")
    chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
    driver = Chrome(options=chrome_options, version_main = 114)

    #driver.get("https://www.google.com")
    # print("----------------------------------------------------------------------------------------------")
    return driver

def login_to_google(driver, email, password, recovery_email, disable_index):
    driver.get("https://accounts.google.com")
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "identifier")))
        input_email = driver.find_element(by=By.XPATH, value="//input[@name='identifier']")
        email_next = driver.find_element(by=By.ID, value="identifierNext")
        input_email.send_keys(email)
        email_next.click()
        time.sleep(2)
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "Passwd")))
            input_password = driver.find_element(by=By.NAME, value="Passwd")
            password_Next = driver.find_element(by=By.ID, value="passwordNext")
            input_password.send_keys(password)
            ActionChains(driver=driver).move_to_element(password_Next).click().perform()
            time.sleep(2)
            try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-challengetype='12']")))
                confirm_recovery_email = driver.find_element(by=By.XPATH, value="//div[@data-challengetype='12']")
                confirm_recovery_email.click()
                time.sleep(2)
                try:
                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "knowledge-preregistered-email-response")))
                    input_recovery_email = driver.find_element(by=By.ID, value="knowledge-preregistered-email-response")
                    input_recovery_email.send_keys(recovery_email)
                    input_recovery_email.send_keys(Keys.ENTER)
                    time.sleep(2)
                    try:
                        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "button")))
                        not_now_button = driver.find_element(by=By.TAG_NAME, value="button")
                        not_now_button.click()
                        time.sleep(2)
                    except:
                        pass
                except:
                    pass
            except:
                try:
                    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//span[@jsname='V67aGc']")))
                    update_file(url_senders, disable_index)
                    with open(url_disabled, "a", encoding="utf-8") as disabled:
                        disabled.write(email)
                except:
                    pass
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
    # cookies = driver.get_cookies()
    # pre_email = '{0}'.format(email.split('@')[0]).strip()
    # filename = "./assets/cookies/" + pre_email + ".txt"
    # with open(filename, "w") as file:
    #     for cookie in cookies:
    #         file.write(f"{cookie['name']}={cookie['value']}")
    time.sleep(5)
    driver.quit()



def main():
    senders = read_file_line_by_line("./assets/txt/senders.txt")
    num_senders = len(senders)
    for i in range(0, num_senders):
        email = senders[i].split(",")[0].strip()
        password = senders[i].split(",")[1].strip()
        recovery = senders[i].split(",")[2].strip()
        profile_subfix = '{0}'.format(email.split('@')[0]).strip().capitalize()
        profile_name = "Profile " + profile_subfix
        profile_dir = f"C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\User Data\\{profile_name}"
        driver = driver_chrome_incognito(profile_dir=profile_dir)
        login_to_google(driver=driver, email=email, password=password, recovery_email=recovery, disable_index=(i + 1))
        time.sleep(1)
        time.sleep(1)


if __name__ == '__main__':
    main()