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


def read_data_from_csv(ticker):
    try:
        df = pd.read_csv(
            'C:/Users/Admin/Documents/code/python/curlUrl/'+str(ticker)+'.csv')
    except:
        print('An exception occurred')
    else:
        return(df)


url = 'https://s.cafef.vn/du-lieu-doanh-nghiep.chn#data'
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
action = ActionChains(driver)
ignored_exceptions = (NoSuchElementException,
                      StaleElementReferenceException)
upcom = WebDriverWait(driver, 5, ignored_exceptions=ignored_exceptions).until(ec.presence_of_element_located(
    (By.XPATH, '//*[@id="CafeF_ThiTruongNiemYet_TabButton_XemUpCom"]')))
upcom.click()
time.sleep(2)
see_all = WebDriverWait(driver, 5, ignored_exceptions=ignored_exceptions).until(
    ec.presence_of_element_located((By.XPATH, '//*[@id="CafeF_ThiTruongNiemYet_Trang"]/a[2]')))
see_all.click()
time.sleep(2)
amen = driver.find_element(
    By.XPATH, '//*[@id="CafeF_ThiTruongNiemYet_Content"]/table/tbody')
with open('data13.txt', 'a', encoding='utf-8') as f:
    f.write(amen.get_attribute('innerText'))
