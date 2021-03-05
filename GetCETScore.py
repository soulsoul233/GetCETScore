
import requests
import json
import pandas as pd

xlsx = pd.ExcelFile('data.xlsx')
df = pd.read_excel(xlsx, 'StudentTemplate')
NameLine = ""
ZKZHLine = ""
Quantity = ""
NAME = []
ZKZH = []
for i in range(0, int(Quantity), 1):
    NAME.append(data[i][int(NameLine)])
for i in range(0, int(Quantity), 1):
    ZKZH.append(data[i][int(ZKZHLine)])


for i in range(0, int(Quantity), 1):
    GET = f"https://zfbxcx.gjzwfw.gov.cn/jimp/jiaoyubu/interfaces/cet.do?name={NAME[i]}&zkzh={ZKZH[i]}"
    SCORE = requests.get(GET)
    print(SCORE.text)





