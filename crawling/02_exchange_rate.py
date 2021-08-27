import re
import requests as req

url = "https://finance.naver.com/marketindex/?tabSel=exchange#tab_section"
res = req.get(url)
body = res.text

r = re.compile(r"h_lst.*?blind\">(.*?)</span>.*?value\">(.*?)</", re.DOTALL)
captures = r.findall(body)

print("==============")
print("Exchange Rate Calculator")
print("==============")
print("")

for c in captures:
    print(c[0], ":", c[1])


usd = float(captures[0][1].replace(",", ""))
won = float(input("Input the WON you want to exchange to dollars => "))
dollar = int(won/usd)
print(f"{dollar}")
