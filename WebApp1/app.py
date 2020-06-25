"""
    날짜 : 2020/06/25
    이름 : 유효진
    내용 : 파이썬 웹 프로그래밍
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello Python Flask!!!</h1>'

@app.route('/hello')
def hello():
    return render_template('/hello.html')

if __name__=='__main__':
    app.run()