from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QVBoxLayout

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ranglar")
        self.setFixedSize(400,400)

        self.vbox = QVBoxLayout()

        self.r1 = QRadioButton("Qizil")
        self.r2 = QRadioButton("Yashil")
        self.r3 = QRadioButton("Ko'k")

        style = "font-size: 18px; color: black;"
        self.r1.setStyleSheet(style)
        self.r2.setStyleSheet(style)
        self.r3.setStyleSheet(style)

        self.vbox.addWidget(self.r1)
        self.vbox.addWidget(self.r2)
        self.vbox.addWidget(self.r3)

        self.r1.toggled.connect(self.rang_ozgar)
        self.r2.toggled.connect(self.rang_ozgar)
        self.r3.toggled.connect(self.rang_ozgar)

        self.setLayout(self.vbox)
        self.show()

    def rang_ozgar(self):
        if self.r1.isChecked():
            self.setStyleSheet("background-color: red;")
        elif self.r2.isChecked():
            self.setStyleSheet("background-color: green;")
        elif self.r3.isChecked():
            self.setStyleSheet("background-color: blue;")


app = QApplication([])
win = Window()
app.exec_()