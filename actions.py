from dialogs import MealDialog
from PyQt4 import *
#from mainui import Ui_MessManager
class Members:
	def getMembersList(self):
		members=["abir","rayan","pratiq"]
		return members
	def view(self,options, member):
		colname=["col1","col2"]
		table=(('ABC', 1L), ('BBC', 2L), ('cBC', 3L), ('DBC', 4L), ('EBC', 5L), ('FBC', 6L), ('GBC', 7L), ('HBC', 8L), ('HBC', 8L), ('IBC', 9L), ('JBC', 10L))
		return colname,table

class Operations(Members):
	def __init__(self, selectedDate):
		self.selectedDate=selectedDate;

	def mealUpdate(self,mealtype):
		selectedDate=self.selectedDate
		print selectedDate
		selectedDate=str(selectedDate)[19:].replace(')','')
		print selectedDate, mealtype
		dates=[1,2,3] #get dates column from database
		members=["ruhshan","ahmed","abir"]
		#for m in members:
			#if selected date not in date:
				#insert date in members table:
				#call popup(0)
			#else:
				#get meal for that date
				#call pop(mean)
		#democall
		for m in members:		
			self.w = MealDialog(m,1,mealtype)
			self.w.exec_()

	def bazarSet(self,expend,retrn,member):
		print self.selectedDate
		print "bazarSet called",expend,retrn,member

	def depositUpdate(self, member, amount):
		print self.selectedDate, member,amount

	def remainingDays(self):
		daysInMonth={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
		year,month,date=map(int,str(QtCore.QDate.currentDate())[18:].replace('(','').replace(')','').split(','))
		if year%4==0 and year%100==0 or year %400!=0:
			daysInMonth[2]=29
		else:
			"letitbe"
		return daysInMonth[month]-date

	def remainingBalance(self):
		return 9999

	def currentMealRate(self):
		return 8989


		
		



		 



