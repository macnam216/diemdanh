# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'q_li_nv.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel
import mysql.connector
from datetime import datetime
import Login
import main
import os
import shutil


class Thread(QtCore.QThread):
    data = QtCore.pyqtSignal(dict)

    def __init__(self, parent=None):
        super(Thread, self).__init__(parent)
        self._stopped = True
        self._mutex = QtCore.QMutex()

    def stop(self):
        self._mutex.lock()
        self._stopped = True
        self._mutex.unlock()

    def run(self):
        self._stopped = False

        while True:
            if self._stopped:
                break
            self.sleep(1)
            data = {};
            self.data.emit(data)


class Thread_2(QtCore.QThread):
    data = QtCore.pyqtSignal(dict)

    def __init__(self, parent=None):
        super(Thread_2, self).__init__(parent)
        self._stopped = True
        self._mutex = QtCore.QMutex()

    def stop(self):
        self._mutex.lock()
        self._stopped = True
        self._mutex.unlock()

    def run(self):
        self._stopped = False

        while True:
            if self._stopped:
                break
            self.sleep(3)
            data = {};
            self.data.emit(data)


class InformationDialog(QtWidgets.QDialog):
    def __init__(self):
        super(InformationDialog, self).__init__()

        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/add1.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon1)

        self.QBtn1 = QtWidgets.QPushButton()
        self.QBtn1.setText("Sua")
        # self.QBtn.setStyleSheet("background: #CCFFFF;\n""height:40px; \n""font-size:18px")

        self.setWindowTitle("Sua thong tin nhân viên")
        self.setFixedWidth(500)
        self.setFixedHeight(500)

        self.QBtn1.clicked.connect(self.update_employee)

        layout1 = QtWidgets.QVBoxLayout()

        self.nameinputId = QtWidgets.QLineEdit()
        self.nameinput1 = QtWidgets.QLineEdit()
        self.nameinput1.setPlaceholderText("Nhập tên *")
        # self.nameinput.setStyleSheet(
        #     "border:1px solid #00FF00;\n""height:30px; \n""border-radius:8px;\n""font-size:18px")
        layout1.addWidget(self.nameinput1)
        # layout1.addWidget(self.nameinputId)

        self.code1 = QtWidgets.QLineEdit()
        self.code1.setPlaceholderText("Nhập code *")
        # self.code.setStyleSheet(
        #     "border:1px solid #00FF00;\n""height:30px; \n""border-radius:8px;\n""font-size:18px")
        layout1.addWidget(self.code1)

        self.branchinput1 = QtWidgets.QComboBox()
        self.branchinput1.addItem("----Chọn bộ phận----")
        self.branchinput1.addItem("Marketing")
        self.branchinput1.addItem("Sale")
        self.branchinput1.addItem("IT")
        self.branchinput1.addItem("Support")
        self.branchinput1.addItem("Account")
        self.branchinput1.addItem("Manager")
        # self.branchinput.setStyleSheet(
        #     "border:1px solid #00FF00;\n""height:30px; \n""border-radius:8px;\n""font-size:18px")
        layout1.addWidget(self.branchinput1)

        self.mobileinput1 = QtWidgets.QLineEdit()
        self.onlyInt = QtGui.QIntValidator()
        self.mobileinput1.setValidator(self.onlyInt)  # chi nhap dc so
        self.mobileinput1.setPlaceholderText("Nhập Số điện thoại")
        # self.mobileinput.setStyleSheet(
        #     "border:1px solid #00FF00;\n""height:30px; \n""border-radius:8px;\n""font-size:18px")
        layout1.addWidget(self.mobileinput1)

        self.addressinput1 = QtWidgets.QLineEdit()
        self.addressinput1.setPlaceholderText("Nhập địa chỉ")
        # self.addressinput.setStyleSheet(
        #     "border:1px solid #00FF00;\n""height:30px; \n""border-radius:8px;\n""font-size:18px")
        layout1.addWidget(self.addressinput1)

        # self.status1 = QtWidgets.QLineEdit()
        # self.onlyInt = QtGui.QIntValidator()
        # self.status1.setValidator(self.onlyInt)  # chi nhap dc so
        # self.status1.setPlaceholderText("Nhập quyền truy cập *")
        self.status1 = QtWidgets.QComboBox()
        self.status1.addItem("---Chọn quyền truy cập---")
        self.status1.addItem("Có")
        self.status1.addItem("Không")
        # self.status.setStyleSheet(
        #     "border:1px solid #00FF00;\n""height:30px; \n""border-radius:8px;\n""font-size:18px")
        layout1.addWidget(self.status1)

        self.hoursalary1 = QtWidgets.QComboBox()
        self.hoursalary1.addItem("---Chọn mức lương theo giờ---")
        self.hoursalary1.addItem("15.000 vnđ")
        self.hoursalary1.addItem("20.000 vnđ")
        self.hoursalary1.addItem("30.000 vnđ")
        # self.hoursalary.setStyleSheet(
        #     "border:1px solid #00FF00;\n""height:30px; \n""border-radius:8px;\n""font-size:18px")
        layout1.addWidget(self.hoursalary1)

        layout1.addWidget(self.QBtn1)
        self.setLayout(layout1)

    def checkExist(self, code, id):
        try:
            self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="1234",
                database="quanlynhanvien"
            )
            self.mycursor = self.mydb.cursor()
            query = "SELECT * FROM quan_li_nv WHERE code = %s "
            if id != '':
                query = query + "and id != %s"
            data = (code)
            if id != '':
                data = (code, id)

            print(query, data)
            self.mycursor.execute(query, data)
            result = self.mycursor.fetchone()

            row_exist = result[0]
            self.mydb.commit()
            self.mycursor.close()
            self.mydb.close()
            return True
        except Exception:
            return False

    def update_employee(self):
        searchrol = self.nameinputId.text()
        name = self.nameinput1.text()
        code = self.code1.text()
        branch = self.branchinput1.itemText(self.branchinput1.currentIndex())
        phone = self.mobileinput1.text()
        address = self.addressinput1.text()
        status = self.status1.itemText(self.status1.currentIndex())
        hoursalary = self.hoursalary1.itemText(self.hoursalary1.currentIndex())
        check = self.checkExist(code, searchrol)
        print(check)
        if hoursalary == '---Chọn mức lương theo giờ---':
            hoursalary = 0
        elif hoursalary == '15.000 vnđ':
            hoursalary = 15
        elif hoursalary == '20.000 vnđ':
            hoursalary = 20
        else:
            hoursalary = 30

        if status == 'Có':
            status = 1
        elif status == 'Không':
            status = 0
        else:
            status = 2

        if name == '':
            QtWidgets.QMessageBox.warning(QtWidgets.QMessageBox(), 'Error', 'Vui lòng nhập tên.')
        elif branch == '----Chọn bộ phận----':
            QtWidgets.QMessageBox.warning(QtWidgets.QMessageBox(), 'Error', 'Vui lòng chọn bộ phận.')
        elif status == '':
            QtWidgets.QMessageBox.warning(QtWidgets.QMessageBox(), 'Error', 'Vui lòng nhập quyền truy cập.')
        elif check == True:
            QtWidgets.QMessageBox.warning(QtWidgets.QMessageBox(), 'Error', 'Mã nhân viên không được trùng.')
        else:
            print(name, branch, phone, address, status, hoursalary, searchrol)
            self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="1234",
                database="quanlynhanvien"
            )
            self.mycursor = self.mydb.cursor()

            query = "UPDATE quan_li_nv SET name = %s,code = %s,branch = %s, phone = %s, address = %s, status = %s, hoursalary = %s where id =%s"
            data = (name, code, branch, int(phone), address, int(status), int(hoursalary), searchrol)
            query2 = "UPDATE checkInOut SET code = %s where id = %s"
            data2 = (code, searchrol)
            self.mycursor.execute(query, data)
            # self.mycursor.execute(query2, data2)

            self.mydb.commit()

            QtWidgets.QMessageBox.information(QtWidgets.QMessageBox(), 'Successful',
                                              'Sua thong tin nhân viên thành công.')

            self.mycursor.close()
            self.close()


class SearchDialog(QtWidgets.QDialog):
    def __init__(self):
        super(SearchDialog, self).__init__()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/s1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        self.QBtn = QtWidgets.QPushButton()
        self.QBtn.setText("Tìm kiếm")
        self.QBtn.setStyleSheet("background: #CCFFFF;\n""height:40px; \n""font-size:18px")

        self.setWindowTitle("Tìm kiếm nhân viên")
        self.setFixedWidth(300)
        self.setFixedHeight(200)
        self.QBtn.clicked.connect(self.search_employee)
        layout = QtWidgets.QVBoxLayout()

        self.searchinput = QtWidgets.QLineEdit()
        self.onlyInt = QtGui.QIntValidator()
        self.searchinput.setValidator(self.onlyInt)
        self.searchinput.setPlaceholderText("Nhập mã id cần tìm")
        self.searchinput.setStyleSheet(
            "border:1px solid #00FF00;\n""height:30px; \n""border-radius:8px;\n""font-size:18px")
        layout.addWidget(self.searchinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def search_employee(self):

        searchrol = self.searchinput.text()
        if searchrol == '':
            QtWidgets.QMessageBox.warning(QtWidgets.QMessageBox(), 'Error', 'Vui lòng nhập mã id của nhân viên cần tìm')
        else:
            try:
                self.mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="1234",
                    database="quanlynhanvien"
                )
                self.mycursor = self.mydb.cursor()

                self.mycursor.execute(
                    "SELECT quan_li_nv.id ,quan_li_nv.name,quan_li_nv.code,quan_li_nv.branch,quan_li_nv.phone,quan_li_nv.address FROM quan_li_nv WHERE  quan_li_nv.id=" + str(
                        searchrol))

                row = self.mycursor.fetchone()

                serachresult = "Id : " + str(row[0]) + '\n' + "Tên : " + str(row[1]) + '\n' + "Ma nhan vien : " + str(
                    row[2]) + '\n' + "Bộ phận : " + str(row[3]) + '\n' + "Số điện thoại : " + str(
                    row[4]) + '\n' + "địa chỉ : " + str(row[5])

                QtWidgets.QMessageBox.information(QtWidgets.QMessageBox(), 'Thông tin', serachresult)
                self.mydb.commit()

                self.close()
            except Exception:
                QtWidgets.QMessageBox.warning(QtWidgets.QMessageBox(), 'Error', 'Không tìm thấy nhân viên')


class DeleteDialog(QtWidgets.QDialog):
    def __init__(self):
        super(DeleteDialog, self).__init__()

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/d1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        self.QBtn = QtWidgets.QPushButton()
        self.QBtn.setText("Delete")
        self.QBtn.setStyleSheet("background: #CCFFFF;\n""height:40px; \n""font-size:18px")

        self.setWindowTitle("Xóa nhân viên")
        self.setFixedWidth(300)
        self.setFixedHeight(100)
        self.QBtn.clicked.connect(self.delete_employee)
        layout = QtWidgets.QVBoxLayout()

        self.deleteinput = QtWidgets.QLineEdit()
        self.onlyInt = QtGui.QIntValidator()
        self.deleteinput.setValidator(self.onlyInt)
        self.deleteinput.setPlaceholderText("Nhập id của nhân viên cần xóa")
        self.deleteinput.setStyleSheet(
            "border:1px solid #00FF00;\n""height:30px; \n""border-radius:8px;\n""font-size:18px")
        layout.addWidget(self.deleteinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def delete_employee(self):

        delrol = self.deleteinput.text()
        if delrol == '':
            QtWidgets.QMessageBox.warning(QtWidgets.QMessageBox(), 'Error', 'Vui lòng nhập mã id của nhân viên cần xóa')
        else:
            try:
                self.mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="1234",
                    database="quanlynhanvien"
                )
                self.mycursor = self.mydb.cursor()

                # check nhan vien exist, neu ko thi nhay toi except
                self.mycursor.execute("SELECT status, code FROM quan_li_nv WHERE id=" + str(delrol))
                result = self.mycursor.fetchone()
                self.current_path = os.path.join(os.getcwd(), "datasets", str(result[0]) + "-" + result[1])
                print(self.current_path)
                shutil.rmtree(self.current_path)

                self.mycursor.execute("DELETE FROM quan_li_nv WHERE id=" + str(delrol))
                self.mycursor.execute("DELETE FROM luong WHERE id=" + str(delrol))

                self.mydb.commit()
                self.mycursor.close()
                self.mydb.close()

                QtWidgets.QMessageBox.information(QtWidgets.QMessageBox(), 'Successful', 'Xóa nhân viên thành công')
                self.close()
            except Exception:
                QtWidgets.QMessageBox.warning(QtWidgets.QMessageBox(), 'Error', 'Mã id nhân viên không tồn tại.')


class UpdateDialog(QtWidgets.QDialog):
    def __init__(self):
        super(UpdateDialog, self).__init__()
        self.informationDialog = InformationDialog()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/s1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        self.QBtn = QtWidgets.QPushButton()
        self.QBtn.setText("Sửa thông tin")
        self.QBtn.setStyleSheet("background: #CCFFFF;\n""height:40px; \n""font-size:18px")

        self.setWindowTitle("Sửa thông tin nhân viên")
        self.setFixedWidth(300)
        self.setFixedHeight(200)

        layout = QtWidgets.QVBoxLayout()
        self.searchinput = QtWidgets.QLineEdit()
        self.onlyInt = QtGui.QIntValidator()
        self.searchinput.setValidator(self.onlyInt)
        self.searchinput.setPlaceholderText("Nhập mã id cần tìm")
        self.searchinput.setStyleSheet(
            "border:1px solid #00FF00;\n""height:30px; \n""border-radius:8px;\n""font-size:18px")
        layout.addWidget(self.searchinput)
        self.QBtn.clicked.connect(self.GotoInformation)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def showInformation(self):
        searchrol = self.searchinput.text()
        try:
            self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="1234",
                database="quanlynhanvien"
            )
            self.mycursor = self.mydb.cursor()

            self.mycursor.execute(
                "SELECT quan_li_nv.id ,quan_li_nv.name,quan_li_nv.code,quan_li_nv.branch,quan_li_nv.phone,quan_li_nv.address,quan_li_nv.status,quan_li_nv.hoursalary,luong.salary FROM quan_li_nv INNER JOIN luong ON quan_li_nv.id=luong.id AND quan_li_nv.id=" + str(
                    searchrol))

            row = self.mycursor.fetchone()

            name = str(row[1])
            code = str(row[2])
            branch = str(row[3])
            phone = str(row[4])
            address = str(row[5])
            status = str(row[6])
            hoursalary = str(row[7])

            self.mydb.commit()
            print(name, code, branch, phone, address, status, hoursalary)
            return name, code, branch, phone, address, status, hoursalary
        except Exception:
            QtWidgets.QMessageBox.warning(QtWidgets.QMessageBox(), 'Error', 'Không tìm thấy nhân viên')

    def checkHoursalary(self, hoursalary):
        hoursalary = int(hoursalary)
        if hoursalary == 0:
            hoursalary = '---Chọn mức lương theo giờ---'

        elif hoursalary == 15:
            hoursalary = '15.000 vnđ'

        elif hoursalary == 20:
            hoursalary = '20.000 vnđ'

        else:
            hoursalary = '30.000 vnđ'
        return hoursalary
    def checkPermission(self,status):
        status = int(status)
        if status == 0:
            status = 'Không'
        elif status == 1:
            status = 'Có'
        else:
            status == '---Chọn quyền truy cập'

        return status



    def GotoInformation(self):

        delrol = self.searchinput.text()

        if delrol == '':
            QtWidgets.QMessageBox.warning(QtWidgets.QMessageBox(), 'Error', 'Vui lòng nhập mã id của nhân viên cần sửa')
        else:
            try:
                name, code, branch, phone, address, status, hoursalary = self.showInformation()
                hoursalary = self.checkHoursalary(hoursalary)
                status = self.checkPermission(status)
                print(name, code, branch, phone, address, status, hoursalary)
                self.mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="1234",
                    database="quanlynhanvien"
                )
                self.mycursor = self.mydb.cursor()

                # check nhan vien exist, neu ko thi nhay toi except
                self.mycursor.execute("SELECT status, code FROM quan_li_nv WHERE id=" + str(delrol))
                result = self.mycursor.fetchone()
                # print(result[0],result[1])

                row_exist = result[0]
                self.mydb.commit()
                self.mycursor.close()
                self.mydb.close()
                dlg = InformationDialog()
                dlg.nameinputId.setText(delrol)
                dlg.code1.setText(code)
                dlg.nameinput1.setText(name)
                dlg.branchinput1.setCurrentText(branch)
                dlg.mobileinput1.setText(phone)
                dlg.addressinput1.setText(address)
                dlg.hoursalary1.setCurrentText(hoursalary)
                dlg.status1.setCurrentText(status)
                dlg.exec_()
                self.close()
            except Exception:
                QtWidgets.QMessageBox.warning(QtWidgets.QMessageBox(), 'Error', 'Mã id nhân viên không tồn tại.')


class Ui_QMainWindow(QtWidgets.QDialog):

    def setupUi(self, QMainWindow):

        # QMainWindow.resize(802, 600)
        QMainWindow.setFixedWidth(760)
        QMainWindow.setFixedHeight(640)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/nhan_vien.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        QMainWindow.setWindowIcon(icon)
        QMainWindow.setIconSize(QtCore.QSize(30, 30))
        self.centralwidget = QtWidgets.QWidget(QMainWindow)
        self.centralwidget.setObjectName("centralwidget")

        ### table 1
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(140, 80, 601, 241))
        self.tableWidget.setStyleSheet("background:#f9fdff")
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setProperty("showDropIndicator", True)
        self.tableWidget.setColumnCount(8)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setHorizontalHeaderLabels(
            ("Id", "Ma nhan vien", "Tên", "Bộ phận", "SĐT", "Địa chỉ", "Hệ số lương", "Quyền truy cập"))
        self.tableWidget.setObjectName("tableWidget")
        # self.btn_them = QtWidgets.QPushButton(self.centralwidget)
        # self.btn_them.setGeometry(QtCore.QRect(10, 80, 101, 51))
        ###

        # font = QtGui.QFont()
        # font.setPointSize(11)
        # font.setBold(True)
        # font.setWeight(75)
        # self.btn_them.setFont(font)
        # self.btn_them.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # self.btn_them.setStyleSheet("color:red;\n""background : yellow;")
        # icon1 = QtGui.QIcon()
        # icon1.addPixmap(QtGui.QPixmap("icon/add1.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.btn_them.setIcon(icon1)
        # self.btn_them.setIconSize(QtCore.QSize(30, 30))
        # self.btn_them.setObjectName("btn_them")

        self.btn_xoa = QtWidgets.QPushButton(self.centralwidget)
        self.btn_xoa.setGeometry(QtCore.QRect(10, 180, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_xoa.setFont(font)
        self.btn_xoa.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_xoa.setStyleSheet("color:white;\n"
                                   "background:#ff7a06")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/d1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_xoa.setIcon(icon2)
        self.btn_xoa.setIconSize(QtCore.QSize(30, 30))
        self.btn_xoa.setObjectName("btn_xoa")
        self.btn_search = QtWidgets.QPushButton(self.centralwidget)
        self.btn_search.setGeometry(QtCore.QRect(10, 270, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_search.setFont(font)
        self.btn_search.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_search.setStyleSheet("color:red;\n"
                                      "background:#fffdb5")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icon/s1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_search.setIcon(icon3)
        self.btn_search.setIconSize(QtCore.QSize(20, 20))
        self.btn_search.setObjectName("btn_search")
        self.btn_update = QtWidgets.QPushButton(self.centralwidget)
        self.btn_update.setGeometry(QtCore.QRect(10, 380, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_update.setFont(font)
        self.btn_update.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_update.setStyleSheet("color:red;\n"
                                      "background:#bbd3ff;")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icon/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_update.setIcon(icon4)
        self.btn_update.setObjectName("btn_update")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 0, 411, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 50, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        # table 2 ###
        ##
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(140, 379, 599, 151))
        self.tableWidget_2.setStyleSheet("background:#fbffea")
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setProperty("showDropIndicator", True)
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.setHorizontalHeaderLabels(("Mã Nhân Viên", "Thời gian", "Phạt (vnđ)", "Trạng thái"))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(199)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(0)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(28)
        ####

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 350, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(420, 550, 161, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)

        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(590, 550, 151, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        ##

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(220, 550, 151, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:green;")
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 550, 230, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 580, 250, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(220, 580, 250, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:red;")
        self.label_9.setObjectName("label_8")

        ###
        self.btn_load = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load.setGeometry(QtCore.QRect(10, 10, 51, 51))
        self.btn_load.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_load.setToolTipDuration(-1)
        self.btn_load.setStyleSheet("background:#effcff;\n"
                                    "border-radius : 10px;")
        self.btn_load.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icon/house.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_load.setIcon(icon5)
        self.btn_load.setIconSize(QtCore.QSize(30, 30))
        self.btn_load.setObjectName("btn_load")
        ###

        QMainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(QMainWindow)
        self.statusbar.setObjectName("statusbar")
        QMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(QMainWindow)
        QtCore.QMetaObject.connectSlotsByName(QMainWindow)

        ###  Event   ###
        # self.btn_load.clicked.connect(self.loaddata)
        # self.btn_them.clicked.connect(self.insert)
        self.btn_search.clicked.connect(self.search)
        self.btn_xoa.clicked.connect(self.delete)
        self.btn_update.clicked.connect(self.update)

    def preView(self, QMainWindow):

        thread1 = Thread()

        thread1.data.connect(ui.callback_function1)
        thread1.start()

        thread2 = Thread_2()
        thread2.data.connect(ui.callback_function2)
        thread2.start()

        thread3 = Thread_2()
        thread3.data.connect(ui.callback_function3)
        thread3.start()

    def retranslateUi(self, QMainWindow):
        _translate = QtCore.QCoreApplication.translate
        QMainWindow.setWindowTitle(_translate("QMainWindow", "Quản lí nhân viên"))
        # self.btn_them.setText(_translate("QMainWindow", "Thêm"))
        self.btn_xoa.setText(_translate("QMainWindow", "Xóa"))
        self.btn_search.setText(_translate("QMainWindow", "Tìm kiếm"))
        self.btn_update.setText(_translate("QMainWindow", "Sửa"))
        self.label.setText(_translate("QMainWindow", "HỆ THỐNG QUẢN LÍ NHÂN VIÊN"))
        self.label_2.setText(_translate("QMainWindow", "Bảng danh sách nhân viên"))
        self.tableWidget_2.setSortingEnabled(False)
        time = datetime.now()
        self.label_3.setText(_translate("QMainWindow", "Bảng CheckIn/Out tháng " + time.strftime('%m')))

        # self.label_7.setText(_translate("QMainWindow", "Nhân viên có tiền lương cao nhất: "))
        # self.label_8.setText(_translate("QMainWindow", "Nhân viên có giờ làm thấp nhất: "))

    def loaddata(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="1234",
            database="quanlynhanvien"
        )
        self.mycursor = self.mydb.cursor()

        query = "SELECT * FROM quan_li_nv "

        self.mycursor.execute(query)
        result = self.mycursor.fetchall()

        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        # query2 = "SELECT * FROM luong"
        query2 = "SELECT code,timeIn,fine,status FROM checkInOut where month = 6"
        self.mycursor.execute(query2)
        result = self.mycursor.fetchall()

        self.tableWidget_2.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget_2.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_2.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        self.mycursor.close()

    # def insert(self):
    #     dlg = InsertDialog()
    #     dlg.exec_()

    def search(self):
        dlg = SearchDialog()
        dlg.exec_()

    def update(self):
        dlg = UpdateDialog()
        dlg.exec_()

    def delete(self):
        dlg = DeleteDialog()
        dlg.exec_()

    def exit(self):
        exit()

    def checkPermission(self):
        searchrol = self.searchinput.text()
        try:
            self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="1234",
                database="quanlynhanvien"
            )
            self.mycursor = self.mydb.cursor()

            self.mycursor.execute(
                "SELECT quan_li_nv.status FROM quan_li_nv WHERE quan_li_nv.id =" + str(
                    searchrol))
            row = self.mycursor.fetchone()
            result = row[0]
            self.mydb.commit()
            self.close()
            if result == 1:
                return True
            else:
                return False
        except Exception:
            return False
    def max_salary(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="1234",
            database="quanlynhanvien"
        )
        self.mycursor = self.mydb.cursor()

        self.mycursor.execute("SELECT MAX(salary) FROM luong ")
        salary_max = self.mycursor.fetchone()[0]

        self.mycursor.execute(
            "SELECT quan_li_nv.name,MAX(salary) FROM quan_li_nv INNER JOIN luong ON salary = %d AND luong.id = quan_li_nv.id" % salary_max)

        result_max = self.mycursor.fetchone()
        print("max salary: ", result_max);

        self.label_6.setText(str(result_max))

    def min_hour(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="1234",
            database="quanlynhanvien"
        )
        self.mycursor = self.mydb.cursor()

        self.mycursor.execute("SELECT MIN(status) FROM quan_li_nv ")
        min_hour = self.mycursor.fetchone()[0]

        self.mycursor.execute("SELECT name,MIN(status) FROM quan_li_nv WHERE status=%d" % min_hour)

        result_min = self.mycursor.fetchone()
        print("min hour: ", result_min);

        self.label_9.setText(str(result_min))

    def callback_function1(self, data):
        self.loaddata()

    def callback_function2(self):
        self.max_salary()

    def callback_function3(self):
        self.min_hour()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    QMainWindow = QtWidgets.QMainWindow()
    ui = Ui_QMainWindow()
    ui.setupUi(QMainWindow)
    thread1 = Thread()
    thread1.data.connect(ui.callback_function1)
    thread1.start()

    # thread2 = Thread_2()
    # thread2.data.connect(ui.callback_function2)
    # thread2.start()

    # thread3 = Thread_2()
    # thread3.data.connect(ui.callback_function3)
    # thread3.start()
    QMainWindow.show()

    sys.exit(app.exec_())
