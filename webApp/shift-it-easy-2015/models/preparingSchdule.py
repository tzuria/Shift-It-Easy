
from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.ext import db
from employee import Employee

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

	
	
	
	
	
	
	
	