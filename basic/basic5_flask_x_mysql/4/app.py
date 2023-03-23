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

# Controller = localhost:5000/join
@app.route('/join', methods=['GET', 'POST'])
# model
def join():
    return render_template('join.html')

# Controller = localhost:5000/joinpost
@app.route('/joinpost', methods=['POST'])
# model
def joinpost():
    # 회원가입 로직.
    id = request.form['id']
    pw = request.form['pw']
    pwc = request.form['pwc']
    username = request.form['username']  
    gender = request.form['gender']
    tel = request.form['tel']
    email = request.form['email']
    birth = request.form['birth']
    address = request.form['address']

    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute('SELECT * FROM user2 WHERE id=%s', (id))
    idcheck = cursor.fetchone()

    if idcheck:
        return "<script>alert('이미 있는 아이디입니다.');history.back()</script>"
    elif not (id and pw and pwc and username):
        return "<script>alert('필수 정보를 모두 입력해주십시오.');history.back()</script>"
    elif pw != pwc:
        return "<script>alert('비밀번호를 확인해주십시오.');history.back()</script>"
    else:
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        query = "INSERT INTO user2 (id, pw, username, gender, tel, email, birth, address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        value = (id, pw, username, gender, tel, email, birth, address)
        cursor.execute(query, value)
        joincheck = cursor.fetchall()

        if not joincheck:
            conn.commit()
            session['member'] = True
            session['id'] = id
            session['username'] = username
            session['gender'] = gender
            session['tel'] = tel
            session['email'] = email
            session['birth'] = birth
            session['address'] = address
            return render_template('index.html')
        else:
            conn.rollback()
            return "회원가입 실패"

# 下から新しい機能の開発
@app.route('/memberinfo', methods=['GET', 'POST'])
def memberinfo():
  return render_template('memberinfo.html')

@app.route('/membermod', methods=['GET', 'POST'])
def membermod():
  return render_template('membermod.html')

@app.route('/membermodpost', methods=['POST'])
def membermodpost():
    # 会員の情報を生成
    id = request.form['id']
    username = request.form['username']
    gender = request.form['gender']
    email = request.form['email']
    tel = request.form['tel']
    birth = request.form['birth']
    address = request.form['address']

    # 修正の実行
    if not (username) :
        return "<script>alert('필수항목을 모두 입력해주세요.');history.back();</script>"
    else: # 全ての必須項目が記入された場合、下の命令を実行（DBの中に入れる)
        # cursor
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        query = "UPDATE user2 SET `username` = %s, `gender` = %s, `birth` = %s, `email` = %s, `tel` = %s, `address` = %s WHERE `id` = %s"
        value = (username, gender, birth, email, tel, address, id)
        cursor.execute(query, value)
        membermodcheck = cursor.fetchall()

        if not membermodcheck:
            conn.commit()
            # session = login処理
            session['member'] = True
            session['id'] = id
            session['username'] = username
            session['gender'] = gender
            session['birth'] = birth
            session['email'] = email
            session['tel'] = tel
            session['address'] = address
            return render_template('memberinfo.html')
        else:
            conn.rollback()
            return "Membermod Failed"

@app.route('/memberout', methods=['GET', 'POST'])
def memberout():
  return render_template('memberout.html')

@app.route('/memberoutpost', methods=['POST'])
def memberoutpost():
    if request.method == 'POST' and 'pw' in request.form:
        password = request.form['pw']
        # DB Search * select
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute('SELECT * FROM user2 WHERE id = %s AND pw = %s', (session['id'], password))
        # DB Search * select　の　Result → member1
        memberout = cursor.fetchone()
        # SUCCESS
        if memberout:
            # Delete User
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute('DELETE FROM user2 WHERE id = %s AND pw = %s', (session['id'], password))
            # Logout
            session.pop('member', None)
            session.pop('id', None)
            session.pop('username', None)
            session.pop('gender', None)
            session.pop('birth', None)
            session.pop('email', None)
            session.pop('tel', None)
            session.pop('address', None)
            session.pop('joindate', None)
            return render_template('index.html')
        # FAIL
        else:
            # return 'Delete failed'
            msg = '회원탈퇴를 실패했습니다. 비밀번호를 확인해주세요.'
            return render_template('index.html', msg=msg)

# Controller = localhost:5000/bbs
@app.route('/bbs', methods=['GET', 'POST'])
# model
def getBBS():
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM bbs1 WHERE `del_flg`=%s", (0))
    conn.commit
    bbs1rows = cursor.fetchall()    
    return render_template('bbs.html', bbs1rows=bbs1rows)

# Controller = localhost:5000/bbsdetail
@app.route('/bbsdetail', methods=['GET', 'POST'])
# model
def getBBSdetail():
    # GET 정보를 받는 방법
    for key in request.args.to_dict().keys():
        no = request.args[key]
    # GET 정보(no)에 해당하는 게시물을 DB로부터 불러온다. : bbs 전체
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM bbs1 WHERE no=%s", (no))
    conn.commit
    bbs1row = cursor.fetchall()
    # GET 정보(no)에 해당하는 게시물을 DB로부터 불러온다. : writer
    cursor.execute("SELECT writer FROM bbs1 WHERE no=%s", (no))
    conn.commit
    writer = cursor.fetchall()[0]['writer']
    # print(writer)
    return render_template('bbsdetail.html', bbs1row=bbs1row, writer=writer, no=no)

# Controller = localhost:5000/bbsdetail
@app.route('/bbswrite', methods=['GET', 'POST'])
# model
def getBBSwrite():
    return render_template('bbswrite.html', member1=member1_row)

# Controller = localhost:5000/bbswritepost
@app.route('/bbswritepost', methods=['POST'])
# model
def getBBSwritepost():
    title = request.form['title']
    content = request.form['content']
    writer = request.form['writer']    

    cursor = conn.cursor(pymysql.cursors.DictCursor)
    query="INSERT INTO bbs1 (no, writer, title, content, uploadDate, del_flg) VALUES (NULL, %s, %s, %s, current_timestamp(), '0')"
    value=(writer, title, content)
    cursor.execute(query, value)
    writecheck = cursor.fetchall()
    if not writecheck:
        conn.commit()
        return render_template('bbs.html')
    else:
        return "BBS1write Failed"

# Controller = localhost:5000/bbsdelete
@app.route('/bbsdelete', methods=['GET', 'POST'])
# model
def getBBSdelete():    
    # GET 정보를 받는 방법
    for key in request.args.to_dict().keys():
        no = request.args[key]
    # GET 정보(no)에 해당하는 게시물을 DB로부터 삭제한다.
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("UPDATE bbs1 SET `del_flg`=%s WHERE `no`=%s", (1, no))
    conn.commit()
    return redirect('/bbs')    




# ****



# Controller = localhost:5000/bbsmodify
@app.route('/bbsmodify', methods=['GET', 'POST'])
# model
def getBBSmodify():    
    # GET 정보를 받는 방법
    for key in request.args.to_dict().keys():
        no = request.args[key]
    # GET 정보(no)에 해당하는 게시물 수정페이지를 연다.
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM bbs1 WHERE no=%s", (no))
    conn.commit()
    bbs1modrow = cursor.fetchall()

    return render_template('bbsmodify.html', bbs1modrow=bbs1modrow) 












# ***


# Controller = localhost:5000/bbsmodifypost
@app.route('/bbsmodifypost', methods=['GET', 'POST'])
# model
def getBBSmodifypost():
    title = request.form['title']
    content = request.form['content']
    writer = request.form['writer']

    # GET 정보를 받는 방법
    for key in request.args.to_dict().keys():
        no = request.args[key]

    # GET 정보(no)에 해당하는 게시물을 DB로부터 수정한다.
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    query = "UPDATE bbs1 SET `title`=%s, `content`=%s WHERE `no`=%s"
    value = (title, content, no)
    cursor.execute(query, value)
    conn.commit()
    return redirect('/bbsdetail?no='+no)

if __name__ == '__main__':
    app.run(debug=True)