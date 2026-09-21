import curl_cffi
from curl_cffi import requests
import requests as ar
import asyncio

# from curl_cffi.requests.headers import Headers

from camoufox.sync_api import Camoufox

link = "https://www.skiddle.com/festivals/search/?ajaxing=1&sort=0&fest_name=&from_date=20%20Sep%202026&to_date=&genre%5B%5D=pop&maxprice=500&o=48&bannertitle=April"
prooo = {"server": "socks5://31.59.138.171:1080"}
# test_link = "https://httpbin.org/headers"
with Camoufox(headless = True) as br:
    pagee = br.new_page()
    respo = pagee.goto(link, wait_until='networkidle')
    kuki = pagee.context.cookies()
    user_ag = respo.request.headers.get('user-agent')
    respo = pagee.goto(link, wait_until='networkidle')
    print(respo.status)
 
reque = requests.get(link, cookies= kuki, headers= {'User-Agent' : user_ag})
with open('l.txt', 'w', encoding='utf-8') as f:
    f.write(reque.text)


# request = curl_cffi.get(link, impersonate="chrome136", proxies=prooo, timeout=80)
# print(request.status_code)
# with Session(impersonate= 'chrome124') as s:
#     reque = s.get(test_link, allow_redirects=False)
#     print(reque.headers)
# reque = curl_cffi.get(test_link, impersonate= 'chrome120')
# print(reque.headers)
# cffi_header = Headers(browser="chrome").get_default_headers()
# print(cffi_header)
