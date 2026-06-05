from PyQt5.QtWidgets import (
    QApplication, QWidget, QLineEdit, QPushButton, QComboBox, QHBoxLayout, QVBoxLayout
    )

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("So'z qo'shish")
        self.setFixedSize(400, 300)
        self.setStyleSheet("background-color: white;")

        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()

        self.input = QLineEdit()
        self.input.setPlaceholderText("So'z kiriting:")
        self.input.setStyleSheet("font-size: 17px; padding: 8px; color: white; background-color: #313244; border: 2px solid #c084fc; border-radius: 6px;")

        self.btn = QPushButton("Qo'shish")
        self.btn.setStyleSheet("font-size: 17px; padding: 8px; color: white; background-color: #313244; border-radius: 6px;")

        self.combo = QComboBox()
        self.combo.setStyleSheet("font-size: 17px; padding: 6px;")

        self.hbox.addWidget(self.input)
        self.hbox.addWidget(self.btn)

        self.vbox.addLayout(self.hbox)
        self.vbox.addWidget(self.combo)

        self.btn.clicked.connect(self.qoshish)

        self.setLayout(self.vbox)
        self.show()

    def qoshish(self):
        text = self.input.text().strip()

        if not text:
            return

        self.combo.addItem(text)
        self.input.clear()


app = QApplication([])
win = Window()
app.exec_()