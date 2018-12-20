import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_main import Ui_mainWindow

app = QApplication(sys.argv)
window = QMainWindow()
ui = Ui_mainWindow()
ui.setupUi(window)

window.show()
sys.exit(app.exec_())
