from selenium import webdriver
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
            'C:/Users/Admin/Documents/code/python/curlUrl/'+str(ticker)+'.csv')
    except:
        print('An exception occurred')
    else:
        return(df)


def main_data(name):
    header = [f'{name};Chi so tai chinh']
    index = []
    col_1 = []
    col_2 = []
    col_3 = []
    col_4 = []
    tr = WebDriverWait(driver, 5, ignored_exceptions=ignored_exceptions).until(
        EC.presence_of_all_elements_located((By.XPATH, '//*[@id="table-2"]/tbody/tr')))
    up = WebDriverWait(driver, 5, ignored_exceptions=ignored_exceptions).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="table-2"]/thead')))
    head = up.find_elements(By.CLASS_NAME, 'text-center.col-100.al-middle')
    for i in range(len(head)):
        quarter = head[i].find_element(By.TAG_NAME, 'b')
        header.append(quarter.get_attribute('innerText'))
    for i in range(len(tr)):
        name_inside = tr[i].find_element(By.TAG_NAME, 'span')
        cl = tr[i].find_elements(By.CLASS_NAME, 'text-right')
        col_1.append(cl[0].get_attribute('innerText'))
        col_2.append(cl[1].get_attribute('innerText'))
        col_3.append(cl[2].get_attribute('innerText'))
        col_4.append(cl[3].get_attribute('innerText'))
        index.append(name_inside.get_attribute('innerText'))
    with open('data15.txt', 'a', encoding='utf-8') as f:
        for j in range(len(header)):
            f.write(str(header[j])+';')
        f.write('\n')
        for i in range(len(index)):
            f.write(str(name)+';'+str(index[i])+';'+str(col_1[i])+';'+str(
                col_2[i])+';'+str(col_3[i])+';'+str(col_4[i])+';'+'\n')
    time.sleep(0.2)


filter = read_data_from_csv('filter')
for i in range(len(filter)):

    driver = webdriver.Chrome(ChromeDriverManager().install())
    url = 'https://finance.vietstock.vn/'
    driver.get(url)
    action = ActionChains(driver)
    ignored_exceptions = (NoSuchElementException,
                          StaleElementReferenceException)
    log = WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[6]/div/div[2]/div[2]/a[3]')))
    action.move_to_element(to_element=log).click().perform()
    email = driver.find_element(By.XPATH, '//*[@id="txtEmailLogin"]')
    passwd = driver.find_element(By.XPATH, '//*[@id="txtPassword"]')
    submit = driver.find_element(By.XPATH, '//*[@id="btnLoginAccount"]')
    log.click()
    email.send_keys('cuong123go@gmail.com')
    passwd.send_keys('hungcu123@@')
    submit.click()
    time.sleep(2)
    search = driver.find_element(By.XPATH, '//*[@id="txt-top-filter"]')
    search.click()
    search_stock = driver.find_element(
        By.XPATH, '//*[@id="popup-search-txt"]')
    name = f"{filter.iloc[i]['name']}"
    search_stock.send_keys(name)
    time.sleep(3)
    search_stock.send_keys(Keys.RETURN)
    time.sleep(2)
    quarter_btn = WebDriverWait(driver, 3, ignored_exceptions=ignored_exceptions).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="finance-content"]/div/div/div[3]/div[1]/a[1]')))
    action.move_to_element(to_element=quarter_btn).click().perform()
    back = WebDriverWait(driver, 3, ignored_exceptions=ignored_exceptions).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="finance-content"]/div/div/div[3]/div[2]/div[2]')))
    time.sleep(1)
    while back:
        is_disabled = "disabled" in back.get_attribute("class")
        main_data(name)
        time.sleep(1)
        back.click()
        if is_disabled:
            main_data(name)
            time.sleep(1)
            driver.quit()
            break
