from PyQt5.QtCore import Qt
from gui import *
from src.app import ValidationFormDialog


def test_inputs(qtbot):

    qtMainWindow = ValidationFormDialog()

    # Setup
    window = qtMainWindow
    # window.show()
    qtbot.addWidget(window)

    qtbot.mouseClick(
        window.mi_widget_input_nombre['Abigail Sánchez'], Qt.LeftButton
    )
    assert str.isascii(window.mi_widget_input.text())


def test_button(qtbot):

    qtMainWindow = ValidationFormDialog()

    # Setup
    window = qtMainWindow
    # window.show()
    qtbot.addWidget(window)

    qtbot.mouseClick(window.buttons['Validar'], Qt.LeftButton)
    assert window.mi_widget_output.value() == True
