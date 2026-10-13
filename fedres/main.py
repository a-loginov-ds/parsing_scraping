from curl_cffi import requests
from camoufox.sync_api import Camoufox
from playwright.sync_api import sync_playwright

base_link = "https://yandex.ru/maps/api/masstransit/getVehiclesInfoWithRegion?ajax=1&csrfToken=138e6c28122afe9edae4f376cea620760e52d210%3A1791884888&lang=ru&ll=50.192182%2C53.215419&locale=ru_RU&s=2343437899&sessionId=1791884888825294-3630113134377858875-enqmiibfipsyxiv2-BAL&spn=0.014892%2C0.009467"
cook = "yandexuid=1805756561773161108; yuidss=1805756561773161108; receive-cookie-deprecation=1; gdpr=0; _ym_uid=1773161110335851228; ymex=1814269087.yrts.1782733087; amcuid=1650739431784747816; _ym_d=1784798432; ancQTZw=1; is_gdpr=0; is_gdpr_b=CO+MChDSmAMoAg==; yashr=5902041411788778998; maps_aadb=1; pi=VbC9DGHMPbeSJJgU25uxKPyR5ZsjElWGWT2LQcVIvx0SnHp4VXCUsu615PwNJrnpDBxV8FSYB0OSVPpeG6qZjaplCeg=; i=ihk/wUSS+XMUw1iyoaIS0fuY5MpHQ8U72XwUkaVzPA9LXIMYI8qGjP00wUB1XQ6D0vTY2JCXSqdJ4vVcXRRsn6nW/YE=; spravka=dD0xNzkxNTIzNjgxO2k9OTQuNzcuNy4xNDY7RD03OUFBNTVFNTc5ODY1OEYwMURGMDA3MjBEM0NBM0U0RUY1NzI3MjkzMDE0QkFDQUY4RUZDQjFERTBDMDM1NkQyODJGNDI3M0U3RkE4RUQ3RDc5QzcwOEVERDMzOTFBRDkxMjk1RTdGNThCNUE0NTJCQTg3NjM3NDM0RDM0QzhBQTc2MDlGRkUxQTEzM0UyMTY0RUY5QjUzODMyMUQ4NzI5REM7dT0xNzkxNTIzNjgxMDc5MjQxMjUxO2g9ODk2MzUyZTE2Yjg4ODA0NTc5ODdhMGM1ZmUwM2YzZjM=; L=ehBXQktCBlhidU1ifFBGbVlTQ1YFc0hBLxE/LVxcIEBJEiIAV1E=.1791544986.2232615.318134.3e26976b4f86895d39b9f54c1998be32; yandex_login=; yp=1816283803.favs_hls.1784747803677#1816283803.favs_hsc.1#1794201925.hdrc.1#1792128361.szm.1_25%3A1680x1050%3A1521x735%3A15#2107193056.pcs.0#1797017054.atds.1#2106905108.multib.1#1792408599.dlp.1; maps_session_id=1791884888825294-3630113134377858875-enqmiibfipsyxiv2-BAL; yandex_expboxes=1704154%2C0%2C61%3B1687304%2C0%2C81%3B1707342%2C0%2C17%3B1721897%2C0%2C95%3B1690091%2C0%2C89%3B663872%2C0%2C45%3B663860%2C0%2C3%3B1708003%2C0%2C36; _ym_isad=2; bh=EjkiQnJhdmUiO3Y9IjE1NSIsICJDaHJvbWl1bSI7dj0iMTU1IiwgIk5vdChBOkJyYW5kIjt2PSIyNCIaBSJ4ODYiIgkxNTUuMC4wLjAqAj8wMgIiIjoJIldpbmRvd3MiQggiMTkuMC4wIkoEIjY0IlJLIkJyYXZlIjt2PSIxNTUuMC4wLjAiLCAiQ2hyb21pdW0iO3Y9IjE1NS4wLjAuMCIsICJOb3QoQTpCcmFuZCI7dj0iMjQuMC4wLjAiWgI/MGDf/LfWBmoe3Mrh/wiS2KGxA5/P4eoD+/rw5w3r//32D6G1zYcI; _yasc=AA7iV2qwQiUVecnFU1M6mdxPTnq/ephZ34MjcuDseS0Sq8A7ahrmHcdg6VfMlhOmDMMitlQy74hDQWpDQhmr47HX7KQ8UKb9oQUoiPTSyTS1++BIhm1ZzIZaT4fxEuuwbO2braOrMhqdmS0WlCYSwcKcs3VOhLYXvASvn7TnH9+sRT+0pa9reMgZXAlFoSExN+ZT3sS7WyQs8jjfoZqLUFmepzyob4dQWe2yAgF1YQwqWIzl7Jrc5ocrhXNh/hqjE+KejbxuhM+cdXQanmN4zgm+.MTc5MDY3NTM1NjUzOQ=="

cookie_string = cook

cookies = dict(
    item.strip().split("=", 1)
    for item in cookie_string.split(";")
    if "=" in item
)

resp = requests.get(
    base_link,
    cookies=cookies,
    impersonate="chrome",
    timeout=30,
)

print(resp.status_code)
print(resp.text)
while True:
    pass