#ui를 파이썬에 불러오기
#버튼을 눌렀을 때 Good Evening으로 바꾸기

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import random

#UI파일 연결
form_class = uic.loadUiType("myqt09.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class MainClass(QMainWindow, form_class) :
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.leMine.returnPressed.connect(self.myclick)
        self.show();
        
    def myclick(self):
        mine = self.leMine.text()
        com = ""
        result = ""
        
        rnd = random.random()
        if rnd > 0.66:
            com = "가위"
        elif rnd > 0.33:
            com = "바위"
        else:
            com = "보"
            
        if mine==com: 
            result = "비김"
        elif mine=="가위" and com=="바위" or mine=="바위" and com=="보" or mine=="보" and com=="가위":
            result = "짐"
        else:
            result ="이김"
         
        self.leCom.setText(com)
        self.leResult.setText(result)    
      
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()
    
    