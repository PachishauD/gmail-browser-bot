import base64
import time

import requests


def convert_img_to_base64(img_path):
    with open(img_path, "rb") as img_file:
        b64_string = base64.b64encode(img_file.read())
        return b64_string.decode("utf8")


class OneStCaptchaClient:
    def __init__(self, apikey):
        self.apikey = apikey
        self.BASE_URL = "https://api.1stcaptcha.com"

    def get_balance(self):
        r = requests.get(f"{self.BASE_URL}/user/balance?apikey=" + self.apikey)
        if r.status_code == 200:
            data = r.json()
            if data['Code'] == 0:
                return data['Balance']
            else:
                raise RuntimeError("Error " + str(data))
        else:
            raise RuntimeError("Error " + r.text)

    def get_result(self, task_id, timeout, time_sleep, type_captcha=""):
        t_start = time.time()
        while (time.time() - t_start) < timeout:
            r = requests.get(f"{self.BASE_URL}/getresult?apikey=" + self.apikey + "&taskid=" + str(task_id))
            if r.status_code == 200:
                data = r.json()
                if data['Code'] == 0:
                    if data['Status'] == "SUCCESS":
                        if type_captcha == "image2text" or type_captcha == "recaptcha_click":
                            return data["Data"]
                        elif type_captcha == "v3_enterprise":
                            return data["Data"]
                        return data["Data"]["Token"]
                    elif data['Status'] == "ERROR":
                        raise Exception(data["Message"])
                    time.sleep(time_sleep)
                else:
                    raise RuntimeError("Error " + data["Message"])
            else:
                raise RuntimeError("Error " + r.text)
        raise RuntimeError("TIMEOUT")

    def recaptcha_v2_task_proxyless(self, site_url, site_key, invisible=False, timeout=180, time_sleep=1):
        try:
            r = requests.get(
                f"{self.BASE_URL}/recaptchav2?apikey={self.apikey}&sitekey={site_key}&siteurl={site_url}&version=v2&invisible={str(invisible).lower()}"
            )
            if r.status_code == 200:
                data = r.json()
                if data['Code'] == 0:
                    task_id = data['TaskId']
                else:
                    raise RuntimeError("Error " + str(data))
            else:
                raise RuntimeError("Error " + r.text)
            return {"code": 0, "token": self.get_result(task_id, timeout, time_sleep)}
        except Exception as e:
            return {"code": 1, "messeage": str(e)}

    def recaptcha_v2_enterprise_task_proxyless(self, site_url, site_key, timeout=180, time_sleep=1):
        try:
            r = requests.get(
                f"{self.BASE_URL}/recaptchav2_enterprise?apikey={self.apikey}&sitekey={site_key}&siteurl={site_url}"
            )
            if r.status_code == 200:
                data = r.json()
                if data['Code'] == 0:
                    task_id = data['TaskId']
                else:
                    raise RuntimeError("Error " + str(data))
            else:
                raise RuntimeError("Error " + r.text)
            return {"code": 0, "token": self.get_result(task_id, timeout, time_sleep)}
        except Exception as e:
            return {"code": 1, "messeage": str(e)}

    def recaptcha_v3_task_proxyless(self, site_url, site_key, page_action, min_score: float = 0.3, timeout=180,
                                    time_sleep=1):
        try:
            r = requests.get(
                f"{self.BASE_URL}/recaptchav3?apikey={self.apikey}&sitekey={site_key}&siteurl={site_url}&version=v3&pageaction={page_action}&minscore={min_score}"
            )
            if r.status_code == 200:
                data = r.json()
                if data['Code'] == 0:
                    task_id = data['TaskId']
                else:
                    raise RuntimeError("Error " + str(data))
            else:
                raise RuntimeError("Error " + r.text)
            return {"code": 0, "token": self.get_result(task_id, timeout, time_sleep)}
        except Exception as e:
            return {"code": 1, "messeage": str(e)}

    def recaptcha_v3_enterprise_task_proxyless(
            self,
            site_url,
            site_key,
            page_action,
            min_score: float = 0.3,
            timeout=180,
            time_sleep=1
    ):
        try:
            r = requests.get(
                f"{self.BASE_URL}/recaptchav3_enterprise?apikey={self.apikey}&sitekey={site_key}&siteurl={site_url}&pageaction={page_action}&minscore={min_score}"
            )
            if r.status_code == 200:
                data = r.json()
                if data['Code'] == 0:
                    task_id = data['TaskId']
                else:
                    raise RuntimeError("Error " + str(data))
            else:
                raise RuntimeError("Error " + r.text)
            result = self.get_result(task_id, timeout, time_sleep, type_captcha="v3_enterprise")
            return {"code": 0, "token": result.get("Token"), "user_agent": result.get("UserAgent")}
        except Exception as e:
            return {"code": 1, "messeage": str(e)}

    def fun_captcha_task_proxyless(self, site_url, site_key, timeout=180, time_sleep=3):
        try:
            r = requests.get(
                f"{self.BASE_URL}/funcaptchatokentask?apikey={self.apikey}&sitekey={site_key}&siteurl={site_url}"
            )
            if r.status_code == 200:
                data = r.json()
                if data['Code'] == 0:
                    task_id = data['TaskId']
                else:
                    raise RuntimeError("Error " + str(data))
            else:
                raise RuntimeError("Error " + r.text)
            return {"code": 0, "token": self.get_result(task_id, timeout, time_sleep)}
        except Exception as e:
            return {"code": 1, "messeage": str(e)}

    def recaptcha_click(self, url_list, caption, timeout=60, time_sleep=3):
        try:
            r = requests.post(
                f"{self.BASE_URL}/recognition",
                json={'Image_urls': url_list, 'Caption': caption, "Apikey": self.apikey, "Type": "recaptcha"}
            )
            if r.status_code == 200:
                data = r.json()
                if data['Code'] == 0:
                    task_id = data['TaskId']
                else:
                    raise RuntimeError("Error " + str(data))
            else:
                raise RuntimeError("Error " + r.text)
            return {"code": 0, "token": self.get_result(task_id, timeout, time_sleep, type_captcha="recaptcha_click")}
        except Exception as e:
            return {"code": 1, "messeage": str(e)}

    def image_to_text(self, base64img=None, file=None, timeout=60, time_sleep=1):
        try:
            if base64img is None:
                if file is None:
                    raise RuntimeError("base64img and file is None ")
                else:
                    base64img = convert_img_to_base64(file)
            r = requests.post(
                f"{self.BASE_URL}/recognition", json={
                    'Image': base64img, "Apikey": self.apikey, "Type": "imagetotext"
                })
            if r.status_code == 200:
                data = r.json()
                if data['Code'] == 0:
                    task_id = data['TaskId']
                else:
                    raise RuntimeError("Error " + str(data))
            else:
                raise RuntimeError("Error " + r.text)
            return {"code": 0, "token": self.get_result(task_id, timeout, time_sleep, type_captcha="image2text")}
        except Exception as e:
            return {"code": 1, "messeage": str(e)}
