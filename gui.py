# -*- coding: utf-8 -*-
import logic
import matplotlib.pyplot as pp
import subprocess
from PyQt4 import QtCore, QtGui
from operator import itemgetter

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
        self.p = ''
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 120, 221, 101))
        self.label.setObjectName(_fromUtf8("label"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(300, 100, 471, 191))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(470, 10, 301, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.textEdit2 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit2.setGeometry(QtCore.QRect(310, 380, 451, 131))
        self.textEdit2.setObjectName(_fromUtf8("textEdit2"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 310, 451, 35))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.button_clicked)
        self.pushButton2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(20, 490, 201, 35))
        self.pushButton2.setObjectName(_fromUtf8("pushButton2"))
        self.pushButton2.clicked.connect(self.button2_clicked)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 400, 99, 25))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 33))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def button_clicked(self):
        self.mytext = self.textEdit.toPlainText()
        output = logic.find_similarity(((self.mytext)),logic.code_list)
        print output
        idx = dict(zip(logic.class_list, output))
        sorted_vals = sorted(idx.items(), key=itemgetter(1))[-3:]
        print sorted_vals
        self.p = ''
        for i in range(3):
            self.p += sorted_vals[i][0] +'\n\n'
        print self.p
        self.textEdit2.setText(self.p)
        pp.plot(output,"x")
        pp.ylim([0,sorted(output)[-2]])
        pp.show()

    def button2_clicked(self):
        files = self.p.split('\n\n')
        for f in files:
            proc = subprocess.Popen(['gedit', logic.root_path+f])


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Enter Bug Description", None))
        self.label_2.setText(_translate("MainWindow", "Bugs Annoy! - Eclipse", None))
        self.pushButton.setText(_translate("MainWindow", "Find Buggy Files", None))
        self.pushButton2.setText(_translate("MainWindow", "Open Result Files", None))
        self.label_3.setText(_translate("MainWindow", "Result", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

