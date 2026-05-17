import sys
from PyQt6.QtWidgets import (QMainWindow, QApplication,
                             QWidget, QGroupBox, QVBoxLayout, QHBoxLayout, QRadioButton,
                             QPushButton, QLabel, QLineEdit, QMessageBox, QDialog)
from PyQt6.QtGui import QImage, QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nadaj Przesyłkę numer_zdajacego")
        self.groupRadio1 = QGroupBox("Rodzaj przesyłki")
        self.groupRadio2 = QGroupBox("Dane adresowe")
        self.radioPocztowka = QRadioButton("Pocztówka")
        self.radioList = QRadioButton("List")
        self.radioPaczka = QRadioButton("Paczka")
        self.ulicaLineEdit = QLineEdit()
        self.kodLineEdit = QLineEdit()
        self.miastoLineEdit = QLineEdit()
        self.buttonSprawdzCene = QPushButton("Sprawdź Cenę")
        self.buttonSprawdzCene.clicked.connect(self.sprawdz_cene)
        self.buttonZatwierdz = QPushButton("Zatwierdź")
        self.buttonZatwierdz.clicked.connect(self.sprawdz_dane)
        self.imageLabel = QLabel()
        self.cenaLabel = QLabel("Cena: 1,5 zł")
        self.setContentsMargins(20, 5, 20, 5)
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_layout = QVBoxLayout()
        main_layout = QHBoxLayout()
        central_widget.setLayout(central_layout)

        left_layout = QVBoxLayout()

        group_layout1 = QVBoxLayout()
        group_layout1.addWidget(self.radioPocztowka)
        group_layout1.addWidget(self.radioList)
        group_layout1.addWidget(self.radioPaczka)
        self.groupRadio1.setLayout(group_layout1)
        self.groupRadio1.setFixedWidth(200)
        self.buttonSprawdzCene.setFixedWidth(200)
        pocztowka_layout = QHBoxLayout()
        self.imageLabel.setPixmap(QPixmap("pocztowka.png"))
        self.cenaLabel.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.cenaLabel.setFixedWidth(110)
        pocztowka_layout.setSpacing(30)
        pocztowka_layout.addWidget(self.imageLabel)
        pocztowka_layout.addWidget(self.cenaLabel)

        left_layout.addWidget(self.groupRadio1)
        left_layout.addWidget(self.buttonSprawdzCene)
        left_layout.addLayout(pocztowka_layout)

        right_layout = QVBoxLayout()

        group_layout2 = QVBoxLayout()
        group_layout2.addWidget(QLabel("Ulica z numerem"))
        group_layout2.addWidget(self.ulicaLineEdit)
        group_layout2.addWidget(QLabel("Kod pocztowy"))
        group_layout2.addWidget(self.kodLineEdit)
        group_layout2.addWidget(QLabel("Miasto"))
        group_layout2.addWidget(self.miastoLineEdit)
        self.groupRadio2.setFixedWidth(250)
        self.groupRadio2.setLayout(group_layout2)

        right_layout.addWidget(self.groupRadio2)

        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)
        central_layout.addLayout(main_layout)
        central_layout.addWidget(self.buttonZatwierdz)

    def sprawdz_cene(self):
        if self.radioPocztowka.isChecked():
            self.imageLabel.setPixmap(QPixmap("pocztowka.png"))
            self.cenaLabel.setText("Cena: 1zł")
        if self.radioList.isChecked():
            self.imageLabel.setPixmap(QPixmap("list.png"))
            self.cenaLabel.setText("Cena: 1,5zł")
        if self.radioPaczka.isChecked():
            self.imageLabel.setPixmap(QPixmap("paczka.png"))
            self.cenaLabel.setText("Cena: 10zł")

    def sprawdz_dane(self):
        text = self.kodLineEdit.text()
        poprawnie = True
        if len(text) != 5:
            message = QMessageBox()
            message.setText("Nieprawidłowa liczba cyfr w kodzie pocztowym")
            message.exec()
            poprawnie = False

        for i in text:
            if not i.isnumeric():
                message = QMessageBox()
                message.setText("Kod pocztowy powinien się składać z samych cyfr")
                message.exec()
                poprawnie = False
                break

        if poprawnie:
            message = QMessageBox()
            message.setText("Dane przesyłki zostały wprowadzone")
            message.exec()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()