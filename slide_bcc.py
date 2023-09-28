import time
import pyperclip
import multiprocessing
import random
import os
import threading
import SMSverification

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.utilities.select_message_for_sending import select_random_msg, read_file_line_by_line, update_file

url_senders = "./assets/txt/200 accs.txt"
url_recipients = "./assets/txt/real_gmails.txt"
url_links = "./assets/txt/10kloveincsv.txt"
url_message = "./assets/txt/Slidebot messages 700.txt"
url_total_sent = "./assets/txt/slide_total_sent.txt"

url_total_sent = "./assets/txt/total_sent.txt"
url_recipients_backup = "./assets/txt/recipients_backup.txt"
url_body_links = "./assets/txt/R Bodylinks 100 Eng.txt"
url_txts = "./assets/txt/R Texts 100 Eng.txt"
url_subject = "./assets/txt/R Subjects 100 Eng.txt"
url_ricipients = "./assets/txt/recipients.txt"
url_bcc_links = "./assets/txt/gmail links total bitly.txt"
lock = threading.Lock()

def copy(string):
    pyperclip.copy(string)

def login(profile_dir, email, password, recovery_email):
    from undetected_chromedriver import Chrome, ChromeOptions
    chrome_options = ChromeOptions()
    chrome_options.add_argument(f"--user-data-dir={profile_dir}")
    driver = Chrome(options=chrome_options, version_main=114)
    driver.get("https://accounts.google.com")
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "identifier")))
        mail_input = driver.find_element(by=By.XPATH, value="//input[@name='identifier']")
        next_button = driver.find_element(by=By.ID, value="identifierNext")
        mail_input.send_keys(email)
        next_button.click()
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "Passwd")))
            password_input = driver.find_element(by=By.NAME, value="Passwd")
            next_button = driver.find_element(by=By.ID, value="passwordNext")
            ActionChains(driver=driver).move_to_element(password_input).click().send_keys(password).perform()
            ActionChains(driver=driver).move_to_element(next_button).click().perform()
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
                temp_array = ["uchitosato@gmail.com", "Stacho1988@gmail.com"]
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
                    copy(subject_content)
                    # subject.send_keys(subject_content + "!")
                    subject.send_keys(Keys.CONTROL + "v")
                    try:
                        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='Am Al editable LW-avf tS-tW']")))
                        # msg_body = driver.find_element(by=By.XPATH, value="//div[@aria-label='Message Body']")
                        msg_body = driver.find_element(by=By.XPATH, value="//div[@class='Am Al editable LW-avf tS-tW']")
                        time.sleep(1)
                        ActionChains(driver=driver).move_to_element(msg_body).click().perform()
                        msg_text = select_random_msg(url_txts)
                        # msg_body.send_keys(msg_text)
                        copy(msg_text)
                        msg_body.send_keys(Keys.CONTROL + "v")
                        msg_body.send_keys(Keys.CONTROL + Keys.END)             
                        msg_hyperlinks = select_random_msg(url_body_links)
                        bitlylinks = select_random_msg(url_bcc_links).strip()
                        try:
                            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='e5 aaA aMZ']")))
                            add_link = driver.find_element(by=By.XPATH, value="//div[@class='e5 aaA aMZ']")
                            add_link.click()
                        except:
                            pass
                        try:
                            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "linkdialog-text")))
                            label = driver.find_element(by=By.ID, value="linkdialog-text")
                            copy(msg_hyperlinks)
                            # label.send_keys(msg_hyperlinks)
                            label.send_keys(Keys.CONTROL + "v")
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
    slide_recipients = read_file_line_by_line(url_recipients)
    bcc_recipients = read_file_line_by_line(url_ricipients)
    if len(bcc_recipients) == 0:
        pass
    else:
        for k in range(0, 3):
            for i in range(30, 143):
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
                        for i in range(0, 1):
                            share_link = read_file_line_by_line(url_links)[0].strip()
                            share_slides(driver=driver, link=share_link)
                            update_file(url_links, 1)
                        # if i % 2 == 0:
                        #     update_file(url_links, 1)
                        try: 
                            for j in range(0, 1):
                                send_mail(driver=driver)
                        except:
                            pass
                    except:
                        pass
                except:
                    pass
                driver.close()
            time.sleep(200)
    print("sent all bcc")

if __name__ == "__main__":
    main()