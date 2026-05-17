import sys
from PyQt6.QtWidgets import (QWidget, QApplication, QMainWindow,
                             QGroupBox, QLineEdit, QComboBox, QLabel,
                             QVBoxLayout, QHBoxLayout, QPushButton, QCheckBox, QMessageBox)
from PyQt6.QtCore import Qt
import random


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dodaj pracownika numer_zdajacego")
        self.firstGroupBox = QGroupBox("Dane pracownika")
        self.firstNameLineEdit = QLineEdit()
        self.lastNameLineEdit = QLineEdit()
        self.comboBox = QComboBox()
        self.charsQuantityLineEdit = QLineEdit()

        self.firstCheckBox = QCheckBox("Małe i wielkie litery")
        self.secondCheckBox = QCheckBox("Cyfry")
        self.thirdCheckBox = QCheckBox("Znaki specjalne")

        self.secondGroupBox = QGroupBox("Generowanie hasła")
        self.submit_button = QPushButton("Zatwierdź")
        self.submit_button.clicked.connect(self.submit_data)
        self.submit_button.setStyleSheet("background-color: #4682B4; color: white;")
        self.generate_password_button = QPushButton("Generuj hasło")
        self.generate_password_button.clicked.connect(self.generate_password)
        self.generate_password_button.setStyleSheet("background-color: #4682B4; color: white;")

        self.generated_password = ""

        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        central_widget.setStyleSheet("background-color: #B0C4DE;")
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        self.firstGroupBox.setFixedWidth(300)
        self.firstNameLineEdit.setFixedWidth(150)
        self.lastNameLineEdit.setFixedWidth(150)
        self.charsQuantityLineEdit.setFixedWidth(150)
        self.comboBox.setFixedWidth(150)
        self.comboBox.addItem("Kierownik")
        self.comboBox.addItem("Starszy programista")
        self.comboBox.addItem("Młodszy programista")
        self.comboBox.addItem("Tester")

        layout1 = QHBoxLayout()
        layout1.addWidget(QLabel("Imię"))
        layout1.addWidget(self.firstNameLineEdit)
        layout2 = QHBoxLayout()
        layout2.addWidget(QLabel("Nazwisko"))
        layout2.addWidget(self.lastNameLineEdit)
        layout3 = QHBoxLayout()
        layout3.addWidget(QLabel("Stanowisko"))
        layout3.addWidget(self.comboBox)

        first_group_layout = QVBoxLayout()
        first_group_layout.addLayout(layout1)
        first_group_layout.addLayout(layout2)
        first_group_layout.addLayout(layout3)
        first_group_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        first_group_layout.setSpacing(15)

        layout4 = QHBoxLayout()
        layout4.addWidget(QLabel("Ile znaków?"))
        layout4.addWidget(self.charsQuantityLineEdit)
        layout5 = QVBoxLayout()
        layout5.addWidget(self.firstCheckBox)
        layout5.addWidget(self.secondCheckBox)
        layout5.addWidget(self.thirdCheckBox)
        layout5.addWidget(self.generate_password_button, alignment=Qt.AlignmentFlag.AlignCenter)

        second_group_layout = QVBoxLayout()
        second_group_layout.addLayout(layout4)
        second_group_layout.addLayout(layout5)
        second_group_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        second_group_layout.setSpacing(15)

        self.firstGroupBox.setLayout(first_group_layout)
        self.secondGroupBox.setLayout(second_group_layout)

        self.secondGroupBox.setFixedWidth(350)

        group_layout = QHBoxLayout()
        group_layout.addWidget(self.firstGroupBox)
        group_layout.addWidget(self.secondGroupBox)

        main_layout.addLayout(group_layout)
        self.submit_button.setFixedWidth(200)
        main_layout.addWidget(self.submit_button, alignment=Qt.AlignmentFlag.AlignCenter)
        main_layout.setSpacing(50)
        main_layout.setContentsMargins(25, 25, 25, 15)

    def submit_data(self):
        imie = self.firstNameLineEdit.text()
        nazwisko = self.lastNameLineEdit.text()
        stanowisko = self.comboBox.currentText()
        haslo = getattr(self, "generated_password", "Brak")

        QMessageBox.information(
            self,
            "Dane pracownika",
            f"Imię: {imie}\n"
            f"Nazwisko: {nazwisko}\n"
            f"Stanowisko: {stanowisko}\n"
            f"Hasło: {haslo}"
        )

    def generate_password(self):
        male_litery = "abcdefghijklmnoprstuwxyz"
        wielkie_litery = "ABCDEFGHIJKLMNOPRSTUWXYZ"
        cyfry = "0123456789"
        symbole = "!@#$%^&*()_+-="

        dlugosc_hasla = int(self.charsQuantityLineEdit.text())
        czy_wielkie_litery = self.firstCheckBox.isChecked()
        czy_cyfry = self.secondCheckBox.isChecked()
        czy_symbole = self.thirdCheckBox.isChecked()

        haslo = []
        for i in range(dlugosc_hasla):
            haslo.append(random.choice(male_litery))

        if czy_wielkie_litery:
            haslo[0] = random.choice(wielkie_litery)
        if czy_cyfry:
            haslo[1] = random.choice(cyfry)
        if czy_symbole:
            haslo[2] = random.choice(symbole)

        self.generated_password = "".join(haslo)

        QMessageBox.information(
            self,
            "Wygenerowane hasło",
            f"Hasło:\n{self.generated_password}"
        )

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()