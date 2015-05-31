
from google.appengine.api import users
from google.appengine.ext import ndb
from employee import Employee

class CurrentSchedule(ndb.Model):
	Date = ndb.DateProperty()
	ShiftType = ndb.StringProperty()
	ShiftHead = ndb.KeyProperty(kind = Employee)
	SimpleNurse = ndb.KeyProperty(kind = Employee)
	Standby = ndb.KeyProperty(kind = Employee)

	
	
	
	
	
	
	
	