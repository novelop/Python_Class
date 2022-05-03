#ui를 파이썬에 불러오기
#버튼을 눌렀을 때 Good Evening으로 바꾸기

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import random

#UI파일 연결
form_class = uic.loadUiType("myqt04.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class MainClass(QMainWindow, form_class) :
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.show();
        
    def myclick(self):
        mine = self.le_mine.text()
        com = ""
        result = ""
        rnd = random.random()
        if rnd > 0.5:
            com = "홀"
        else:
            com = "짝"
        if mine == com: 
            result = "이김"
        else: 
            result = "짐"
         
        self.le_com.setText(com)
        self.le_result.setText(result)    
      
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()
    
    