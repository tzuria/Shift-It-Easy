
from google.appengine.api import users
from google.appengine.ext import ndb
from employee import Employee

class CurrentSchedule(ndb.Model):
	date = ndb.DateProperty()
	ShiftType = ndb.IntegerProperty()
	nurseUserName = ndb.StringProperty()
	rule = ndb.IntegerProperty()

	@classmethod
	def checkIfAssignAlready(self, date, shift, rule):
		assign = []
		assign = CurrentSchedule.query(CurrentSchedule.date == date, CurrentSchedule.ShiftType == shift, CurrentSchedule.rule == rule).get()
	
		if assign:
			return assign.nurseUserName
			
		else:
			return None
			
	
	@classmethod
	def checkIfAssignAlready1(self, date, shift, rule):
		assign = []
		assign = CurrentSchedule.query(CurrentSchedule.date == date, CurrentSchedule.ShiftType == shift, CurrentSchedule.rule == rule).get()
	
		if assign:
			return assign
			
		else:
			return None
	