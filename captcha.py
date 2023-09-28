CAPATCHA_API = 'd986a91575ce491c992f197b1209de67'
from selenium.webdriver.common.by import By
import time, os, sys
from onest_captcha import OneStCaptchaClient


def captcha_solver(driver):
    try:
        url = driver.current_url
        element = driver.find_element(By.XPATH,'//*[@data-site-key]')
        key = element.get_attribute("data-site-key")
        print(key)
        client = OneStCaptchaClient(apikey=CAPATCHA_API)
        result = client.recaptcha_v2_task_proxyless(site_url=url, site_key=key, invisible=True)
        if result["code"] == 0:  # success:
            print("sucessfull")
            print(result["token"])
            token = result["token"]

        else:  # wrong
            print(result["messeage"])

        time.sleep(2)
        driver.execute_script('var element=document.getElementById("g-recaptcha-response"); element.style.display="";')

        # Set captcha response
        script = f'document.getElementById("g-recaptcha-response").value = "{token}";'
        driver.execute_script(script)
        try:
            driver.execute_script(f"___grecaptcha_cfg.clients[0].l.l.callback('{token}')")
        except:
            try:
                driver.execute_script(f"___grecaptcha_cfg.clients[0].P.P.callback('{token}')")
            except:
                try:
                    driver.execute_script(f"___grecaptcha_cfg.clients[0].O.O.callback('{token}')")
                except:
                    driver.execute_script(f"___grecaptcha_cfg.clients[0].L.L.callback('{token}')")



    except Exception as e:
        print(e)
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)


