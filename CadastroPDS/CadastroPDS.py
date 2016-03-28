import sys
import mysql.connector
from login import Ui_MainWindow
from index import Ui_IndexDialog
from create import Ui_CreateDialog
from PyQt4 import QtCore, QtGui

try:
	cnn= mysql.connector.connect(user="root",password="katrina",host="localhost", database="sys")
	cur=cnn.cursor()
except mysql.connector.Error as err: # erro de conexao com o banco de dados 
	print("Something went wrong: {}".format(err))

class MeuCreate(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui= Ui_CreateDialog()
        self.ui.setupUi(self)

        QtCore.QMetaObject.connectSlotsByName(self)
        QtCore.QObject.connect(self.ui.buttonSair, QtCore.SIGNAL("clicked()"), self.Sair)
        QtCore.QObject.connect(self.ui.buttonCadastrar, QtCore.SIGNAL("clicked()"), self.Cadastrar)
        QtCore.QObject.connect(self.ui.buttonFoto, QtCore.SIGNAL("clicked()"), self.BrowseFoto)

    def Sair(self):
        self.hide()

    def Cadastrar(self):

        login= str(self.ui.lineEditLogin.text())
        senha= str(self.ui.lineEditSenha.text())
        nome= str(self.ui.lineEditNome.text())
        endereco= str(self.ui.lineEditEndereco.text())
        data_nasc= str(self.ui.lineEditNascimento.text())
        tel= str(self.ui.lineEditTel.text())
        cel= str(self.ui.lineEditCel.text())
        email= str(self.ui.lineEditEmail.text())
        
        if login == "" or senha == "" or nome == "" or endereco == "" or data_nasc == "" or tel == "" or cel == "" or email == "":
            erroMsg= QtGui.QMessageBox()
            erroMsg.setText("Campo vazio")
            erroMsg.setWindowTitle("Erro")
            erroMsg.exec_()

        else :
            try:
                cur.execute("INSERT INTO usuarios (login, senha, nome, endereco, dataNascimento, telefone, celular, email, foto) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                            (login, senha, nome, endereco, data_nasc, tel, cel, email, "FOTO"))
            except mysql.connector.Error as err: # erro de gravacao
                erroMsg= QtGui.QMessageBox()
                erroMsg.setText("Something went wrong: {}".format(err))
                erroMsg.setWindowTitle("Erro")
                erroMsg.exec_()

            self.hide()
            cnn.commit()

    def BrowseFoto(self):
        filePath = QtGui.QFileDialog.getOpenFileName(self, 
                                                       'Single File',
                                                       "~/Desktop",
                                                      '*.txt')
        print('filePath',filePath.toUtf8, '\n')
        txt= filePath.toUtf8
        fileHandle = open(txt,'r')
        lines = fileHandle.readlines()
        for line in lines:
            print(line)
        
        

class MeuIndex(QtGui.QDialog):
    def __init__(self, login, senha):
        QtGui.QDialog.__init__(self)
        self.ui= Ui_IndexDialog()
        self.ui.setupUi(self)
        self.login= login
        self.senha= senha

        cur.execute("SELECT * FROM usuarios WHERE login = \""+self.login+"\"")
        data= cur.fetchall()

        # (login, senha, nome, endereco, dataNascimento, telefone, celular, email, foto)
        self.ui.lineEditNome.setText(data[0][2])
        self.ui.lineEditEndereco.setText(data[0][3])
        self.ui.lineEditNasc.setText(data[0][4])
        self.ui.lineEditTel.setText(data[0][5])
        self.ui.lineEditCel.setText(data[0][6])
        self.ui.lineEditEmail.setText(data[0][7])
        self.ui.lineEditLogin.setText(data[0][0])

        QtCore.QMetaObject.connectSlotsByName(self)
        QtCore.QObject.connect(self.ui.buttonSair, QtCore.SIGNAL("clicked()"), self.Sair)

    def Sair(self):
        self.hide()


        

class MeuLogin(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui= Ui_MainWindow()
        self.ui.setupUi(self)
        
        QtCore.QMetaObject.connectSlotsByName(self)
        QtCore.QObject.connect(self.ui.buttonEntrar, QtCore.SIGNAL("clicked()"), self.Entrar)
        QtCore.QObject.connect(self.ui.buttonCreate, QtCore.SIGNAL("clicked()"), self.Create)

    def Entrar(self):
        login= str(self.ui.lineEditUser.text())
        senha= str(self.ui.lineEditPass.text())

        cur.execute("SELECT login, senha FROM usuarios")
        data= cur.fetchall()
        existe= False
        for x in data:
            if x[0] == login and x[1] == senha:
                existe= True

        if existe :
            self.ui.lineEditUser.setText("");
            self.ui.lineEditPass.setText("");
            self.index= MeuIndex(login, senha)
            self.index.show()
        else:
            erroMsg= QtGui.QMessageBox()
            erroMsg.setText("Login nao cadastrado")
            erroMsg.setWindowTitle("Erro")
            erroMsg.exec_()

    def Create(self):
        self.create= MeuCreate()
        self.create.show()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    login= MeuLogin()
    login.show()
    sys.exit(app.exec_())