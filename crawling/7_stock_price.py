from bs4 import BeautifulSoup as bs
import requests as req


url = "https://sg.finance.yahoo.com/most-active"
res = req.get(url)
soup = bs(res.text, "html.parser")

for tr in soup.select("table tbody tr"):
    title = tr.select("td:nth-child(1) a")[0].get_text(strip=True)
    price = tr.select("td:nth-child(3) span")[0].get_text(strip=True)
    change = tr.select("td:nth-child(5) span")[0].get_text(strip=True)

    print(title, price, change)
