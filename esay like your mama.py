import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("Test Window")
    window.show()
    sys.exit(app.exec_())