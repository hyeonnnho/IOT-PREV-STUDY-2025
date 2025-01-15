print('함수 모듈') # 내장함수

def add(a,b):
  result = a + b
  return result

def minus(a,b):
  result = a - b
  return result

def multi(a,b):
  result = a * b
  print('곱은 -> ', result)

def divide():
  result = 100/4
  print('나누기 결과', result)

x = 100
y = 5
divide()

x = 11
y = 22
z = add(x,y)
print('합의 결과는', z)

x = 101
y = 203
print('합의 결과는 ', add(x,y))

x = 35
y = 10
z = multi(x,y)

'''내장 함수'''

print(max(1,3,7,15))
print(min(1,3,7,15))
print(abs(5))
print(2**10)
print(pow(2,10))