from bs4 import BeautifulSoup as bs
import requests as req

url = "https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user"
res = req.get(url, headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
})
soup = bs(res.text, "html.parser")


# list comprehension
for desc in soup.select("div.descriptions-inner"):
    ads = desc.select("span.ad-badge-icon")
    if len(ads) > 0:
        print("광고!")
    else:
        print(desc.select("div.name")[0].get_text(strip=True))
