from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_calculator(object):
    def setupUi(self, calculator):
        calculator.setObjectName("calculator")
        calculator.resize(300, 475)
        self.centralwidget = QtWidgets.QWidget(calculator)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, -20, 301, 471))
        self.widget.setObjectName("widget")
        self.btn_c = QtWidgets.QPushButton(self.widget, clicked= lambda: self.func_num("C"))
        self.btn_c.setGeometry(QtCore.QRect(0, 80, 74, 74))
        self.btn_c.setObjectName("btn_c")
        self.btn_del = QtWidgets.QPushButton(self.widget, clicked= lambda: self.del_func())
        self.btn_del.setGeometry(QtCore.QRect(75, 80, 74, 74))
        self.btn_del.setObjectName("btn_del")
        self.btn_radical = QtWidgets.QPushButton(self.widget, clicked= lambda: self.func_radical())
        self.btn_radical.setGeometry(QtCore.QRect(150, 80, 74, 74))
        self.btn_radical.setObjectName("btn_radical")
        self.btn_plus = QtWidgets.QPushButton(self.widget, clicked= lambda: self.func_num("+"))
        self.btn_plus.setGeometry(QtCore.QRect(225, 80, 74, 74))
        self.btn_plus.setObjectName("btn_plus")
        self.btn_7 = QtWidgets.QPushButton(self.widget, clicked= lambda: self.func_num("7"))
        self.btn_7.setGeometry(QtCore.QRect(0, 155, 74, 74))
        self.btn_7.setObjectName("btn_7")
        self.btn_9 = QtWidgets.QPushButton(self.widget, clicked= lambda: self.func_num("9"))
        self.btn_9.setGeometry(QtCore.QRect(150, 155, 74, 74))
        self.btn_9.setObjectName("btn_9")
        self.btn_8 = QtWidgets.QPushButton(self.widget, clicked= lambda: self.func_num("8"))
        self.btn_8.setGeometry(QtCore.QRect(75, 155, 74, 74))
        self.btn_8.setObjectName("btn_8")
        self.btn_minus = QtWidgets.QPushButton(self.widget, clicked= lambda: self.func_num("-"))
        self.btn_minus.setGeometry(QtCore.QRect(225, 155, 74, 74))
        self.btn_minus.setObjectName("btn_minus")
        self.btn_4 = QtWidgets.QPushButton(self.widget, clicked= lambda: self.func_num("4"))
        self.btn_4.setGeometry(QtCore.QRect(0, 230, 74, 74))
        self.btn_4.setObjectName("btn_4")
        self.btn_5 = QtWidgets.QPushButton(self.widget, clicked= lambda: self.func_num("5"))
        self.btn_5.setGeometry(QtCore.QRect(75, 230, 74, 74))
        self.btn_5.setObjectName("btn_5")
        self.btn_6 = QtWidgets.QPushButton(self.widget, clicked= lambda: self.func_num("6"))
        self.btn_6.setGeometry(QtCore.QRect(150, 230, 74, 74))
        self.btn_6.setObjectName("btn_6")
        self.btn_multiply = QtWidgets.QPushButton(self.widget, clicked= lambda: self.func_num("*"))
        self.btn_multiply.setGeometry(QtCore.QRect(225, 230, 74, 74))
        self.btn_multiply.setObjectName("btn_multiply")
        self.btn_1 = QtWidgets.QPushButton(self.widget, clicked= lambda: self.func_num("1"))
        self.btn_1.setGeometry(QtCore.QRect(0, 305, 74, 74))
        self.btn_1.setObjectName("btn_1")
        self.btn_2 = QtWidgets.QPushButton(self.widget, clicked= lambda: self.func_num("2"))
        self.btn_2.setGeometry(QtCore.QRect(75, 305, 74, 74))
        self.btn_2.setObjectName("btn_2")
        self.btn_3 = QtWidgets.QPushButton(self.widget, clicked= lambda: self.func_num("3"))
        self.btn_3.setGeometry(QtCore.QRect(150, 305, 74, 74))
        self.btn_3.setObjectName("btn_3")
        self.btn_divide = QtWidgets.QPushButton(self.widget, clicked= lambda: self.func_num("/"))
        self.btn_divide.setGeometry(QtCore.QRect(225, 305, 74, 74))
        self.btn_divide.setObjectName("btn_divide")
        self.btn_0 = QtWidgets.QPushButton(self.widget, clicked= lambda: self.func_num("0"))
        self.btn_0.setGeometry(QtCore.QRect(0, 380, 149, 74))
        self.btn_0.setObjectName("btn_0")
        self.btn_dot = QtWidgets.QPushButton(self.widget, clicked= lambda: self.examp_dot())
        self.btn_dot.setGeometry(QtCore.QRect(150, 380, 74, 74))
        self.btn_dot.setObjectName("btn_dot")
        self.btn_equals = QtWidgets.QPushButton(self.widget, clicked= lambda: self.func_equals())
        self.btn_equals.setGeometry(QtCore.QRect(225, 380, 74, 74))
        self.btn_equals.setObjectName("btn_equals")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(0, 20, 300, 59))
        self.lineEdit.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.lineEdit.setObjectName("lineEdit")
        calculator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(calculator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        self.menubar.setObjectName("menubar")
        calculator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(calculator)
        self.statusbar.setObjectName("statusbar")
        calculator.setStatusBar(self.statusbar)

        self.retranslateUi(calculator)
        QtCore.QMetaObject.connectSlotsByName(calculator)

    def retranslateUi(self, calculator):
        _translate = QtCore.QCoreApplication.translate
        calculator.setWindowTitle(_translate("calculator", "calculator"))
        self.btn_c.setText(_translate("calculator", "C"))
        self.btn_del.setText(_translate("calculator", "del"))
        self.btn_radical.setText(_translate("calculator", "√"))
        self.btn_plus.setText(_translate("calculator", "+"))
        self.btn_7.setText(_translate("calculator", "7"))
        self.btn_9.setText(_translate("calculator", "9"))
        self.btn_8.setText(_translate("calculator", "8"))
        self.btn_minus.setText(_translate("calculator", "-"))
        self.btn_4.setText(_translate("calculator", "4"))
        self.btn_5.setText(_translate("calculator", "5"))
        self.btn_6.setText(_translate("calculator", "6"))
        self.btn_multiply.setText(_translate("calculator", "*"))
        self.btn_1.setText(_translate("calculator", "1"))
        self.btn_2.setText(_translate("calculator", "2"))
        self.btn_3.setText(_translate("calculator", "3"))
        self.btn_divide.setText(_translate("calculator", "/"))
        self.btn_0.setText(_translate("calculator", "0"))
        self.btn_dot.setText(_translate("calculator", "."))
        self.btn_equals.setText(_translate("calculator", "="))


    def func_num(self, pressed):
        if pressed == 'C':
            self.lineEdit.setText('0')
        else:
            if self.lineEdit.text() == '0':
                self.lineEdit.setText("")
            self.lineEdit.setText(f"{self.lineEdit.text()}{pressed}")


    def func_dot(self):
        if '.' in self.lineEdit.text():
            pass
        else:
            self.lineEdit.setText(f"{self.lineEdit.text()}.")



    def del_func(self):
        self.lineEdit.setText(self.lineEdit.text()[:-1])



    def examp_dot(self):
        if self.lineEdit.text()[-1] == ".":
            pass
        else:
           self.lineEdit.setText(f"{self.lineEdit.text()}.") 


    def func_radical(self):
        self.lineEdit.setText(f"{self.lineEdit.text()} ** {1/2}")


    def func_equals(self):
        try:
            rezult = eval(self.lineEdit.text())
            self.lineEdit.setText(str(rezult))
        except:
            self.lineEdit.setText(':(')

    



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    calculator = QtWidgets.QMainWindow()
    ui = Ui_calculator()
    ui.setupUi(calculator)
    calculator.show()
    sys.exit(app.exec_())