from PyQt5.QtWidgets import QDialog, QLabel
from PyQt5.QtGui import QPixmap
from src.ui.MainWindow import Ui_Dialog


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

        # Test de cambio de icono en los checks de validadicon
        self.changeCheckStatus(self.dialog.checkName, self.CHECK_OK)
        self.changeCheckStatus(self.dialog.checkLastname, self.CHECK_ERROR)
        self.changeCheckStatus(
            self.dialog.checkInstitutional, self.CHECK_BLANK)

    def changeCheckStatus(self, checkLabel: QLabel, status=None):
        # Metodo encargado de gestionar el cambio de icono
        # en los checks de verificacion
        if status == None:
            status = self.CHECK_BLANK

        checkLabel.setPixmap(status)

    def validateForm(self):
        # Ejecucion de las validaciones
        print('Validando formulario...')
