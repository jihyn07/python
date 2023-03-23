from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello():
    return '<h1>hello</h1>'

if __name__ == '__main__':
    app.run(debug=True)


# 템플릿 받기 -> templates, static 넣기 -> including 처리 -> 띄워서 안깨지게 url 수정

# 예시 : <link href="{{ url_for('static'), filename='lib/bootstrap/css/bootstrap.min.css' }}" rel="stylesheet">