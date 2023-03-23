from flask import Flask, render_template, request
import sys
import asyncio
import learner

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

@application.route("/predict", methods=['POST'])
def predict():
    return render(float(request.form['x']))

# id x 인풋에 들어간 x값을 이용하여 y값을 예측
def render(x):
    global weightAndBias
    global learning

    formular = f"[학습중 {learner.progress}] " if learning else ""

    if weightAndBias is not None:
        formular += f"y = { weightAndBias[0] } * x + { weightAndBias[1] }"
    else:
        formular += "수식이 들어갈 곳 : 학습된 수식이 없습니다"

    predicted = "예측값이 들어갈 곳 : 학습된 수식이 없습니다"
    if (x is not None and weightAndBias is not None):
        predicted = (weightAndBias[0] * x + weightAndBias[1])

    return render_template("index.html", formular=formular, predicted=predicted)

# learner 모듈 사용하여 학습
@application.route("/learn", methods=['POST'])
def learn():
    global xList
    global yList
    global weightAndBias
    global learning

    # 1, 2.5, 3 -> [1.0, 2.5, 3.0]
    xList = xList + list(map(float, request.json['xList'].strip().split(",")))
    yList = yList + list(map(float, request.json['yList'].strip().split(",")))

    xList = xList[0: min(len(xList), len(yList))]
    yList = yList[0: min(len(xList), len(yList))]

    epochs = (int(request.json['epochs']))

    if not learning:
        learning = True
        weightAndBias = learner.learn(xList, yList, epochs)
        learning = False

application.run()