# 1에서 부터 9까지의 수중에서 3가지를 랜덤 중복없이 
# 출력하시오 
import random

arr9 = [1,2,3,4,5,6,7,8,9] 
for i in range(100):
    rnd = int(random.random() * 9) 
    a = arr9[rnd]
    b = arr9[0]
    arr9[0]=a
    arr9[rnd]=b

print("arr9",arr9)
print(arr9[0:3])


# while True:
#
#     ran1 = int(random.random() * 9 + 1)
#     ran2 = int(random.random() * 9 + 1)
#     ran3 = int(random.random() * 9 + 1)
#
#     if ran1 != ran2 and ran1 != ran3 and ran2 != ran3: break
#
# print(ran1,ran2,ran3)