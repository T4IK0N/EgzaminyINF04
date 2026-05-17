import sys
import string
from os import write

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QTextEdit, \
    QPushButton, QFileDialog

def szyfrowanie(tekst: str, klucz: int):
    szyfr = ""
    alfabet = string.ascii_lowercase

    for litera in tekst:
        if litera not in alfabet:
            szyfr += litera
            continue

        index = alfabet.index(litera)
        nowy_index = (index + klucz) % 26
        szyfr += alfabet[nowy_index]

    return szyfr

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Szyfrowanie. Wykonanie przez numer_zdajacego")
        self.setStyleSheet("background-color: #5F9EA0;")

        self.klucz = QLineEdit()
        self.tekst = QTextEdit()
        self.szyfr = QLabel("def")
        self.szyfr.setWordWrap(True)

        self.zaszyfruj_button = QPushButton("Zaszyfruj")
        self.zaszyfruj_button.clicked.connect(self.zaszyfruj_clicked)
        self.zaszyfruj_button.setStyleSheet("background-color: #ADD8E6; color: black;")
        self.szyfr_do_pliku = QPushButton("Zapisz szyfr w pliku")
        self.szyfr_do_pliku.clicked.connect(self.zapisz_do_pliku)
        self.szyfr_do_pliku.setStyleSheet("background-color: #ADD8E6; color: black;")

        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)

        left_layout = QVBoxLayout()
        label1 = QLabel("Podaj wartość klucza")
        label1.setStyleSheet("font-size: 30px; color: #FAEBD7;")
        label2 = QLabel("Podaj tekst")
        label2.setStyleSheet("font-size: 30px; color: #FAEBD7;")
        self.tekst.setFixedHeight(200)
        self.tekst.setFixedWidth(200)

        left_layout.addWidget(label1)
        self.klucz.setFixedWidth(60)
        left_layout.addWidget(self.klucz, alignment=Qt.AlignmentFlag.AlignCenter)
        left_layout.addWidget(label2)
        self.tekst.setFixedWidth(300)
        self.tekst.setFixedHeight(250)
        left_layout.addWidget(self.tekst)

        right_layout = QVBoxLayout()
        label3 = QLabel("Tekst zaszyfrowany")
        label3.setStyleSheet("font-size: 30px; color: #FAEBD7;")
        self.szyfr.setFixedWidth(300)
        self.szyfr.setFixedHeight(300)
        self.szyfr.setStyleSheet("""
            color: #F0F8FF;
            padding: 10px;
            border: 2px solid #FAEBD7;
            border-radius: 20px;
        """)
        self.szyfr.setAlignment(Qt.AlignmentFlag.AlignTop)
        right_layout.addWidget(label3)
        right_layout.addWidget(self.szyfr)
        right_layout.addWidget(self.szyfr_do_pliku)

        main_layout.addLayout(left_layout)
        main_layout.addWidget(self.zaszyfruj_button)
        main_layout.addLayout(right_layout)

    def zaszyfruj_clicked(self):
        self_tekst = self.tekst.toPlainText()
        self_klucz = self.klucz.text()

        if self_klucz == "":
            self_klucz = 0

        self.szyfr.setText(szyfrowanie(self_tekst, int(self_klucz)))

    def zapisz_do_pliku(self):
        filename, _ = QFileDialog.getSaveFileName()
        if filename:
            with open(filename, "w") as f:
                f.write(self.szyfr.text())


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()