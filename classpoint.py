from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from names import FIRST, LAST
from random import choice
from time import sleep
import pyautogui

##################################################################################
random_names = True
bot_name_input = 'Name'
bot_amount_input = 15
pin = 16585
##################################################################################

PATH = "chromedriver/chromedriverwindows.exe"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/" \
             "537.36 (KHTML, like Gecko) Chrome/" \
             "87.0.4280.88 Safari/537.36"
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument(f"user-agent={USER_AGENT}")
options.add_argument("--window-size=1920,1080")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--allow-running-insecure-content")
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")


def create_bot(pin, bot_name):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    driver.get("https://classpoint.app/join")
    pin_entry = driver.find_element_by_name("classcode")
    pin_entry.send_keys(pin)
    pin_entry.send_keys(Keys.RETURN)
    bot_name_entry = driver.find_element_by_name("name")
    bot_name_entry.send_keys(bot_name + str(i + 1))
    bot_name_entry.send_keys(Keys.RETURN)
    
    sleep(0.45)

for i in range(bot_amount_input):
    if random_names:
        bot_name_input = choice(FIRST) + choice(LAST)
    create_bot(pin, bot_name_input)
    pyautogui.hotkey('ctrl','w')

end = ''
while end == '':
    end = input("done? ")
    if end == "done":
        driver.quit()
        print("bots deleted")
    else:
        end = ''
