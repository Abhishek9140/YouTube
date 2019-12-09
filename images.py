import requests as r
from bs4 import BeautifulSoup as bs
import urllib as u

url = "https://github.com"
html = r.get(url)

s = bs(html.text, "html.parser")
img = s.find_all("img")
k = 1
for i in img:
    url_img = i.get("src")
    if url_img != "" and "https://" in url_img:
        f_name = "github_imgs/"+str(k)+".jpg"
        u.request.urlretrieve(url_img, filename=f_name)
        k += 1
