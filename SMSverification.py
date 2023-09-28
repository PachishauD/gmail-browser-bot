import os, subprocess, sys, time, re
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
try:
    from smsactivate.api import SMSActivateAPI
except:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'smsactivate'])
    from smsactivate.api import SMSActivateAPI
from selenium.webdriver.support.ui import Select
API_SMS = '0445e4Ab50d5fb53830deA51ff4591b9'


def version_two_number_generator_based_on_condition(driver):
    # hit the api till you get nice response


    while True:
        while True:
            try:
                sa = SMSActivateAPI(API_SMS)
                # sa.debug_mode = True
                sa.setStatus(status=1)
                break
            except Exception as error:
                print("this error during hit api", str(error))
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)

        select_country = Select(driver.find_element(By.XPATH, '//*[@id="countryList"]'))

       
        #elif try_number <= 3:
        if True:
            try:
                number = sa.getNumber(service='go', country=6, maxPrice = 'freePrice')
                select_country.select_by_value('ID')
            except:
                try:
                    number = sa.getNumber(service='go', country=22)
                    select_country.select_by_value('IN')
                except:
                    number = sa.getNumber(service='go', country=0)
                    select_country.select_by_value('RU')

       

        try:
            if number['error'] != "NO_NUMBERS":
                print("We got a number")
                break
            else:
                print(number)
                #try_number = try_number + 1
                continue
        except Exception as e:
            print("error for testing", str(e))
            break
    print(number)
    return number,sa


def version_one_number_generator_based_on_condition(driver, consumption):
    # hit the api till you get nice response

    sa = None
    number = None
    
    while True:
        while True:
            try:
                sa = SMSActivateAPI(API_SMS)
                # sa.debug_mode = True
                sa.setStatus(status=1)
                break
            except:
                continue

        if consumption == 0:
            print("First time SMS verification will use Polish Number")
            try:
                country = "poland"
                number = sa.getNumber(service='go', country=15)
                driver.find_element(By.XPATH, '//*[@id="countryList"]/div/div[1]').click()
                element = driver.find_element(By.XPATH, '//*[@id="countryList"]/div/div[2]/ul/li[169]/span[1]')
                actions = ActionChains(driver)
                actions.move_to_element(element).perform()
                time.sleep(3)
                driver.execute_script("arguments[0].click();", element)
                time.sleep(2)
                # input("check what exist in the phone cell")
                phone_number_cell = driver.find_element(By.XPATH, '//*[@id="phoneNumberId"]')
                phone_number_cell.clear()
                # input("check what exist in the phone cell 2")
            except Exception as error:
                print("There's no polish number availabe let's try Chile")
            try:
                if number['error'] == "NO_NUMBERS":

                        country = "Chile"
                        number = sa.getNumber(service='go', country=151)
                        driver.find_element(By.XPATH, '//*[@id="countryList"]/div/div[1]').click()
                        element = driver.find_element(By.XPATH, '//*[@id="countryList"]/div/div[2]/ul/li[46]/span[1]')
                        actions = ActionChains(driver)
                        actions.move_to_element(element).perform()
                        time.sleep(3)
                        driver.execute_script("arguments[0].click();", element)
                        time.sleep(2)
                        # input("check what exist in the phone cell")
                        phone_number_cell = driver.find_element(By.XPATH, '//*[@id="phoneNumberId"]')
                        phone_number_cell.clear()
            except Exception as error:
                pass
                #print("error during choosing chile ", str(error))
                #input()
                #exc_type, exc_obj, exc_tb = sys.exc_info()
                #fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                #print(exc_type, fname, exc_tb.tb_lineno)
            try:
                if number['error'] == "NO_NUMBERS":

                    print("There's no Chilian number availabe let's try Neitherland")
                    country = "Neitherland"
                    number = sa.getNumber(service='go', country=48)
                    driver.find_element(By.XPATH, '//*[@id="countryList"]/div/div[1]').click()
                    element = driver.find_element(By.XPATH, '//*[@id="countryList"]/div/div[2]/ul/li[148]/span[1]')
                    actions = ActionChains(driver)
                    actions.move_to_element(element).perform()
                    time.sleep(3)
                    driver.execute_script("arguments[0].click();", element)
                    time.sleep(2)
                    # input("check what exist in the phone cell")
                    phone_number_cell = driver.find_element(By.XPATH, '//*[@id="phoneNumberId"]')
                    phone_number_cell.clear()

            except:
                pass

        else:
            try:
                number = sa.getNumber(service='go', country=0)
            except:
                try:
                    country = "India"
                    number = sa.getNumber(service='go', country=22)

                    element = driver.find_element(By.XPATH, '//*[@id="countryList"]/div/div[2]/ul/li[99]/span[1]')
                    actions = ActionChains(driver)
                    actions.move_to_element(element).perform()
                    time.sleep(3)
                    driver.execute_script("arguments[0].click();", element)
                except:
                    country = "Indonesia"
                    number = sa.getNumber(service='go', country=6)
                    element = driver.find_element(By.XPATH, '//*[@id="countryList"]/div/div[2]/ul/li[100]/span[1]')
                    actions = ActionChains(driver)
                    actions.move_to_element(element).perform()
                    time.sleep(3)
                    driver.execute_script("arguments[0].click();", element)


        try:
            if number['error'] != "NO_NUMBERS":
                print("We got a number")
            else:
                print(number)
                #country_list=["Poland", "Chile","Neitherland"]
                #try_number = try_number + 1
                continue

        except Exception as e:
            print("error for testing", str(e))
            break
    print(number)
    return number, sa


def activate_phone_number_during_login(driver,consumption):
    sms_verification_status = None
    number_validation_status = True
    message = None

    try:



        number, sa = version_one_number_generator_based_on_condition(driver, consumption)

        activation_id = number['activation_id']
        phone_number = str(number['phone'])


        driver.find_element(By.XPATH, '//*[@id="phoneNumberId"]').send_keys(phone_number)

        # time.sleep(7)

        driver.find_element(By.XPATH, '//*[@id="idvanyphonecollectNext"]/div/button').click()

        time.sleep(5)

        if number_validation_status:
            message = sa.getFullSms(activation_id)
            counter_time = 0

            while message == 'STATUS_WAIT_CODE':
                time.sleep(1)
                # print(message)
                counter_time = counter_time + 1
                if counter_time == 60:
                    sms_verification_status = "TimeOut"
                    sa.setStatus(id=activation_id, status=8)
                    print("it's time out let's try to get other number")
                    #input("it's time out let's check what to do")
                    break
                try:
                    message = sa.getFullSms(activation_id)

                    message = re.findall(r'\d+', message)[0]
                except Exception as error:
                    # print("this error in the checking errors for number as sms ", str(error))
                    # exc_type, exc_obj, exc_tb = sys.exc_info()
                    # fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    # print(exc_type, fname, exc_tb.tb_lineno)
                    continue

        if sms_verification_status != 'STATUS_WAIT_CODE':
            driver.find_element(By.XPATH,'//*[@id="idvAnyPhonePin"]').send_keys(message)
            driver.find_element(By.XPATH,'//*[@id="idvanyphoneverifyNext"]').click()
            sms_verification_status = True
            time.sleep(5)
            sa.setStatus(id=activation_id, status=6)
        if message == 'STATUS_WAIT_CODE':
            sms_verification_status = "TimeOut"

    except Exception as error:
        print("error during sms verification ", str(error))
        sms_verification_status = False

    return sms_verification_status





def activate_phone_number_during_login2(driver,try_number,internal_tries):


    number_validation_status = None
    sms_verification_status = None
    sa = None
    activation_id = None
    
    try:
        number, sa = version_two_number_generator_based_on_condition(driver)
        activation_id = number['activation_id']
        phone_number = str(number['phone'])
        the_whole_process_counter = 0

        while True:
            print("we entering the while true of error checking now")
            phone_number_fild = driver.find_element(By.XPATH, '//*[@id="deviceAddress"]')
            phone_number_fild.clear()
            phone_number_fild.send_keys(phone_number)
            driver.find_element(By.XPATH, '//*[@id="next-button"]').click()
            time.sleep(5)
            print("we finished the pasting number and clicked next button")
            try:
                print("we on the try")
                check_usage_of_number = driver.find_element(By.XPATH, '//*[@id="error"]').text
                print("bad number", check_usage_of_number)
                internal_tries = internal_tries+1
                try_number = try_number + 1
                print("we finished the try and going to check the if conditions")
                if internal_tries >= 10:
                    sa.setStatus(id=activation_id, status=8)
                    sms_verification_status = "Internal_Tries"
                    number_validation_status = False
                    break
                if len(check_usage_of_number) > 3:
                    print("We got an error ", check_usage_of_number)
                    sa.setStatus(id=activation_id, status=8)
                    number, sa = version_two_number_generator_based_on_condition(driver)
                    activation_id = number['activation_id']
                    phone_number = str(number['phone'])
                    continue
                    
            except Exception as e:
                print("we didn't get any errors")
                #exc_type, exc_obj, exc_tb = sys.exc_info()
                #fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                #print(exc_type, fname, exc_tb.tb_lineno)
                number_validation_status = True
                break

        if number_validation_status:
            print("this number is good to use")
            message = sa.getFullSms(activation_id)
            counter_time = 0
            while message == 'STATUS_WAIT_CODE':
                time.sleep(1)
                #print(message)
                counter_time = counter_time + 1
                if counter_time == 60:
                    sms_verification_status = "TimeOut"
                    sa.setStatus(id=activation_id, status=8)
                    print("it's time out let's try to get other number")
                    break
                try:
                    message = sa.getFullSms(activation_id)

                    message = re.findall(r'\d+', message)[0]
                except Exception as error:
                    #print("this error in the checking errors for number as sms ", str(error))
                    #exc_type, exc_obj, exc_tb = sys.exc_info()
                    #fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    #print(exc_type, fname, exc_tb.tb_lineno)
                    continue

            if message != 'STATUS_WAIT_CODE':
                driver.find_element(By.XPATH, '//*[@id="smsUserPin"]').send_keys(message)
                driver.find_element(By.XPATH, '//*[@id="next-button"]').click()
                time.sleep(5)
                sms_verification_status = True
                sa.setStatus(id=activation_id, status=6)

            if message == 'STATUS_WAIT_CODE':
                sms_verification_status = "TimeOut"
                sa.setStatus(id=activation_id, status=8)
    except Exception as error:
        print("error during sms verification ", str(error))
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        sms_verification_status = False

    if sms_verification_status != True:
        sa.setStatus(id=activation_id, status=8)
    #print("sms_verification_status from activate_phone_number_during_login2 ", sms_verification_status)
    return sms_verification_status

def main_sms_verifier(driver, status,consumption):
    sms_verification_status = None
    if status == "new_version_sms_page":
        print(status)
        for i in range(0, 10):
            sms_verification_status = activate_phone_number_during_login(driver, consumption)

            if sms_verification_status == "TimeOut":
                print("try number {}".format(i))
                driver.back()
                time.sleep(2)
                continue
            else:
                break

    elif status == "old_version_sms_page":
        print(status)
        for i in range(1, 10):
            ##print("This number didn't work let's try new one")

            sms_verification_status = activate_phone_number_during_login2(driver, i, internal_tries=0)
            if sms_verification_status == "Internal_Tries":
                break
            if sms_verification_status == "TimeOut":
                print("try number {}".format(i))
                driver.back()
                time.sleep(2)
                try:
                    phone_number_field=driver.find_element(By.XPATH, '//*[@id="deviceAddress"]')
                    phone_number_field.clear()
                except:
                    pass
                continue
            else:
                break
            
    return sms_verification_status

#sa = SMSActivateAPI(API_SMS)
#sa.setStatus(status=1)
#print(sa.getNumber(service='go', country=22))