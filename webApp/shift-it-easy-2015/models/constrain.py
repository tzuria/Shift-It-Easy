
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
	def addConstrains(userName,date):
		for i in range(14):
			for j in range(3):
				constrain = Constrain()
				constrain.employeeUN = userName
				constrain.constrainDate = date + timedelta(days = (i))
				constrain.ShiftType = j
				constrain.constrainKind = 0
				constrain.put()
	
	@staticmethod
	def getUserConstraintsAndNotes(userName):
		constrains = Constrain.query(Constrain.employeeUN == userName.userName).fetch()
		if constrains:

			constrains = sorted(constrains)
			temp0 = Constrain()
			temp1 = Constrain()
			temp2 = Constrain()
			j = 0
			for i in range(len(constrains)/3):
				j = i*3
				if j <= 41:
					if constrains[j].ShiftType == 0:
						temp0.CopyConstrain(constrains[j])
					elif constrains[j].ShiftType == 1:
						temp1.CopyConstrain(constrains[j])
					elif constrains[j].ShiftType == 2:
						temp2.CopyConstrain(constrains[j])
				if j <= 40:	
					if constrains[j+1].ShiftType == 0:
						temp0.CopyConstrain(constrains[j+1])
					elif constrains[j+1].ShiftType == 1:
						temp1.CopyConstrain(constrains[j+1])
					elif constrains[j+1].ShiftType == 2:
						temp2.CopyConstrain(constrains[j+1])
				if j <= 39:	
					if constrains[j+2].ShiftType == 0:
						temp0.CopyConstrain(constrains[j+2])
					elif constrains[j+2].ShiftType == 1:
						temp1.CopyConstrain(constrains[j+2])
					elif constrains[j+2].ShiftType == 2:
						temp2.CopyConstrain(constrains[j+2])
			
				if j <= 41:
					constrains[j].CopyConstrain(temp0)
				if j <= 40:
					constrains[j+1].CopyConstrain(temp1)
				if j <= 39:
					constrains[j+2].CopyConstrain(temp2)
				
			
			
			userConstrains = []
			userNotes = []
			userConstrainsAndNotes = []
			for c in constrains:
				userConstrains.append(c.constrainKind)
				userNotes.append(c.notes)
			userConstrainsAndNotes.append(userConstrains)
			userConstrainsAndNotes.append(userNotes)
			return userConstrainsAndNotes
		else:
			return
	
	
	def __cmp__(self, other):
		if self.constrainDate > other.constrainDate:
			return 1
		elif self.constrainDate < other.constrainDate:
			return -1
		else:
			return 0
			
	def CopyConstrain(self,other):
		self.employeeUN = other.employeeUN
		self.constrainDate = other.constrainDate
		self.ShiftType = other.ShiftType
		self.constrainKind = other.constrainKind
		self.notes = other.notes
		
	
	