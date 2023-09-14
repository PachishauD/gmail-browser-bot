

import time
import time
import pyperclip
import pickle
import multiprocessing
import pyautogui
import random

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
url_senders = "./assets/csv/110 valid account.csv"
url_ricipients = "./assets/txt/recipients.txt"
url_links = "./assets/txt/Links test manualbot gmail.txt"
url_message = "./assets/txt/First Msgs 300.txt"
url_reply_message = "./assets/txt/Reply Message 200 Eng.txt"
url_total_sent = "./assets/txt/total_sent.txt"
url_total_reply = "./assets/txt/total_reply.txt"
url_disabled = "./assets/accounts/disabled.txt"
url_recipients_backup = "./assets/txt/recipients_backup.txt"
url_body_links = "./assets/txt/R Bodylinks 100 Eng.txt"
url_txts = "./assets/txt/R Texts 100 Eng.txt"
url_subject = "./assets/txt/R Subjects 100 Eng.txt"

recipients = read_file_line_by_line(url_ricipients)
num = 0

def copy(string):
    pyperclip.copy(string)

def login(profile_dir, email, password, backupcode):
    print(email)
    print(password)
    print(backupcode)
    from undetected_chromedriver import Chrome, ChromeOptions
    chrome_options = ChromeOptions()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument(f"--user-data-dir={profile_dir}")
    # chrome_options.add_argument('--log-level=3')
    # chrome_options.add_argument("--log-level=OFF")
    # chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
    driver = Chrome(options=chrome_options, version_main = 114)

    # # Navigate to the Google login page
    driver.get("https://gmail.com")
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "identifier")))
        input_email = driver.find_element(by=By.XPATH, value="//input[@name='identifier']")
        email_next = driver.find_element(by=By.ID, value="identifierNext")
        input_email.send_keys(email)
        email_next.click()
        time.sleep(3)
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "Passwd")))
            input_password = driver.find_element(by=By.NAME, value="Passwd")
            password_Next = driver.find_element(by=By.ID, value="passwordNext")
            ActionChains(driver=driver).move_to_element(input_password).click().send_keys(password).perform()
            ActionChains(driver=driver).move_to_element(password_Next).click().perform()
            time.sleep(5)
            pyautogui.hotkey("enter")
            time.sleep(2)
            try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@jsname='QkNstf']")))
                try_another_way = driver.find_element(by=By.XPATH, value="//div[@jsname='QkNstf']")
                try_another_way.click()
                time.sleep(2)
                try:
                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-challengetype='8']")))
                    enter_backup_code = driver.find_element(by=By.XPATH, value="//div[@data-challengetype='8']")
                    enter_backup_code.click()
                    time.sleep(2)
                    try:
                        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "backupCodePin")))
                        back_up_code_pin = driver.find_element(by=By.ID, value="backupCodePin")
                        back_up_code_pin.send_keys(backupcode)
                        time.sleep(2)
                        try:
                            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@jsname='Njthtb']")))
                            next_button = driver.find_element(by=By.XPATH, value="//div[@jsname='Njthtb']")
                            next_button.click()
                            time.sleep(2)

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
    except:
        pass
    return driver

def share_slides(driver):
    driver.get("https://docs.google.com/presentation/u/0/")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, ":1i")))
    blank_slide = driver.find_element(by=By.ID, value=":1i")
    blank_slide.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "docs-titlebar-share-client-button")))
    share_button = driver.find_element(by=By.ID, value="docs-titlebar-share-client-button")
    share_button.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@class='modal-dialog-userInput jfk-textinput']")))
    input_element = driver.find_element(by=By.XPATH, value="//input[@class='modal-dialog-userInput jfk-textinput']")
    input_element.send_keys(Keys.ENTER)
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//iframe[@class='share-client-content-iframe']")))
        iframe_div = driver.find_element(by=By.XPATH, value="//iframe[@class='share-client-content-iframe']")
        driver.switch_to.frame(iframe_div)
        # email_input = driver.find_element(by=By.XPATH, value="//input[@aria-label='Add people and groups']")
        # email_input.click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@class='zeumMd d2j1H']")))
        add_people = driver.find_element(by=By.XPATH, value="//input[@class='zeumMd d2j1H']")
        temp_array = []
        add_people.send_keys("uchitosato@gmail.com,")
        for i in range(0, 9):
            all_recipients = read_file_line_by_line(url_ricipients)
            # recipient.send_keys(all_recipients[i])
            temp_array.append(all_recipients[0].strip())
            update_file(url_ricipients, 1)
            add_people.send_keys(all_recipients[0].strip())
            add_people.send_keys(",")

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//textarea[@jsname='YPqjbf']")))
        Message_element = driver.find_element(by=By.XPATH, value="//textarea[@jsname='YPqjbf']")
        Message_element.send_keys(select_random_msg(url_links))

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@jsname='ymIaV']")))
        send_button = driver.find_element(by=By.XPATH, value="//button[@jsname='ymIaV']")
        send_button.click()
        # print(temp_array)
        # delimeter = ","
        # string_to_send = delimeter.join(temp_array)   
        # print(string_to_send)

    except:
        print("y")
        pass
    time.sleep(1000)

    time.sleep(1)
    
    return driver


def main():
    senders = read_file_line_by_line(url_senders)
    num_senders = len(senders)
    recipients = read_file_line_by_line(url_ricipients)
    if len(recipients) == 0:
        pass
    else:
        for i in range(53, 54):
            email = senders[i].split(",")[0].strip()
            password = senders[i].split(",")[1].strip()
            recovery = senders[i].split(",")[2].strip()
            app_password = senders[i].split(",")[3].strip()
            backup_code1 = senders[i].split(",")[4].strip()
            backup_code2 = senders[i].split(",")[7].strip()
            profile_subfix = '{0}'.format(email.split('@')[0]).strip().capitalize()
            profile_name = "Profile " + profile_subfix
            profile_dir = f"C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\User Data\\{profile_name}"
            
            print(profile_dir)
            driver = login(profile_dir=profile_dir, email=email, password=password, backupcode=backup_code2)
            for i in range(0, 1):
                recipients = read_file_line_by_line(url_ricipients)
                share_slides(driver=driver)
                time.sleep(1)
            driver.quit()


if __name__ == "__main__":
    process = multiprocessing.Process(target=main)
    process.start()