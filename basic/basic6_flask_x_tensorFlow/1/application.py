from flask import Flask, render_template, request
import sys
import asyncio

application = Flask(__name__)

# 앱 변수
weightAndBias = None # y = ax + b 기울기와 편향
xList = [] # x 값 리스트
yList = [] # y 값 리스트
learning = False # 학습 완료 여부
progress = "" # 진행상황 텍스트

# 컨트롤러
@application.route("/")
def index():
    return render(None)

# learner 모듈 사용하여 학습

# id x 인풋에 들어간 x값을 이용하여 y값을 예측
def render(x):
    return render_template("index.html", formula="학습된 수식", predicated="예측값")

application.run()