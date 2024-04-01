# GUI Test
import os
import sys
import tkinter as tk

from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import*
from PyQt5 import uic
from PyQt5.QtTest import QTest
from secondGUI import SecondClass

'''PyInstaller로 프로그램을 생성하였을 때, 코드에서 호출하는 파일을 상대경로로 호출하기 위한 함수입니다.'''
@(lambda f: f())
def _(): os.chdir(getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__))))

form_class = uic.loadUiType("order_here.ui")[0]

class WindowClass(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.numAme = 0
        self.numLatte = 0
        self.orderNum = 100

        # 메뉴 표시 순서를 위한 FLAG
        self._block1_empty = False
        self._block1_with_Ame = False
        self._block1_with_Latte = False
        self._block2_empty = False
        self._block2_with_Ame = False
        self._block2_with_Latte = False

    def initUI(self):
        self.setupUi(self)
        self.setWindowTitle('ORDER HERE')
        self.setInitStyle()
        self.show()

    def setInitStyle(self):
        self.imgAmericano.setStyleSheet("border-image: url(./images/americano.jpg);")
        self.imgIcelatte.setStyleSheet("border-image: url(./images/icelatte.jpg);")

        self.americanoButton.clicked.connect(lambda: self.clickAme())
        self.latteButton.clicked.connect(lambda: self.clickLatte())
        self.orderButton.clicked.connect(lambda: self.clickOrder())
        self.reset.clicked.connect(lambda: self.clickReset())

    def clickAme(self):
        #
        print("click Americano")
        if self._block1_empty == False or self._block1_with_Ame == True:
            self.widget_2.setStyleSheet("border-image: url(./images/americano.jpg);")
            self.numAme += 1
            self.num1.setText("%d 잔"%(self.numAme))

            self._block1_empty = True
            self._block1_with_Ame = True
            self._block2_with_Latte = True


        if self._block2_with_Ame == True:
            self.widget_3.setStyleSheet("border-image: url(./images/americano.jpg);")
            self.numAme += 1
            self.num2.setText("%d 잔"%(self.numAme))

            self._block2_empty = True
            self._block2_with_Ame = True
            

    def clickLatte(self):
        #
        print("click Latte")
        if self._block1_empty == False or self._block1_with_Latte == True:
            self.widget_2.setStyleSheet("border-image: url(./images/icelatte.jpg);")
            self.numLatte += 1
            self.num1.setText("%d 잔"%(self.numLatte))

            self._block1_empty = True
            self._block1_with_Latte = True
            self._block2_with_Ame = True

        if self._block2_with_Latte == True:
            self.widget_3.setStyleSheet("border-image: url(./images/icelatte.jpg);")
            self.numLatte += 1
            self.num2.setText("%d 잔"%(self.numLatte))

            self._block2_empty = True
            self._block2_with_Latte = True

    def clickOrder(self):
        self.second = SecondClass()
        
        if self.numLatte +self.numAme == 0:
            self.second.label.setText("주문을 입력하세요")

        else:
            self.orderNum += 1
            self.second.label.setText("주문이 완료되었습니다.")
            self.second.label_2.setText("주문번호: %d"%(self.orderNum))
            self.second.label_3.setText("아이스 아메리카노 : %d 잔, 카페라떼 : %d 잔"%(self.numAme, self.numLatte))
            self.clickReset()

    def clickReset(self):
        self.numAme = 0
        self.numLatte = 0

        self._block1_empty = False
        self._block1_with_Ame = False
        self._block1_with_Latte = False
        self._block2_empty = False
        self._block2_with_Ame = False
        self._block2_with_Latte = False

        self.widget_2.setStyleSheet("color: white")
        self.widget_3.setStyleSheet("color: white")
        self.num1.setText("")
        self.num2.setText("")

            

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = WindowClass()
   sys.exit(app.exec_())
   