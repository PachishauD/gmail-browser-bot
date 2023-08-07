import time
import time
import pyperclip
import pickle
import random
import threading

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
# driver = webdriver.Chrome()

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

def driver_chrome_incognito():
    from undetected_chromedriver import Chrome, ChromeOptions
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument('--encoding=UTF-8')
    chrome_options.add_argument("--log-level=OFF")
    chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
    driver = Chrome(options=chrome_options, version_main = 114)
    return driver


def login_to_gmail(driver, email, password, recovery_email, disable_index):
    driver.get("https://gmail.com")
    try:
        WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.NAME, "identifier")))
        input_email = driver.find_element(by=By.XPATH, value="//input[@name='identifier']")
        email_next = driver.find_element(by=By.ID, value="identifierNext")
        input_email.send_keys(email)
        email_next.click()
        time.sleep(2)
        try:
            WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.NAME, "Passwd")))
            input_password = driver.find_element(by=By.NAME, value="Passwd")
            password_Next = driver.find_element(by=By.ID, value="passwordNext")
            input_password.send_keys(password)
            ActionChains(driver=driver).move_to_element(password_Next).click().perform()
            time.sleep(2)
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
                try:
                    WebDriverWait(driver, 100).until(EC.presence_of_all_elements_located((By.XPATH, "//span[@jsname='V67aGc']")))
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
    return driver

def send_mail(driver, msg_content, recipient_email):
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='T-I T-I-KE L3']")))
        driver.find_element(by=By.XPATH, value="//div[@class='T-I T-I-KE L3']").click()
        time.sleep(1)
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@class='agP aFw']")))
            recipient = driver.find_element(by=By.XPATH, value="//input[@class='agP aFw']")
            recipient.send_keys(recipient_email)
            time.sleep(1)
            try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "subjectbox")))
                subject = driver.find_element(by=By.NAME, value="subjectbox")
                subject_content ='{0}'.format(recipient_email.split('@')[0]).strip().capitalize()
                subject.send_keys(subject_content)
                time.sleep(1)
                try:
                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='Am Al editable LW-avf tS-tW']")))
                    # msg_body = driver.find_element(by=By.XPATH, value="//div[@aria-label='Message Body']")
                    msg_body = driver.find_element(by=By.XPATH, value="//div[@class='Am Al editable LW-avf tS-tW']")
                    time.sleep(1)
                    time.sleep(1)
                    ActionChains(driver=driver).move_to_element(msg_body).click().perform()
                    # msg_body.send_keys(msg_content)
                    copy(msg_content)
                    msg_body.send_keys(Keys.CONTROL + "v")
                    time.sleep(2)
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
    # return driver

def watch_unread_gmails(driver):
    print("watching.....")
    total_reply = int(read_file_line_by_line(url_total_reply)[0])
    # time.sleep(1000)
    try:
        WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "//div[@class='aio UKr6le']")))    
        inbox_button = driver.find_element(by=By.XPATH, value="//div[@class='aio UKr6le']")
        inbox_button.click()
        
        try:
            unread_email = driver.find_element(by=By.XPATH, value="//tr[@class='zA zE']")
            email_senders = unread_email.find_elements(by=By.XPATH, value='//span[@class="zF"]')
            recipients = read_file_line_by_line(url_recipients_backup)
            temp_mails = []
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
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@class='T-I J-J5-Ji m9 T-I-ax7 L3']")))
            time.sleep(2)
            mark_read = driver.find_element(by=By.XPATH, value="//div[@class='T-I J-J5-Ji m9 T-I-ax7 L3']")
            time.sleep(2)
            ActionChains(driver=driver).move_to_element(mark_read).click().perform()
            time.sleep(2)

        except:
            pass
        # else:
            # driver.close()
            # email_body = email.find_element_by_xpath('.//span[@class="y2"]').text
    except:
        pass
    # return driver
    


def send_watch(index):
    senders = read_file_line_by_line(url_senders)
    print(senders[index])
    Email = senders[index].split(",")[0].split()
    Passwd = senders[index].split(",")[1].split()
    Recovery = senders[index].split(",")[2].split()
    Driver = driver_chrome_incognito()
    Login= login_to_gmail(driver=Driver, email=Email, password=Passwd, recovery_email=Recovery, disable_index=(index+1))
    while True:
        for i in range(0, 30):
            recipients = read_file_line_by_line(url_ricipients)
            num_recipients = len(recipients)
            if num_recipients == 0:
                break
            else:
                Message = select_random_msg(url_message)
                Recipient = recipients[0]
                send_mail(driver=Login, msg_content=Message, recipient_email=Recipient.strip())
                update_file(url_ricipients, 1)
                Login.get("https://gmail.com")
                time.sleep(3)
        watch_unread_gmails(driver=Login)
        time.sleep(30)

        

def main():
    threads = []
    senders = read_file_line_by_line(url_senders)
    for i in range(0, len(senders)):
        threads.append(threading.Thread(target=lambda:send_watch(index=i)))
        threads[i].start()
        time.sleep(10)

if __name__ == '__main__':
    main()

