import requests as req


url = "https://api.imgur.com/3/image?client_id=546c25a59c58ad7"

# read binary
with open("./materials/img.png", "rb") as f:
    img = f.read()

print(len(img))

res = req.post(url, files={
    "image": img,
    "type": "file",
    "name": "img.png"
})
print(res.status_code)
print(res.text)
link = res.json()["data"]["link"]
print(link)

html = f"""
<html>
<head>
  <title>uploaded image</title>
</head>
<body>
  <img src="{link}">
</body>
</html>
"""

with open("image.html", "w") as f:
    f.write(html)
