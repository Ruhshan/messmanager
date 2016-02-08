# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created: Sun Feb  7 02:07:22 2016
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import MySQLdb
from popwindow import MyPopup
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(120, 10, 98, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.UpdateTree)
        self.treeWidget = QtGui.QTreeWidget(Form)
        self.treeWidget.setGeometry(QtCore.QRect(50, 70, 300, 192))
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.headerItem().setText(0, _fromUtf8("1"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
    def UpdateTree(self):
    	db = MySQLdb.connect("localhost","root","root","test" )
    	cursor = db.cursor()
    	cursor.execute("show columns from nameVal")
        col = cursor.fetchall()
        print col
        cursor.execute("select * from nameVal;")
        table = cursor.fetchall()
        
        for c in range(len(col)):
        	self.treeWidget.setColumnWidth(c,20)
        	self.treeWidget.header().setResizeMode(c,QtGui.QHeaderView.Stretch | QtGui.QHeaderView.Interactive)
        	self.treeWidget.headerItem().setText(c,str(col[c][0]))
        
        self.treeWidget.clear()
        
        for item in range(len(table)):
            QtGui.QTreeWidgetItem(self.treeWidget)
            for value in range(len(table[item])):
                self.treeWidget.topLevelItem(item).setText(value, str(table[item][value]))
    def newWindow(self):
		self.w = MyPopup()
		self.w.setGeometry(QtCore.QRect(100, 100, 400, 200))
		self.w.show()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

