#ui를 파이썬에 불러오기
#버튼을 눌렀을 때 Good Evening으로 바꾸기

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic

#UI파일 연결
form_class = uic.loadUiType("myqt08.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class MainClass(QMainWindow, form_class) :
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pb1.clicked.connect(self.myclick)
        self.pb2.clicked.connect(self.myclick)
        self.pb3.clicked.connect(self.myclick)
        self.pb4.clicked.connect(self.myclick)
        self.pb5.clicked.connect(self.myclick)
        self.pb6.clicked.connect(self.myclick)
        self.pb7.clicked.connect(self.myclick)
        self.pb8.clicked.connect(self.myclick)
        self.pb9.clicked.connect(self.myclick)
        self.pb0.clicked.connect(self.myclick)
        self.pb_call.clicked.connect(self.mycall)
        self.show();
    
    def mycall(self):
        str_tel = self.le.text()
        QMessageBox.about(self, 'calling', str_tel)
            
    def myclick(self):
        str_new = self.sender().text()
        str_old = self.le.text()
        self.le.setText(str_old + str_new)
        
       

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()
    
    