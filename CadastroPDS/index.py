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
        IndexDialog.resize(529, 403)
        IndexDialog.setModal(True)
        self.label_8 = QtGui.QLabel(IndexDialog)
        self.label_8.setGeometry(QtCore.QRect(380, 30, 61, 51))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.buttonSair = QtGui.QPushButton(IndexDialog)
        self.buttonSair.setGeometry(QtCore.QRect(320, 340, 75, 23))
        self.buttonSair.setObjectName(_fromUtf8("buttonSair"))
        self.widget = QtGui.QWidget(IndexDialog)
        self.widget.setGeometry(QtCore.QRect(150, 70, 241, 230))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lineEditNome = QtGui.QLineEdit(self.widget)
        self.lineEditNome.setEnabled(False)
        self.lineEditNome.setObjectName(_fromUtf8("lineEditNome"))
        self.verticalLayout.addWidget(self.lineEditNome)
        self.lineEditEndereco = QtGui.QLineEdit(self.widget)
        self.lineEditEndereco.setEnabled(False)
        self.lineEditEndereco.setObjectName(_fromUtf8("lineEditEndereco"))
        self.verticalLayout.addWidget(self.lineEditEndereco)
        self.lineEditNasc = QtGui.QLineEdit(self.widget)
        self.lineEditNasc.setEnabled(False)
        self.lineEditNasc.setObjectName(_fromUtf8("lineEditNasc"))
        self.verticalLayout.addWidget(self.lineEditNasc)
        self.lineEditTel = QtGui.QLineEdit(self.widget)
        self.lineEditTel.setEnabled(False)
        self.lineEditTel.setObjectName(_fromUtf8("lineEditTel"))
        self.verticalLayout.addWidget(self.lineEditTel)
        self.lineEditCel = QtGui.QLineEdit(self.widget)
        self.lineEditCel.setEnabled(False)
        self.lineEditCel.setObjectName(_fromUtf8("lineEditCel"))
        self.verticalLayout.addWidget(self.lineEditCel)
        self.lineEditEmail = QtGui.QLineEdit(self.widget)
        self.lineEditEmail.setEnabled(False)
        self.lineEditEmail.setObjectName(_fromUtf8("lineEditEmail"))
        self.verticalLayout.addWidget(self.lineEditEmail)
        self.lineEditLogin = QtGui.QLineEdit(self.widget)
        self.lineEditLogin.setEnabled(False)
        self.lineEditLogin.setObjectName(_fromUtf8("lineEditLogin"))
        self.verticalLayout.addWidget(self.lineEditLogin)
        self.widget1 = QtGui.QWidget(IndexDialog)
        self.widget1.setGeometry(QtCore.QRect(50, 70, 81, 231))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.widget1)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.widget1)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(self.widget1)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtGui.QLabel(self.widget1)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtGui.QLabel(self.widget1)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_6 = QtGui.QLabel(self.widget1)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_2.addWidget(self.label_6)
        self.label_7 = QtGui.QLabel(self.widget1)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_2.addWidget(self.label_7)

        self.retranslateUi(IndexDialog)
        QtCore.QMetaObject.connectSlotsByName(IndexDialog)

    def retranslateUi(self, IndexDialog):
        IndexDialog.setWindowTitle(_translate("IndexDialog", "Dialog", None))
        self.label_8.setText(_translate("IndexDialog", "FOTO", None))
        self.buttonSair.setText(_translate("IndexDialog", "Sair", None))
        self.label.setText(_translate("IndexDialog", "Nome", None))
        self.label_2.setText(_translate("IndexDialog", "Endereço", None))
        self.label_3.setText(_translate("IndexDialog", "Nascimento", None))
        self.label_4.setText(_translate("IndexDialog", "Telefone", None))
        self.label_5.setText(_translate("IndexDialog", "Celular", None))
        self.label_6.setText(_translate("IndexDialog", "email", None))
        self.label_7.setText(_translate("IndexDialog", "login", None))

