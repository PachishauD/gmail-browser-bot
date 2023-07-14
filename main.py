import time
import xlrd
import threading, time
import random
import pyautogui
import pyperclip

from email.parser import Parser
from email.message import EmailMessage

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from src.utilities.constants import PROXY_IP, PROXY_PORT, RECIPIENT_ADDRESS, SMTP_SERVER, SMTP_INTERVAL, POP3_SERVER, POP3_INTERVAL
from src.utilities.select_message_for_sending import select_random_msg, read_file_line_by_line
# driver = webdriver.Chrome()

sender = []
senders = []
recipients = read_file_line_by_line("./assets/txt/recipients_backup.txt")
number_of_recipients = len(recipients)
recipients_backup = recipients
senders_file = xlrd.open_workbook("./assets/xls/50-pcs-2020-16.6.xlsx") 
senders_list = senders_file.sheet_by_index(0)
number_of_senders = senders_list.nrows

total_sent = 0
total_reply = 0
total_recive = 0

def copy(string):
    pyperclip.copy(string)

for i in range(0, number_of_senders):
    senders.append(i)

def driver_chrome_incognito():
    from undetected_chromedriver import Chrome, ChromeOptions
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument('--encoding=UTF-8')
    chrome_options.add_argument("--log-level=OFF")
    chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
    driver = Chrome(options=chrome_options, version_main = 114)

    #driver.get("https://www.google.com")
    # print("----------------------------------------------------------------------------------------------")
    return driver


def login_to_gmail(driver, index, status):
    relogin_driver = driver
    email = senders_list.cell_value(index, 0)
    password = senders_list.cell_value(index, 1)
    recovery_email = senders_list.cell_value(index,2)
    driver.get("https://gmail.com")
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
            print("This account was disabled!")
            if status == "sending":
                senders.remove(index)
                with open("./assets/accounts/disabled.txt", "a", encoding="utf-8") as disabled_accs:
                    disabled_accs_list = read_file_line_by_line("./assets/accounts/disabled.txt")
                    if email + "\n" not in disabled_accs_list:
                        disabled_accs.write(email + "\n")
            else:
                return driver
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
    return driver

def send_mail(driver, msg_content, recipient_email, is_reply):  
    global total_sent
    global total_reply
    try:
        driver.find_element(by=By.XPATH, value="//div[@class='T-I T-I-KE L3']").click()
        time.sleep(1)
        try:
            recipient = driver.find_element(by=By.XPATH, value="//input[@class='agP aFw']")
            recipient.send_keys(recipient_email)
            time.sleep(1)
            try:
                subject = driver.find_element(by=By.NAME, value="subjectbox")
                subject_content ='{0}'.format(recipient_email.split('@')[0]).strip()
                subject.send_keys(subject_content)
                time.sleep(1)
                try:    
                    msg_body = driver.find_element(by=By.XPATH, value="//div[@aria-label='Message Body']")
                    time.sleep(1)
                    # encoded_msg = msg_content.encode("utf-8")
                    time.sleep(1)
                    ActionChains(driver=driver).move_to_element(msg_body).click().perform()
                    copy(msg_content)
                    msg_body.send_keys(Keys.CONTROL + "v")
                    time.sleep(2)
                    # print("entered message")
                    try:
                        send_button = driver.find_element(by=By.XPATH, value="//div[@class='T-I J-J5-Ji aoO v7 T-I-atl L3']")
                        send_button.click()
                        print("---------------------------------------------------------->")
                        if is_reply == "no_reply":
                            total_sent += 1
                            print("This bot totally sent: " + format(total_sent) + " emails!")
                        else:
                            total_reply += 1
                            print("This bot totally replied: " + format(total_reply) + " emails!")
                            
                        print("<----------Total sent: " + format(total_sent) + " Total reply: " + format(total_reply) + "---------->")
                        time.sleep(2)

                    except:
                        # print("Cannot find send button")
                        pass
                except:
                    # print("Cannot find msg body!")
                    pass
            except:
                # print("cannot find subject!")
                pass
        except:
            # print("Cannot find receipient!")
            pass
    except:
        # print("Cannot find 'Compose' button'!")
        pass

    return driver

def watch_unread_gmails(index):
    global total_recive
    init_driver = driver_chrome_incognito()
    driver = login_to_gmail(driver=init_driver, index=index, status="listening")
    try:
        inbox_button = driver.find_element(by=By.XPATH, value="//div[@class='aio UKr6le']")
        inbox_button.click()
        time.sleep(5)
        try:
            unread_gmails = driver.find_elements(by=By.XPATH, value="//tr[@class='zA zE']")
            time.sleep(1)
            if len(unread_gmails) == 0:
                driver.close()
            else:
                time.sleep(1)
                for email in unread_gmails:
                    # email_subject = email.find_element(by=By.XPATH, value='//span[@class="bqe"]').text()
                    email_sender = email.find_element(by=By.XPATH, value='//span[@class="zF"]').get_attribute('email')
                    recipients = read_file_line_by_line("./assets/txt/recipients test.txt")
                    if email_sender.strip() + '\n' in recipients:
                        # print("This sender is in recipients!")
                        reply_msg = select_random_msg("assets/txt/Reply Message 200 Eng.txt").split(":")[0] + " : " + select_random_msg("assets/txt/links.txt")
                        send_mail(driver=driver, msg_content=reply_msg, recipient_email=email_sender, is_reply="reply")
                        print("------------------------------------------------->")
                        total_recive += 1
                        print(format(total_recive) + " recipients replied to this bot!")
                        time.sleep(1)
                        ActionChains(driver=driver).move_to_element(email).click().perform()
                        time.sleep(1)
                        ActionChains(driver=driver).move_to_element(inbox_button).click().perform()
                        time.sleep(1)
                        continue
                    time.sleep(1)
                # email_body = email.find_element_by_xpath('.//span[@class="y2"]').text
        except:
            # print("cannot find such class!")
            pass
    except:
        # print("cannot find inbox button")
        pass

    driver.close()

def send_in_loop():
    recipient_index = 0
    while True:
        number_of_recipients = len(recipients_backup)
        number_of_senders_backup = len(senders)
        # number_of_loop = int(number_of_recipients / number_of_senders_backup)
        number_of_loop = 200
        try:
            if number_of_recipients == 0:
                break
            elif number_of_recipients <= number_of_senders:
                for i in senders:
                    driver = driver_chrome_incognito()
                    time.sleep(1)
                    login_driver = login_to_gmail(driver=driver, index=i, status="sending")
                    msg_content = select_random_msg("assets/txt/First Message 200 Eng.txt")
                    random_number = random.randrange(0, number_of_recipients)
                    send_mail(driver=login_driver, msg_content=msg_content, recipient_email=recipients[recipient_index].strip(), is_reply="no_reply")
                    recipients_backup.remove(recipients_backup[recipient_index])
                    number_of_recipients = len(recipients_backup)
                    recipient_index += 1
                    time.sleep(1)
                driver.close()
            else:
                for i in senders:
                    driver = driver_chrome_incognito()
                    time.sleep(1)
                    login_driver = login_to_gmail(driver=driver, index=i, status="sending")
                    for j in range(0, number_of_loop):
                        msg_content = select_random_msg("assets/txt/First Message 200 Eng.txt")
                        try:
                            recipient_index = random.randrange(0, number_of_recipients)
                            send_mail(driver=login_driver, msg_content=msg_content, recipient_email=recipients[recipient_index].strip(), is_reply="no_reply")
                            recipients_backup.remove(recipients_backup[recipient_index])
                            number_of_recipients = len(recipients_backup)
                            time.sleep(1)
                            recipient_index += 1
                        except:
                            pass
                    driver.close()
        except:
            pass
    
    print("Sent to all recipients!")
    

def main():
    # thread_sender = threading.Thread(target=send_in_loop)
    # thread_sender.start()
    # thread_sender.join()
    # send_in_loop()
    
    while True:
        for i in senders:
            time.sleep(2)
            index = number_of_senders - i -1
            # threading.Thread(target=lambda:watch_unread_gmails(index=i)).start()
            watch_unread_gmails(index=index)

if __name__ == '__main__':
    main()

