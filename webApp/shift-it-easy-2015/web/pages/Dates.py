from google.appengine.ext.webapp import template
import time
from datetime import date
from datetime import timedelta
from datetime import datetime

class Dates():

	today = date.today()
	sunday0 = today
	monday0 = today
	tuesday0 = today
	wednesday0 = today
	thursday0 = today
	friday0 = today
	saturday0 = today
	
	sunday1 = today
	monday1 = today
	tuesday1 = today
	wednesday1 = today
	thursday1 = today
	friday1 = today
	saturday1 = today
	
	myTemplate = None
	
	def __init__(self,template):
		self.myTemplate = template
		
	def assignDatesOnTemplate(self):
		self.myTemplate['sunday0'] = "%d/%d"%(self.sunday0.day ,self.sunday0.month)
		self.myTemplate['monday0'] = "%d/%d"%(self.monday0.day ,self.monday0.month)
		self.myTemplate['tuesday0'] = "%d/%d"%(self.tuesday0.day ,self.tuesday0.month)
		self.myTemplate['wednesday0'] = "%d/%d"%(self.wednesday0.day ,self.wednesday0.month)
		self.myTemplate['thursday0'] = "%d/%d"%(self.thursday0.day ,self.thursday0.month)
		self.myTemplate['friday0'] = "%d/%d"%(self.friday0.day ,self.friday0.month)
		self.myTemplate['saturday0'] = "%d/%d"%(self.saturday0.day ,self.saturday0.month)
		self.myTemplate['sunday1'] = "%d/%d"%(self.sunday1.day ,self.sunday1.month)
		self.myTemplate['monday1'] = "%d/%d"%(self.monday1.day ,self.monday1.month)
		self.myTemplate['tuesday1'] = "%d/%d"%(self.tuesday1.day ,self.tuesday1.month)
		self.myTemplate['wednesday1'] = "%d/%d"%(self.wednesday1.day ,self.wednesday1.month)
		self.myTemplate['thursday1'] = "%d/%d"%(self.thursday1.day ,self.thursday1.month)
		self.myTemplate['friday1'] = "%d/%d"%(self.friday1.day ,self.friday1.month)
		self.myTemplate['saturday1'] = "%d/%d"%(self.saturday1.day ,self.saturday1.month)
		
	
	def macheDates(self):
		if (self.today.weekday() == 6):
			self.sunday0 = self.today
			self.monday0 = self.sunday0 + timedelta(days=1)
			self.tuesday0 = self.monday0 + timedelta(days=1)
			self.wednesday0 = self.tuesday0 + timedelta(days = 1)
			self.thursday0 = self.wednesday0 + timedelta(days = 1)
			self.friday0 = self.thursday0 + timedelta(days = 1)
			self.saturday0 = self.friday0 + timedelta(days = 1)
			
		if (self.today.weekday() == 0):
			self.monday0 = self.today
			self.tuesday0 = self.monday0 + timedelta(days=1)
			self.wednesday0 = self.tuesday0 + timedelta(days = 1)
			self.thursday0 = self.wednesday0 + timedelta(days = 1)
			self.friday0 = self.thursday0 + timedelta(days = 1)
			self.saturday0 = self.friday0 + timedelta(days = 1)
			self.sunday0 = self.saturday0 - timedelta(days = 6)
			
		if (self.today.weekday() == 1):
			self.tuesday0 = self.today
			self.wednesday0 = self.tuesday0 + timedelta(days = 1)
			self.thursday0 = self.wednesday0 + timedelta(days = 1)
			self.friday0 = self.thursday0 + timedelta(days = 1)
			self.saturday0 = self.friday0 + timedelta(days = 1)
			self.sunday0 = self.saturday0 - timedelta(days = 6)
			self.monday0 = self.sunday0 + timedelta(days=1)
			
		if (self.today.weekday() == 2):
			self.wednesday0 = self.today
			self.thursday0 = self.wednesday0 + timedelta(days = 1)
			self.friday0 = self.thursday0 + timedelta(days = 1)
			self.saturday0 = self.friday0 + timedelta(days = 1)
			self.sunday0 = self.saturday0 - timedelta(days = 6)
			self.monday0 = self.sunday0 + timedelta(days=1)
			self.tuesday0 = self.monday0 + timedelta(days=1)
			
		if (self.today.weekday() == 3):
			self.thursday0 = self.today
			self.friday0 = self.thursday0 + timedelta(days = 1)
			self.saturday0 = self.friday0 + timedelta(days = 1)
			self.sunday0 = self.saturday0 - timedelta(days = 6)
			self.monday0 = self.sunday0 + timedelta(days=1)
			self.tuesday0 = self.monday0 + timedelta(days=1)
			self.wednesday0 = self.tuesday0 + timedelta(days = 1)
			
		if (self.today.weekday() == 4):
			self.friday0 = self.today
			self.saturday0 = self.friday0 + timedelta(days = 1)
			self.sunday0 = self.saturday0 - timedelta(days = 6)
			self.monday0 = self.sunday0 + timedelta(days=1)
			self.tuesday0 = self.monday0 + timedelta(days=1)
			self.wednesday0 = self.tuesday0 + timedelta(days = 1)
			self.thursday0 = self.wednesday0 + timedelta(days = 1)
			
		if (self.today.weekday() == 5):
			self.saturday0 = self.today
			self.sunday0 = self.saturday0 - timedelta(days = 6)
			self.monday0 = self.sunday0 + timedelta(days=1)
			self.tuesday0 = self.monday0 + timedelta(days=1)
			self.wednesday0 = self.tuesday0 + timedelta(days = 1)
			self.thursday0 = self.wednesday0 + timedelta(days = 1)
			self.friday0 = self.thursday0 + timedelta(days = 1)		
		
		if self.saturday0:
			self.sunday1 = self.saturday0 + timedelta(days=1)
			self.monday1 = self.saturday0 + timedelta(days=2)
			self.tuesday1 = self.saturday0 + timedelta(days=3)
			self.wednesday1 = self.saturday0 + timedelta(days=4)
			self.thursday1 = self.saturday0 + timedelta(days=5)
			self.friday1 = self.saturday0 + timedelta(days=6)
			self.saturday1 = self.saturday0 + timedelta(days=7)
		
		
	
	def lastTwoWeeks(self):
		if(int(self.today.strftime("%U"))%2 == 0):
			self.today = self.today - timedelta(days = 7)
			
		self.macheDates()	
		self.assignDatesOnTemplate()
				
		return self.myTemplate

		
	
	def theseTwoWeeks(self):
		if(int(self.today.strftime("%U"))%2 == 0):
			self.today = self.today - timedelta(days = 7)	
		self.macheDates()
		self.assignDatesOnTemplate()
		return self.myTemplate
	
	
	def nextTwoWeeks(self):
		self.today = self.today + timedelta(days = 14)
		if(int(self.today.strftime("%U"))%2 == 0):
			self.today = self.today - timedelta(days = 7)
		
		self.macheDates()
				
		self.assignDatesOnTemplate()
				
		return self.myTemplate
		
		
	def createDateObject(self, week, day):
		if week == 0:
			if day == 1:
				return date(self.sunday0.year, self.sunday0.month, self.sunday0.day)
			if day == 2:
				return date(self.monday0.year, self.monday0.month, self.monday0.day)
			if day == 3:
				return date(self.tuesday0.year, self.tuesday0.month, self.tuesday0.day)
			if day == 4:
				return date(self.wednesday0.year, self.wednesday0.month, self.wednesday0.day)
			if day == 5:
				return date(self.thursday0.year, self.thursday0.month, self.thursday0.day)
			if day == 6:
				return date(self.friday0.year, self.friday0.month, self.friday0.day)
			if day == 7:
				return date(self.saturday0.year, self.saturday0.month, self.saturday0.day)
		if week == 1:
			if day == 1:
				return date(self.sunday1.year, self.sunday1.month, self.sunday1.day)
			if day == 2:
				return date(self.monday1.year, self.monday1.month, self.monday1.day)
			if day == 3:
				return date(self.tuesday1.year, self.tuesday1.month, self.tuesday1.day)
			if day == 4:
				return date(self.wednesday1.year, self.wednesday1.month, self.wednesday1.day)
			if day == 5:
				return date(self.thursday1.year, self.thursday1.month, self.thursday1.day)
			if day == 6:
				return date(self.friday1.year, self.friday1.month, self.friday1.day)
			if day == 7:
				return date(self.saturday1.year, self.saturday1.month, self.saturday1.day)
			
			
	@staticmethod
	def submitSession():
		now = datetime.now()
		thisDay = date.today()
		if(int(thisDay.strftime("%U"))%2 == 0) and thisDay.weekday() == 6 and now.hour > 8:
			return True
			
		elif (int(thisDay.strftime("%U"))%2 == 0) and thisDay.weekday() != 6:
			return True
		return False
			