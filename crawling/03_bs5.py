from bs4 import BeautifulSoup as bs
import requests as req

url = "https://finance.naver.com//marketindex/exchangeList.nhn"
res = req.get(url)

soup = bs(res.text, "html.parser")
# print(soup.title)
# print(soup.title.string)

tds = soup.find_all("td")


names = []
for td in tds:
    if len(td.find_all("a")) == 0:
        continue
    # print(td.get_text(strip=True))
    names.append(td.get_text(strip=True))

prices = []
for td in tds:
    if "class" in td.attrs:
        if "sale" in td.attrs["class"]:
            prices.append(td.get_text(strip=True))

print(names)
print(prices)


# CSS SELECTOR
names = []
for td in soup.select("td.tit"):
    names.append(td.get_text(strip=True))

prices = []
for td in soup.select("td.sale"):
    prices.append(td.get_text(strip=True))

print(names)
print(prices)
