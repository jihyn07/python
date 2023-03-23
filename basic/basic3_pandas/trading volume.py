# https://github.com/sharebook-kr/pykrx
from pykrx import stock
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import datasets

df = stock.get_market_ohlcv_by_ticker("20210319", market="KOSPI") # Kospi의 해당날자 주가정보 뽑기
df = df.sort_values(by=['거래량'], axis=0, ascending=False) #해당 컬럼의 내림차순으로 정렬
print(df)

# 만들고싶은거:
# 3거래일의 거래량 상위 10프로를 비교하여 증감을 확인
# OBV 계산식도입하여 판단하기 On Balance Volume
#    (1)   If 오늘 주식 종가 > 전날의 주식 종가, 이전까지의 거래량 합산에 오늘 거래량을 합함
#    (2)   If 오늘 주식 종가 < 전날의 주식 종가, 이전까지의 거래량 합산에 오늘 거래량을 뺌


# # # 이거만 바꾸면 상관도 나오는 거!
# X = df.거래량.values  
# Y = df.등락률.values 

# # 1. 산점도로 육안으로 일단 확인
# plt.scatter(X, Y)
# plt.show()

# # 2. 공분산(covariance) : 2개의 변수의 상관도를 나타내는 값
# cov_value = (np.sum(X*Y)-len(X)*np.mean(X)*np.mean(Y))/len(X)
# print('공분산:', cov_value) # 2.14... ? 양수의 의미는 상승시 상승

# # 3. 상관계수(correlation coeffect) : 공분산을 0~1 사이로 표준화시킨 값 (0 상관없음, 0.3~0.7 뚜렷한 상관, 0.8 이상 절대적인 상관)
# corr_value = cov_value/(np.std(X)*np.std(Y))
# print('상관계수:', corr_value)

# # 4. 검정(test) : 상관계수의 값이 유의미한지를 검정
# import scipy.stats as stats # pip install scipy
# corr_test = stats.pearsonr(X, Y)
# print(corr_test) # 0.58.. 3.46...e-42 (뒷값이 0에 가까울수록 신뢰가능한데, 거의 0에 가까우므로 신뢰할 값입니다.)
