# flask 설치하기
# pip install flask
# python
# >>> import flask
# >>> exit()

# DB mysql과 연동
# pip install pymysql
# python -> >>> import pymysql -> exit()

from flask import Flask, render_template, request, redirect, session
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
member1_sql = "select * from user2"
curs.execute(member1_sql)
member1_row = curs.fetchall() # 전부 가져오기 # fetchone 하나 가져오기

# Controller = localhost:5000/
@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
# model
def getIndex():
    return render_template('index.html', member1=member1_row)

# Controller = localhost:5000/bbs
@app.route('/bbs', methods=['GET', 'POST'])
# model
def getBBS():
    return render_template('bbs.html', member1=member1_row)

# Controller = localhost:5000/bbsdetail
@app.route('/bbsdetail', methods=['GET', 'POST'])
# model
def getBBSdetail():
    return render_template('bbsdetail.html', member1=member1_row)

# Controller = localhost:5000/login
@app.route('/login', methods=['GET', 'POST'])
# model
def getLogin():
    return render_template('login.html')

# Controller = localhost:5000/write
@app.route('/write', methods=['GET', 'POST'])
# model
def getWrite():
    return render_template('write.html')

# Controller = localhost:5000/loginpost
@app.route('/loginpost', methods=['POST'])
# model
def loginpost():
    global member1
    if request.method == 'POST' and 'id' in request.form and 'password' in request.form:
        id = request.form['id']
        password = request.form['password']
        curs = conn.cursor(pymysql.cursors.DictCursor)
        curs.execute('select * from user2 where id = %s and pw = %s', (id, password))
        member1 = curs.fetchone() # 전부 가져오기 # fetchone 하나 가져오기

        # login 성공시
        if member1:
            session['member'] = True
            session['id'] = member1['id']
            session['username'] = member1['username']
            session['gender'] = member1['gender']
            session['tel'] = member1['tel']
            session['email'] = member1['email']
            session['birth'] = member1['birth']
            session['address'] = member1['address']
            session['joindate'] = member1['joindate']
            # return 'login success!'
            return render_template('index.html')            
        else:
            msg = '로그인이 실패했습니다. \n아이디와 비밀번호를 체크해주세요.'
            # return 'login fail...'
            return render_template('index.html', msg=msg)

# Controller = localhost:5000/loginpost
@app.route('/logout', methods=['GET'])
# model
def logout():
    session.pop('member', None)
    session.pop('id', None)
    session.pop('username', None)
    session.pop('gender', None)
    session.pop('tel', None)
    session.pop('email', None)
    session.pop('birth', None)
    session.pop('address', None)
    session.pop('joindate', None)
    return redirect('login')

if __name__ == '__main__':
    app.run(debug=True)