import subprocess
import json
from this import s
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
respones = requests.get(
    "https://s.cafef.vn/hose/AAA-cong-ty-co-phan-nhua-an-phat-xanh.chn")
soup = BeautifulSoup(respones.text, "lxml")

