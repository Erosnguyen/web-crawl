import re
from sre_parse import FLAGS

f = open('data10.txt', encoding='utf-8')


def get_date(file):
    parttern = re.compile(
        r"\d\d/\d\d/\d\d\d\d")
    match = parttern.findall(file)
    with open('data12.txt', 'a', encoding='utf-8') as f:
        for i in match:
            f.write(i+'\n')


def get_slcp(file):
    parttern = re.compile(
        r"\d{1,3}?\,?\d{0,3}\,?\d{0,3}\,?\d{0,3}\scp\b")
    match = parttern.findall(file)
    for i in match:
        print(i)


def get_volume(file):
    parttern = re.compile(r"(\b\d+\.\d\b)\s")
    match = parttern.finditer(file)
    for i in match:
        print(i.group(1))


def get_title(file):
    parttern = re.compile(r"^(\b[A-Z]{3}\b)\s+")
    match = parttern.finditer(file, re.MULTILINE)
    for m in match:
        print(m.group(1))
    # print(match)


def get_name(file):
    match2 = re.sub(
        'TÊN CỔ ĐÔNG SỐ CỔ PHIẾU TỶ LỆ % TÍNH ĐẾN NGÀY', ' ', file)
    parttern = re.compile(
        r"(\b[A-Z].[^\d]+\b).+(\b\d\d/\d\d/\d\d\d\d\b)\s+")
    match = parttern.finditer(str(match2), re.MULTILINE)
    with open('data11.txt', 'a', encoding='utf8') as f:
        for m in match:
            f.write(m.group(1)+'\n')


get_volume(f.read())
