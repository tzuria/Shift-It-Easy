
from google.appengine.ext import ndb
import hashlib      #we need this to safely store passwords
import logging

class Employee(ndb.Model):
	workerID = ndb.StringProperty()
	firstName = ndb.StringProperty()
	lastName = ndb.StringProperty()
	userName = ndb.StringProperty()
	password = ndb.StringProperty()
	percentJob = ndb.IntegerProperty()
	shiftHead = ndb.BooleanProperty(default=True)
	isManager = ndb.BooleanProperty(default=False)
	
	def setPassword(self, password):
		self.password = hashlib.md5(password).hexdigest()
		self.put()

	def NewPassword(self, password):
		self.password = hashlib.md5(password).hexdigest()

	@staticmethod
	def getEmployeeByUserName(userName):
		employee = []
		employee = Employee.query(Employee.userName == userName).get()
		if employee:
			return employee
		return
	
	@staticmethod	
	def Get_All_Employees():
		employees = Employee.query().fetch()
		if employees:
			return employees
		return
		
	@staticmethod
	def checkToken(token):
		userName = Employee.get_by_id(long(token))
		return userName
		
	def checkPassword(self, password):
		if not password:
			return False
			
		if self.password == hashlib.md5(password).hexdigest():
			return True
		return False
			
		
	
	
	
	
	
	
	
	