# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

for i in range(1):
    # 资源的url & headers
    url = "http://soft.duba.com/c2_7.htm"
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}

    # 发送GET请求获取链接返回内容
    response = requests.get(url, headers=headers)
    response.encoding = response.apparent_encoding

    # 使用BeautifulSoup解析返回内容
    soup = BeautifulSoup(response.text, "html.parser")
    context = soup.find_all('div', class_='fl')

    # 转换数据类型后再次find_all
    data_1 = str(context)
    soup2 = BeautifulSoup(data_1,"html.parser")

    data_2 = list(soup2.find_all('img'))

    # 取出html里需要的数据
    for s in range(10):
        data_3 = str(data_2[s]).split(",")
        data_4 = str(data_3).split("\"")
        # print(data_4[1], data_4[5])

        # 写入文件
        with open(".\软件信息.txt",'a') as f:
            f.write(data_4[1]+' '+data_4[5]+'\n')
            f.close()

        with open(".\软件介绍.txt",'a') as f:
            f.write(data_4[1]+' 软件介绍'+'\n')
            f.close()

