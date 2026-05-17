import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QFocusEvent
from PyQt6.QtWidgets import (QWidget, QApplication, QMainWindow, QHBoxLayout,
                             QVBoxLayout, QLabel, QLineEdit, QGroupBox, QRadioButton, QPushButton, QMessageBox)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wprowadzenie danych do paszportu. Wykonał: numer_zdajacego")
        self.setContentsMargins(20, 20, 20, 20)
        self.numer_line = QLineEdit()
        self.numer_line.editingFinished.connect(self.focus_out_event)
        self.imie_line = QLineEdit()
        self.nazwisko_line = QLineEdit()

        self.niebieskie_radio = QRadioButton("niebieskie")
        self.niebieskie_radio.setChecked(True)
        self.zielone_radio = QRadioButton("zielone")
        self.piwne_radio = QRadioButton("piwne")

        self.image_1 = QLabel()
        self.image_2 = QLabel()

        self.button = QPushButton("OK")
        self.button.clicked.connect(self.clicked_event)
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)

        numer_layout = QHBoxLayout()
        numer_layout.addWidget(QLabel("Numer"))
        numer_layout.addWidget(self.numer_line)
        self.numer_line.setFixedWidth(150)
        imie_layout = QHBoxLayout()
        imie_layout.addWidget(QLabel("Imię"))
        imie_layout.addWidget(self.imie_line)
        self.imie_line.setFixedWidth(150)
        nazwisko_layout = QHBoxLayout()
        nazwisko_layout.addWidget(QLabel("Nazwisko"))
        nazwisko_layout.addWidget(self.nazwisko_line)
        self.nazwisko_line.setFixedWidth(150)

        kolor_oczu_layout = QVBoxLayout()
        kolor_oczu_layout.addWidget(self.niebieskie_radio)
        kolor_oczu_layout.addWidget(self.zielone_radio)
        kolor_oczu_layout.addWidget(self.piwne_radio)
        kolor_oczu_group_box = QGroupBox("Kolor oczu")
        kolor_oczu_group_box.setLayout(kolor_oczu_layout)

        left_layout = QVBoxLayout()
        left_layout.addLayout(numer_layout)
        left_layout.addLayout(imie_layout)
        left_layout.addLayout(nazwisko_layout)

        left_layout.addWidget(kolor_oczu_group_box)

        self.image_1.setPixmap(QPixmap("000-zdjecie.jpg"))
        self.image_1.setFixedHeight(225)
        self.image_1.setFixedWidth(195)
        self.image_2.setPixmap(QPixmap("000-odcisk.jpg"))
        self.image_2.setFixedHeight(225)
        self.image_2.setFixedWidth(195)

        image_layout = QHBoxLayout()
        image_layout.addWidget(self.image_1)
        image_layout.addWidget(self.image_2)
        image_layout.setSpacing(40)
        image_layout.setContentsMargins(30, 0, 30, 0)
        self.button.setFixedHeight(40)
        self.button.setFixedWidth(240)

        right_layout = QVBoxLayout()
        right_layout.addLayout(image_layout)
        right_layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignCenter)

        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)

        self.setStyleSheet("""
            QPushButton,
            QLineButton {
                background-color: #F0FFFF;
                color: black;
            }
            QMainWindow {
                background-color: #5F9EA0;
            }
        """)

    def focus_out_event(self):
        numer = self.numer_line.text()
        self.image_1.setPixmap(QPixmap(f"{numer}-zdjecie"))
        self.image_2.setPixmap(QPixmap(f"{numer}-odcisk"))

    def clicked_event(self):
        numer = self.numer_line.text()
        imie = self.imie_line.text()
        nazwisko = self.nazwisko_line.text()
        if numer and imie and nazwisko:
            kolor = ""
            if self.niebieskie_radio.isChecked():
                kolor = self.niebieskie_radio.text()
            if self.zielone_radio.isChecked():
                kolor = self.zielone_radio.text()
            if self.piwne_radio.isChecked():
                kolor = self.piwne_radio.text()

            message = QMessageBox()
            message.setText(f"{imie} {nazwisko} kolor oczu {kolor}")
            message.exec()
        if not imie or not nazwisko:
            message = QMessageBox()
            message.setText(f"Wprowadź dane")
            message.exec()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()