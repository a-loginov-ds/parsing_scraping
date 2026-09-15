import curl_cffi
from selectolax.lexbor import LexborHTMLParser
import json
import os
import csv
import time
# url = (
#     "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"
# )
user_ag = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36"
}
# req = curl_cffi.get(url=url, headers=user_ag)
# tree = LexborHTMLParser(req.text)
# with open(r'.\parsing_scraping\l_02\web_wite_fata.html', 'w', encoding='utf-8') as f:
#     f.write(tree.html)


# with open(r"parsing_scraping\l_02\web_wite_fata.html", encoding="utf-8") as f:
#     src = f.read()
# tree = LexborHTMLParser(src)
# all_cat = {}
# for cat in tree.css(".mzr-tc-group-item-href"):
#     te = cat.text()
#     links = f"https://health-diet.ru{cat.attributes.get('href')}"
#     all_cat[te] = links
# with open(r"parsing_scraping\l_02\start_links.json", "w", encoding="utf-8") as file:
#     json.dump(all_cat, file, indent=4, ensure_ascii=False)

with open(r"parsing_scraping\l_02\start_links.json", encoding="utf-8") as file:
    all_cat = json.load(file)
loo = len(all_cat)
count = 1
for links in all_cat:
    
    os.makedirs(fr'parsing_scraping\l_02\{links}', exist_ok=True) # Create folders
    requst = curl_cffi.get(all_cat[links], headers=user_ag) # Add HTML DOM
    with open(fr'parsing_scraping\l_02\{links}\{links}.html', 'w', encoding='utf-8') as f: # Save in case..
        f.write(requst.text)
    tree = LexborHTMLParser(requst.text)
    thr = tree.css_first('thead tr')
    if thr is None:
            print(fr'На {links} нету таблицы...')
            count += 1
            time.sleep(.3)
            continue
    head = thr.css('th') # Headers
    strings = tree.css('tbody tr')
    with open(fr'parsing_scraping\l_02\{links}\{links}.csv', 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file,delimiter=';')
        writer.writerow([th.text(strip = True) for th in head])
        for i in strings:
            temp = []
            for j in i.css('td'):

                temp.append(j.text().strip())
            writer.writerow(temp)
    print(f'{links} я завершил... делаю паузу осталось {loo - count} из {loo} STATUS {requst.status_code}')
    count += 1
    time.sleep(.3)
