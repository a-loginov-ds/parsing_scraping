import json
import curl_cffi
from selectolax.parser import HTMLParser

with open(
    r"C:\Users\zizu9\Desktop\Python's_projects\parsing_scraping\l_01.py\data.html",
    encoding="utf-8",
) as file:
    scr = file.read()

tree = HTMLParser(scr)
title = tree.css_first("title").text()
user_id = tree.css_first("div .user__name").text().strip()
user_info = tree.css(".user__info span")
links = tree.css_first(".social__networks").css("li a")
url_s = []
for i in links:
    url_s.append(i.attributes.get("href"))

another_links = []
links_2 = tree.css("a")
for i in links_2:
    print(f"{i.text()} : {i.attributes.get('href')}")
