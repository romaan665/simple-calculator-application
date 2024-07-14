import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit, QPushButton
from PyQt6.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('PyQt6 Calculator')
        self.setGeometry(100, 100, 300, 400)

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.createDisplay()
        self.createButtons()

    def createDisplay(self):
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setFixedHeight(50)
        self.layout.addWidget(self.display, 0, 0, 1, 4)

    def createButtons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for btn_text, row, col in buttons:
            button = QPushButton(btn_text)
            button.setFixedSize(50, 50)
            self.layout.addWidget(button, row, col)
            button.clicked.connect(self.onButtonClick)

    def onButtonClick(self):
        button = self.sender()
        text = button.text()

        if text == '=':
            try:
                expression = self.display.text()
                result = eval(expression)
                self.display.setText(str(result))
            except Exception as e:
                self.display.setText('Error')
        elif text == 'C':
            self.display.clear()
        else:
            current_text = self.display.text()
            new_text = current_text + text
            self.display.setText(new_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec())
