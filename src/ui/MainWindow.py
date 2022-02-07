# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\gui\form.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import src.ui.resource_rc as resource_rc
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(563, 260)
        Dialog.setStyleSheet("QLabel {\n"
                             "    font: 12pt \"MS Shell Dlg 2\";\n"
                             "}\n"
                             "\n"
                             "QLineEdit {\n"
                             "    font: 10pt \"MS Shell Dlg 2\";\n"
                             "}")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.grpForm = QtWidgets.QGroupBox(Dialog)
        self.grpForm.setObjectName("grpForm")
        self.formLayout = QtWidgets.QFormLayout(self.grpForm)
        self.formLayout.setContentsMargins(12, 12, 12, 12)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.grpForm)
        self.label.setObjectName("label")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.tfdName = QtWidgets.QLineEdit(self.grpForm)
        self.tfdName.setObjectName("tfdName")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.tfdName)
        self.label_2 = QtWidgets.QLabel(self.grpForm)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.tfdLastname = QtWidgets.QLineEdit(self.grpForm)
        self.tfdLastname.setObjectName("tfdLastname")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.tfdLastname)
        self.label_3 = QtWidgets.QLabel(self.grpForm)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.tfdEmail = QtWidgets.QLineEdit(self.grpForm)
        self.tfdEmail.setObjectName("tfdEmail")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.tfdEmail)
        self.label_4 = QtWidgets.QLabel(self.grpForm)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.tfdPhone = QtWidgets.QLineEdit(self.grpForm)
        self.tfdPhone.setObjectName("tfdPhone")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.FieldRole, self.tfdPhone)
        self.label_5 = QtWidgets.QLabel(self.grpForm)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.tfdCi = QtWidgets.QLineEdit(self.grpForm)
        self.tfdCi.setObjectName("tfdCi")
        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.FieldRole, self.tfdCi)
        spacerItem = QtWidgets.QSpacerItem(
            80, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(5, QtWidgets.QFormLayout.LabelRole, spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(
            200, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(
            5, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        self.btnValidate = QtWidgets.QPushButton(self.grpForm)
        self.btnValidate.setObjectName("btnValidate")
        self.formLayout.setWidget(
            6, QtWidgets.QFormLayout.FieldRole, self.btnValidate)
        self.horizontalLayout.addWidget(self.grpForm)
        self.grpChecks = QtWidgets.QGroupBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.grpChecks.sizePolicy().hasHeightForWidth())
        self.grpChecks.setSizePolicy(sizePolicy)
        self.grpChecks.setMinimumSize(QtCore.QSize(24, 0))
        self.grpChecks.setMaximumSize(QtCore.QSize(48, 16777215))
        self.grpChecks.setTitle("")
        self.grpChecks.setFlat(False)
        self.grpChecks.setCheckable(False)
        self.grpChecks.setObjectName("grpChecks")
        self.formLayout_2 = QtWidgets.QFormLayout(self.grpChecks)
        self.formLayout_2.setContentsMargins(12, 24, 12, 12)
        self.formLayout_2.setVerticalSpacing(10)
        self.formLayout_2.setObjectName("formLayout_2")
        self.checkName = QtWidgets.QLabel(self.grpChecks)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkName.sizePolicy().hasHeightForWidth())
        self.checkName.setSizePolicy(sizePolicy)
        self.checkName.setMinimumSize(QtCore.QSize(22, 22))
        self.checkName.setMaximumSize(QtCore.QSize(22, 22))
        self.checkName.setText("")
        self.checkName.setScaledContents(True)
        self.checkName.setObjectName("checkName")
        self.formLayout_2.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.checkName)
        self.checkLastname = QtWidgets.QLabel(self.grpChecks)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkLastname.sizePolicy().hasHeightForWidth())
        self.checkLastname.setSizePolicy(sizePolicy)
        self.checkLastname.setMinimumSize(QtCore.QSize(22, 22))
        self.checkLastname.setMaximumSize(QtCore.QSize(22, 22))
        self.checkLastname.setText("")
        self.checkLastname.setScaledContents(True)
        self.checkLastname.setObjectName("checkLastname")
        self.formLayout_2.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.checkLastname)
        self.checkEmail = QtWidgets.QLabel(self.grpChecks)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkEmail.sizePolicy().hasHeightForWidth())
        self.checkEmail.setSizePolicy(sizePolicy)
        self.checkEmail.setMinimumSize(QtCore.QSize(22, 22))
        self.checkEmail.setMaximumSize(QtCore.QSize(22, 22))
        self.checkEmail.setText("")
        self.checkEmail.setScaledContents(True)
        self.checkEmail.setObjectName("checkEmail")
        self.formLayout_2.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.checkEmail)
        self.checkPhone = QtWidgets.QLabel(self.grpChecks)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkPhone.sizePolicy().hasHeightForWidth())
        self.checkPhone.setSizePolicy(sizePolicy)
        self.checkPhone.setMinimumSize(QtCore.QSize(22, 22))
        self.checkPhone.setMaximumSize(QtCore.QSize(22, 22))
        self.checkPhone.setText("")
        self.checkPhone.setScaledContents(True)
        self.checkPhone.setObjectName("checkPhone")
        self.formLayout_2.setWidget(
            3, QtWidgets.QFormLayout.LabelRole, self.checkPhone)
        self.checkCi = QtWidgets.QLabel(self.grpChecks)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkCi.sizePolicy().hasHeightForWidth())
        self.checkCi.setSizePolicy(sizePolicy)
        self.checkCi.setMinimumSize(QtCore.QSize(22, 22))
        self.checkCi.setMaximumSize(QtCore.QSize(22, 22))
        self.checkCi.setText("")
        self.checkCi.setScaledContents(True)
        self.checkCi.setObjectName("checkCi")
        self.formLayout_2.setWidget(
            4, QtWidgets.QFormLayout.LabelRole, self.checkCi)
        self.horizontalLayout.addWidget(self.grpChecks)
        self.grpValidation = QtWidgets.QGroupBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.grpValidation.sizePolicy().hasHeightForWidth())
        self.grpValidation.setSizePolicy(sizePolicy)
        self.grpValidation.setObjectName("grpValidation")
        self.checkInstitutional = QtWidgets.QLabel(self.grpValidation)
        self.checkInstitutional.setGeometry(QtCore.QRect(10, 80, 22, 22))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkInstitutional.sizePolicy().hasHeightForWidth())
        self.checkInstitutional.setSizePolicy(sizePolicy)
        self.checkInstitutional.setMinimumSize(QtCore.QSize(22, 22))
        self.checkInstitutional.setMaximumSize(QtCore.QSize(22, 22))
        self.checkInstitutional.setText("")
        self.checkInstitutional.setScaledContents(True)
        self.checkInstitutional.setObjectName("checkInstitutional")
        self.label_12 = QtWidgets.QLabel(self.grpValidation)
        self.label_12.setGeometry(QtCore.QRect(40, 80, 91, 19))
        self.label_12.setObjectName("label_12")
        self.label_15 = QtWidgets.QLabel(self.grpValidation)
        self.label_15.setGeometry(QtCore.QRect(10, 130, 91, 19))
        self.label_15.setObjectName("label_15")
        self.tfdProvince = QtWidgets.QLineEdit(self.grpValidation)
        self.tfdProvince.setGeometry(QtCore.QRect(10, 150, 151, 20))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.tfdProvince.sizePolicy().hasHeightForWidth())
        self.tfdProvince.setSizePolicy(sizePolicy)
        self.tfdProvince.setObjectName("tfdProvince")
        self.horizontalLayout.addWidget(self.grpValidation)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.grpForm.setTitle(_translate("Dialog", "Formulario"))
        self.label.setText(_translate("Dialog", "Nombre"))
        self.label_2.setText(_translate("Dialog", "Apellido"))
        self.label_3.setText(_translate("Dialog", "Correo"))
        self.label_4.setText(_translate("Dialog", "Teléfono"))
        self.label_5.setText(_translate("Dialog", "Cédula"))
        self.btnValidate.setText(_translate("Dialog", "VALIDAR"))
        self.grpValidation.setTitle(_translate("Dialog", "Validación"))
        self.label_12.setText(_translate("Dialog", "Institucional"))
        self.label_15.setText(_translate("Dialog", "Provincia"))
