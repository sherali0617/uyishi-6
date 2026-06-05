import os 
os.system("cls")

from PyQt5.QtWidgets import (
    QVBoxLayout,QPushButton,QApplication,QWidget,
)



class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500,500)
        self.setWindowTitle("3ta tugma")
        self.vbox=QVBoxLayout()
        self.btn1=QPushButton("1")
        self.btn2=QPushButton("2")
        self.btn3=QPushButton("3")


        # layout qoshish
        self.vbox.addWidget(self.btn1)
        self.vbox.addWidget(self.btn2)
        self.vbox.addWidget(self.btn3)

        # ulash
        self.btn1.clicked.connect(self.bosildi1)
        self.btn2.clicked.connect(self.bosildi2)
        self.btn3.clicked.connect(self.bosildi3)

        self.setLayout(self.vbox)
        self.show()


    def bosildi1(self):
        print("1-tugma bosildi!")
    def bosildi2(self):
        print("2-tugma bosildi!")
    def bosildi3(self):
        print("3-tugma bosildi!")

app=QApplication([])
win=Window()
app.exec_()
