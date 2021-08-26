import requests as req

res = req.get("https://www.naver.com/")
# print(res.text)
print(res.status_code)


# Find My IP
# http://api.ipify.org/
res = req.get("http://api.ipify.org/")
print(res.text)
# 내가 보낸 request를 확인 가능. 항상 짝지어져 있으니깐
print(res.request.method)
print(res.request.headers)
print(res.elapsed)
# bite value, using when scraping the image or video etc.
print(res.raw)
