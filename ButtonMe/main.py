from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout
import sys

class ButtonMeApp(QWidget):
    """Main application window for ButtonMe."""
    def __init__(self, title, functions):
        super().__init__()
        self.setWindowTitle(title)

        layout = QVBoxLayout()
        for function, args, kwargs in functions:
            layout.addWidget(FunctionButton(function, *args, **kwargs))

        self.setLayout(layout)


class FunctionButton(QPushButton):
    """Button that calls a function when clicked."""

    def __init__(self, function, *args, **kwargs):
        super().__init__(function.__name__)
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.clicked.connect(self.on_click)

    def on_click(self):
        self.function(*self.args, **self.kwargs)


def buttonize(function, *args, **kwargs):
    """
    Decorator to register a function to be displayed as a button in the ButtonMe app.
    """

    global functions
    if 'functions' not in globals():
        functions = []
    functions.append((function, args, kwargs))
    print(f"Registered function: {function.__name__}")
    return function
    

def run(title="Python Buttons"):
    """
    Launch the ButtonMe application.
    Raises ValueError if no functions have been registered.

    Need to be called in the main script to start the GUI.
    """

    if len(functions) == 0:
        raise ValueError("No functions to display.")
    

    app = QApplication(sys.argv)
    window = ButtonMeApp(title=title, functions=functions)
    window.show()
    sys.exit(app.exec())
