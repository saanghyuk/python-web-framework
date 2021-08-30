from bs4 import BeautifulSoup as bs


html = """
<html>
<body>
  <div>Hello, World</div>
</body>
</html>
"""


soup = bs(html, "html.parser")
div = soup.select("div")
print(div[0].get_text(strip=True))


# enabled
arr = soup.select("input:enabled")

# checked
arr = soup.select("input:checked")

# disabled
arr = soup.select("input:disabled")

# empty
# label 옆, input:empty
arr = soup.select("label+input:empty")

# first_child
arr = soup.select("b:first-child")

# last_child
arr = soup.select("table tbody tr:last-child")

# first-of-type
# 자신이 부모의 첫번째 인 놈들이 다 나온다.
arr = soup.select("table tbody td:first-of-type")

# last-of-type
# 자신이 부모의 첫번째 인 놈들이 다 나온다.
arr = soup.select("table tbody td:last-of-type")

# not
arr = soup.select("b:not(:first-of-type)")

# nth-child
arr = soup.select("table tobody tr:nth-child(2)")

# nth-of-type
arr = soup.select("table tobody tr:nth-of-type(2)")
