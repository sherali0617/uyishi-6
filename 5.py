from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QLabel, QVBoxLayout

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mahsulotlar")
        self.setFixedSize(400, 250)
        self.setStyleSheet("background-color: #1e1e2e;")

        self.vbox = QVBoxLayout()

        self.narxlar = {
            "Olma":  5000,
            "Banan": 7000,
            "Uzum":  8000
        }

        self.checkboxlar = []

        for nom, narx in self.narxlar.items():
            cb = QCheckBox(f"{nom} - {narx} so'm")
            cb.setStyleSheet("font-size: 18px; color: white;")
            cb.stateChanged.connect(self.hisobla)
            self.vbox.addWidget(cb)
            self.checkboxlar.append((cb, narx))

        self.label = QLabel("Jami: 0 so'm")
        self.label.setStyleSheet("font-size: 20px; color: white; font-weight: bold;")
        self.vbox.addWidget(self.label)

        self.setLayout(self.vbox)
        self.show()

    def hisobla(self):
        jami = 0
        for cb, narx in self.checkboxlar:
            if cb.isChecked():
                jami += narx
        self.label.setText(f"Jami: {jami} so'm")


app = QApplication([])
win = Window()
app.exec_()