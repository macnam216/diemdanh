# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
import q_li_nv

class Ui_MainWindow(QtWidgets.QDialog):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        
        MainWindow.setFixedWidth(525)
        MainWindow.setFixedHeight(439)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/nhan_vien.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(30, 30))

        MainWindow.setStyleSheet("QFrame{background-color: rgb(190, 255, 248);}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-320, -70, 1071, 551))
        self.frame.setStyleSheet("QFrame{background-image: url(:/newPrefix/mac.png);}\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setGeometry(QtCore.QRect(540, 400,85, 40))
        self.pushButton.setStyleSheet("color: rgb(255, 0, 0);\n"
"gridline-color: rgb(255, 0, 127);\n"
"background-color: rgb(255, 255, 0);")

        self.pushButton.setObjectName("pushButton")

        ### EVENT ####
        self.pushButton.clicked.connect(self.loginCheck)


        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(500, 290, 151, 31))
        self.lineEdit.setStyleSheet("border-radius:10px;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(500, 350, 151, 31))
        self.lineEdit_2.setStyleSheet("border-radius:10px;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(360, 80, 451, 71))
        self.textEdit.setStyleSheet("")
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.pushButton.setText(_translate("MainWindow", "LOGIN"))

        self.lineEdit.setPlaceholderText(_translate("MainWindow", "User Name"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Password"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffff00;\">Made by:</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffff00;\">Lê Ngọc Thành</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffff00;\">Nguyễn Văn Bắc</span></p></body></html>"))


    def loginCheck(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        if username=='' or password=='':
            QtWidgets.QMessageBox.warning(QtWidgets.QMessageBox(), 'Error', 'Vui lòng nhập đầy đủ các trường')
        else:
            self.mydb = mysql.connector.connect(
              host="localhost",
              user="nam",
              passwd="1234",
              database="quanlynhanvien"
            )
            self.mycursor = self.mydb.cursor() 
            
            result = self.mycursor.execute("SELECT * FROM users WHERE username = '{}' AND password = '{}' ".format(username,password))
            row = self.mycursor.fetchall()
            if(len(row) > 0):
                self.ql_nv_Show()
                self.close()
               
            else:
                QtWidgets.QMessageBox.warning(QtWidgets.QMessageBox(), 'Error', 'Tài khoản or mật khẩu không chính xác')
       


    def ql_nv_Show(self):
        self.ql_nv_form = QtWidgets.QMainWindow()
        self.ui = q_li_nv.Ui_QMainWindow()
        self.ui.setupUi(self.ql_nv_form)
        self.ql_nv_form.show()
        

import image_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

