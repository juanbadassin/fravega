from selenium import webdriver
import os
from configparser import ConfigParser
from selenium.webdriver.chrome.options import Options


def before_all(context):
    config = ConfigParser()
    print((os.path.join(os.getcwd(), 'setup.cfg')))
    my_file = (os.path.join(os.getcwd(), 'setup.cfg'))
    config.read(my_file)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=1420,1080')
    chrome_options.add_argument('--headless')
    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.maximize_window()
    context.driver.implicitly_wait(30)


def after_all(context):
    context.driver.close()
