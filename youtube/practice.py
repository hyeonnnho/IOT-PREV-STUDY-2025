station = "부산역"
print(station + "행 열차가 도착했습니다.")

print(2**3) # 2^3 = 8
print(5%3) # 나머지 구하기 2
print(5//3) # 몫 구하기 1
print(4 == 2) # False
print(1 != 3) # True
print(not(1 != 3)) # False

print((3 > 0) and (3 < 5)) # True
print((3 > 0) & (3 < 5)) # True

print((3 > 0) or (3 > 5)) # True
print((3 > 0) | (3 > 5)) # True

number = 2 + 3 * 4 # 14
number = number + 2 # 16
print(number)
number += 2 # 18
print(number)
number *= 2 # 36
print(number)
number /= 2 # 18
print(number)
number -= 2 # 16
print(number)
number %= 5 # 1 나머지
print(number)

print(abs(-5)) # 5
print(pow(4,2)) # 16
print(round(3.14)) # 3
print(round(4.99)) # 5

from math import *
print(floor(4.99)) # 내림 4
print(ceil(3.14)) # 올림 4
print(sqrt(16)) # 제곱근 4

from random import *
print(random()) # 0.0 ~ 1.0 랜덤
print(random()* 10) # 0.0 ~ 10.0
print(int(random()*10)+1) # 1 ~ 10
print(randrange(1,11)) # 1 ~ 11미만
print(randint(1, 45)) # 1 ~ 45이하

date = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월" +str(date)+ "일로 선정되었습니다.")
print(f"오프라인 스터디 모임 날짜는 매월 {date}일로 선정되었습니다.")

haeno = "990814-1234567"
print("성별 : " + haeno[7])
print("연 : " + haeno[0:2])
print("생년월일 : " + haeno[:6])
print("뒤 7자리 : " + haeno[7:])
print("뒤 7자리 : " + haeno[-7:])


python = "Python is Amazing"
print(python.lower()) # 소문자
print(python.upper()) # 대문자
print(python[0].isupper()) # 첫글자 대문자인지?
print(len(python)) # 글자 길이
print(python.replace("Python", "Java")) # 글자 대체

index = python.index("n") # n이 몇 번째 인지
print(index)
index = python.index("n", index + 1) # 두번째 n이 몇 번째 인지
print(index)

print(python.find("n")) # n이 몇 번째 인지
print(python.find("Java")) # -1 :글자가 없음
# print(python.index("Java")) # error

print(python.count("n")) # n이 몇 번 나오는지


print("나는 %d살 입니다." %20) #정수
print("나는 %s을 좋아해요." %"파이썬") #문자,숫자 다 가능
print("Apple은 %c로 시작해요." %"A") #한글자
print("나는 %s색과 %s색을 좋아해요." %("파란", "빨간"))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "빨간"))
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}을 좋아해요.")

print("저는 \"이현호\" 입니다.")
print("\\")
print("Red Apple\rPine") #커서를 맨앞으로 이동
print("Redd\bApple") #Backspace
print("Red\tApple") #tab


site = "http://naver.com"
site = site.replace("http://", "")
site = site[:site.index(".")]
# print(site[:3] + str(len(site)) + str(site.count("e")) + "!")
pw = site[:3] + str(len(site)) + str(site.count("e")) + "!"
print(f"생성된 비밀번호 : {pw}") 