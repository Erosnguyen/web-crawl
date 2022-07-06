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
from selenium.webdriver.support import expected_conditions

ck = ['AAA']


def read_data_from_csv(ticker):
    try:
        df = pd.read_csv(
            'C:/Users/Admin/Documents/code/python/curlUrl/'+str(ticker)+'.csv', index_col=False)
    except:
        print('An exception occurred')
    else:
        return(df)


read = read_data_from_csv('company name')
companys = pd.DataFrame(read)
driver = webdriver.Chrome(ChromeDriverManager().install())

for company in np.array(companys.iloc[:, 0]):
    url = f"https://s.cafef.vn/Lich-su-giao-dich-{companys.loc[company][1]}-4.chn"
    if url:
        driver.get(url)
        try:
            whole_page = driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_ctl03_panelAjax"]/div/div/div[3]/div/table')
            parttern = re.compile(r"(\d*)\s+")
            match1 = parttern.finditer(whole_page.get_attribute('innerText'))
            for m in match1:
                t = int(m.group(1))+1
                print(t)
                page = driver.find_element(
                    By.XPATH, f'//*[@id="ctl00_ContentPlaceHolder1_ctl03_panelAjax"]/div/div/div[3]/div/table/tbody/tr/td[{t}]')
                if page:
                    page.click()
                    ignored_exceptions = (NoSuchElementException,
                                          StaleElementReferenceException)
                    tr = WebDriverWait(driver, 2, ignored_exceptions=ignored_exceptions).until(
                        expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_ctl03_panelAjax"]/div/table/tbody')))
                    with open('data10.txt', 'a', encoding='utf-8') as f:
                        f.write(tr.get_attribute('innerText')+'\n')
                        time.sleep(2)
                else:
                    continue
        except:
            continue
    else:
        continue


# def cal_page(numpage):
#     page = driver.find_element(
#         By.XPATH, f'//*[@id="ctl00_ContentPlaceHolder1_ctl03_panelAjax"]/div/div/div[3]/div/table/tbody/tr/td[{numpage}]')
#     return page


# for company in range(len(ck)):
#     url = f"https://s.cafef.vn/Lich-su-giao-dich-{ck[company]}-4.chn"
#     driver.get(url)
#     action = ActionChains(driver)
#     page = cal_page(1)
#     page.click()
#     ignored_exceptions = (NoSuchElementException,
#                           StaleElementReferenceException)
#     tr = WebDriverWait(driver, 2, ignored_exceptions=ignored_exceptions).until(
#         expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_ctl03_panelAjax"]/div/table/tbody')))
#     with open('data10.txt', 'a', encoding='utf-8') as f:
#         f.write(tr.get_attribute('innerText')+'\n')
#         time.sleep(2)
#     action.click(cal_page(2)).perform()
# for company in range(len(ck)):
#     url = f"https://s.cafef.vn/Lich-su-giao-dich-{ck[company]}-4.chn"
#     if url:
#         driver.get(url)
#         whole_page = driver.find_element(
#             By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_ctl03_panelAjax"]/div/div/div[3]/div/table')
#         parttern = re.compile(r"(\d*)\s+")
#         match1 = parttern.finditer(whole_page.get_attribute('innerText'))
#         match = []
#         for m in match1:
#             t = int(m.group(1))
#             match.append(t)
#         for i in range(len(match)):
#             print(i)
#             find_tr = driver.find_element(
#                 By.XPATH, f'//*[@id="ctl00_ContentPlaceHolder1_ctl03_panelAjax"]/div/div/div[3]/div/table/tbody/tr/td[{match[-1]+2}]')
#             next_page = find_tr.find_element(
#                 By.TAG_NAME, "a")
#             next_page.click()
#             ignored_exceptions = (NoSuchElementException,
#                                   StaleElementReferenceException)
#             tr = WebDriverWait(driver, 2, ignored_exceptions=ignored_exceptions).until(
#                 expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_ctl03_panelAjax"]/div/table/tbody')))
#             with open('data10.txt', 'a', encoding='utf-8') as f:
#                 f.write(tr.get_attribute('innerText')+'\n')
#                 time.sleep(2)
#     else:
#         print('error')
