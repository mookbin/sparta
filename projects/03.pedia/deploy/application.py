from flask import Flask, render_template, request, jsonify
application = app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.zliwcuv.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

import requests
from bs4 import BeautifulSoup

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/movie", methods=["POST"])
def movie_post():
    url_receive = request.form['url_give']
    comment_receive = request.form['comment_give']
    star_receive = request.form['star_give']

    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive,headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    ogtitle = soup.select_one('meta[property="og:title"]')['content']
    ogdesc = soup.select_one('meta[property="og:description"]')['content']
    ogimage = soup.select_one('meta[property="og:image"]')['content']

    doc = {
        'title':ogtitle,
        'desc':ogdesc,
        'image':ogimage,
       # 'url':url_receive, 카드에 들어가는 부분 없기때문에 삭제 
        'star':star_receive,
        'comment':comment_receive
        
    }
    db.movies.insert_one(doc)

    return jsonify({'msg':'저장완료'})

@app.route("/movie", methods=["GET"])
def movie_get():
    all_movies = list(db.movies.find({},{'_id':False})) #movie에 대한 데이터를 쭉 갖다 넣은 변수 
    return jsonify({'result':all_movies})

@app.route('/movie/delete', methods=['POST'])
def delete_movie():
    title_receive = request.form['title_give']
    db.movies.delete_one({'title': title_receive})

    return jsonify({'msg': 'delete 완료되었습니다!'})


if __name__ == '__main__':
    app.run()