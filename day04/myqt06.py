#ui를 파이썬에 불러오기
#버튼을 눌렀을 때 Good Evening으로 바꾸기

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import random

#UI파일 연결
form_class = uic.loadUiType("myqt06.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class MainClass(QMainWindow, form_class) :
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.show();
        
    def myclick(self):
        arr45 = list(range(1,45+1)) 
        arr6 = []
        while True:
            rnd = int(random.random() * 45)
            if arr45[rnd] == "-1":
                pass
            else:
                arr6.append(str(arr45[rnd]))
                arr45[rnd]= "-1"
            if len(arr6) >= 6:
                break
        
        self.lbl1.setText(arr6[0])
        self.lbl2.setText(arr6[1])
        self.lbl3.setText(arr6[2])
        self.lbl4.setText(arr6[3])
        self.lbl5.setText(arr6[4])
        self.lbl6.setText(arr6[5])
         
       

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()
    
    