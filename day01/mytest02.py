#가위/바위/보를 선택하세요  가위 Enter
#나 : 가위
#컴 : 바위
#결과 : 짐
import random

a = input("가위/바위/보를 선택하세요")
com = ""
result = ""

rnd = int(random.random() * 3)
#print(rnd)

if rnd == 0:
    com = "가위"
elif rnd == 1:
    com = "바위"
else:
    com = "보"

if a == com:
    result = "비김"
elif a=="가위" and com=="바위" or a=="바위" and com == "보" or a=="보" and com=="가위":
    result = "짐"
else:
    result = "이김"


print("결과:",result)