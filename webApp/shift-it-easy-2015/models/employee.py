
from google.appengine.api import users
from google.appengine.ext import ndb

class employee(ndb.Model)
	workerID = ndb.KeyProperty(kind = String)
	workerType = ndb.StringProperty()
	firstName = ndb.StringProperty()
	lastName = ndb.StringProperty()
	userName = ndb.StringProperty()
	password = ndb.StringProperty()
	percentJob = ndb.DoubleProperty()
	shiftHead = ndb.BooleanProperty(default=True)
	
	
	
	
	
	