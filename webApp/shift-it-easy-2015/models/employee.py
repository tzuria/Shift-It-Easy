
from google.appengine.ext import ndb

class employee(ndb.Model)
	workerID = ndb.IntegerProperty()
	workerType = ndb.StringProperty()
	firstName = ndb.StringProperty()
	lastName = ndb.StringProperty()
	userName = ndb.StringProperty()
	password = ndb.StringProperty()
	percentJob = ndb.DoubleProperty()
	shiftHead = ndb.BooleanProperty(default=True)
	
	
	
	
	