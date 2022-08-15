from click import Command
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.select import Select1
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert

def text():
    options = webdriver.ChromeOptions()
    options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    b = webdriver.Chrome(chrome_options=options)
    b.maximize_window()
    b.get("http://192.168.1.111:10050/index")
    b.find_element_by_name("username").send_keys("admin")
    b.find_element_by_name("password").send_keys("123456")
    b.find_element_by_xpath("/html/body/div[1]/div[1]/form/div[1]/div[3]/input").send_keys("0")
    b.find_element_by_id("btnSubmit").click()
    time.sleep(2)
    js = b.find_element_by_xpath("/html/body/div[3]/div")
    print(js.text)
    if text() == '验证码错误':
        b.find_element_by_xpath("/html/body/div[1]/div[1]/form/div[1]/div[3]/input").send_keys("0")
        b.find_element_by_id("btnSubmit").click()
        time.sleep(2)
    else:
        print("登录成功")


if text() == '验证码错误':
    print("验证码错误")
else:
    print("登录成功1")

