from flask import Blueprint, render_template, request, redirect
import pymysql as db
register_blueprint = Blueprint('register', __name__)

@register_blueprint.route('/register', methods=['GET'])
def register1():
    return render_template('/register.html')

@register_blueprint.route('/register', methods=['POST'])
def register2():

    # 파라미터 수신
    uid  = request.form['uid']
    name = request.form['name']
    hp   = request.form['hp']
    age  = request.form['age']

    # 데이터베이스 접속
    conn = db.connect(host='192.168.44.46',
                      user='rhj',
                      password='1234',
                      db='rhj',
                      charset='utf8')

    # 쿼리문 실행 객체 생성
    cur = conn.cursor()

    # 쿼리문 실행
    sql = "INSERT INTO `USER1` VALUES ('%s', '%s', '%s', '%s')"
    cur.execute(sql % (uid, name, hp, age))
    conn.commit()

    # 데이터베이스 종료
    conn.close()

    return redirect('/list')