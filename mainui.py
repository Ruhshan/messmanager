# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'messmanager.ui'
#
# Created: Mon Feb  8 22:46:31 2016
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from actions import Operations,Members

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MessManager(object):	
    teststring=""
    def setupUi(self, MessManager):
        MessManager.setObjectName(_fromUtf8("MessManager"))
        MessManager.resize(400, 372)
        self.tabWidget = QtGui.QTabWidget(MessManager)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 796, 2012))
        self.tabWidget.setToolTip(_fromUtf8(""))
        self.tabWidget.setStatusTip(_fromUtf8(""))
        self.tabWidget.setWhatsThis(_fromUtf8(""))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))

        self.OplabDate = QtGui.QLabel(self.tab)
        self.OplabDate.setGeometry(QtCore.QRect(10, 0, 41, 21))
        self.OplabDate.setStatusTip(_fromUtf8(""))
        self.OplabDate.setWhatsThis(_fromUtf8(""))
        self.OplabDate.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.OplabDate.setObjectName(_fromUtf8("OplabDate"))
        
        self.OplabUpdateMeal = QtGui.QLabel(self.tab)
        self.OplabUpdateMeal.setGeometry(QtCore.QRect(10, 30, 161, 17))
        self.OplabUpdateMeal.setStatusTip(_fromUtf8(""))
        self.OplabUpdateMeal.setWhatsThis(_fromUtf8(""))
        self.OplabUpdateMeal.setObjectName(_fromUtf8("OplabUpdateMeal"))
        
        self.memberslist=["abir","ruhshan", "ahmed"]

        self.OpBntBf = QtGui.QPushButton(self.tab)
        self.OpBntBf.setGeometry(QtCore.QRect(40, 50, 98, 27))
        self.OpBntBf.setToolTip(_fromUtf8(""))
        self.OpBntBf.setStatusTip(_fromUtf8(""))
        self.OpBntBf.setWhatsThis(_fromUtf8(""))
        self.OpBntBf.setObjectName(_fromUtf8("OpBntBf"))
        
        self.OpBtnLnch = QtGui.QPushButton(self.tab)
        self.OpBtnLnch.setGeometry(QtCore.QRect(170, 50, 98, 27))
        self.OpBtnLnch.setStatusTip(_fromUtf8(""))
        self.OpBtnLnch.setWhatsThis(_fromUtf8(""))
        self.OpBtnLnch.setObjectName(_fromUtf8("OpBtnLnch"))
        
        self.OpBtnDnr = QtGui.QPushButton(self.tab)
        self.OpBtnDnr.setGeometry(QtCore.QRect(300, 50, 98, 27))
        self.OpBtnDnr.setStatusTip(_fromUtf8(""))
        self.OpBtnDnr.setWhatsThis(_fromUtf8(""))
        self.OpBtnDnr.setObjectName(_fromUtf8("OpBtnDnr"))
        
        self.OplabBrfIcon = QtGui.QLabel(self.tab)
        self.OplabBrfIcon.setGeometry(QtCore.QRect(10, 50, 24, 24))
        self.OplabBrfIcon.setStatusTip(_fromUtf8(""))
        self.OplabBrfIcon.setWhatsThis(_fromUtf8(""))
        self.OplabBrfIcon.setText(_fromUtf8(""))
        self.OplabBrfIcon.setPixmap(QtGui.QPixmap(_fromUtf8("breakfast3-512.png")))
        self.OplabBrfIcon.setScaledContents(True)
        self.OplabBrfIcon.setObjectName(_fromUtf8("OplabBrfIcon"))
        
        self.OplabLnchIcon = QtGui.QLabel(self.tab)
        self.OplabLnchIcon.setGeometry(QtCore.QRect(140, 50, 25, 27))
        self.OplabLnchIcon.setStatusTip(_fromUtf8(""))
        self.OplabLnchIcon.setWhatsThis(_fromUtf8(""))
        self.OplabLnchIcon.setText(_fromUtf8(""))
        self.OplabLnchIcon.setPixmap(QtGui.QPixmap(_fromUtf8("lunch.png")))
        self.OplabLnchIcon.setScaledContents(True)
        self.OplabLnchIcon.setObjectName(_fromUtf8("OplabLnchIcon"))
        self.OplabDnrIcon = QtGui.QLabel(self.tab)
        
        self.OplabDnrIcon.setGeometry(QtCore.QRect(270, 50, 24, 24))
        self.OplabDnrIcon.setStatusTip(_fromUtf8(""))
        self.OplabDnrIcon.setWhatsThis(_fromUtf8(""))
        self.OplabDnrIcon.setText(_fromUtf8(""))
        self.OplabDnrIcon.setPixmap(QtGui.QPixmap(_fromUtf8("dinner.png")))
        self.OplabDnrIcon.setScaledContents(True)
        self.OplabDnrIcon.setObjectName(_fromUtf8("OplabDnrIcon"))
        
        self.OplabBazar = QtGui.QLabel(self.tab)
        self.OplabBazar.setGeometry(QtCore.QRect(10, 90, 66, 17))
        self.OplabBazar.setStatusTip(_fromUtf8(""))
        self.OplabBazar.setWhatsThis(_fromUtf8(""))
        self.OplabBazar.setObjectName(_fromUtf8("OplabBazar"))
        
        self.Oplabexpnd = QtGui.QLabel(self.tab)
        self.Oplabexpnd.setGeometry(QtCore.QRect(10, 110, 66, 17))
        self.Oplabexpnd.setStatusTip(_fromUtf8(""))
        self.Oplabexpnd.setWhatsThis(_fromUtf8(""))
        self.Oplabexpnd.setObjectName(_fromUtf8("Oplabexpnd"))
        
        self.Oplinedtexpnd = QtGui.QLineEdit(self.tab)
        self.Oplinedtexpnd.setGeometry(QtCore.QRect(70, 106, 51, 27))
        self.Oplinedtexpnd.setStatusTip(_fromUtf8(""))
        self.Oplinedtexpnd.setWhatsThis(_fromUtf8(""))
        self.Oplinedtexpnd.setObjectName(_fromUtf8("Oplinedtexpnd"))
        
        self.Oplabrtrn = QtGui.QLabel(self.tab)
        self.Oplabrtrn.setGeometry(QtCore.QRect(126, 110, 66, 17))
        self.Oplabrtrn.setStatusTip(_fromUtf8(""))
        self.Oplabrtrn.setWhatsThis(_fromUtf8(""))
        self.Oplabrtrn.setObjectName(_fromUtf8("Oplabrtrn"))
        
        self.Oplnedtrtrn = QtGui.QLineEdit(self.tab)
        self.Oplnedtrtrn.setGeometry(QtCore.QRect(180, 106, 51, 27))
        self.Oplnedtrtrn.setStatusTip(_fromUtf8(""))
        self.Oplnedtrtrn.setWhatsThis(_fromUtf8(""))
        self.Oplnedtrtrn.setObjectName(_fromUtf8("Oplnedtrtrn"))
        
        self.Oplabdeposit = QtGui.QLabel(self.tab)
        self.Oplabdeposit.setGeometry(QtCore.QRect(10, 140, 66, 17))
        self.Oplabdeposit.setStatusTip(_fromUtf8(""))
        self.Oplabdeposit.setWhatsThis(_fromUtf8(""))
        self.Oplabdeposit.setObjectName(_fromUtf8("Oplabdeposit"))
        
        self.Oplabchosemember = QtGui.QLabel(self.tab)
        self.Oplabchosemember.setGeometry(QtCore.QRect(10, 160, 111, 17))
        self.Oplabchosemember.setStatusTip(_fromUtf8(""))
        self.Oplabchosemember.setWhatsThis(_fromUtf8(""))
        self.Oplabchosemember.setObjectName(_fromUtf8("Oplabchosemember"))
        
        self.Opcmbxdpst = QtGui.QComboBox(self.tab)
        self.Opcmbxdpst.setGeometry(QtCore.QRect(130, 151, 101, 27))
        self.Opcmbxdpst.setStatusTip(_fromUtf8(""))
        self.Opcmbxdpst.setWhatsThis(_fromUtf8(""))
        self.Opcmbxdpst.setObjectName(_fromUtf8("Opcmbxdpst"))
        
        self.Oplinedtdpst = QtGui.QLineEdit(self.tab)
        self.Oplinedtdpst.setGeometry(QtCore.QRect(240, 151, 81, 27))
        self.Oplinedtdpst.setStatusTip(_fromUtf8(""))
        self.Oplinedtdpst.setWhatsThis(_fromUtf8(""))
        self.Oplinedtdpst.setObjectName(_fromUtf8("Oplinedtdpst"))
        
        self.Opbtndpstadd = QtGui.QPushButton(self.tab)
        self.Opbtndpstadd.setGeometry(QtCore.QRect(330, 150, 61, 27))
        self.Opbtndpstadd.setStatusTip(_fromUtf8(""))
        self.Opbtndpstadd.setWhatsThis(_fromUtf8(""))
        self.Opbtndpstadd.setAutoFillBackground(False)
        self.Opbtndpstadd.setDefault(True)
        self.Opbtndpstadd.setFlat(False)
        self.Opbtndpstadd.setObjectName(_fromUtf8("Opbtndpstadd"))
        
        self.Opbtnbzrset = QtGui.QPushButton(self.tab)
        self.Opbtnbzrset.setGeometry(QtCore.QRect(330, 105, 61, 27))
        self.Opbtnbzrset.setStatusTip(_fromUtf8(""))
        self.Opbtnbzrset.setWhatsThis(_fromUtf8(""))
        self.Opbtnbzrset.setDefault(True)
        self.Opbtnbzrset.setObjectName(_fromUtf8("Opbtnbzrset"))
        
        self.OpdateEdit = QtGui.QDateEdit(self.tab)
        self.OpdateEdit.setDate(QtCore.QDate.currentDate())
        self.OpdateEdit.setCalendarPopup(True)
        self.OpdateEdit.setGeometry(QtCore.QRect(50, 0, 125, 27))
        self.OpdateEdit.setStatusTip(_fromUtf8(""))
        self.OpdateEdit.setWhatsThis(_fromUtf8(""))
        self.OpdateEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.OpdateEdit.setObjectName(_fromUtf8("OpdateEdit"))
        
        self.Opcmbxbazar = QtGui.QComboBox(self.tab)
        self.Opcmbxbazar.setGeometry(QtCore.QRect(240, 106, 81, 27))
        self.Opcmbxbazar.setStatusTip(_fromUtf8(""))
        self.Opcmbxbazar.setWhatsThis(_fromUtf8(""))
        self.Opcmbxbazar.setObjectName(_fromUtf8("Opcmbxbazar"))
        
        
        self.OplabSummary = QtGui.QLabel(self.tab)
        self.OplabSummary.setGeometry(QtCore.QRect(10, 190, 71, 17))
        self.OplabSummary.setStatusTip(_fromUtf8(""))
        self.OplabSummary.setWhatsThis(_fromUtf8(""))
        self.OplabSummary.setObjectName(_fromUtf8("OplabSummary"))
        
        self.Oplabdetails = QtGui.QLabel(self.tab)
        self.Oplabdetails.setGeometry(QtCore.QRect(30, 220, 331, 81))
        self.Oplabdetails.setStatusTip(_fromUtf8(""))
        self.Oplabdetails.setWhatsThis(_fromUtf8(""))
        self.Oplabdetails.setFrameShape(QtGui.QFrame.StyledPanel)
        self.Oplabdetails.setTextFormat(QtCore.Qt.RichText)
        self.Oplabdetails.setObjectName(_fromUtf8("Oplabdetails"))
        
        self.opbtnrefrsh = QtGui.QPushButton(self.tab)
        self.opbtnrefrsh.setGeometry(QtCore.QRect(130, 310, 141, 27))
        self.opbtnrefrsh.setStatusTip(_fromUtf8(""))
        self.opbtnrefrsh.setWhatsThis(_fromUtf8(""))
        self.opbtnrefrsh.setObjectName(_fromUtf8("opbtncmt"))
        
        self.tabWidget.addTab(self.tab, _fromUtf8("       Operations        "))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        
        self.Memcmboptions = QtGui.QComboBox(self.tab_2)
        self.Memcmboptions.setGeometry(QtCore.QRect(10, 10, 131, 27))
        self.Memcmboptions.setStatusTip(_fromUtf8(""))
        self.Memcmboptions.setWhatsThis(_fromUtf8(""))
        self.Memcmboptions.setObjectName(_fromUtf8("Memcmboptions"))
        self.Memcmboptions.addItem(_fromUtf8(""))
        self.Memcmboptions.addItem(_fromUtf8(""))
        self.Memcmboptions.addItem(_fromUtf8(""))
        
        self.MemCmbNames = QtGui.QComboBox(self.tab_2)
        self.MemCmbNames.setGeometry(QtCore.QRect(150, 10, 131, 27))
        self.MemCmbNames.setStatusTip(_fromUtf8(""))
        self.MemCmbNames.setWhatsThis(_fromUtf8(""))
        self.MemCmbNames.setObjectName(_fromUtf8("MemCmbNames"))
        
        self.Membtnview = QtGui.QPushButton(self.tab_2)
        self.Membtnview.setGeometry(QtCore.QRect(290, 10, 98, 27))
        self.Membtnview.setStatusTip(_fromUtf8(""))
        self.Membtnview.setWhatsThis(_fromUtf8(""))
        self.Membtnview.setDefault(True)
        self.Membtnview.setObjectName(_fromUtf8("Membtnview"))
        
        self.MemtreeWidget = QtGui.QTreeWidget(self.tab_2)
        self.MemtreeWidget.setGeometry(QtCore.QRect(10, 50, 381, 241))
        self.MemtreeWidget.setStatusTip(_fromUtf8(""))
        self.MemtreeWidget.setWhatsThis(_fromUtf8(""))
        self.MemtreeWidget.setObjectName(_fromUtf8("MemtreeWidget"))
        self.MemtreeWidget.headerItem().setText(0, _fromUtf8("1"))
        
        self.Membtnaddmember = QtGui.QPushButton(self.tab_2)
        self.Membtnaddmember.setGeometry(QtCore.QRect(50, 300, 121, 27))
        self.Membtnaddmember.setStatusTip(_fromUtf8(""))
        self.Membtnaddmember.setWhatsThis(_fromUtf8(""))
        self.Membtnaddmember.setDefault(True)
        self.Membtnaddmember.setObjectName(_fromUtf8("Membtnaddmember"))
        
        self.Membtnrmmember = QtGui.QPushButton(self.tab_2)
        self.Membtnrmmember.setGeometry(QtCore.QRect(200, 300, 141, 27))
        self.Membtnrmmember.setStatusTip(_fromUtf8(""))
        self.Membtnrmmember.setWhatsThis(_fromUtf8(""))
        self.Membtnrmmember.setObjectName(_fromUtf8("Membtnrmmember"))
        
        self.tabWidget.addTab(self.tab_2, _fromUtf8("        Members        "))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        
        self.clolabtotal = QtGui.QLabel(self.tab_4)
        self.clolabtotal.setGeometry(QtCore.QRect(10, 10, 81, 17))
        self.clolabtotal.setStatusTip(_fromUtf8(""))
        self.clolabtotal.setWhatsThis(_fromUtf8(""))
        self.clolabtotal.setObjectName(_fromUtf8("clolabtotal"))
        
        self.clolabtotmout = QtGui.QLabel(self.tab_4)
        self.clolabtotmout.setGeometry(QtCore.QRect(110, 10, 66, 17))
        self.clolabtotmout.setStatusTip(_fromUtf8(""))
        self.clolabtotmout.setWhatsThis(_fromUtf8(""))
        self.clolabtotmout.setFrameShape(QtGui.QFrame.Box)
        self.clolabtotmout.setText(_fromUtf8(""))
        self.clolabtotmout.setObjectName(_fromUtf8("clolabtotmout"))
        
        self.clolabtotexpnd = QtGui.QLabel(self.tab_4)
        self.clolabtotexpnd.setGeometry(QtCore.QRect(10, 30, 91, 17))
        self.clolabtotexpnd.setStatusTip(_fromUtf8(""))
        self.clolabtotexpnd.setWhatsThis(_fromUtf8(""))
        self.clolabtotexpnd.setObjectName(_fromUtf8("clolabtotexpnd"))
        
        self.clolabexpndout = QtGui.QLabel(self.tab_4)
        self.clolabexpndout.setGeometry(QtCore.QRect(110, 30, 66, 17))
        self.clolabexpndout.setStatusTip(_fromUtf8(""))
        self.clolabexpndout.setWhatsThis(_fromUtf8(""))
        self.clolabexpndout.setFrameShape(QtGui.QFrame.Box)
        self.clolabexpndout.setText(_fromUtf8(""))
        self.clolabexpndout.setObjectName(_fromUtf8("clolabexpndout"))
        
        self.clolabmrate = QtGui.QLabel(self.tab_4)
        self.clolabmrate.setGeometry(QtCore.QRect(10, 50, 81, 17))
        self.clolabmrate.setObjectName(_fromUtf8("clolabmrate"))
        
        self.clolabmrateout = QtGui.QLabel(self.tab_4)
        self.clolabmrateout.setGeometry(QtCore.QRect(110, 50, 66, 17))
        self.clolabmrateout.setStatusTip(_fromUtf8(""))
        self.clolabmrateout.setWhatsThis(_fromUtf8(""))
        self.clolabmrateout.setFrameShape(QtGui.QFrame.Box)
        self.clolabmrateout.setText(_fromUtf8(""))
        self.clolabmrateout.setObjectName(_fromUtf8("clolabmrateout"))
        
        self.clotreeWidget = QtGui.QTreeWidget(self.tab_4)
        self.clotreeWidget.setGeometry(QtCore.QRect(10, 100, 381, 231))
        self.clotreeWidget.setStatusTip(_fromUtf8(""))
        self.clotreeWidget.setWhatsThis(_fromUtf8(""))
        self.clotreeWidget.setObjectName(_fromUtf8("clotreeWidget"))
        self.clotreeWidget.headerItem().setText(0, _fromUtf8("1"))
        
        self.clbtnCalculate = QtGui.QPushButton(self.tab_4)
        self.clbtnCalculate.setGeometry(QtCore.QRect(280, 10, 98, 27))
        self.clbtnCalculate.setStatusTip(_fromUtf8(""))
        self.clbtnCalculate.setWhatsThis(_fromUtf8(""))
        self.clbtnCalculate.setObjectName(_fromUtf8("clbtnCalculate"))
        
        self.clobtnreset = QtGui.QPushButton(self.tab_4)
        self.clobtnreset.setGeometry(QtCore.QRect(280, 40, 98, 27))
        self.clobtnreset.setToolTip(_fromUtf8(""))
        self.clobtnreset.setStatusTip(_fromUtf8(""))
        self.clobtnreset.setWhatsThis(_fromUtf8(""))
        self.clobtnreset.setDefault(True)
        self.clobtnreset.setObjectName(_fromUtf8("clobtnreset"))
        
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setEnabled(False)
        self.tab_3.setStatusTip(_fromUtf8(""))
        self.tab_3.setWhatsThis(_fromUtf8(""))
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        #self.tabWidget.addTab(self.tab_3, _fromUtf8(""))

        ####
        ####
        ####
        self.OpdateEdit.dateChanged.connect(self.reInitiateActions)##if date changes
        self.Opmethod=Operations(self.OpdateEdit.date())#Methods class instance
        self.updateMembers()#sets or updates memberslist throught all comboboxes
        self.OpBntBf.clicked.connect(lambda:self.Opmethod.mealUpdate("Breakfast"))
        self.OpBtnLnch.clicked.connect(lambda:self.Opmethod.mealUpdate("Lunch"))
        self.OpBtnDnr.clicked.connect(lambda:self.Opmethod.mealUpdate("Dinner"))

        self.Opbtnbzrset.clicked.connect(lambda:self.Opmethod.bazarSet(self.Oplinedtexpnd.text(),self.Oplnedtrtrn.text(),self.Opcmbxbazar.currentText()))
        self.Opbtndpstadd.clicked.connect(lambda:self.Opmethod.depositUpdate(self.Opcmbxdpst.currentText(),self.Oplinedtdpst.text()))

        self.opbtnrefrsh.clicked.connect(self.refresh)

        self.MemMethods=Members()
        self.Membtnview.clicked.connect(self.memberView)

        self.retranslateUi(MessManager)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MessManager)
    	


    def updateMembers(self):
    	mlist=self.Opmethod.getMembersList()
    	self.Opcmbxdpst.addItems(mlist)
    	self.Opcmbxbazar.addItems(mlist)
    	self.MemCmbNames.addItems(mlist)

    	#self.Opcmbxdpst.setItemText(0,"aaa")

    def reInitiateActions(self):
    	self.Opmethod=Operations(self.OpdateEdit.date())

    def refresh(self):
    	self.OpdateEdit.setDate(QtCore.QDate.currentDate())
    	remDays=self.Opmethod.remainingDays()
    	remBalance=self.Opmethod.remainingBalance()
    	currMealRate=self.Opmethod.currentMealRate()
    	richtext="<html><head/><body><p>Remaining Days: {}</p><p>Remaining Balance: {}</p><p>Current Mealrate: {}</p><p><br/></p><p><br/></p></body></html>".format(remDays,remBalance,currMealRate)
    	self.Oplabdetails.setText(richtext)
    	print remDays

    def memberView(self):
    	colname,table=self.MemMethods.view(self.Memcmboptions.currentText(),self.MemCmbNames.currentText())

    	for c in range(len(colname)):
    		self.MemtreeWidget.headerItem().setText(c,colname[c])
    	for c in range(len(colname)):
    		self.MemtreeWidget.setColumnWidth(c,100)

    	for item in range(len(table)):
    		QtGui.QTreeWidgetItem(self.MemtreeWidget)
    		for value in range(len(table[item])):
    			self.MemtreeWidget.topLevelItem(item).setText(value,str(table[item][value]))



    def retranslateUi(self, MessManager):
        MessManager.setWindowTitle(QtGui.QApplication.translate("MessManager", "MessManager", None, QtGui.QApplication.UnicodeUTF8))
        self.OplabDate.setText(QtGui.QApplication.translate("MessManager", "Date:", None, QtGui.QApplication.UnicodeUTF8))
        self.OplabUpdateMeal.setText(QtGui.QApplication.translate("MessManager", "Update Meal For Today:", None, QtGui.QApplication.UnicodeUTF8))
        self.OpBntBf.setText(QtGui.QApplication.translate("MessManager", "Breakfast", None, QtGui.QApplication.UnicodeUTF8))
        self.OpBtnLnch.setText(QtGui.QApplication.translate("MessManager", "Lunch", None, QtGui.QApplication.UnicodeUTF8))
        self.OpBtnDnr.setText(QtGui.QApplication.translate("MessManager", "Dinner", None, QtGui.QApplication.UnicodeUTF8))
        self.OplabBazar.setText(QtGui.QApplication.translate("MessManager", "Bazar:", None, QtGui.QApplication.UnicodeUTF8))
        self.Oplabexpnd.setText(QtGui.QApplication.translate("MessManager", "Expend:", None, QtGui.QApplication.UnicodeUTF8))
        self.Oplabrtrn.setText(QtGui.QApplication.translate("MessManager", "Return:", None, QtGui.QApplication.UnicodeUTF8))
        self.Oplabdeposit.setText(QtGui.QApplication.translate("MessManager", "Deposit:", None, QtGui.QApplication.UnicodeUTF8))
        self.Oplabchosemember.setText(QtGui.QApplication.translate("MessManager", "Choose Member:", None, QtGui.QApplication.UnicodeUTF8))
        self.Opbtndpstadd.setText(QtGui.QApplication.translate("MessManager", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.Opbtnbzrset.setText(QtGui.QApplication.translate("MessManager", "Set", None, QtGui.QApplication.UnicodeUTF8))
        self.OplabSummary.setText(QtGui.QApplication.translate("MessManager", "Summary:", None, QtGui.QApplication.UnicodeUTF8))
        self.Oplabdetails.setText(QtGui.QApplication.translate("MessManager", "<html><head/><body><p>Remaining Days: ##</p><p>Remaining Balance: ##</p><p>Current Mealrate: ##</p><p><br/></p><p><br/></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.opbtnrefrsh.setText(QtGui.QApplication.translate("MessManager", "Refresh", None, QtGui.QApplication.UnicodeUTF8))
        self.Memcmboptions.setItemText(0, QtGui.QApplication.translate("MessManager", "Money", None, QtGui.QApplication.UnicodeUTF8))
        self.Memcmboptions.setItemText(1, QtGui.QApplication.translate("MessManager", "Meal", None, QtGui.QApplication.UnicodeUTF8))
        self.Memcmboptions.setItemText(2, QtGui.QApplication.translate("MessManager", "Bazar", None, QtGui.QApplication.UnicodeUTF8))
        self.Membtnview.setText(QtGui.QApplication.translate("MessManager", "View", None, QtGui.QApplication.UnicodeUTF8))
        self.Membtnaddmember.setText(QtGui.QApplication.translate("MessManager", "Add Member", None, QtGui.QApplication.UnicodeUTF8))
        self.Membtnrmmember.setText(QtGui.QApplication.translate("MessManager", "Remove Member", None, QtGui.QApplication.UnicodeUTF8))
        self.clolabtotal.setText(QtGui.QApplication.translate("MessManager", "Total Meal:", None, QtGui.QApplication.UnicodeUTF8))
        self.clolabtotexpnd.setText(QtGui.QApplication.translate("MessManager", "Total Expend:", None, QtGui.QApplication.UnicodeUTF8))
        self.clolabmrate.setText(QtGui.QApplication.translate("MessManager", "Meal Rate:", None, QtGui.QApplication.UnicodeUTF8))
        self.clbtnCalculate.setText(QtGui.QApplication.translate("MessManager", "Calculate All", None, QtGui.QApplication.UnicodeUTF8))
        self.clobtnreset.setText(QtGui.QApplication.translate("MessManager", "Reset All", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QtGui.QApplication.translate("MessManager", "         Closing         ", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("MessManager", "Balance", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MessManager = QtGui.QWidget()
    ui = Ui_MessManager()
    ui.setupUi(MessManager)
    MessManager.show()
    sys.exit(app.exec_())

