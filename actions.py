from dialogs import mealdialog
from PyQt4 import *
class Methods:
	def mealupdate(self,selectedDate,mealtype):
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
			self.w = mealdialog(m,1,mealtype)
			self.w.exec_()
		
		



		 



