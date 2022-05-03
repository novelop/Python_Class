#출력하고 싶은 단수를 입력하세요 6 Enter
# 6*1 = 6
#.
#.



a = input("출력하고 싶은 단수를 입력하세요")

for i in range(1,9+1):
   # print(a , "*", i, "=", int(a)*i)

    print("{}*{}={}".format(a,i,int(a)*i))