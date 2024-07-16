import sys
import math
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout
from PyQt5.QtGui import QFont, QColor


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.setGeometry(200, 200, 200, 300)  
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        
        self.input_box = QLineEdit()
        self.input_box.setAlignment(Qt.AlignRight)  
        font = QFont("Arial", 16, QFont.Bold)  
        self.input_box.setFont(font)
        self.input_box.setReadOnly(True)  
        self.layout.addWidget(self.input_box)

        
        self.result_box = QLineEdit()
        self.result_box.setAlignment(Qt.AlignRight)
        font = QFont("Arial", 12, QFont.Normal)  
        self.result_box.setFont(font)
        self.result_box.setReadOnly(True)
        self.result_box.setStyleSheet("color: gray")  
        self.layout.addWidget(self.result_box)

        
        grid = QGridLayout()

        
        buttons = [
            ('←', self.backspaceClicked), ('C', self.clearClicked), ('±', self.negateClicked), ('√', self.sqrtClicked),
            ('7', self.buttonClicked), ('8', self.buttonClicked), ('9', self.buttonClicked), ('÷', self.buttonClicked),
            ('4', self.buttonClicked), ('5', self.buttonClicked), ('6', self.buttonClicked), ('×', self.buttonClicked),
            ('1', self.buttonClicked), ('2', self.buttonClicked), ('3', self.buttonClicked), ('-', self.buttonClicked),
            ('0', self.buttonClicked), ('.', self.buttonClicked), ('=', self.equalClicked), ('+', self.buttonClicked),
            ('%', self.percentClicked)
        ]

        
        positions = [(i, j) for i in range(7) for j in range(4)]
        for (text, handler), (i, j) in zip(buttons, positions):
            button = QPushButton(text)
            button.clicked.connect(handler)
            button.setFixedSize(50, 30)  
            grid.addWidget(button, i, j)

        self.layout.addLayout(grid)
        self.setLayout(self.layout)

        
        self.input_box.setFocus()

    def buttonClicked(self):
        button = self.sender()
        current_text = self.input_box.text()
        
        replacements = {
            '÷': '/', '×': '*', '|': '-',
        }
        if button.text() in replacements:
            current_text += replacements[button.text()]
        else:
            current_text += button.text()
        self.input_box.setText(current_text)

    def equalClicked(self):
        try:
            result = eval(self.input_box.text())
            self.result_box.setText(str(result))
        except Exception as e:
            self.result_box.setText("Error")

    def clearClicked(self):
        self.input_box.clear()
        self.result_box.clear()

    def backspaceClicked(self):
        current_text = self.input_box.text()
        new_text = current_text[:-1]
        self.input_box.setText(new_text)

    def negateClicked(self):
        current_text = self.input_box.text()
        if current_text and current_text[0] == '-':
            new_text = current_text[1:]
        else:
            new_text = '-' + current_text
        self.input_box.setText(new_text)

    def sqrtClicked(self):
        try:
            number = float(self.input_box.text())
            result = math.sqrt(number)
            self.input_box.setText(str(result))
            self.result_box.setText(str(result))  
        except ValueError:
            self.input_box.setText("Error")
            self.result_box.setText("")

    def percentClicked(self):
        try:
            number = float(self.input_box.text())
            result = number / 100
            self.input_box.setText(str(result))
            self.result_box.setText(str(result))  
        except ValueError:
            self.input_box.setText("Error")
            self.result_box.setText("")

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Backspace:
            self.backspaceClicked()
        elif key == Qt.Key_Escape:
            self.clearClicked()
        elif key == Qt.Key_Return or key == Qt.Key_Enter:
            self.equalClicked()
        elif key == Qt.Key_Plus:
            self.input_box.setText(self.input_box.text() + '+')
        elif key == Qt.Key_Minus:
            self.input_box.setText(self.input_box.text() + '-')
        elif key == Qt.Key_Asterisk:
            self.input_box.setText(self.input_box.text() + '*')
        elif key == Qt.Key_Slash:
            self.input_box.setText(self.input_box.text() + '/')
        elif key == Qt.Key_Percent:
            self.percentClicked()
        elif key == Qt.Key_AsciiCircum:
            self.input_box.setText(self.input_box.text() + '**')
        elif key >= Qt.Key_0 and key <= Qt.Key_9:
            self.input_box.setText(self.input_box.text() + chr(key))
        elif key == Qt.Key_Period:
            self.input_box.setText(self.input_box.text() + '.')
        elif key == Qt.Key_ParenLeft:
            self.input_box.setText(self.input_box.text() + '(')
        elif key == Qt.Key_ParenRight:
            self.input_box.setText(self.input_box.text() + ')')
        elif key == Qt.Key_Exclam:
            self.sqrtClicked()
        elif key == Qt.Key_Question:
            self.negateClicked()
        else:
            super().keyPressEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
