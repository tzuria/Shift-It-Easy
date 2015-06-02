from google.appengine.ext import ndb
from employee import Employee

class Constrain(ndb.Model):
	employee = ndb.KeyProperty(kind = Employee)
	constrianDay = ndb.IntegerProperty()
	constrianWeek = ndb.IntegerProperty()
	ShiftType = ndb.IntegerProperty()
	constrainKind = ndb.IntegerProperty()
	notes = ndb.StringProperty()

		
	def getShiftHeads(self, day, month, shift, satisfactory):
		if not day or not month or not shift or not satisfactory:
			return False
	
		employees = []
		list = Constrain.query(Constrain.constrainDay == day and Constrain.constrainMonth == month
								and Constrain.shiftType == shift, Constrain.constrainKind == satisfactory and Constrain.employee.shiftHead)
		
		if list:
			for l in list:
				employees.append(l.employee.userName)
				
			return employees
		else:
<<<<<<< HEAD
			return None	

=======
			return None
>>>>>>> origin/master
