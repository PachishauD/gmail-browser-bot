from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# login to google account
def driver_chrome_incognito(proxy_ip):

    proxy_port = 3128
    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Disable automation detection
    chrome_options.add_argument("--disable-infobars")  # Disable infobars
    chrome_options.add_argument("--disable-notifications")  # Disable notifications
    chrome_options.add_argument("--disable-popup-blocking")  # Disable popup blocking
    chrome_options.add_argument("--disable-extensions")  # Disable extensions
    chrome_options.add_argument("--disable-dev-shm-usage")  # Disable /dev/shm usage
    chrome_options.add_argument("--disable-browser-side-navigation")  # Disable browser side navigation
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
    chrome_options.add_argument("--no-sandbox")  # Disable sandbox mode
    chrome_options.add_argument("--ignore-certificate-errors")  # Ignore certificate errors
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument('--proxy-server={}:{}'.format(proxy_ip, proxy_port))
    driver = webdriver.Chrome(options=chrome_options)
    return driver