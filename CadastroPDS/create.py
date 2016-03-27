# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_CreateDialog(object):
    def setupUi(self, CreateDialog):
        CreateDialog.setObjectName(_fromUtf8("CreateDialog"))
        CreateDialog.resize(534, 384)
        CreateDialog.setModal(True)
        self.layoutWidget = QtGui.QWidget(CreateDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 60, 91, 231))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_8 = QtGui.QLabel(self.layoutWidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_3.addWidget(self.label_8)
        self.label_9 = QtGui.QLabel(self.layoutWidget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_3.addWidget(self.label_9)
        self.label_10 = QtGui.QLabel(self.layoutWidget)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_3.addWidget(self.label_10)
        self.label_11 = QtGui.QLabel(self.layoutWidget)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayout_3.addWidget(self.label_11)
        self.label_12 = QtGui.QLabel(self.layoutWidget)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.verticalLayout_3.addWidget(self.label_12)
        self.label_13 = QtGui.QLabel(self.layoutWidget)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.verticalLayout_3.addWidget(self.label_13)
        self.label_14 = QtGui.QLabel(self.layoutWidget)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.verticalLayout_3.addWidget(self.label_14)
        self.label_16 = QtGui.QLabel(self.layoutWidget)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.verticalLayout_3.addWidget(self.label_16)
        self.layoutWidget_2 = QtGui.QWidget(CreateDialog)
        self.layoutWidget_2.setGeometry(QtCore.QRect(170, 60, 241, 231))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.lineEditNome = QtGui.QLineEdit(self.layoutWidget_2)
        self.lineEditNome.setObjectName(_fromUtf8("lineEditNome"))
        self.verticalLayout_4.addWidget(self.lineEditNome)
        self.lineEditEndereco = QtGui.QLineEdit(self.layoutWidget_2)
        self.lineEditEndereco.setObjectName(_fromUtf8("lineEditEndereco"))
        self.verticalLayout_4.addWidget(self.lineEditEndereco)
        self.lineEditNascimento = QtGui.QLineEdit(self.layoutWidget_2)
        self.lineEditNascimento.setObjectName(_fromUtf8("lineEditNascimento"))
        self.verticalLayout_4.addWidget(self.lineEditNascimento)
        self.lineEditTel = QtGui.QLineEdit(self.layoutWidget_2)
        self.lineEditTel.setObjectName(_fromUtf8("lineEditTel"))
        self.verticalLayout_4.addWidget(self.lineEditTel)
        self.lineEditCel = QtGui.QLineEdit(self.layoutWidget_2)
        self.lineEditCel.setObjectName(_fromUtf8("lineEditCel"))
        self.verticalLayout_4.addWidget(self.lineEditCel)
        self.lineEditEmail = QtGui.QLineEdit(self.layoutWidget_2)
        self.lineEditEmail.setObjectName(_fromUtf8("lineEditEmail"))
        self.verticalLayout_4.addWidget(self.lineEditEmail)
        self.lineEditLogin = QtGui.QLineEdit(self.layoutWidget_2)
        self.lineEditLogin.setObjectName(_fromUtf8("lineEditLogin"))
        self.verticalLayout_4.addWidget(self.lineEditLogin)
        self.lineEditSenha = QtGui.QLineEdit(self.layoutWidget_2)
        self.lineEditSenha.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEditSenha.setObjectName(_fromUtf8("lineEditSenha"))
        self.verticalLayout_4.addWidget(self.lineEditSenha)
        self.label_15 = QtGui.QLabel(CreateDialog)
        self.label_15.setGeometry(QtCore.QRect(430, 30, 61, 51))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.buttonCadastrar = QtGui.QPushButton(CreateDialog)
        self.buttonCadastrar.setGeometry(QtCore.QRect(300, 320, 75, 23))
        self.buttonCadastrar.setObjectName(_fromUtf8("buttonCadastrar"))
        self.buttonSair = QtGui.QPushButton(CreateDialog)
        self.buttonSair.setGeometry(QtCore.QRect(390, 320, 75, 23))
        self.buttonSair.setObjectName(_fromUtf8("buttonSair"))

        self.retranslateUi(CreateDialog)
        QtCore.QMetaObject.connectSlotsByName(CreateDialog)

    def retranslateUi(self, CreateDialog):
        CreateDialog.setWindowTitle(_translate("CreateDialog", "Dialog", None))
        self.label_8.setText(_translate("CreateDialog", "Nome", None))
        self.label_9.setText(_translate("CreateDialog", "Endereço", None))
        self.label_10.setText(_translate("CreateDialog", "Nascimento", None))
        self.label_11.setText(_translate("CreateDialog", "Telefone", None))
        self.label_12.setText(_translate("CreateDialog", "Celular", None))
        self.label_13.setText(_translate("CreateDialog", "email", None))
        self.label_14.setText(_translate("CreateDialog", "login", None))
        self.label_16.setText(_translate("CreateDialog", "senha", None))
        self.label_15.setText(_translate("CreateDialog", "FOTO", None))
        self.buttonCadastrar.setText(_translate("CreateDialog", "Cadastrar", None))
        self.buttonSair.setText(_translate("CreateDialog", "Cancelar", None))

