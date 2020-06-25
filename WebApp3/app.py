"""
    날짜 : 2020/06/25
    이름 : 유효진
    내용 : 파이썬 웹 프로그래밍 블루프린트
"""
from flask import Flask, render_template
from WebApp3.views.index import index_blueprint
from WebApp3.views.sub1.sub1_1 import sub1_1_blueprint
from WebApp3.views.sub1.sub1_2 import sub1_2_blueprint
from WebApp3.views.sub2.sub2_1 import sub2_1_blueprint
from WebApp3.views.sub2.sub2_2 import sub2_2_blueprint

app = Flask(__name__)

# 블루프린트 모듈 등록
app.register_blueprint(index_blueprint)
app.register_blueprint(sub1_1_blueprint)
app.register_blueprint(sub1_2_blueprint)
app.register_blueprint(sub2_1_blueprint)
app.register_blueprint(sub2_2_blueprint)

if __name__=='__main__':
    app.run()