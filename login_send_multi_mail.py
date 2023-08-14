

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
url_body_links = "./assets/txt/bodylinks.txt"
url_txts = "./assets/txt/texts.txt"
url_subject = "./assets/txt/subjects.txt"

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
                            time.sleep(10)

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

def send_mail(driver):
    driver.get("https://gmail.com")
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='T-I T-I-KE L3']")))
        driver.find_element(by=By.XPATH, value="//div[@class='T-I T-I-KE L3']").click()
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@class='agP aFw']")))
            recipient = driver.find_element(by=By.XPATH, value="//input[@class='agP aFw']")
            recipient.send_keys(Keys.CONTROL + Keys.SHIFT + "b")
            try:
                all_recipients = read_file_line_by_line(url_ricipients)
                temp_array = ["Stacho1988@gmail.com", "afoucher7255@gmail.com"]
                rand_number = random.randrange(10, 19)
                for i in range(0, rand_number):
                    # recipient.send_keys(all_recipients[i])
                    temp_array.append(all_recipients[1].strip())
                    update_file(url_ricipients, 1)
                recipient_inputs = driver.find_elements(by=By.XPATH, value="//input[@class='agP aFw']")
                bcc_element = recipient_inputs[1]
                delimeter = ","
                string_to_send = delimeter.join(temp_array)   
                bcc_element.send_keys(string_to_send)
                try:
                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "subjectbox")))
                    subject = driver.find_element(by=By.NAME, value="subjectbox")
                    # subject_content ='{0}'.format(recipient_email.split('@')[0]).strip().capitalize()
                    subject_content = select_random_msg(url_subject)
                    subject.send_keys(subject_content + "!")
                    try:
                        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='Am Al editable LW-avf tS-tW']")))
                        # msg_body = driver.find_element(by=By.XPATH, value="//div[@aria-label='Message Body']")
                        msg_body = driver.find_element(by=By.XPATH, value="//div[@class='Am Al editable LW-avf tS-tW']")
                        time.sleep(1)
                        ActionChains(driver=driver).move_to_element(msg_body).click().perform()
                        msg_text = select_random_msg(url_txts)
                        msg_body.send_keys(msg_text)
                        msg_hyperlinks = select_random_msg(url_body_links)
                        bitlylinks = select_random_msg(url_links).strip()
                        try:
                            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='e5 aaA aMZ']")))
                            add_link = driver.find_element(by=By.XPATH, value="//div[@class='e5 aaA aMZ']")
                            add_link.click()
                        except:
                            pass
                        try:
                            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "linkdialog-text")))
                            label = driver.find_element(by=By.ID, value="linkdialog-text")
                            label.send_keys(msg_hyperlinks)
                            time.sleep(1)
                        except:
                            pass
                        try:
                            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "linkdialog-onweb-tab-input")))
                            link = driver.find_element(by=By.ID, value="linkdialog-onweb-tab-input")
                            link.send_keys(bitlylinks)
                            time.sleep(1)
                        except:
                            pass
                        try:
                            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "ok")))
                            ok_button = driver.find_element(by=By.NAME, value="ok")
                            ok_button.click()
                            time.sleep(1)
                        except:
                            pass  
                        time.sleep(1)
                        
                        # msg_body.send_keys(msg_content)
                       
                        time.sleep(1)
                        try:
                            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='T-I J-J5-Ji aoO v7 T-I-atl L3']")))
                            send_button = driver.find_element(by=By.XPATH, value="//div[@class='T-I J-J5-Ji aoO v7 T-I-atl L3']")
                            ActionChains(driver=driver).move_to_element(send_button).click().perform()
                            print("---------------------------------------------------------->")
                            total_sent = int(read_file_line_by_line(url_total_sent)[0])
                            total_reply = int(read_file_line_by_line(url_total_reply)[0])
                            total_sent += rand_number
                            print("<----------Total sent: " + format(total_sent) + "---------->")
                            with open(url_total_sent, "w", encoding="utf-8") as file:
                                file.write(format(total_sent))
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


def main():
    senders = read_file_line_by_line(url_senders)
    num_senders = len(senders)
    recipients = read_file_line_by_line(url_ricipients)
    if len(recipients) == 0:
        pass
    else:
        for i in range(1, 50):
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
                send_mail(driver=driver)
                time.sleep(1)
            driver.quit()


if __name__ == "__main__":
    process = multiprocessing.Process(target=main)
    process.start()