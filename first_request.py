import requests as r

res = r.get("https://news.ycombinator.com/")

print(res.headers)

print(res.text)
