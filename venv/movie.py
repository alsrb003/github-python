from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
request = Request("http://movie.naver.com/movie/running/current.nhn")
response = urlopen(request)
html = response.read()
# print(html[:256])  # 코드가 깨진다... 인코딩을 변경하자
html = html.decode("utf-8")
# print(html[:256]) # 코드가 정상적이다.
# 이제 BeautifulSoup으로 html을 정제하자
bs = BeautifulSoup(html, "html.parser")
print(bs.title)
print(bs.title.name)
# 이쁘게 표현해보자
print(bs.prettify()[:1024])

print()

currents = bs.find("ul", attrs={"class":"lst_detail_t1"})

for child in currents:
    try:
        titles = child.find("dt", attrs={"class":"tit"})
        for title in titles:
            try:
                if title.name == "a":
                    print(title.text, title['href'])
            except:
                pass
    except:
        pass

print()
print("----------------------------------------------------")
print()

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
request = Request("http://movie.naver.com/movie/running/current.nhn")
response = urlopen(request)
html = response.read().decode("utf-8")
bs = BeautifulSoup(html, "html.parser")

current_movies = bs.select(".lst_detail_t1 > li")

for movie in current_movies:
    titles = movie.select(".lst_dsc > .tit > a")

    for title in titles:
        print(title.text, title['href'])



