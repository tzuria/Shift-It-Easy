
from google.appengine.ext import ndb

class Employee(ndb.Model):
	workerID = ndb.StringProperty()
	workerType = ndb.StringProperty()
	firstName = ndb.StringProperty()
	lastName = ndb.StringProperty()
	userName = ndb.StringProperty()
	password = ndb.StringProperty()
	percentJob = ndb.FloatProperty()
	shiftHead = ndb.BooleanProperty(default=True)
	
	
	
	
	
	
	
	