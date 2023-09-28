import time
import pyperclip
import multiprocessing
import random
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.utilities.select_message_for_sending import select_random_msg, read_file_line_by_line, update_file

url_senders = "./assets/txt/200 accs.txt"
url_recipients = "./assets/txt/real_gmails.txt"
url_links = "./assets/txt/Slide links.txt"
url_message = "./assets/txt/Reply Message 200 Eng.txt"
url_total_sent = "./assets/txt/slide_total_sent.txt"

def copy(string):
    pyperclip.copy(string)

def login(profile_dir, email, password, recovery_email):
    from undetected_chromedriver import Chrome, ChromeOptions
    chrome_options = ChromeOptions()
    chrome_options.add_argument(f"--user-data-dir={profile_dir}")
    driver = Chrome(options=chrome_options, version_main=114)
    driver.get("https://accounts.google.com")
    try:
        WebDriverWait(driver,100).until(EC.presence_of_element_located((By.NAME, "identifier")))
        mail_input = driver.find_element(by=By.XPATH, value="//input[@name='identifier']")
        next_button = driver.find_element(by=By.ID, value="identifierNext")
        mail_input.send_keys(email)
        next_button.click()
        try:
            WebDriverWait(driver,100).until(EC.presence_of_element_located((By.NAME, "Passwd")))
            password_input = driver.find_element(by=By.NAME, value="Passwd")
            next_button = driver.find_element(by=By.ID, value="passwordNext")
            ActionChains(driver=driver).move_to_element(password_input).click().send_keys(password).perform()
            ActionChains(driver=driver).move_to_element(next_button).click().perform()
            try:
                WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "//div[@data-challengetype='12']")))
                confirm_recovery_email = driver.find_element(by=By.XPATH, value="//div[@data-challengetype='12']")
                confirm_recovery_email.click()
                time.sleep(2)
                try:
                    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID, "knowledge-preregistered-email-response")))
                    input_recovery_email = driver.find_element(by=By.ID, value="knowledge-preregistered-email-response")
                    input_recovery_email.send_keys(recovery_email)
                    input_recovery_email.send_keys(Keys.ENTER)
                    time.sleep(2)
                    try:
                        WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.TAG_NAME, "button")))
                        not_now_button = driver.find_element(by=By.TAG_NAME, value="button")
                        not_now_button.click()
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
    recipients = read_file_line_by_line(url_recipients)
    if len(recipients) == 0:
        pass
    else:
        for i in range(144, 145):
            email = senders[i].split(",")[0].strip()
            password = senders[i].split(",")[1].strip()
            recovery = senders[i].split(",")[2].strip()
            # profile_subfix = '{0}'.format(email.split('@')[0]).strip().capitalize()
            profile_subfix = format(i + 1)
            profile_name = "Profile " + profile_subfix
            windows_profile_path = os.environ["USERPROFILE"]
            profile_dir = f"{windows_profile_path}\\AppData\\Local\\Google\\Chrome\\User Data\\{profile_name}"
            print(profile_dir)
            try:
                driver = login(profile_dir=profile_dir, email=email, password=password, recovery_email=recovery)
                try:
                    share_link = select_random_msg(url_links).strip()
                    for i in range(0, 5):
                        share_slides(driver=driver,link=share_link)
                    # if i % 2 == 0:
                    #     update_file(url_links, 1)
                except:
                    pass
            except:
                pass
            driver.close()
    print("sent all")
                

if __name__ == "__main__":
    process = multiprocessing.Process(target=main)
    process.start()
