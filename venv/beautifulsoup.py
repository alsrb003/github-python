from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

# HTTP GET Request
req = urlopen('http://media.daum.net')

# 먼저 req가 정상 코드를 받아왔는지 확인한다
print(req.getcode()) # HTTP 200은 정상값이다

if req.getcode() == 200:
    # html을 받아오자
    html = req.read()
    print(html) # 인코딩이 깨진다.

    html = html.decode("utf-8")
    print(html) # 정상이다
else:
    print("HTTP ERROR")

# 이제 soup을 만들어 즐겨보자
soup = BeautifulSoup(html, "html.parser") # soup을 만들었다
# print(soup.prettify())

print(soup.title)
# 타이틀에서 텍스트를 뽑아오자
print(soup.title.text)

