import time

from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome

EXE_PATH = "C:\\Users\\matan\\Documents\\Python Scripts\\Bots\\chromedriver.exe"
PROMPT = " spam generator by philip "
TARGET = '"אופיר שמש"'


def get_msg():
    return PROMPT + time.strftime("%H:%M:%S")


def _spam_msg(target, msg):
    driver = Chrome(executable_path=EXE_PATH)
    driver.get("https://web.whatsapp.com/")
    wait = WebDriverWait(driver, 600)
    x_arg = '//span[contains(@title,' + target + ')]'
    group_title = wait.until(presence_of_element_located((By.XPATH, x_arg)))
    group_title.click()
    while True:
        message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
        message.send_keys(msg())
        sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
        sendbutton.click()
        time.sleep(1)
    driver.close()


_spam_msg(TARGET, get_msg)
