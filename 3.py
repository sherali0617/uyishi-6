import os 
os.system("cls")

from PyQt5.QtWidgets import (
    QApplication,QWidget,QComboBox,QLabel,QVBoxLayout
)

class oyna(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("titul")
        self.setFixedSize(400,200)
        self.setStyleSheet("bacground-color: #1e1e2e;")

        self.vbox=QVBoxLayout()
        self.combo=QComboBox()
        self.combo.addItems(["Python","C++","java"])
        self.combo.setStyleSheet("font-size: 18px; padding: 6px;")
        self.label = QLabel("Tilni tanlang:")
        self.label.setStyleSheet("font-size: 20px; color: black;")

        self.vbox.addWidget(self.combo)
        self.vbox.addWidget(self.label)

        self.combo.currentTextChanged.connect(self.tanlandi)


        self.setLayout(self.vbox)
        self.show()

    def tanlandi(self, text):
        self.label.setText(f"Tanlangan til: {text}")


app = QApplication([])
win = oyna()
app.exec_()

