from cgitb import reset
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_calculator(object):
    def setupUi(self, calculator):
        calculator.setObjectName("calculator")
        calculator.resize(376, 475)
        #Fixed window size
        calculator.setFixedSize(376,475)

        self.centralwidget = QtWidgets.QWidget(calculator)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, -20, 381, 471))
        self.widget.setObjectName("widget")

        self.btn_c = QtWidgets.QPushButton(self.widget, clicked= lambda: self.button_nums("C"))
        self.btn_c.setGeometry(QtCore.QRect(0, 80, 74, 74))
        self.btn_c.setStyleSheet("background-color: rgb(235, 235, 235);\n"
        "font: 18pt \"Bodoni MT\";")
        self.btn_c.setObjectName("btn_c")

        self.btn_del = QtWidgets.QPushButton(self.widget, clicked= lambda: self.func_del())
        self.btn_del.setGeometry(QtCore.QRect(75, 80, 74, 74))
        self.btn_del.setStyleSheet("background-color: rgb(235, 235, 235);\n"
        "font: 10pt \"Bodoni MT\";")
        self.btn_del.setObjectName("btn_del")

        self.btn_radical = QtWidgets.QPushButton(self.widget, clicked= lambda: self.func_radical())
        self.btn_radical.setGeometry(QtCore.QRect(150, 80, 74, 74))
        self.btn_radical.setStyleSheet("background-color: rgb(235, 235, 235);\n"
        "font: 12pt \"Bodoni MT\";")
        self.btn_radical.setObjectName("btn_radical")

        self.btn_plus = QtWidgets.QPushButton(self.widget, clicked= lambda: self.button_nums("+"))
        self.btn_plus.setGeometry(QtCore.QRect(225, 80, 74, 74))
        self.btn_plus.setStyleSheet("background-color: rgb(235, 235, 235);\n"
        "font: 20pt \"Bodoni MT\";")
        self.btn_plus.setObjectName("btn_plus")

        self.btn_7 = QtWidgets.QPushButton(self.widget, clicked= lambda: self.button_nums("7"))
        self.btn_7.setGeometry(QtCore.QRect(0, 155, 74, 74))
        self.btn_7.setStyleSheet("background-color: rgb(247, 247, 247);\n"
        "font: 11pt \"Bodoni MT\";")
        self.btn_7.setObjectName("btn_7")

        self.btn_9 = QtWidgets.QPushButton(self.widget, clicked= lambda: self.button_nums("9"))
        self.btn_9.setGeometry(QtCore.QRect(150, 155, 74, 74))
        self.btn_9.setStyleSheet("background-color: rgb(247, 247, 247);\n"
        "font: 11pt \"Bodoni MT\";")
        self.btn_9.setObjectName("btn_9")

        self.btn_8 = QtWidgets.QPushButton(self.widget, clicked= lambda: self.button_nums("8"))
        self.btn_8.setGeometry(QtCore.QRect(75, 155, 74, 74))
        self.btn_8.setStyleSheet("background-color: rgb(247, 247, 247);\n"
        "font: 11pt \"Bodoni MT\";")
        self.btn_8.setObjectName("btn_8")

        self.btn_minus = QtWidgets.QPushButton(self.widget, clicked= lambda: self.button_nums("-"))
        self.btn_minus.setGeometry(QtCore.QRect(225, 155, 74, 74))
        self.btn_minus.setStyleSheet("background-color: rgb(235, 235, 235);\n"
        "font: 20pt \"Bodoni MT\";")
        self.btn_minus.setObjectName("btn_minus")

        self.btn_4 = QtWidgets.QPushButton(self.widget, clicked= lambda: self.button_nums("4"))
        self.btn_4.setGeometry(QtCore.QRect(0, 230, 74, 74))
        self.btn_4.setStyleSheet("background-color: rgb(247, 247, 247);\n"
        "font: 11pt \"Bodoni MT\";")
        self.btn_4.setObjectName("btn_4")

        self.btn_5 = QtWidgets.QPushButton(self.widget, clicked= lambda: self.button_nums("5"))
        self.btn_5.setGeometry(QtCore.QRect(75, 230, 74, 74))
        self.btn_5.setStyleSheet("background-color: rgb(247, 247, 247);\n"
        "font: 11pt \"Bodoni MT\";")
        self.btn_5.setObjectName("btn_5")

        self.btn_6 = QtWidgets.QPushButton(self.widget, clicked= lambda: self.button_nums("6"))
        self.btn_6.setGeometry(QtCore.QRect(150, 230, 74, 74))
        self.btn_6.setStyleSheet("background-color: rgb(247, 247, 247);\n"
        "font: 11pt \"Bodoni MT\";")
        self.btn_6.setObjectName("btn_6")

        self.btn_multiply = QtWidgets.QPushButton(self.widget, clicked= lambda: self.button_nums("*"))
        self.btn_multiply.setGeometry(QtCore.QRect(225, 230, 74, 74))
        self.btn_multiply.setStyleSheet("background-color: rgb(235, 235, 235);\n"
        "font: 15pt \"Bodoni MT\";")
        self.btn_multiply.setObjectName("btn_multiply")

        self.btn_1 = QtWidgets.QPushButton(self.widget, clicked= lambda: self.button_nums("1"))
        self.btn_1.setGeometry(QtCore.QRect(0, 305, 74, 74))
        self.btn_1.setStyleSheet("background-color: rgb(247, 247, 247);\n"
        "font: 11pt \"Bodoni MT\";")
        self.btn_1.setObjectName("btn_1")

        self.btn_2 = QtWidgets.QPushButton(self.widget, clicked= lambda: self.button_nums("2"))
        self.btn_2.setGeometry(QtCore.QRect(75, 305, 74, 74))
        self.btn_2.setStyleSheet("background-color: rgb(247, 247, 247);\n"
        "font: 11pt \"Bodoni MT\";")
        self.btn_2.setObjectName("btn_2")

        self.btn_3 = QtWidgets.QPushButton(self.widget, clicked= lambda: self.button_nums("3"))
        self.btn_3.setGeometry(QtCore.QRect(150, 305, 74, 74))
        self.btn_3.setStyleSheet("background-color: rgb(247, 247, 247);\n"
        "font: 11pt \"Bodoni MT\";")
        self.btn_3.setObjectName("btn_3")

        self.btn_divide = QtWidgets.QPushButton(self.widget, clicked= lambda: self.button_nums("/"))
        self.btn_divide.setGeometry(QtCore.QRect(225, 305, 74, 74))
        self.btn_divide.setStyleSheet("background-color: rgb(235, 235, 235);\n"
        "font: 20pt \"Bodoni MT\";")
        self.btn_divide.setObjectName("btn_divide")

        self.btn_0 = QtWidgets.QPushButton(self.widget, clicked= lambda: self.button_nums("0"))
        self.btn_0.setGeometry(QtCore.QRect(0, 380, 149, 74))
        self.btn_0.setStyleSheet("background-color: rgb(247, 247, 247);\n"
        "font: 11pt \"Bodoni MT\";")
        self.btn_0.setObjectName("btn_0")

        self.btn_dot = QtWidgets.QPushButton(self.widget, clicked= lambda: self.func_dot())
        self.btn_dot.setGeometry(QtCore.QRect(150, 380, 74, 74))
        self.btn_dot.setStyleSheet("background-color: rgb(235, 235, 235);\n"
        "font: 20pt \"Bodoni MT\";")
        self.btn_dot.setObjectName("btn_dot")

        self.btn_equals = QtWidgets.QPushButton(self.widget, clicked= lambda: self.func_equals())
        self.btn_equals.setGeometry(QtCore.QRect(225, 380, 74, 74))
        self.btn_equals.setStyleSheet("background-color: rgb(235, 235, 235);\n"
        "font: 20pt \"Bodoni MT\";")
        self.btn_equals.setObjectName("btn_equals")

        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(1, 20, 373, 59))
        self.lineEdit.setStyleSheet("font: 20pt \"Bodoni MT\";\n"
        "background-color: rgb(247, 247, 247);")
        self.lineEdit.setObjectName("lineEdit")

        self.btn_x3 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.func_x3())
        self.btn_x3.setGeometry(QtCore.QRect(300, 135, 74, 74))
        self.btn_x3.setStyleSheet("background-color: rgb(235, 235, 235);\n"
        "font: 8pt \"Bodoni MT\";")
        self.btn_x3.setObjectName("btn_x3")

        self.btn_x2 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.func_x2())
        self.btn_x2.setGeometry(QtCore.QRect(300, 60, 74, 74))
        self.btn_x2.setStyleSheet("background-color: rgb(235, 235, 235);\n"
        "font: 8pt \"Bodoni MT\";")
        self.btn_x2.setObjectName("btn_x2")

        self.btn_open_brack = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.button_nums("("))
        self.btn_open_brack.setGeometry(QtCore.QRect(300, 210, 74, 74))
        self.btn_open_brack.setStyleSheet("background-color: rgb(235, 235, 235);\n"
        "font: 12pt \"Bodoni MT\";")
        self.btn_open_brack.setObjectName("btn_open_brack")

        self.btn_close_brack = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.button_nums(")"))
        self.btn_close_brack.setGeometry(QtCore.QRect(300, 285, 74, 74))
        self.btn_close_brack.setStyleSheet("background-color: rgb(235, 235, 235);\n"
        "font: 12pt \"Bodoni MT\";")
        self.btn_close_brack.setObjectName("btn_close_brack")

        self.btn_plus_minus = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.func_plus_minus())
        self.btn_plus_minus.setGeometry(QtCore.QRect(300, 360, 74, 74))
        self.btn_plus_minus.setStyleSheet("background-color: rgb(235, 235, 235);\n"
        "font: 15pt \"Bodoni MT\";")
        self.btn_plus_minus.setObjectName("btn_plus_minus")

        calculator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(calculator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 376, 21))
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
        self.btn_x3.setText(_translate("calculator", "x3"))
        self.btn_x2.setText(_translate("calculator", "x2"))
        self.btn_open_brack.setText(_translate("calculator", "("))
        self.btn_close_brack.setText(_translate("calculator", ")"))
        self.btn_plus_minus.setText(_translate("calculator", "+/-"))



    def button_nums(self, tuch):
        if tuch == 'C':
            self.lineEdit.setText('0')
        else:
            if self.lineEdit.text() == '0':
                self.lineEdit.setText("")
            self.lineEdit.setText(f"{self.lineEdit.text()}{tuch}")



    def func_equals(self):
        try:
            result = eval(self.lineEdit.text())
            self.lineEdit.setText(str(result))
        except:
            self.lineEdit.setText(":(")



    # petqa algoritm grel 
    def func_dot(self):
        if self.lineEdit.text()[-1] == '.':
            pass
        else:
            self.lineEdit.setText(f"{self.lineEdit.text()}.")



    def func_plus_minus(self): 
        self.lineEdit.setText(f"{'-'}{self.lineEdit.text()}")



    def func_x2(self):
        result = eval(f"{self.lineEdit.text()} ** 2")
        self.lineEdit.setText(f"{result}")



    def func_x3(self):
        result = eval(f"{self.lineEdit.text()} ** 3")
        self.lineEdit.setText(f"{result}")



    def func_radical(self):
        result = eval(f"{self.lineEdit.text()} ** (1/2)")
        self.lineEdit.setText(f"{result}")



    def func_del(self):
        self.lineEdit.setText(f"{self.lineEdit.text()[:-1]}")

    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    calculator = QtWidgets.QMainWindow()
    ui = Ui_calculator()
    ui.setupUi(calculator)
    calculator.show()
    sys.exit(app.exec_())