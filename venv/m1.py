# 모듈이란 변수, 함수 클래스를 모은 파일을 의미
# from ~ import를 이용하여 모듈 호출
# 모듈이 되는 파일은 if __name__ == '__main__' 코드를 포함시켜 효율적인 모듈관리
# as를 이용하여 복잡한 모듈의 이름을 간단하게 변경후 사용가능
# pip를 이용하여 외부 패키지 및 모듈을 설치할 수 있음

from m2 import var1 as m2_var1, var2 as m2_var2, f1 as m2_f1

var1 = 'm1 hello'
var2 = 'm1 world'

def f1():
    print('m1.py f1() 함수')

if __name__ == "__main__":

    print(var1)
    print(var2)
    print(m2_var1)
    print(m2_var2)
    f1()
    m2_f1()

# 다른 파일을 from ~ import로 가져고 올 수 있다.
# 다른 파일에 있는 변수나 함수를 가지고 와서 사용하는데, 변수 이름이나 함수이름을 as를 통해서 바꿀 수 있다.

########################################################################################################
print()

# 예외 처리
# try ~ except를 통해서 다양한 에러를 처리할 수 있음

try:
    a = 10
    b= 0

    print(a)
    print(b)
    print(a/0)

except IndexError:
    print('Index error 발생')
except ZeroDivisionError:
    print('ZeroDivision error 발생')

# try, except 이외의 else와 finally를 통해 확장가능
# try가 정상적으로 실행되면 else 구문 실행
# finally는 최종적으로 무조건 실행되는 코드 (예외가 발생해도 except가 끝나면 호출)

try:
    a = 10
    b = 0

    print(a)
    print(b)
    print(a / 0) # 이게 있으면 예외가 발생함으로 else 구문이 실행되지 않는다.

except IndexError:
    print('Index error 발생')
except ZeroDivisionError:
    print('ZeroDivision error 발생')
else:
    print('try가 정상적으로 실행됐을 때')
finally:
    print('최종적으로 무조건 실행되는 구문')


# 강제로 에러 발생
# 프로그래머에 의해서 의도적인 에러발생이 필요한 경우
# raise를 이용하여 에러발생 가능
# 특정 함수, 메소드를 사용시 의도하지 않은 값을 받았을 때 에러를 발생할 수 있음

def f(x):
    if x == 1:
        raise ValueError('1값을 넣지 마세요')
    else:
        print('success')
# f(1)

print()
########################################################################################################################

# 모듈 설치

# requests 모듈 설치
# 터미널에서 pip install requests를 하여 requests 모듈 설치

# requests 사용

import requests as rq

url = "http://blog.naver.com/pjt3591oo"
res = rq.get(url) # 해당 URL로 GET 요청
res = rq.post(url) # 해당 URL로 POST 요청

print(res) # 응답객체
print(res.status_code) # 응답코드 확인 정상적으로 가져오면 200 출력
print(res.headers) # 헤더 가져오기
print(res.cookies) # 쿠키 가져오기
print(res.text) # HTML 코드 가져오기
print(res.content) # 바이너리 형태로 변환된 HTML 코드 가져오기
print(res.encoding) # 페이지 인코딩 확인

import requests as rq

url = "http://blog.naver.com/pjt3591oo"
res = rq.get(url, params={"key1":"value1", "key2":"value2"})

print(res.url)

import requests as rq

url = "http://www.example.com"
res = rq.post(url, data={"key1":"value1", "key2":"value2"})

print(res.url)

import requests as rq

url = "http://blog.naver.com/pjt3591oo"
res = rq.get(url, headers={"User-Agent":"Mozilla/5.0(Macintosh:Intel Mac OS X 10_12_5) AppleWebKit/537.36(KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"})
print(res.url)

# requests 오류를 처리하는 방법
import requests as rq

url = "http://blog.naver.com/pjt3591oo"
try:
    res = rq.get(url)
    print(res.url)
except rq.exceptions.HTTPError:
    print('HTTP 에러 발생')
except rq.exceptions.Timeout:
    print('timeout 에러 발생')
else:
    print('1111')

import requests as rq
import time

url = "http://blog.naver.com/pjt3591oo"
delay_time = 1

def connection(u):
    return rq.get(u)

try:
    connection(url)
except rq.exceptions.Timeout:
    time.sleep(delay_time)
    connection(url)
else:
    print('2222')

# Timeout 에러가 발생했다면 일정시간 딜레이를 준 후 다시 요청하여 해결

# HTTPerror : HTTP 오류 발생
# ConnectionError : 연결 오류 발생
# Timeout 에러 : 일정 시간 동안 서버가 응답하지 않을 때 오류 발생

############################################################################################################

# urllib url라이브러리

from urllib.request import urlopen, Request

url = "http://blog.naver.com/pjt3591oo"

req = Request(url)
page = urlopen(req)

print(page) # 응답 객체
print(page.code) # 응답 코드
print(page.headers) # 헤더 확인
print(page.url) # 요청 url 확인
print(page.info().get_content_charset()) # 인코딩 설정 확인
print(page.read()) # HTML 코드 가져오기

# urllib로 요청후 데이터 가져오기
from urllib.request import urlopen, Request

url = "http://blog.naver.com/pjt3591oo/1/"

req_post = Request(url)
page = urlopen(req_post)

print(page)
print(page.url)

# urllib는 없는 페이지 요청시 에러 발생

from urllib.request import urlopen, Request
import urllib

url = "http://blog.naver.com/pjt3591oo"

# post 요청 시 보낼 데이터 만들기
data = {'key1':'value1', 'key2':'value2'}
data = urllib.parse.urlencode(data)
data = data.encode('utf-8')

print(data)

# post 요청
req_post = Request(url, data=data, headers={}) # 2번째 인자 데이터, 세 번째 인자 헤더
page = urlopen(req_post)

print(page)
print(page.url)

# get 요청
req_get = Request(url+"?key1=value1&key2&value2",None, headers={}) # 2번째 인자 데이터, 세 번째 인자 헤더
page = urlopen(req_get)

print(page)
print(page.url)

# urllib은 data의 유무로 GET 요청과 POST 요청을 구분함

# request VS urllib
# requests와 urllib는 요청시 요청 객체를 만드는 방법에 차이가 있음
# 데이터를 보낼 때 requests는 딕셔너리 형태로 urillib는 인코딩하여 바이너리 형태로 전송

##################################################################################################################

# bs4를 사용하여 HTML코드를 파이썬이 사용가능한 객체로 변경
# bs4가 없다고 뜬다면 pip install bs4를 이용하여 설치
# 만약 lxml이 없다고 뜬다면 pip install lxml을 이용하여 설치

# pip install selenium 으로 selenium 설치
# https://sites.google.com/a/chromium.org/chromedriver/downloads 로 크롬 웹 드라이버 설치 페이지

from selenium import webdriver
# driver = webdriver.Chrome('chromedriver.exe') # 해당 코드를 실행하면 반 웹 브라우저가 뜸
# 윈도는 chromedriver.exe로 명시

# chrome_driver = webdriver.Chrome('chromedriver.exe')
# iexplore_driver = webdriver.Ie('IEDriverServer.exe')
# firefox_driver = webdriver.Firefox('FirefoxDriver.exe')
# 웹 브라우저와 웹 드라이버만 설치되어 있다면 다양한 웹 브라우저 횔용가능


##################################################################################################################
from bs4 import BeautifulSoup

html = """<html><p>test</p></html>"""
soup = BeautifulSoup(html, 'lxml')
print(soup)

html = """<body><p>test</p></body>"""
soup = BeautifulSoup(html, 'lxml')
print(soup)
# html과 body 태그가 없다면 해당 태그를 만들어 줌


# from bs4 import BeautifulSoup
#
# html = """<p>test</p>"""
#
# soup = BeautifulSoup(html, 'html5lib')
# print(soup)


# import time
# from bs4 import  BeautifulSoup
# html = """<html><head></head><p>test</p></html>"""
#
# start_time = time.time()
# BeautifulSoup(html, 'lxml')
# lxml_end_time = time.time() - start_time
#
# start_time = time.time()
# BeautifulSoup(html,'html5lib')
# html5lib_end_time = time.time() - start_time
#
# print('lxml 시간 측정 : %f'%(lxml_end_time))
# print('html5lib 시간 측정 : %f'%(html5lib_end_time))
# print(html5lib_end_time / lxml_end_time)


from bs4 import BeautifulSoup
html = """<html><head><title>test site</title></head><body><p>test</p><p>test1</p><p>test2</p></body></html>"""
soup = BeautifulSoup(html,'lxml')
print(soup.prettify())
# prettify() 를 이용해서 보기좋게 정렬해서 출력한다.

# bs4 에서 find_all(), find(), select()를 이용하여 원하는 요소를 리스트 또는 단일 객체의 형태로 가져올 수 있음

# find_all() 은 일치하는 모든 요소를 가지고 옴 ( 리스트 형태로 데이터를 가져옴 )

# find_all()
from bs4 import BeautifulSoup

html = """<html><head><title>test site</title></head><body><p>test1</p><p id="d">test2</p><p>test3</p></body></html>"""
soup = BeautifulSoup(html, 'lxml')

print(soup.find_all('p', id='d'))
print(soup.find_all('p', id='c'))

from bs4 import BeautifulSoup

html = """<html><head><title>test site</title></head><body><p>test1</p><p class="d">test2</p><p class="c">test3</p></body></html>"""
soup = BeautifulSoup(html, 'lxml')

print(soup.find_all('p', class_='d'))
print(soup.find_all('p', class_='c'))

from bs4 import BeautifulSoup

html = """<html><head><title>test site</title></head><body><p>test1</p><p class="d">test2</p><p class="c">test3</p><a>a tag</a><b>b tag</b></body></html>"""
soup = BeautifulSoup(html, 'lxml')

print(soup.find_all(['a','b']))

from bs4 import BeautifulSoup

html = """<html><head><title>test site</title></head><body><p>test1</p><p class="d">test2</p><p class="c">test3</p></body></html>"""
soup = BeautifulSoup(html, 'lxml')

print(soup.find_all('p', text='test1'))
print(soup.find_all('p', text='t'))


# find()
# find() 로 찾은 객체는 단일 객체이기 때문에 양쪽에 []가 없다.
# find() 는 처음 발견된 것 하나만 가져온다.
from bs4 import BeautifulSoup

html = """<html><head><title>test site</title></head><body><p id="i" class="a">test1</p><p class="d">test2</p><p class="d">test3</p><a>a tag</a><b>b tag</b></body></html>"""
soup = BeautifulSoup(html, 'lxml')

print(soup.find('p', class_='d'))
print(soup.find('p', class_='d'))
print(soup.find('p', id="i"))
print()

# select()
# 리스트로 가져온다.
from bs4 import BeautifulSoup

html = """<html><head><title>test site</title></head><body><div><p id="i" class="a">test1</p><p class="d">test2</p></div><p class="d">test3</p><a>a tag</a><b>b tag</b></body></html>"""
soup = BeautifulSoup(html, 'lxml')

print(soup.select('body p')) # body 태그에서 p태그 가져오기
print(soup.select('body .d')) # body 태그에서 클래스가 d인 태그 가져오기
print(soup.select('body p.d')) # body 태그에서 클래스가 d인 p태그 가져오기
print(soup.select('body #i')) # body 태그에서 아이디가 i인 태그 가져오기
print(soup.select('body p#i')) # body 태그에서 아이디가 i인 p태그 가져오기
print(soup.select('div p')) # div 태그에서 p태그 가져오기
print()


# extract()
# 필요없는 태그를 없앨 때 사용한다.
# 주로 script 나 style 같이 크롤링에서 필요없는 태그를 없앨 때 사용

from bs4 import BeautifulSoup

html = """<html><head><title>test site</title></head><body><div><p id="i" class="a">test1</p><p class="d">test2</p></div><p class="d">test3</p><a>a tag</a><b>b tag</b></body></html>"""
soup = BeautifulSoup(html, 'lxml')

for tag in soup.find_all(['p','a']):
    print(tag.extract())

print('제거 완료')
print(soup)
print()

#####################################################################################################################

# 정규표현식
# https://regexr.com/ 정규 표현식 연습할 수 있는 사이트

from bs4 import BeautifulSoup
import re

html = """<html><head><title>test site</title></head><body><div><p id="i" class="a">test1</p><p class="d">test2</p></div><p class="d">test3</p><a href="/example/test1">a tag</a><b>b tag</b></body></html>"""
soup = BeautifulSoup(html, 'lxml')

print(soup.find_all(class_=re.compile('d'))) # 클래스에 d가 포함된 모든 요소 가져오기
print(soup.find_all(id=re.compile('i'))) # 아이디에 i가 포함된 모든 요소 가져오기
print(soup.find_all(re.compile('t'))) # 태그에 t가 포함된 모든 요소 가져오기
print(soup.find_all(re.compile('^t'))) # 태그가 t로 시작하는 모든 요소 가져오기
print(soup.find_all(href=re.compile('/'))) # href에 슬래시(/)가 포함된 모든 요소 가져오기
print()


# 대문자 + 소문자 찾기

import re
test_str = """I am Park Jeong-tae. i live in Paju. I lived in Paju for 25 years. Sample text for testing: abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789 _+-.,!@#$%^&&*()<> 12345 -98.7 3.141 .6180 9.000 +45"""

pattern = re.compile('[a-zA-Z]')
pattern1 = re.compile('[a-zA-Z]+')
pattern2 = re.compile('[A-Z]+')
c = pattern.findall(test_str)
d = pattern1.findall(test_str)
e = pattern2.findall(test_str)

print(c)
print(d)
print(e)

import re
test_num = "저의 전화번호는 010-6666-7777 입니다."

pattern = re.compile('[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]')
pattern1 = re.compile('\d\d\d-\d\d\d\d-\d\d\d\d')
pattern2 = re.compile('\d{3}-\d{4}-\d{4}')
c = pattern.findall(test_num)
d = pattern1.findall(test_num)
e = pattern2.findall(test_num)

print(c)
print(d)
print(e)

test_str = """I am Park Jeong-tae. i live in Paju. I lived in Paju for 25 years. Sample text for testing: test test1 test2 abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789 _+-.,!@#$%^&&*()<> 12345 -98.7 3.141 .6180 9.000 +45"""

pattern = re.compile('[a-zA-Z0-9]+') # a부터 z까지, A부터 Z까지, 0부터 9까지 포함된 것
pattern1 = re.compile('\w+')

c = pattern.findall(test_str)
d = pattern.findall(test_str)
print(c)
print(d)

pattern = re.compile('[^a-z]+') # a부터 z까지 포함되지 않는 것
c = pattern.findall(test_str)
print(c)

pattern = re.compile('[^A-Z]+') # A부터 Z까지 포함되지 않는 것
c = pattern.findall(test_str)
print(c)

pattern = re.compile('t..t') # t문자문자t 패턴
pattern1 = re.compile('t...t') # t문자문자문자t 패턴
c = pattern.findall(test_str)
d = pattern1.findall(test_str)
print(c)
print(d)

pattern = re.compile('t?est\w+') # test나 est로 시작하는 문자열 뒤에 \w가 있어야 됨
pattern1 = re.compile('t?est\w*') # test나 est로 시작하는 문자열 뒤에 \w가 없어도 됨
c = pattern.findall(test_str)
d = pattern1.findall(test_str)
print(c)
print(d)

# 파이썬 정규표현식 정리 사이트
# https://wikidocs.net/4308

# \d - 숫자와 매치, [0-9]와 동일한 표현식이다.
# \D - 숫자가 아닌 것과 매치, [^0-9]와 동일한 표현식이다.
# \s - whitespace 문자와 매치, [ \t\n\r\f\v]와 동일한 표현식이다. 맨 앞의 빈 칸은 공백문자(space)를 의미한다.
# \S - whitespace 문자가 아닌 것과 매치, [^ \t\n\r\f\v]와 동일한 표현식이다.
# \w - 문자+숫자(alphanumeric)와 매치, [a-zA-Z0-9_]와 동일한 표현식이다.
# \W - 문자+숫자(alphanumeric)가 아닌 문자와 매치, [^a-zA-Z0-9_]와 동일한 표현식이다.

# ^ 는 자바에서 !처럼 부정의 의미인 것 같다.
print()
#####################################################################################################################

# 크롤러 만들기
# 1. 타겟 정하기
# 2. 사이트 분석 - 원하는 데이터 확인 ( 검사창에서 소스 확인 가능 )
# 3. 사이트 분석 - URL 확인 ( 페이지 네이션 확인 )
# 4. 크롤러 만들기
# 5.

import requests as rq
from bs4 import BeautifulSoup

def get_post(soup): # 돔 접근
    return  soup.select('body main.page-content div.wrapper div.home div.p')

def data_parse(posts): # 해당 돔에서 필요한 데이터 뽑기
    for post in posts:
        title = post.find('h3').text.strip()
        descript = post.find('h4').text.strip()
        author = post.find('span').text.strip()
        print(title, descript, author)

base_url = 'https://pjt3591oo.github.io'
page_path = '/page%d' # url을 변경할 수 있도록 포멧팅 활용
page = 2

res = rq.get(base_url)
soup = BeautifulSoup(res.content,'lxml')

posts = get_post(soup)
data_parse(posts)

while True: # 다음 페이지로 접속할 수 있도록 반복문 이용
    sub_path = page_path%(page) # url을 생성해 준다.
    page += 1
    res = rq.get(base_url+sub_path)

    if(res.status_code != 200): # 200 코드가 아니라면 해당 반복문을 탈출
        break

    soup = BeautifulSoup(res.content, 'lxml')
    posts = get_post(soup)

    data_parse(posts)

# 1. https://pjt3591oo.github.io 접속
# 2. body > main.page-content > div.wrqpper > div.home
# 2-1. 원하는 요소에 접근 후 text 속성을 가져오면 해당 태그
# 3. /page 숫자 형태로 다음 페이지 접속
# 4. 응답 코드가 404가 나올 때까지 2~3 반복
