import requests
from bs4 import BeautifulSoup
import os

Url = "https://oto.com.vn/"
os.mkdir("photo_car")
for i in range(5):
    res = requests.get(Url+"mua-ban-xe-cu-da-qua-su-dung/p" + str(i))
    soup = BeautifulSoup(res.content,"html.parser")
    links = soup.select(".box-list-car > .item-car > .photo > a > img")
    i = 1
    for index, link in enumerate(links):
        if i <= len(links):
            img_data = requests.get(link["data-src"]).content
            with open("photo_car\\" +str(index+1)+'.jpg','wb+') as f:
                f.write(img_data)
                i +=1
        else:
            f.close()
            break