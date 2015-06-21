
from google.appengine.ext import ndb
from employee import Employee
import time
from datetime import date
from datetime import timedelta

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
			
	@staticmethod	
	def deleteEmployeesConstrains(userName):
		constrains = Constrain.query(Constrain.employeeUN == userName).fetch()
		if constrains:
			for constrain in constrains:
				constrain.key.delete()
				
	@staticmethod
	def addConstrain(userName,date):
		for i in range(14):
			for j in range(3):
				constrain = Constrain()
				constrain.employeeUN = userName
				constrain.constrainDate = date + timedelta(days = (i))
				constrain.ShiftType = j
				constrain.constrainKind = 0
				constrain.put()
	
	
	
	
	