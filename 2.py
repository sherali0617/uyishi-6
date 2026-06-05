import os 
os.system("cls")

from PyQt5.QtWidgets import (
    QVBoxLayout,QPushButton,QApplication,QWidget,QLabel
)



class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500,500)
        self.setWindowTitle("Dastur")
        self.vbox=QVBoxLayout()
        self.btn1=QPushButton("chapga")
        self.btn2=QPushButton("Ortaga")
        self.btn3=QPushButton("O'nga")


        # layout qoshish
        self.vbox.addWidget(self.btn1)
        self.vbox.addWidget(self.btn2)
        self.vbox.addWidget(self.btn3)

        # label
        self.label=QLabel("")
        self.label.setStyleSheet("font-size: 18px; color: black;")
        self.vbox.addWidget(self.label)

        # ulash
        self.btn1.clicked.connect(self.bosildi1)
        self.btn2.clicked.connect(self.bosildi2)
        self.btn3.clicked.connect(self.bosildi3)

        self.setLayout(self.vbox)
        self.show()


    def bosildi1(self):
        self.label.setText("1-tugma bosildi!")
    def bosildi2(self):
        self.label.setText("2-tugma bosildi!")
    def bosildi3(self):
        self.label.setText("3-tugma bosildi!")

app=QApplication([])
win=Window()
app.exec_()
