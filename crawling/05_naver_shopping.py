from bs4 import BeautifulSoup as bs
import requests as req

url = "https://search.shopping.naver.com/search/all?query=%EB%86%80%EC%9D%B4%EB%B0%A9%EB%A7%A4%E3%85%8C&cat_id=&frm=NVSHATC"
res = req.get(url)
soup = bs(res.text, "html.parser")

arr = soup.select("ul.list_basis div > a:nth-of-type(1)")

for a in arr:
    if a.get('title'):
        print(a.get('title').strip())
    # print(a.get_text(strip=True))
