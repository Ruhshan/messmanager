from dialogs import MealDialog
from PyQt4 import *
class Operations:
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
		
		



		 



