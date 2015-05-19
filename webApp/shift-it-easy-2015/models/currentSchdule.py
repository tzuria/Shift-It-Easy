
from google.appengine.api import users
from google.appengine.ext import ndb

class currentSchdule(ndb.Model):
	Date = ndb.KeyProperty(kind = String)
	ShiftType = ndb.StringProperty()
	ShiftHead = ndb.StringProperty()
	SimpleNurse = ndb.StringProperty()
	Standby = ndb.StringProperty()

	
	
	
	
	
	
	
	