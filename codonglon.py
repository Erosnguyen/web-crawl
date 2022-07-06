from distutils.log import error
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


def read_data_from_csv(ticker):
    try:
        df = pd.read_csv(
            'C:/Users/Admin/Documents/code/python/curlUrl/'+str(ticker)+'.csv')
    except:
        print('An exception occurred')
    else:
        return(df)


def get_title(file):
    parttern = re.compile(
        r"\d\d/\d\d/\d\d\d\d")
    match = parttern.findall(file)
    for i in match:
        print(i)


companys = read_data_from_csv('dataCK')
for company in range(len(companys)):
    url = f"https://s.cafef.vn/hose/{companys.iloc[company][0]}/co-dong-lon.chn"
    driver = webdriver.Chrome(ChromeDriverManager().install())
    if(url):
        driver.get(url)
        try:
            codong = driver.find_element(
                By.XPATH, ".//div[@id='divViewCoDongLon']").get_attribute('innerText')
            with open('data9.txt', 'a', encoding="utf-8") as data10:
                data10.write(companys.iloc[company][0] + " |"+"\n")
                data10.write(codong+"\n")
        except:
            continue
    else:
        continue
