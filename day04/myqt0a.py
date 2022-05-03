#ui를 파이썬에 불러오기
#버튼을 눌렀을 때 Good Evening으로 바꾸기

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic
import random

#UI파일 연결
form_class = uic.loadUiType("myqt0a.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class MainClass(QMainWindow, form_class) :
    
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.setCom()
        self.show()
        
    def setCom(self): 
        arr9 = ["1","2","3","4","5","6","7","8","9"]
        arr3 = []
        while len(arr3) < 3:
            rnd = int(random.random() * 9)
            if not (arr9[rnd] == "-1"):
                arr3.append(arr9[rnd])
                arr9[rnd]= "-1"
            
        self.com = arr3[0] + arr3[1] + arr3[2];
        print("com :", self.com)
        return self.com
    
    def myclick(self):
        str_old = self.te.toPlainText()
        str_new = self.getBallStrike()
        self.te.setText(str_old + str_new) 
        
    def getBallStrike(self):
        input = self.le.text()
        
        strike = 0
        ball = 0
        
        n1 = input[0:1]
        n2 = input[1:2]
        n3 = input[2:3]
        
        c1 = self.com[0:1]
        c2 = self.com[1:2]
        c3 = self.com[2:3]
        
        if n1 == c1:
            strike += 1
        if n2 == c2:
            strike += 1
        if n3 == c3:
            strike += 1
        
        if n1 == c2 or n1 == c3:
            ball += 1
        if n2 == c1 or n1 == c3:
            ball += 1
        if n3 == c1 or n1 == c2:
            ball += 1
        
        if strike==3:
            QMessageBox.about(self, 'baseball', 'congratulation~~!!')
        
        result =  "{} - {}S{}B \n".format(input,strike,ball) 
        
        return result
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()
    
    