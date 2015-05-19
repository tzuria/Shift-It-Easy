
from google.appengine.ext import ndb

class consrains(ndb.Model):
	Date = ndb.StringProperty(kind = String)
	EmployeeID = ndb.StringProperty(kind = int)
	ShiftType = ndb.StringProperty()
	ConstrainKind = ndb.StringProperty()
	Notes = ndb.StringProperty()
	
	
	
	
	
	
	
	
	