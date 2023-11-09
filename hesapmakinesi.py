import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit


class HesapMakinesi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Hesap Makinesi')
        self.setGeometry(100, 100, 400, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.result_display = QLineEdit()
        self.layout.addWidget(self.result_display)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]

        grid_layout = QVBoxLayout()

        for label in buttons:
            button = QPushButton(label)
            button.clicked.connect(self.on_button_click)
            grid_layout.addWidget(button)

        self.layout.addLayout(grid_layout)

        self.current_input = ''

    def on_button_click(self):
        button = self.sender()
        if button.text() == '=':
            try:
                result = str(eval(self.current_input))
                self.result_display.setText(result)
            except Exception as e:
                self.result_display.setText('Hatalı Giriş')
            self.current_input = ''
        elif button.text() == 'C':
            self.current_input = ''
            self.result_display.clear()
        else:
            self.current_input += button.text()
            self.result_display.setText(self.current_input)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HesapMakinesi()
    window.show()
    sys.exit(app.exec_())
