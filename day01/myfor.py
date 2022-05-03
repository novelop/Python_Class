import random

a = input("홀짝을 입력하세요")
rnd = random.random()
b = ""
if rnd > 0.5:
    b ="짝"
else:
    b ="홀"

print(b)
if a == b:
    print("이겼습니다.")
else:
    print("졌습니다.")