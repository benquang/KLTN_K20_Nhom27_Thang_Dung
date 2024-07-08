import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from items import *

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
driver = uc.Chrome(options=options)
wait = WebDriverWait(driver, 15)
driver.get('https://nowsecure.nl')
driver.save_screenshot('nowsecure.png')
driver.quit()