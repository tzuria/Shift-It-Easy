
from google.appengine.ext import ndb
from employee import Employee

class Constrain(ndb.Model):
	employeeUN = ndb.StringProperty()
	constrainDate = ndb.DateProperty()
	ShiftType = ndb.IntegerProperty()
	constrainKind = ndb.IntegerProperty()
	notes = ndb.StringProperty()

	@classmethod
	def getShiftHeads(self, date, shift, satisfactory):
		employees = []
		list = Constrain.query(Constrain.constrainDate == date, Constrain.ShiftType == shift, Constrain.constrainKind == satisfactory).fetch()		
		if list:
			for l in list:
				shiftHead = Employee.getEmployeeByUserName(l.employeeUN)
				if shiftHead:
					if shiftHead.shiftHead:
						employees.append(shiftHead.userName)		
			
			return employees
		else:
			return None
			
	@classmethod
	def getCrew(self, date, shift, satisfactory):
		employees = []
		list = Constrain.query(Constrain.constrainDate == date, Constrain.ShiftType == shift, Constrain.constrainKind == satisfactory).fetch()		
		if list:
			for l in list:
				shiftHead = Employee.getEmployeeByUserName(l.employeeUN)
				if shiftHead:
					employees.append(shiftHead.userName)		
			
			return employees
		else:
			return None
	
	
	
	
	