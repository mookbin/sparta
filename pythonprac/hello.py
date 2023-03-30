from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.zliwcuv.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta


import requests
from bs4 import BeautifulSoup #requests 와 BeautifulSoup을 이용한다는 뜻


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829',headers=headers)
# 접속을 해서 데이터를 받아와라.


soup = BeautifulSoup(data.text, 'html.parser')
#데이터를 솎아낼 준비를 한다.



trs = soup.select('#old_content > table > tbody > tr')
for tr in trs:
    a = tr.select_one('td.title > div > a')
    if a is not None: 
        title = a.text
        rank = tr.select_one(' td:nth-child(1) > img')['alt']
        star = tr.select_one('td.point').text
       
        doc = { 
            'title':title,
            'rank':rank,
            'star':star 

        }
        db.movies.insert_one(doc)
