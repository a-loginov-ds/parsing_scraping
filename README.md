# Playwright
## from playwright.sync_api import sync_playwright 
## from playwright.async_api import async_playwright
## from camoufox.async_api import AsyncCamoufox

### browser.. with ... as p:
- p.webkit.launch() iPhone
    - headless = bool
    - timeout = ...
    - downloads_path = ...
    - proxy = ..
    - args = ['...']
        - "--disable-blink-features=AutomationControlled" - No driver
        - "--no-sandbox"
        - "--disable-infobars" info boxes...
        - "--disable-extensions
        - "--disable-gpu"
        - "--disable-background-networking"
        - "--disable-software-rasterizer" No 3D
        - "--disable-translate"

- p.chromium.launch()
## contectst browser.new_context()
### cookies()
- proxy = 
- user_agent = '..'
- viewport = {"width": 1280, "height": 720}
- geolocation = {"latitude": 55.75, "longitude": 37.61}
- is_mobile= bool
- java_script_enabled= bool

##  page = browser.new_page()
    - reload()
- .goto(..., timeout = ... wait_until = domcontentloaded/networkidle/commit)
- .get_by_role(role, name = '...', timeout = ...)
- .get_by_text()
- locator.click(, timeout = ...)
- .title(, timeout = ...)
- .screenshot(path = '.png')
- .fill('txt')
- .dblclick()
- .press_sequentially('text...)
- .locator()
- .press("Enter")
- .drag_to(...)



#
#
#
# GET 
## r = curl_cffi. ... :anchor:
- .get(URL)
    - :green_circle:impersonate = ... (mb from standart pack)
    - params = /...?... (after '/' sep '?')
    - :green_circle:headers = {'User-Agent' : ' '} (mb cusom)
    - stream = True
        - for _ in r.iter_content(): .... GENERATOR
    - allow_redirects = False
    - auth=("my_user", "password123")
    - proxy = "http://user:pass@example.com:3128"
    - proxies = {
    "http": "http://localhost:3128",\
     "https": "http://localhost:3128" }
     - ja3 = ..
     - akamai ...
     - http_version = "v1, v2, v3, v3only"

- .get_fingerprint
    - impersonate = ...  after getting can change only needed
## Reading responce
responce = ...get(...)
- :green_circle:.text 
- :green_circle:.content
- :green_circle:.status_code
- :green_circle:.headers
- :green_circle:.history
- :green_circle:.cookies
# Post
## r = curl_cffi. ...
- .post(URL)
    - data = {'data' : 'Value'}
    - json = {'data' : 'Value'}
- .CurlMime() --Files--
    - r.addpart
        - name = "name in the form"
        - content_type="image/png"
        - filename="image.png" 
        - local_path="./image.png" / data=file.read() # in memory
# Session
### :green_circle:from curl_cffi import Session
## s = curl_cffi.Session()
- cache = (timedelta(minutes=5))
- :green_circle:count=3 (times)
- :green_circle:delay=0.2 (sec)
- :green_circle:jitter=0.1 (sec)
- :green_circle:backoff="exponential"/"constant"/"linear"
- :green_circle:max_delay=10.0 (sec)          # 
- retry_statuses={500, 502, 503, 504, 429} react to...
- retry_methods={"GET", "POST", "PUT"}
- raise_for_status= bool 
- discard_cookies = True/False
- .upkeep() # re session
# Asyncio 
## from curl_cffi import AsyncSession
# C level applications
## from curl_cffi.curl import CurlOpt, CurlInfo
 - .curl.setopt(CurlOpt. ...)
    - :green_circle:.VERBOSE, bool # all log to console
    - :green_circle:.MAX_RECV_SPEED_LARGE, int # download speed
    - .SSL_VERIFYPEER, bool # SSl sertificate
    - .HTTP_VERSION , int # 1.1, 2.0 ..
    - .TIMEOUT, num # max time
    - .CONNECTTIMEOUT, num 
    - .MAXREDIRS, int # max redirecting..
    - .NOBODY, bool # get() or head()
    - :green_circle:.DEBUGFUNCTION, funk ...(type, text or 0)  # __call__ lambda a, b: (
            check_logs.append(b.decode("utf-8", errors="ignore")) 
            if a in (0, 1, 2) else 0)
- curl.getinfo(CurlInfo. ...)
    - .NAMELOOKUP_TIME # time DNS -> IP
    - :green_circle:.CONNECT_TIME # TCP connections
    - :green_circle:.APPCONNECT_TIME # time of TLS/SSL handsheke
    - :green_circle:.TOTAL_TIME 
    - .REDIRECT_TIME # all time redirectings
    - :green_circle:.SPEED_DOWNLOAD 
    - .PRIMARY_IP 
    - .SSL_VERIFYRESULT # ssl problem
    
#
#
#
# Selectolax
## HTMLParser
### from selectolax.parser import HTMLParser
### from selectolax.lexbor import LexborHTMLParser
#### tree = HTMLParser(text(str or bytes))
#### tree = LexborHTMLParser \("<\div>Привет</\div>", is_fragment=True)
- .any_css_matches(selectors)
- .body
- .css(need selectors)
- .css_first(str, default = 'text if not find')
- .head
- .html - all HTML
- .text(deep= True, separator = '', strip = False)
- .attributes
- .attrs
- .parent
- .next
- .prev
- .id
- .tag
- .text_lexbor
- .text_content

# RE ------ r'.....'
 - .search(pattern, str)
 - .findall(pattern, str)
### Symbols
- . everything exept \n
- ^ - start of string
- $ finish of string
- /* 0 or >
- /+ 1 or >
- ? 0 or 1
- {min, max} - {exact} - {min, } - {, max}
- [] everything what inside
- [^ ...] everything exept...
- \d digit 0-9
- \D --> \d
- \s every ' ' --> ' ', \n, \t
- \w a-zA-Z0-9_
## rounds
- (?=...) forward not block
- (?!...) forward block
- (?<=...) back not block
- (?<!...) back block
### re.INGORECASE or re.I