from os import read
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import re
import numpy as np
import datetime as dt
import pandas as pd
import matplotlib as mpl
from matplotlib import pyplot as plt
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(ChromeDriverManager().install())
url = 'https://finance.vietstock.vn/ket-qua-kinh-doanh'
driver.get(url)
ignored_exceptions = (NoSuchElementException,
                      StaleElementReferenceException)
log = driver.find_element(
    By.XPATH, '/html/body/div[2]/div[6]/div/div[2]/div[2]/a[3]')
email = driver.find_element(By.XPATH, '//*[@id="txtEmailLogin"]')
passwd = driver.find_element(By.XPATH, '//*[@id="txtPassword"]')
submit = driver.find_element(By.XPATH, '//*[@id="btnLoginAccount"]')
log.click()
email.send_keys('cuong123go@gmail.com')
passwd.send_keys('hungcu123@@')
submit.click()
time.sleep(5)
for i in range(1, 37):
    btn = driver.find_element(By.XPATH, '//*[@id="btn-page-next"]/i')
    table = WebDriverWait(driver, 5, ignored_exceptions=ignored_exceptions).until(
        ec.presence_of_element_located((By.XPATH, '//*[@id="kqkd-content"]/table')))
    with open('data10.txt', 'a', encoding='utf-8') as f:
        f.write(table.get_attribute('innerText') + "\n")
    time.sleep(3)
    btn.click()
