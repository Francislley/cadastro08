# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'index.ui'
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

class Ui_IndexDialog(object):
    def setupUi(self, IndexDialog):
        IndexDialog.setObjectName(_fromUtf8("IndexDialog"))
        IndexDialog.resize(540, 450)
        IndexDialog.setStyleSheet(_fromUtf8("QLineEdit{\n"
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
        IndexDialog.setModal(True)
        self.layoutWidget = QtGui.QWidget(IndexDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 20, 371, 51))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_23 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_23.setObjectName(_fromUtf8("horizontalLayout_23"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem)
        self.label_22 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_22.setFont(font)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.horizontalLayout_23.addWidget(self.label_22)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem1)
        self.layoutWidget1 = QtGui.QWidget(IndexDialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(30, 140, 371, 281))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget1)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEditNome = QtGui.QLineEdit(self.layoutWidget1)
        self.lineEditNome.setEnabled(False)
        self.lineEditNome.setObjectName(_fromUtf8("lineEditNome"))
        self.horizontalLayout.addWidget(self.lineEditNome)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.layoutWidget1)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEditEndereco = QtGui.QLineEdit(self.layoutWidget1)
        self.lineEditEndereco.setEnabled(False)
        self.lineEditEndereco.setObjectName(_fromUtf8("lineEditEndereco"))
        self.horizontalLayout_2.addWidget(self.lineEditEndereco)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(self.layoutWidget1)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEditNasc = QtGui.QLineEdit(self.layoutWidget1)
        self.lineEditNasc.setEnabled(False)
        self.lineEditNasc.setObjectName(_fromUtf8("lineEditNasc"))
        self.horizontalLayout_3.addWidget(self.lineEditNasc)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_4 = QtGui.QLabel(self.layoutWidget1)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lineEditTel = QtGui.QLineEdit(self.layoutWidget1)
        self.lineEditTel.setEnabled(False)
        self.lineEditTel.setObjectName(_fromUtf8("lineEditTel"))
        self.horizontalLayout_4.addWidget(self.lineEditTel)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_5 = QtGui.QLabel(self.layoutWidget1)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_5.addWidget(self.label_5)
        self.lineEditCel = QtGui.QLineEdit(self.layoutWidget1)
        self.lineEditCel.setEnabled(False)
        self.lineEditCel.setObjectName(_fromUtf8("lineEditCel"))
        self.horizontalLayout_5.addWidget(self.lineEditCel)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_6 = QtGui.QLabel(self.layoutWidget1)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_6.addWidget(self.label_6)
        self.lineEditEmail = QtGui.QLineEdit(self.layoutWidget1)
        self.lineEditEmail.setEnabled(False)
        self.lineEditEmail.setObjectName(_fromUtf8("lineEditEmail"))
        self.horizontalLayout_6.addWidget(self.lineEditEmail)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_7 = QtGui.QLabel(self.layoutWidget1)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_7.addWidget(self.label_7)
        self.lineEditLogin = QtGui.QLineEdit(self.layoutWidget1)
        self.lineEditLogin.setEnabled(False)
        self.lineEditLogin.setObjectName(_fromUtf8("lineEditLogin"))
        self.horizontalLayout_7.addWidget(self.lineEditLogin)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        spacerItem2 = QtGui.QSpacerItem(78, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.buttonSair = QtGui.QPushButton(self.layoutWidget1)
        self.buttonSair.setObjectName(_fromUtf8("buttonSair"))
        self.horizontalLayout_8.addWidget(self.buttonSair)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.layoutWidget2 = QtGui.QWidget(IndexDialog)
        self.layoutWidget2.setGeometry(QtCore.QRect(30, 90, 371, 41))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.label_9 = QtGui.QLabel(self.layoutWidget2)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_2.addWidget(self.label_9)
        self.horizontalLayout_9.addLayout(self.verticalLayout_2)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem4)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_9)
        self.labelFoto = QtGui.QLabel(IndexDialog)
        self.labelFoto.setGeometry(QtCore.QRect(410, 140, 120, 120))
        self.labelFoto.setObjectName(_fromUtf8("labelFoto"))

        self.retranslateUi(IndexDialog)
        QtCore.QMetaObject.connectSlotsByName(IndexDialog)

    def retranslateUi(self, IndexDialog):
        IndexDialog.setWindowTitle(_translate("IndexDialog", "Usuario", None))
        self.label_22.setText(_translate("IndexDialog", "Você está no Cadastro!", None))
        self.label.setText(_translate("IndexDialog", "Nome", None))
        self.label_2.setText(_translate("IndexDialog", "Endereço", None))
        self.label_3.setText(_translate("IndexDialog", "Nascimento", None))
        self.label_4.setText(_translate("IndexDialog", "Telefone", None))
        self.label_5.setText(_translate("IndexDialog", "Celular", None))
        self.label_6.setText(_translate("IndexDialog", "email", None))
        self.label_7.setText(_translate("IndexDialog", "login", None))
        self.buttonSair.setText(_translate("IndexDialog", "Sair", None))
        self.label_9.setText(_translate("IndexDialog", "Dados pessoais:", None))
        self.labelFoto.setText(_translate("IndexDialog", "FOTO", None))

