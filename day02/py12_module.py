#pymodule.py - 모듈

import py10_function as calc

calc.multi(10,4)

import math

result = math.pow(2,10)
print(result)

result = math.log(4)
print(result)

## 패키지 - 모듈들을 모아둔 디렉토리(폴더)
## pip install requests

import requests

res = requests.get('http://www.naver.com') #네이버를 접속하라
print(res.status_code) #200
print(res.content) ## 웹페이지 내용을 긁어오는 작업