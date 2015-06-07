
from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.ext import db
from employee import Employee
from datetime import timedelta

class PreparingSchedule(ndb.Model):
	date = ndb.DateProperty()
	ShiftType = ndb.IntegerProperty()
	nurseUserName = ndb.StringProperty()
	rule = ndb.IntegerProperty()
	
	@classmethod
	def checkIfAssignAlready(self, date, shift, rule):
		assign = []
		assign = PreparingSchedule.query(PreparingSchedule.date == date, PreparingSchedule.ShiftType == shift, PreparingSchedule.rule == rule).get()
	
		if assign:
			return assign.nurseUserName
			
		else:
			return None
			
	
	
	def checkIfAssignAlready1(self, date, shift, rule):
		assign = []
		assign = PreparingSchedule.query(PreparingSchedule.date == date, PreparingSchedule.ShiftType == shift, PreparingSchedule.rule == rule).get()
	
		if assign:
			return assign
			
		else:
			return None
			
	
			
	def deleteItem(self):
		self.key.delete()
		
		
	def checkLegalAssign_Night_After_Night(self):
		assign = []
		yesturday = self.date - timedelta(days=1)
		tomorrow = self.date + timedelta(days=1)
		
		#Checking if the assign is two sequence nights.
		if self.ShiftType == 0:
			nightBefore = PreparingSchedule.query(PreparingSchedule.date == yesturday, PreparingSchedule.ShiftType == 0,PreparingSchedule.nurseUserName == self.nurseUserName ).get()
			nightAfter = PreparingSchedule.query(PreparingSchedule.date == tomorrow, PreparingSchedule.ShiftType == 0,PreparingSchedule.nurseUserName == self.nurseUserName ).get()
			
			if nightBefore or nightAfter:
				return False
		return True
			
	
	
	
	
	
	
	
	