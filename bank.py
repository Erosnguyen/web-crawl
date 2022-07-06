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
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def read_data_from_csv(ticker):
    try:
        df = pd.read_csv(
            'C:/Users/Admin/Documents/code/python/curlUrl/'+str(ticker)+'.csv', index_col=False)
    except:
        print('An exception occurred')
    else:
        return(df)


bank = read_data_from_csv('bank')
for b in range(len(bank)):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    url = 'https://cafef.vn/'
    driver.get(url)
    driver.maximize_window()
    ignored_exceptions = (NoSuchElementException,
                          StaleElementReferenceException)

    time.sleep(3)
    search = driver.find_element(
        By.XPATH, '//*[@id="CafeF_SearchKeyword_Company"]')
    submit = WebDriverWait(driver, 3, ignored_exceptions=ignored_exceptions).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="CafeF_BoxSearchNew"]/div[1]/a')))
    search.send_keys(f'{bank.iloc[b,0]}')
    time.sleep(2)
    submit.click()
    time.sleep(5)
    for i in range(1, 6):
        l = WebDriverWait(driver, 3, ignored_exceptions=ignored_exceptions).until(
            EC.presence_of_element_located((By.XPATH, f'//*[@id="NLoaded"]/table/tbody/tr[{i+1}]')))
        with open('data14.txt', 'a', encoding='utf-8') as f:
            f.write(f'{bank.iloc[b,0]},'+l.get_attribute("innerText")+'\n')
    # logo = driver.find_element(
    #     By.CLASS_NAME, 'logo')
    # logo.click()
    time.sleep(15)
    driver.quit()
