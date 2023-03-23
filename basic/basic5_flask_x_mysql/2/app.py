# flask 설치하기
# pip install flask
# python
# >>> import flask
# >>> exit()

# DB mysql과 연동
# pip install pymysql
# python -> >>> import pymysql -> exit()

from flask import Flask, render_template
import pymysql
app = Flask(__name__)

# DB session 관리 비번
app.secret_key = b'123'

# DB mysql 연동
conn = pymysql.connect(
    user='root',
    passwd='',
    host='127.0.0.1',
    db='test1',
    charset='utf8'
)

# DB 불러오기 예시
curs = conn.cursor(pymysql.cursors.DictCursor)
member1_sql = "select * from user1"
curs.execute(member1_sql)
member1_row = curs.fetchall() # 전부 가져오기 # fetchone 하나 가져오기

# Controller = localhost:5000/
@app.route('/', methods=['GET', 'POST'])
# model
def getIndex():
    return render_template('index.html', member1=member1_row)

# Controller = localhost:5000/join
@app.route('/join', methods=['GET', 'POST'])
# model
def join():
    return render_template('join.html')

# Controller = localhost:5000/write
@app.route('/write', methods=['GET', 'POST'])
# model
def getWrite():
    return render_template('write.html')


if __name__ == '__main__':
    app.run(debug=True)