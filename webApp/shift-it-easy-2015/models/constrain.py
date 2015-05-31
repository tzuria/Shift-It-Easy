
from google.appengine.ext import ndb
from employee import Employee

class Constrain(ndb.Model):
	employeeUN = ndb.StringProperty()
	constrianDay = ndb.NumberProperty()
	constrianWeek = ndb.NumberProperty()
	ShiftType = ndb.StringProperty()
	constrainKind = ndb.StringProperty()
	notes = ndb.StringProperty()

		
	def getWantShiftHead(self, week, day, shift):
		if not date:
			return False
			
		if not shift:
			return False
	
		employees = []
		list = Constrain.query(Constrain.constrainWeek = week and Constrain.constrainDay = day and Constrain.shiftType = type)
		
		if list:
			employees = list
	
	
	
	
	