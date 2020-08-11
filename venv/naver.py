import urllib.request, json
client_id = "A3lqLFUXh9LfoAOKDtSr"
client_secret = "Uajr1W4ytw"
encText = urllib.parse.quote("lck")
url = "https://openapi.naver.com/v1/search/news.json?query={}".format(encText) # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()

    json_rt = response_body.decode("utf-8")
    py_rt = json.loads(json_rt)

    news_list = py_rt['items']

    # print(response_body.decode('utf-8'))

    for news in news_list:
        news['title']
        print("title: {title} @ {pubDate}".format_map(news))

else:
    print("Error Code:" + rescode)