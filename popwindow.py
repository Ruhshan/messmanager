from PyQt4.Qt import *

class MyPopup(QWidget):
    def __init__(self):
        super(MyPopup, self).__init__()
        self.initu()
    def initu(self):
        self.comboBox = QComboBox(self)
        self.comboBox.setGeometry(QRect(140, 30, 78, 27))
        self.comboBox.setObjectName(("comboBox"))
        self.comboBox.addItem(("a"))
        self.comboBox.addItem(("b"))
        self.comboBox.addItem(("c"))
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setGeometry(QRect(130, 80, 113, 27))
        self.lineEdit.setObjectName(("lineEdit"))
        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setGeometry(QRect(100, 180, 176, 27))
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(("buttonBox"))
        


