import sys
from PyQt5.QtWidgets import QApplication
from src.app import ValidationFormDialog


def main():
    app = QApplication(sys.argv)
    dialog = ValidationFormDialog()
    dialog.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
