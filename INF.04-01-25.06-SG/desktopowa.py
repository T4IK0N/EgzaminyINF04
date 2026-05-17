import sys
from tkinter.constants import HORIZONTAL

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget,
                             QLabel, QSlider, QPushButton, QVBoxLayout, QHBoxLayout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wzornik kolorów RGB. Wykonał numer_zdajacego")
        self.setGeometry(700, 300, 700, 300)
        self.rectangle = QLabel()
        self.rectangle.setObjectName("rectangle")

        self.slider_R = QSlider(Qt.Orientation.Horizontal)
        self.slider_R.valueChanged.connect(self.zmien_kolor)
        self.slider_G = QSlider(Qt.Orientation.Horizontal)
        self.slider_G.valueChanged.connect(self.zmien_kolor)
        self.slider_B = QSlider(Qt.Orientation.Horizontal)
        self.slider_B.valueChanged.connect(self.zmien_kolor)
        self.slider_label_R = QLabel("255")
        self.slider_label_G = QLabel("255")
        self.slider_label_B = QLabel("255")
        self.value_r = 255
        self.value_g = 255
        self.value_b = 255

        self.download_button = QPushButton("Pobierz")
        self.download_button.setObjectName("download_button")
        self.download_button.clicked.connect(self.pobierz)
        self.download_label = QLabel("255, 255, 255")
        self.download_label.setObjectName("download_label")

        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        main_layout.setObjectName("main_layout")
        central_widget.setLayout(main_layout)
        central_widget.setObjectName("central_widget")
        central_widget.setContentsMargins(20, 10, 20, 10)

        self.rectangle.setFixedHeight(100)
        self.rectangle.setStyleSheet("background-color: red;")

        slider_layout_R = QHBoxLayout()
        slider_layout_R.addWidget(QLabel("R"))
        self.slider_R.setMaximum(255)
        self.slider_R.setMinimum(0)
        self.slider_R.setValue(255)
        slider_layout_R.addWidget(self.slider_R)
        slider_layout_R.addWidget(self.slider_label_R)
        slider_layout_G = QHBoxLayout()
        slider_layout_G.addWidget(QLabel("G"))
        self.slider_G.setMaximum(255)
        self.slider_G.setMinimum(0)
        self.slider_G.setValue(255)
        slider_layout_G.addWidget(self.slider_G)
        slider_layout_G.addWidget(self.slider_label_G)
        slider_layout_B = QHBoxLayout()
        slider_layout_B.addWidget(QLabel("B"))
        self.slider_B.setMaximum(255)
        self.slider_B.setMinimum(0)
        self.slider_B.setValue(255)
        slider_layout_B.addWidget(self.slider_B)
        slider_layout_B.addWidget(self.slider_label_B)

        slider_layout = QVBoxLayout()
        slider_layout.addWidget(QLabel("Dobierz kolor suwakami i zapisz przyciskiem:"))
        slider_layout.addLayout(slider_layout_R)
        slider_layout.addLayout(slider_layout_G)
        slider_layout.addLayout(slider_layout_B)

        button_layout = QVBoxLayout()
        self.download_button.setFixedWidth(170)
        self.download_label.setFixedWidth(170)
        self.download_button.setFixedHeight(40)
        self.download_label.setFixedHeight(40)
        button_layout.addWidget(self.download_button, alignment=Qt.AlignmentFlag.AlignCenter)
        button_layout.addWidget(self.download_label, alignment=Qt.AlignmentFlag.AlignCenter)
        button_layout.setSpacing(20)

        main_layout.addWidget(self.rectangle, alignment=Qt.AlignmentFlag.AlignTop)
        main_layout.addLayout(slider_layout)
        main_layout.addLayout(button_layout)

        self.setStyleSheet("""
            * {
                color: black;
            }
            #central_widget {
                background-color: #FFF8DC;
            }
            #download_button {
                background-color: #CD853F;
            }
            #download_label {
                background-color: white;
                color: black;
            }
            #rectangle {
                background-color: rgb(255, 255, 255);
            }
        """)

    def zmien_kolor(self):
        value = str(self.sender().value())
        if self.slider_R == self.sender():
            self.slider_label_R.setText(value)
            self.value_r = int(value)
        if self.slider_G == self.sender():
            self.slider_label_G.setText(value)
            self.value_g = int(value)
        if self.slider_B == self.sender():
            self.slider_label_B.setText(value)
            self.value_b = int(value)

        self.rectangle.setStyleSheet(f"background-color: rgb({self.value_r}, {self.value_g}, {self.value_b})")

    def pobierz(self):
        self.download_label.setText(f"{self.value_r}, {self.value_g}, {self.value_b}")
        self.download_label.setStyleSheet(f"background-color: rgb({self.value_r}, {self.value_g}, {self.value_b})")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()