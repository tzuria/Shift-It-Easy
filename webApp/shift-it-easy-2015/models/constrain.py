
from google.appengine.ext import ndb
from employee import Employee

class Constrain(ndb.Model):
	employee = ndb.KeyProperty(kind = Employee)
	constrianDay = ndb.DateProperty()
	constrianMonth = ndb.DateProperty()
	ShiftType = ndb.StringProperty()
	ConstrainKind = ndb.StringProperty()
	Notes = ndb.StringProperty()

		
	
	
	
	
	
	
	
	
	