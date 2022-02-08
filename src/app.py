from PyQt5.QtWidgets import QDialog, QLabel
from PyQt5.QtGui import QPixmap
from src.ui.MainWindow import Ui_Dialog
from src.validar_cedula import validar_cedula
from src.validar_correo import validar_correo
from src.validar_nombre_apellido import validar_nombre_apellido
from src.validar_telefono import validar_telefono


class ValidationFormDialog(QDialog):

    def __init__(self):
        super().__init__()

        # Objetos QPixmap para representar iconos en la iterfaz
        self.CHECK_OK = QPixmap(':/icons/img/Check.png')
        self.CHECK_ERROR = QPixmap(':/icons/img/Cross.png')
        self.CHECK_BLANK = QPixmap(None)

        # Inicializacion de la interfaz
        self.dialog = Ui_Dialog()
        self.dialog.setupUi(self)

        # Conexion de evento clicked con el metodo validateForm
        self.dialog.btnValidate.clicked.connect(self.validateForm)

    def changeCheckStatus(self, checkLabel: QLabel, status=None):
        # Metodo encargado de gestionar el cambio de icono
        # en los checks de verificacion
        if status == None:
            status = self.CHECK_BLANK

        checkLabel.setPixmap(status)

    def validateForm(self):
        # Ejecucion de las validaciones
        if validar_nombre_apellido(str(self.dialog.tfdName.text())):
            self.changeCheckStatus(self.dialog.checkName, self.CHECK_OK)
        else:
            self.changeCheckStatus(self.dialog.checkName, self.CHECK_ERROR)

        if validar_nombre_apellido(str(self.dialog.tfdLastname.text())):
            self.changeCheckStatus(self.dialog.checkLastname, self.CHECK_OK)
        else:
            self.changeCheckStatus(self.dialog.checkLastname, self.CHECK_ERROR)

        correo = validar_correo(str(self.dialog.tfdEmail.text()))
        if correo[0] == True:
            self.changeCheckStatus(self.dialog.checkEmail, self.CHECK_OK)
        else:
            self.changeCheckStatus(self.dialog.checkEmail, self.CHECK_ERROR)

        if correo[1] == True:
            self.changeCheckStatus(
                self.dialog.checkInstitutional, self.CHECK_OK)
        else:
            self.changeCheckStatus(
                self.dialog.checkInstitutional, self.CHECK_ERROR)

        if validar_telefono(str(self.dialog.tfdPhone.text())):
            self.changeCheckStatus(self.dialog.checkPhone, self.CHECK_OK)
        else:
            self.changeCheckStatus(self.dialog.checkPhone, self.CHECK_ERROR)

        provincia = validar_cedula(str(self.dialog.tfdCi.text()))
        if provincia != None:
            self.changeCheckStatus(self.dialog.checkCi, self.CHECK_OK)
            self.dialog.tfdProvince.setText(provincia)
        else:
            self.changeCheckStatus(self.dialog.checkCi, self.CHECK_ERROR)
