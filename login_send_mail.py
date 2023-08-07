

import time
import time
import pyperclip
import pickle
import multiprocessing

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
url_senders = "./assets/txt/senders.txt"
url_ricipients = "./assets/txt/recipients.txt"
url_links = "./assets/txt/links.txt"
url_message = "./assets/txt/First Msgs 300.txt"
url_reply_message = "./assets/txt/Reply Message 200 Eng.txt"
url_total_sent = "./assets/txt/total_sent.txt"
url_total_reply = "./assets/txt/total_reply.txt"
url_disabled = "./assets/accounts/disabled.txt"
url_recipients_backup = "./assets/txt/recipients_backup.txt"

recipients = read_file_line_by_line(url_ricipients)
num = 0

def copy(string):
    pyperclip.copy(string)

def login(profile_dir, email, password, recovery_email):
    from undetected_chromedriver import Chrome, ChromeOptions
    chrome_options = ChromeOptions()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument(f"--user-data-dir={profile_dir}")
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument("--log-level=OFF")
    chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
    driver = Chrome(options=chrome_options, version_main = 114)

    # # Navigate to the Google login page
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

    driver.get("https://gmail.com")
    # Save the profile for later use
    return driver

def send_mail(driver, msg_content, recipient_email):
    driver.get("https://gmail.com")
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='T-I T-I-KE L3']")))
        driver.find_element(by=By.XPATH, value="//div[@class='T-I T-I-KE L3']").click()
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@class='agP aFw']")))
            recipient = driver.find_element(by=By.XPATH, value="//input[@class='agP aFw']")
            print(recipient_email)
            try:
                ActionChains(driver=driver).move_to_element(recipient).send_keys(recipient_email).perform()
                time.sleep(1)
                try:
                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "subjectbox")))
                    subject = driver.find_element(by=By.NAME, value="subjectbox")
                    subject_content ='{0}'.format(recipient_email.split('@')[0]).strip().capitalize()
                    subject.send_keys(subject_content + "!")
                    time.sleep(1)
                    try:
                        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='Am Al editable LW-avf tS-tW']")))
                        # msg_body = driver.find_element(by=By.XPATH, value="//div[@aria-label='Message Body']")
                        msg_body = driver.find_element(by=By.XPATH, value="//div[@class='Am Al editable LW-avf tS-tW']")
                        time.sleep(1)
                        time.sleep(1)
                        ActionChains(driver=driver).move_to_element(msg_body).click().perform()
                        msg_body.send_keys("Hi, " + subject_content + "!" + "\n")
                        time.sleep(1)
                        # msg_body.send_keys(msg_content)
                        copy(msg_content)
                        msg_body.send_keys(Keys.CONTROL + "v")
                        time.sleep(1)
                        try:
                            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='T-I J-J5-Ji aoO v7 T-I-atl L3']")))
                            send_button = driver.find_element(by=By.XPATH, value="//div[@class='T-I J-J5-Ji aoO v7 T-I-atl L3']")
                            send_button.click()
                            print("---------------------------------------------------------->")
                            total_sent = int(read_file_line_by_line(url_total_sent)[0])
                            total_reply = int(read_file_line_by_line(url_total_reply)[0])
                            total_sent += 1
                            print("<----------Total sent: " + format(total_sent) + " Total reply: " + format(total_reply) + "---------->")
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

def watch_unread_gmails(driver):
    print("watching.....")
    total_reply = int(read_file_line_by_line(url_total_reply)[0])
    # time.sleep(1000)
    try:
        WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "//div[@class='aio UKr6le']")))    
        inbox_button = driver.find_element(by=By.XPATH, value="//div[@class='aio UKr6le']")
        inbox_button.click()
        print("x")
        try:
            unread_email = driver.find_element(by=By.XPATH, value="//tr[@class='zA zE']")
            email_senders = unread_email.find_elements(by=By.XPATH, value='//span[@class="zF"]')
            recipients = read_file_line_by_line(url_recipients_backup)
            temp_mails = []
            print("y")
            for email_sender in email_senders:
                if email_sender.get_attribute("email") in temp_mails:
                    continue
                else:
                    temp_mails.append(email_sender.get_attribute("email"))
            for temp_mail in temp_mails:
                if temp_mail.strip() + '\n' in recipients:
                    reply_msg = select_random_msg(url_reply_message).split(":")[0] + " : " + select_random_msg(url_links)
                    total_reply += 1
                    send_mail(driver=driver, msg_content=reply_msg, recipient_email=temp_mail)
                    with open(url_total_reply, "w", encoding="utf-8") as reply:
                        reply.write(format(total_reply))
                    print(format(total_reply) + " recipients replied to this bot!")
                    # ActionChains(driver=driver).move_to_element(unread_email).click().perform()
                else:
                    pass
                    # print(email)
            time.sleep(1)
            select_all = driver.find_element(by=By.XPATH, value="//div[@class='T-I J-J5-Ji T-Pm T-I-ax7 L3 J-JN-M-I']")
            time.sleep(2)
            select_all.click()
            time.sleep(2)
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@class='T-I J-J5-Ji nX T-I-ax7 T-I-Js-Gs mA']")))
            time.sleep(2)
            mark_read = driver.find_element(by=By.XPATH, value="//div[@class='T-I J-J5-Ji nX T-I-ax7 T-I-Js-Gs mA']")
            time.sleep(2)
            ActionChains(driver=driver).move_to_element(mark_read).click().perform()
            time.sleep(2)

        except:
            print("h")
            pass
        # else:
            # driver.close()
            # email_body = email.find_element_by_xpath('.//span[@class="y2"]').text
    except:
        print("g")
        pass

def main():
    senders = read_file_line_by_line("./assets/txt/senders.txt")
    num_senders = len(senders)
    while True:
        recipients = read_file_line_by_line(url_ricipients)
        if len(recipients) == 0:
            break
        else:
            for i in range(0, num_senders):
                email = senders[i].split(",")[0].strip()
                password = senders[i].split(",")[1].strip()
                recovery = senders[i].split(",")[2].strip()
                profile_subfix = '{0}'.format(email.split('@')[0]).strip().capitalize()
                profile_name = "Profile " + profile_subfix
                profile_dir = f"C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\User Data\\{profile_name}"
                
                print(profile_dir)
                driver = login(profile_dir=profile_dir, email=email, password=password, recovery_email=recovery)
                for i in range(0, 10):
                    Message = select_random_msg("./assets/txt/First Msgs 300.txt")
                    recipients = read_file_line_by_line(url_ricipients)
                    Recipient = recipients[0].strip()
                    send_mail(driver=driver, msg_content=Message, recipient_email=Recipient)
                    update_file(url_ricipients, 1)
                    time.sleep(2)
                watch_unread_gmails(driver=driver)
                driver.quit()


if __name__ == "__main__":
    process = multiprocessing.Process(target=main)
    process.start()