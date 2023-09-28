import time
import pyperclip
import multiprocessing
import random
import os
import captcha
import re
import SMSverification
import pyautogui

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.utilities.select_message_for_sending import select_random_msg, read_file_line_by_line, update_file

url_senders = "./assets/accs1.txt"
url_recipients = "./assets/txt/real_gmails.txt"
url_links = "./assets/txt/Slide links.txt"
url_message = "./assets/txt/Reply Message 200 Eng.txt"
url_total_sent = "./assets/txt/slide_total_sent.txt"

def copy(string):
    pyperclip.copy(string)

def login(profile_dir, email, password, recovery_email, backupcode):
    from undetected_chromedriver import Chrome, ChromeOptions
    chrome_options = ChromeOptions()
    chrome_options.add_argument(f"--user-data-dir={profile_dir}")
    driver = Chrome(options=chrome_options, version_main=114)
    driver.get("https://accounts.google.com")
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@jsname='rwl3qc']")))
        continue_button = driver.find_element(by=By.XPATH, value="//div[@jsname='rwl3qc']")
        continue_button.click()
    except:
        pass
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
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@jsname='LgbsSe']")))
            verify_next_button = driver.find_element(by=By.XPATH, value="//button[@jsname='LgbsSe']")
            verify_next_button.click()
            time.sleep(10)
            try:
                captcha.captcha_solver(driver=driver)
                try:
                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@jsname='LgbsSe']")))
                    verify_next_button = driver.find_element(by=By.XPATH, value="//button[@jsname='LgbsSe']")
                    verify_next_button.click()
                    time.sleep(2)
                    try:
                        WebDriverWait(driver,100).until(EC.presence_of_element_located((By.NAME, "password")))
                        password_input = driver.find_element(by=By.NAME, value="password")
                        next_button = driver.find_element(by=By.ID, value="passwordNext")
                        ActionChains(driver=driver).move_to_element(password_input).click().send_keys(password).perform()
                        # ActionChains(driver=driver).move_to_element(next_button).click().perform()
                        password_input.send_keys(Keys.ENTER)
                        time.sleep(10)
                        try:
                            if re.match(r"^https://accounts.google.com/speedbump/idvreenable*", driver.current_url):
                                print("1")
                                SMS_STATUS=SMSverification.main_sms_verifier(driver, "old_version_sms_page",0)
                            elif re.match(r"^https://accounts.google.com/signin/v2/challenge/iap*", driver.current_url):
                                print("2")
                                SMS_STATUS = SMSverification.main_sms_verifier(driver, "new_version_sms_page",0)
                            print("x")
                            time.sleep(1000)
                        except:
                            print("3")
                            pass
                    except:
                        pass
                except:
                    pass
            except:
                print("y")
                pass
        except:
            pass
        pass

    return driver

def share_slides(driver, link):
    driver.get("https://docs.google.com/document/u/0/")
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, ":1i")))
        blank_slide = driver.find_element(by=By.ID, value=":1i")
        blank_slide.click()
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "docs-titlebar-share-client-button")))
            share_button = driver.find_element(by=By.ID, value="docs-titlebar-share-client-button")
            share_button.click()
            try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@class='modal-dialog-userInput jfk-textinput']")))
                input_element = driver.find_element(by=By.XPATH, value="//input[@class='modal-dialog-userInput jfk-textinput']")
                input_element.send_keys(Keys.ENTER)
                try:
                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//iframe[@class='share-client-content-iframe']")))
                    iframe_div = driver.find_element(by=By.XPATH, value="//iframe[@class='share-client-content-iframe']")
                    driver.switch_to.frame(iframe_div)
                    try:
                        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@class='zeumMd d2j1H']")))
                        add_people = driver.find_element(by=By.XPATH, value="//input[@class='zeumMd d2j1H']")
                        temp_array = []
                        add_people.send_keys("uchitosato@gmail.com,")
                        for i in range(0, 10):
                            all_recipients = read_file_line_by_line(url_recipients)
                            temp_array.append(all_recipients[0].strip())
                            update_file(url_recipients, 1)
                            add_people.send_keys(all_recipients[0].strip())
                            add_people.send_keys(",")
                        try:
                            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//textarea[@jsname='YPqjbf']")))
                            Message_element = driver.find_element(by=By.XPATH, value="//textarea[@jsname='YPqjbf']")
                            share_messages = select_random_msg(url_message).split(":")[0].strip() + ": " + link
                            copy(share_messages)
                            Message_element.send_keys(Keys.CONTROL + "v")
                            try:
                                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@jsname='ymIaV']")))
                                send_button = driver.find_element(by=By.XPATH, value="//button[@jsname='ymIaV']")
                                send_button.click()
                                time.sleep(5)
                                try:
                                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@data-id='EBS5u']")))
                                    send_anyway = driver.find_elements(by=By.XPATH, value="//button[@data-id='EBS5u']")
                                    print(len(send_anyway))
                                    send_anyway[1].click()
                                    print("z")
                                    time.sleep(10)
                                except:
                                    pass
                                totoal_sent = int(read_file_line_by_line(url_total_sent)[0])
                                totoal_sent += 10
                                print("------------------" + format(totoal_sent) + " messages were sent totally!-------------")
                                with open(url_total_sent, "w", encoding="utf-8") as file:
                                    file.write(format(totoal_sent))
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
    except:
        pass    
    return driver

def main():
    senders = read_file_line_by_line(url_senders)
    num_senders = len(senders)
    # recipients = read_file_line_by_line(url_ricipients)
    # if len(recipients) == 0:
    #     pass
    # else:
    for i in range(0, 50):
        email = senders[i].split(",")[0].strip()
        password = senders[i].split(",")[1].strip()
        recovery = senders[i].split(",")[2].strip()
        app_password = senders[i].split(",")[3].strip()
        backup_code1 = senders[i].split(",")[8].strip()
        backup_code2 = senders[i].split(",")[9].strip()
        profile_subfix = '{0}'.format(email.split('@')[0]).strip().capitalize()
        profile_name = "Profile " + format(i + 1)
        profile_dir = f"C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\User Data\\{profile_name}"
        
        print(profile_dir)
        print(email, password, recovery, backup_code1)
        try:
            driver = login(profile_dir=profile_dir, email=email, password=password, backupcode=backup_code2)
            driver.close()
        except:
            pass
    print("login all")
                

if __name__ == "__main__":
    process = multiprocessing.Process(target=main)
    process.start()
