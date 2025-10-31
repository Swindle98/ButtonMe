from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout
import sys

class ButtonMeApp(QWidget):
    def __init__(self, functions):
        super().__init__()
        self.setWindowTitle("Python Buttons")

        layout = QVBoxLayout()
        for function in range(functions):
            layout.addWidget


class FunctionButton(QPushButton):

    def __init__(self, function):
        super().__init__(function.__name__)
        self.function = function
        self.clicked.connect(self.on_click)

    def on_click(self):
        self.function()


def buttonize(function):
    global functions
    if 'functions' not in globals():
        functions = []
    functions.append(function)
    return function
    

def run():
    global functions
    functions = []

    if len(functions) == 0:
        raise ValueError("No functions to display.")
        return
    

    app = QApplication(sys.argv)
    window = ButtonMeApp()
    window.show()
    sys.exit(app.exec())
