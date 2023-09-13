import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver import Firefox, FirefoxOptions
from undetected_chromedriver import Chrome, ChromeOptions


class Demo1:
    def __init__(self):
        self._init_chrome()
        # self._init_firefox()
        self.driver.set_window_size(1400, 800)

    def _init_chrome(self):
        opts = ChromeOptions()
        opts.add_argument('--incognito')
        opts.add_argument('--log-level=OFF')
        opts.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        self.driver = Chrome(options=opts, version_main=114)

    def _init_firefox(self):
        opts = FirefoxOptions()
        opts.set_preference('ui.key.menuAccessKeyFocuses', False)
        opts.set_preference('dom.webdriver.enabled', False)
        opts.set_preference('useAutomationExtension', False)
        opts.add_argument('--disable-blink-features=AutomationControlled')  # ???
        self.driver = Firefox(options=opts)

    def page1(self):
        self.driver.get('https://gmail.com')
        while True:
            WebDriverWait(self.driver, 8).until(
                EC.any_of(
                    EC.all_of(
                        EC.visibility_of_element_located((By.XPATH, '//h1[@id="headingText"]/span[text()="Sign in"]')),
                        EC.element_to_be_clickable((By.XPATH, '//input[@id="identifierId"]')),
                        EC.element_to_be_clickable((By.XPATH, '//button/span[text()="Next"]/..')),
                    ),
                    EC.all_of(
                        EC.url_contains('/gmail/about'),
                        EC.element_to_be_clickable(
                            (By.XPATH,
                             '//a[contains(@href,"https://accounts.google.com/AccountChooser/signinchooser")]')),
                    )
                )
            )
            if EC.url_contains('/gmail/about')(self.driver):
                a = self.driver.find_element(By.XPATH,
                                             '//a[contains(@href,"https://accounts.google.com/AccountChooser/signinchooser")]')
                a.click()
            else:
                break

    def test(self):
        cnt = 0
        while True:
            t0 = time.monotonic()
            self.page1()
            inp = self.driver.find_element(By.XPATH, '//input[@id="identifierId"]')
            inp.clear()
            s = str(int(time.time()))
            inp.send_keys(s)
            self.driver.find_element(By.XPATH, '//button/span[text()="Next"]/..').click()
            loc = (By.XPATH, '//input[@id="identifierId"]')
            WebDriverWait(self.driver, 8).until(
                EC.any_of(
                    EC.invisibility_of_element_located(loc),
                    EC.text_to_be_present_in_element_attribute(loc, 'aria-invalid', 'true'),
                    EC.visibility_of_element_located((By.XPATH, '//*[@id="captchaimg"]')),
                )
            )
            cnt += 1
            print(f'{cnt} passed in {time.monotonic() - t0}')
            time.sleep(5)


if __name__ == "__main__":
    d = Demo1()
    d.test()
