import sys
import function as func
from pyqt5_plugins.examplebutton import QtWidgets
from detectionUI import Ui_MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    func.open_camera(ui)
    MainWindow.show()
    sys.exit(app.exec_())
