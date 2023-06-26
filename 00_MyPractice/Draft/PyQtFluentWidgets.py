import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from qfluentwidgets import DisplayLabel, PrimaryToolButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Fluent Widgets Example")
        self.setGeometry(100, 100, 400, 200)

        label = DisplayLabel("Hello, PyQt-Fluent-Widgets!", self)
        label.move(20, 20)

        button = PrimaryToolButton("Click me", self)
        button.move(20, 60)
        button.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        print("Button clicked!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
