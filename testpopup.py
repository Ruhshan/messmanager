from PyQt4.Qt import *
from PyQt4 import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s
class MyPopup(QWidget):
    def __init__(self,a):
        super(MyPopup, self).__init__()
        self.initu(self,a)
    def initu(self,Meal,a):
        Meal.setObjectName(_fromUtf8("Meal"))
        Meal.resize(215, 108)
        self.namelabel = QtGui.QLabel(Meal)
        self.namelabel.setGeometry(QtCore.QRect(30, 10, 141, 17))
        self.namelabel.setFrameShape(QtGui.QFrame.Box)
        self.namelabel.setText(a)
        self.namelabel.setObjectName(_fromUtf8("namelabel"))
        self.label_2 = QtGui.QLabel(Meal)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 41, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.meals = QtGui.QLineEdit(Meal)
        self.meals.setGeometry(QtCore.QRect(60, 30, 81, 27))
        self.meals.setObjectName(_fromUtf8("meals"))
        self.label = QtGui.QLabel(Meal)
        self.label.setGeometry(QtCore.QRect(150, 40, 66, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.ok = QtGui.QPushButton(Meal)
        self.ok.setGeometry(QtCore.QRect(0, 70, 98, 27))
        self.ok.setObjectName(_fromUtf8("ok"))
        self.cancel = QtGui.QPushButton(Meal)
        self.cancel.setGeometry(QtCore.QRect(110, 70, 98, 27))
        self.cancel.setDefault(True)
        self.cancel.setObjectName(_fromUtf8("cancel"))

        self.retranslateUi(Meal)
        QtCore.QMetaObject.connectSlotsByName(Meal)

    def retranslateUi(self, Meal):
        Meal.setWindowTitle(QtGui.QApplication.translate("Meal", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Meal", "has", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Meal", "meals", None, QtGui.QApplication.UnicodeUTF8))
        self.ok.setText(QtGui.QApplication.translate("Meal", "Ok", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel.setText(QtGui.QApplication.translate("Meal", "Cancel", None, QtGui.QApplication.UnicodeUTF8))




