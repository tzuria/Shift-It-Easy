
from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.ext import db
from employee import Employee
from datetime import timedelta

class PreparingSchedule(ndb.Model):
	date = ndb.DateProperty()
	ShiftType = ndb.IntegerProperty()
	nurseUserName = ndb.StringProperty()
	rule = ndb.IntegerProperty()
	
	@classmethod
	def checkIfAssignAlready(self, date, shift, rule):
		assign = []
		assign = PreparingSchedule.query(PreparingSchedule.date == date, PreparingSchedule.ShiftType == shift, PreparingSchedule.rule == rule).get()
	
		if assign:
			return assign.nurseUserName
			
		else:
			return None
			
	
	@classmethod
	def checkIfAssignAlready1(self, date, shift, rule):
		assign = []
		assign = PreparingSchedule.query(PreparingSchedule.date == date, PreparingSchedule.ShiftType == shift, PreparingSchedule.rule == rule).get()
	
		if assign:
			return assign
			
		else:
			return None
			
	
			
	def deleteItem(self):
		self.key.delete()
		
	
	@classmethod	
	def checkLegalAssign_Night_After_Night(self):
		assign = []
		yesterday = self.date - timedelta(days=1)
		tomorrow = self.date + timedelta(days=1)
		
		#Checking if the assign is two sequence nights.
		if self.ShiftType == 0:
			nightBefore = PreparingSchedule.query(PreparingSchedule.date == yesterday, PreparingSchedule.ShiftType == 0,PreparingSchedule.nurseUserName == self.nurseUserName ).get()
			nightAfter = PreparingSchedule.query(PreparingSchedule.date == tomorrow, PreparingSchedule.ShiftType == 0,PreparingSchedule.nurseUserName == self.nurseUserName ).get()
			
			if nightBefore or nightAfter:
				return False
		return True
	
	
	@classmethod	
	def checkLegalAssign_Noon_Morning_Night(self):
		twoDaysAgo = self.date - timedelta(days=2)
		yesterday = self.date - timedelta(days=1)
		tomorrow = self.date + timedelta(days=1)
		dayAfterTomorrow = self.date + timedelta(days=2)
		
		# night, shift if towDaysAgo noon and yesterday morning, Illegal!
		if self.ShiftType == 0: 
			noonCheck = PreparingSchedule.query(PreparingSchedule.date == twoDaysAgo, PreparingSchedule.ShiftType == 2,PreparingSchedule.nurseUserName == self.nurseUserName ).get()
			morningCheck = PreparingSchedule.query(PreparingSchedule.date == yesterday, PreparingSchedule.ShiftType == 1,PreparingSchedule.nurseUserName == self.nurseUserName ).get()
			
			if noonCheck or morningCheck:
				return False
			return True
				
		# morning shift, if yesterday noon and tomorrow night, Illegal!
		if self.ShiftType == 1: 
			noonCheck = PreparingSchedule.query(PreparingSchedule.date == yesterday, PreparingSchedule.ShiftType == 2,PreparingSchedule.nurseUserName == self.nurseUserName ).get()
			nightCheck = PreparingSchedule.query(PreparingSchedule.date == tomorrow, PreparingSchedule.ShiftType == 0,PreparingSchedule.nurseUserName == self.nurseUserName ).get()
			
			if noonCheck or nightCheck:
				return False	
			return True
			
		# noon shift, if tomorrow morning and dayAfterTomorrow night, Illegal!	
		if self.ShiftType == 2: 
			nightCheck = PreparingSchedule.query(PreparingSchedule.date == dayAfterTomorrow, PreparingSchedule.ShiftType == 0,PreparingSchedule.nurseUserName == self.nurseUserName ).get()
			morningCheck = PreparingSchedule.query(PreparingSchedule.date == tomorrow, PreparingSchedule.ShiftType == 1,PreparingSchedule.nurseUserName == self.nurseUserName ).get()
			
			if nightCheck or morningCheck:
				return False
			return True
			
	
	@classmethod
	def checkLegalAssign_Assign_Head_Nurses(self):
		NumberOfHeadNurses = PreparingSchedule.query(PreparingSchedule.rule == 0).fetch()
		
		
		if len(NumberOfHeadNurses) == 42:
			return True
		return False
	
	
	@classmethod	
	def checkLegalAssign_Following_Shifts(self):
		yesterday = self.date - timedelta(days=1)
		tomorrow = self.date + timedelta(days=1)
		
		# night shift, if noon or morning shift on same day already or noon yesterday, Illegal!
		if self.ShiftType == 0:
			noonTodayCheck = PreparingSchedule.query(PreparingSchedule.date == self.date, PreparingSchedule.ShiftType == 2,PreparingSchedule.nurseUserName == self.nurseUserName ).get()
			noonYesterdayCheck = PreparingSchedule.query(PreparingSchedule.date == yesterday, PreparingSchedule.ShiftType == 2,PreparingSchedule.nurseUserName == self.nurseUserName ).get()
			morningCheck = PreparingSchedule.query(PreparingSchedule.date == selfdate, PreparingSchedule.ShiftType == 1,PreparingSchedule.nurseUserName == self.nurseUserName ).get()
			
			if noonTodayCheck or noonYesterdayCheck or morningCheck:
				return False
			return True
			
		# morning shift, if noon or night shift on same day already, Illegal!	
		if self.ShiftType == 1:
			noonCheck = PreparingSchedule.query(PreparingSchedule.date == self.date, PreparingSchedule.ShiftType == 2,PreparingSchedule.nurseUserName == self.nurseUserName ).get()
			nightCheck = PreparingSchedule.query(PreparingSchedule.date == self.date, PreparingSchedule.ShiftType == 0,PreparingSchedule.nurseUserName == self.nurseUserName ).get()
			
			if noonCheck or nightCheck:
				return False	
			return True
			
		# noon shift, if night or morning shift on same day already or night tomorrow, Illegal!	
		if self.ShiftType == 2: 
			nightTodayCheck = PreparingSchedule.query(PreparingSchedule.date == self.date, PreparingSchedule.ShiftType == 0,PreparingSchedule.nurseUserName == self.nurseUserName ).get()
			nightTomorrowCheck = PreparingSchedule.query(PreparingSchedule.date == tomorrow, PreparingSchedule.ShiftType == 0,PreparingSchedule.nurseUserName == self.nurseUserName ).get()
			morningCheck = PreparingSchedule.query(PreparingSchedule.date == self.date, PreparingSchedule.ShiftType == 1,PreparingSchedule.nurseUserName == self.nurseUserName ).get()
			
			if nightTodayCheck or nightTomorrow or morningCheck:
				return False
			return True	
			
	
	
	
	
	
	
	
	