# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(540, 450)
        MainWindow.setStyleSheet(_fromUtf8("QLineEdit{\n"
"    color: #555;\n"
"    background-color: #fff;\n"
"    background-image: none;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    height: 25px;    \n"
"}\n"
"QMainWindow{    \n"
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
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(110, 80, 325, 293))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_4.addWidget(self.label)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEditUser = QtGui.QLineEdit(self.layoutWidget)
        self.lineEditUser.setStyleSheet(_fromUtf8("lineEditUser{\n"
"    color: #555;\n"
"    background-color: #fff;\n"
"    background-image: none;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"}"))
        self.lineEditUser.setObjectName(_fromUtf8("lineEditUser"))
        self.horizontalLayout.addWidget(self.lineEditUser)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(12)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEditPass = QtGui.QLineEdit(self.layoutWidget)
        self.lineEditPass.setInputMask(_fromUtf8(""))
        self.lineEditPass.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEditPass.setObjectName(_fromUtf8("lineEditPass"))
        self.horizontalLayout_2.addWidget(self.lineEditPass)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.buttonEntrar = QtGui.QPushButton(self.layoutWidget)
        self.buttonEntrar.setObjectName(_fromUtf8("buttonEntrar"))
        self.verticalLayout_2.addWidget(self.buttonEntrar)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.buttonCreate = QtGui.QPushButton(self.layoutWidget)
        self.buttonCreate.setObjectName(_fromUtf8("buttonCreate"))
        self.verticalLayout_2.addWidget(self.buttonCreate)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.buttonEntrar, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Login", None))
        self.label.setText(_translate("MainWindow", "Bem Vindo ao Cadastro!", None))
        self.label_2.setText(_translate("MainWindow", "Usuario", None))
        self.label_3.setText(_translate("MainWindow", "Senha", None))
        self.buttonEntrar.setText(_translate("MainWindow", "Entrar", None))
        self.label_4.setText(_translate("MainWindow", "Ainda não se inscreveu?", None))
        self.buttonCreate.setText(_translate("MainWindow", "Inscreva-se!", None))

