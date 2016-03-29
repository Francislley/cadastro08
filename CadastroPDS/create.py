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
        CreateDialog.resize(540, 450)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CreateDialog.sizePolicy().hasHeightForWidth())
        CreateDialog.setSizePolicy(sizePolicy)
        CreateDialog.setAccessibleName(_fromUtf8(""))
        CreateDialog.setStyleSheet(_fromUtf8("QLineEdit{\n"
"    color: #555;\n"
"    background-color: #fff;\n"
"    background-image: none;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    height: 25px;    \n"
"}\n"
"QDialog{    \n"
"    background-color: #eee;\n"
"}\n"
"QPushButton{\n"
"    width: 100px;\n"
"    color: #fff;\n"
"    background-color: #337ab7;\n"
"    font-size: 12px;\n"
"    line-height: 1.3333333;\n"
"    border: 1px solid #2e6da4;\n"
"    border-radius: 4px;\n"
"    height: 25px;    \n"
"}"))
        CreateDialog.setModal(True)
        self.labelFoto = QtGui.QLabel(CreateDialog)
        self.labelFoto.setGeometry(QtCore.QRect(400, 110, 120, 120))
        self.labelFoto.setObjectName(_fromUtf8("labelFoto"))
        self.label_17 = QtGui.QLabel(CreateDialog)
        self.label_17.setGeometry(QtCore.QRect(15, 72, 221, 31))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.layoutWidget = QtGui.QWidget(CreateDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(15, 102, 361, 315))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_8 = QtGui.QLabel(self.layoutWidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout.addWidget(self.label_8)
        self.lineEditNome = QtGui.QLineEdit(self.layoutWidget)
        self.lineEditNome.setObjectName(_fromUtf8("lineEditNome"))
        self.horizontalLayout.addWidget(self.lineEditNome)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_9 = QtGui.QLabel(self.layoutWidget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_2.addWidget(self.label_9)
        self.lineEditEndereco = QtGui.QLineEdit(self.layoutWidget)
        self.lineEditEndereco.setObjectName(_fromUtf8("lineEditEndereco"))
        self.horizontalLayout_2.addWidget(self.lineEditEndereco)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_10 = QtGui.QLabel(self.layoutWidget)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_3.addWidget(self.label_10)
        self.lineEditNascimento = QtGui.QLineEdit(self.layoutWidget)
        self.lineEditNascimento.setObjectName(_fromUtf8("lineEditNascimento"))
        self.horizontalLayout_3.addWidget(self.lineEditNascimento)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_11 = QtGui.QLabel(self.layoutWidget)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_4.addWidget(self.label_11)
        self.lineEditTel = QtGui.QLineEdit(self.layoutWidget)
        self.lineEditTel.setObjectName(_fromUtf8("lineEditTel"))
        self.horizontalLayout_4.addWidget(self.lineEditTel)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_12 = QtGui.QLabel(self.layoutWidget)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_5.addWidget(self.label_12)
        self.lineEditCel = QtGui.QLineEdit(self.layoutWidget)
        self.lineEditCel.setObjectName(_fromUtf8("lineEditCel"))
        self.horizontalLayout_5.addWidget(self.lineEditCel)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_13 = QtGui.QLabel(self.layoutWidget)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_6.addWidget(self.label_13)
        self.lineEditEmail = QtGui.QLineEdit(self.layoutWidget)
        self.lineEditEmail.setObjectName(_fromUtf8("lineEditEmail"))
        self.horizontalLayout_6.addWidget(self.lineEditEmail)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_14 = QtGui.QLabel(self.layoutWidget)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_7.addWidget(self.label_14)
        self.lineEditLogin = QtGui.QLineEdit(self.layoutWidget)
        self.lineEditLogin.setObjectName(_fromUtf8("lineEditLogin"))
        self.horizontalLayout_7.addWidget(self.lineEditLogin)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_16 = QtGui.QLabel(self.layoutWidget)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_8.addWidget(self.label_16)
        self.lineEditSenha = QtGui.QLineEdit(self.layoutWidget)
        self.lineEditSenha.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEditSenha.setObjectName(_fromUtf8("lineEditSenha"))
        self.horizontalLayout_8.addWidget(self.lineEditSenha)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem)
        self.horizontalLayout_17 = QtGui.QHBoxLayout()
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.buttonCadastrar = QtGui.QPushButton(self.layoutWidget)
        self.buttonCadastrar.setObjectName(_fromUtf8("buttonCadastrar"))
        self.horizontalLayout_17.addWidget(self.buttonCadastrar)
        self.buttonSair = QtGui.QPushButton(self.layoutWidget)
        self.buttonSair.setObjectName(_fromUtf8("buttonSair"))
        self.horizontalLayout_17.addWidget(self.buttonSair)
        self.horizontalLayout_18.addLayout(self.horizontalLayout_17)
        self.verticalLayout_3.addLayout(self.horizontalLayout_18)
        self.layoutWidget1 = QtGui.QWidget(CreateDialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(15, 22, 361, 41))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_23 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_23.setObjectName(_fromUtf8("horizontalLayout_23"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem1)
        self.label_22 = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_22.setFont(font)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.horizontalLayout_23.addWidget(self.label_22)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem2)
        self.buttonFoto = QtGui.QPushButton(CreateDialog)
        self.buttonFoto.setGeometry(QtCore.QRect(440, 250, 81, 23))
        self.buttonFoto.setObjectName(_fromUtf8("buttonFoto"))

        self.retranslateUi(CreateDialog)
        QtCore.QMetaObject.connectSlotsByName(CreateDialog)

    def retranslateUi(self, CreateDialog):
        CreateDialog.setWindowTitle(_translate("CreateDialog", "Cadastro", None))
        self.labelFoto.setText(_translate("CreateDialog", "FOTO", None))
        self.label_17.setText(_translate("CreateDialog", "Preencha seus dados pessoais corretamente:", None))
        self.label_8.setText(_translate("CreateDialog", "Nome", None))
        self.label_9.setText(_translate("CreateDialog", "Endereço", None))
        self.label_10.setText(_translate("CreateDialog", "Nascimento", None))
        self.label_11.setText(_translate("CreateDialog", "Telefone", None))
        self.label_12.setText(_translate("CreateDialog", "Celular", None))
        self.label_13.setText(_translate("CreateDialog", "email", None))
        self.label_14.setText(_translate("CreateDialog", "login", None))
        self.label_16.setText(_translate("CreateDialog", "senha", None))
        self.buttonCadastrar.setText(_translate("CreateDialog", "Cadastrar", None))
        self.buttonSair.setText(_translate("CreateDialog", "Cancelar", None))
        self.label_22.setText(_translate("CreateDialog", "Você está no Cadastro!", None))
        self.buttonFoto.setText(_translate("CreateDialog", "Escolha a foto", None))

