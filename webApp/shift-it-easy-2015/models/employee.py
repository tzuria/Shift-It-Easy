
from google.appengine.ext import ndb
import hashlib      #we need this to safely store passwords
import logging

class Employee(ndb.Model):
	workerID = ndb.StringProperty()
	firstName = ndb.StringProperty()
	lastName = ndb.StringProperty()
	userName = ndb.StringProperty()
	password = ndb.StringProperty()
	percentJob = ndb.StringProperty()
	shiftHead = ndb.BooleanProperty(default=True)
	isManager = ndb.BooleanProperty(default=False)
	
	def setPassword(self, password):
		self.password = hashlib.md5(password).hexdigest()
		self.put()
		
	def checkPassword(self, password):
		if not password:
			return False
			
		if self.password == hashlib.md5(password).hexdigest():
			return True
		return False
			
		
	
	
	
	
	
	
	
	