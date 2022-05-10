from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(965, 800)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(30, 10, 811, 781))
        self.frame.setStyleSheet("border-image: url(max-bender-VmX3vmBecFE-unsplash.jpg);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(296, 630, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(0,0,0,0);\n"
"border-style: outset;\n"
"border-width: 3px;\n"
"border-color: white;\n"
"font: bold 16px;\n"
"min-width: 10em;\n"
"padding: 8px;\n"
"color:white;")
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setDragEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(527, 630, 81, 52))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
"font: bold 25px;\n"
"color:white;\n"
"background-color: rgb(85, 255, 255);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color:rgb(170, 255, 255);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color:rgb(43, 255, 224);\n"
"}")
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda:self.City())
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(310, 290, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background-color: rgb(0,0,0,0);\n"
"font: bold 18px;\n"
"color:white;\n"
"border:none;\n"
"border-color: white;")
        self.textBrowser.setLineWidth(0)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_2.setGeometry(QtCore.QRect(310, 210, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setStyleSheet("background-color: rgb(0,0,0,0);\n"
"border-color: white;\n"
"font: bold 18px;\n"
"color:white;\n"
"border:none")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_3.setGeometry(QtCore.QRect(310, 120, 291, 91))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.textBrowser_3.setFont(font)
        self.textBrowser_3.setStyleSheet("background-color: rgb(0,0,0,0);\n"
"color:white;\n"
"border-color: white;\n"
"border:none;\n"
"font: bold 20px;")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QtCore.QRect(270, 120, 41, 41))
        font = QtGui.QFont()
        font.setFamily("IcoMoon-Free")
        font.setPointSize(29)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: none;\n"
"color:white;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setEnabled(True)
        self.label_5.setGeometry(QtCore.QRect(270, 200, 41, 41))
        font = QtGui.QFont()
        font.setFamily("IcoMoon-Free")
        font.setPointSize(29)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: none;\n"
"color:white;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setEnabled(True)
        self.label_6.setGeometry(QtCore.QRect(270, 360, 41, 41))
        font = QtGui.QFont()
        font.setFamily("IcoMoon-Free")
        font.setPointSize(29)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: none;\n"
"color:white;")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setEnabled(True)
        self.label_7.setGeometry(QtCore.QRect(270, 280, 41, 41))
        font = QtGui.QFont()
        font.setFamily("IcoMoon-Free")
        font.setPointSize(29)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: none;\n"
"color:white;")
        self.label_7.setObjectName("label_7")
        self.textBrowser_4 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_4.setGeometry(QtCore.QRect(310, 370, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.textBrowser_4.setFont(font)
        self.textBrowser_4.setStyleSheet("background-color: rgb(0,0,0,0);\n"
"border-color: white;\n"
"font: bold 18px;\n"
"color:white;\n"
"border:none;")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(80, 50, 711, 701))
        self.frame_2.setStyleSheet("background-color: rgb(0,0,0,130);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(189, 579, 31, 54))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton\n"
"{\n"
"font: bold 18px;\n"
"color:white;\n"
"background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color:rgb(255, 85, 127);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color:rgb(170, 0, 0);\n"
"}")
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda:self.clearall())
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setEnabled(True)
        self.label_8.setGeometry(QtCore.QRect(270, 440, 41, 41))
        font = QtGui.QFont()
        font.setFamily("IcoMoon-Free")
        font.setPointSize(29)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: none;\n"
"color:white;")
        self.label_8.setObjectName("label_8")
        self.textBrowser_5 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_5.setGeometry(QtCore.QRect(310, 440, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.textBrowser_5.setFont(font)
        self.textBrowser_5.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.textBrowser_5.setStyleSheet("background-color: rgb(0,0,0,0);\n"
"border-color: white;\n"
"font: bold 18px;\n"
"color:white;\n"
"border:none;\n"
"text-align: center;")
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(86, 59, 701, 51))
        font = QtGui.QFont()
        font.setFamily("Big John PRO Bold")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("font:bold 30px;\n"
"color:white;")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(810, 10, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton\n"
"{\n"
"font: bold 20px;\n"
"color:white;\n"
"background-color: rgb(0, 0, 0,0);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(0, 0, 0,50);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: rgb(0, 0, 0,100);\n"
"}")
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.frame.raise_()
        self.frame_2.raise_()
        self.lineEdit.raise_()
        self.textBrowser_2.raise_()
        self.textBrowser.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.textBrowser_4.raise_()
        self.textBrowser_3.raise_()
        self.label_8.raise_()
        self.textBrowser_5.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        self.pushButton_3.raise_()
        self.pushButton_3.clicked.connect(lambda:sys.exit())

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Press City"))
        self.pushButton.setText(_translate("Form", ""))
        self.textBrowser.setPlaceholderText(_translate("Form", "Temperature", "20"))
        self.textBrowser_2.setPlaceholderText(_translate("Form", "Date", "20"))
        self.textBrowser_3.setPlaceholderText(_translate("Form", "City", "20"))
        self.label_4.setText(_translate("Form", ""))
        self.label_5.setText(_translate("Form", ""))
        self.label_6.setText(_translate("Form", ""))
        self.label_7.setText(_translate("Form", ""))
        self.textBrowser_4.setPlaceholderText(_translate("Form", "Weather", "20"))
        self.pushButton_2.setText(_translate("Form", ""))
        self.label_8.setText(_translate("Form", ""))
        self.textBrowser_5.setPlaceholderText(_translate("Form", "Coordinates", "20"))
        self.pushButton_3.setText(_translate("Form", ""))
    def City(self):
            import requests
            import math
            from datetime import date
            city_name=self.lineEdit.text()
            API_key='Your_api_key'
            self.r = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city_name+'&appid='+API_key)
            city=self.r.json()['name']
            date=date.today()
            temperature=self.r.json()['main']['temp'] 
            weather=self.r.json()['weather'][0]['main']
            coordinates=str(self.r.json()['coord']['lon'])+' Long '+str(self.r.json()['coord']['lat'])+' Lat '
            self.textBrowser.append(str(round(temperature-272.15))+'°C')
            self.textBrowser_2.append(str(date))
            self.textBrowser_3.append(str(city))
            self.textBrowser_4.append(str(weather))
            self.textBrowser_5.append(str(coordinates))
    def clearall(self):
            self.textBrowser.setText('')
            self.textBrowser_2.setText('')
            self.textBrowser_3.setText('')
            self.textBrowser_4.setText('')
            self.textBrowser_5.setText('')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
