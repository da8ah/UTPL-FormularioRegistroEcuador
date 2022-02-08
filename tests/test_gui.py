from PyQt5.QtCore import Qt
import pytest
from src.app import ValidationFormDialog


@pytest.mark.parametrize(
    ['window_widget', 'val'],
    [
        ('window.dialog.tfdName', 'Angel'),
        ('window.dialog.tfdLastname', 'Valdivieso'),
        ('window.dialog.tfdEmail', 'agvaldivieso1@unl.edu.ec'),
        ('window.dialog.tfdPhone', '+593 74 3731700'),
        ('window.dialog.tfdCi', '0987654321')
    ]
)
def test_datos_en_widgets(qtbot, window_widget, val):

    qtMainWindow = ValidationFormDialog()

    # Setup
    window = qtMainWindow
    window.show()
    qtbot.addWidget(window)

    qtbot.keyClicks(eval(window_widget), val)
    assert str.isascii(eval(window_widget + '.text()'))


@pytest.mark.parametrize(
    ['window_widget', 'val', 'check_status', 'check_val'],
    [
        ('window.dialog.tfdName', 'Angel',
         'window.dialog.checkName.pixmap().toImage()', 'window.CHECK_OK.toImage()'),
        ('window.dialog.tfdName', 'Ángel',
         'window.dialog.checkName.pixmap().toImage()', 'window.CHECK_ERROR.toImage()'),
        ('window.dialog.tfdLastname', 'Vasquez',
         'window.dialog.checkLastname.pixmap().toImage()', 'window.CHECK_OK.toImage()'),
        ('window.dialog.tfdLastname', 'Vasquez ',
         'window.dialog.checkLastname.pixmap().toImage()', 'window.CHECK_ERROR.toImage()'),
        ('window.dialog.tfdEmail', 'agvaldivieso1@unl.edu.ec',
         'window.dialog.checkEmail.pixmap().toImage()', 'window.CHECK_OK.toImage()'),
        ('window.dialog.tfdEmail', 'agvaldivieso1',
         'window.dialog.checkEmail.pixmap().toImage()', 'window.CHECK_ERROR.toImage()'),
        ('window.dialog.tfdEmail', 'agvaldivieso1@gmail.com',
         'window.dialog.checkEmail.pixmap().toImage()', 'window.CHECK_OK.toImage()'),
        ('window.dialog.tfdEmail', 'ag.valdivieso_1@unl.edu.ec',
         'window.dialog.checkInstitutional.pixmap().toImage()', 'window.CHECK_OK.toImage()'),
        ('window.dialog.tfdEmail', 'agvaldivieso1_@unl.',
         'window.dialog.checkEmail.pixmap().toImage()', 'window.CHECK_ERROR.toImage()'),
        ('window.dialog.tfdEmail', 'agvaldivieso1_@unl.e',
         'window.dialog.checkEmail.pixmap().toImage()', 'window.CHECK_ERROR.toImage()'),
        ('window.dialog.tfdPhone', '+593 74 3731700',
         'window.dialog.checkPhone.pixmap().toImage()', 'window.CHECK_OK.toImage()'),
        ('window.dialog.tfdPhone', '+593 987654321',
         'window.dialog.checkPhone.pixmap().toImage()', 'window.CHECK_OK.toImage()'),
        ('window.dialog.tfdPhone', '0987654321',
         'window.dialog.checkPhone.pixmap().toImage()', 'window.CHECK_OK.toImage()'),
        ('window.dialog.tfdPhone', '+593 986- 543-210',
         'window.dialog.checkPhone.pixmap().toImage()', 'window.CHECK_OK.toImage()'),
        ('window.dialog.tfdPhone', '(072) - 012 - 3456',
         'window.dialog.checkPhone.pixmap().toImage()', 'window.CHECK_OK.toImage()'),
        ('window.dialog.tfdPhone', '01234567',
         'window.dialog.checkPhone.pixmap().toImage()', 'window.CHECK_ERROR.toImage()'),
        ('window.dialog.tfdCi', '0987654321',
         'window.dialog.checkCi.pixmap().toImage()', 'window.CHECK_OK.toImage()'),
        ('window.dialog.tfdCi', '0987654321',
         'window.dialog.tfdProvince.text()', '\'Guayas\''),
        ('window.dialog.tfdCi', '9876543210',
         'window.dialog.checkCi.pixmap().toImage()', 'window.CHECK_ERROR.toImage()'),
        ('window.dialog.tfdCi', '9876543210',
         'window.dialog.tfdProvince.text()', '\'\''),
        ('window.dialog.tfdCi', '012345678',
         'window.dialog.checkCi.pixmap().toImage()', 'window.CHECK_ERROR.toImage()'),
        ('window.dialog.tfdCi', '0123456789 10',
         'window.dialog.checkCi.pixmap().toImage()', 'window.CHECK_ERROR.toImage()')
    ]
)
def test_validaciones_con_checks(qtbot, window_widget, val, check_status, check_val):

    qtMainWindow = ValidationFormDialog()

    # Setup
    window = qtMainWindow
    qtbot.addWidget(window)

    widget = eval(window_widget)
    qtbot.keyClicks(widget, val)
    qtbot.mouseClick(window.dialog.btnValidate, Qt.LeftButton)

    status = eval(check_status)
    check = eval(check_val)
    assert status == check
