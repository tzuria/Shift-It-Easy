#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from google.appengine.ext.webapp import template
from models.constrain import Constrain
from models.employee import Employee
import webapp2
import json
from Dates import Dates
import time
from datetime import date
from datetime import timedelta
import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
		userName = None
		if self.request.cookies.get('our_token'):    #the cookie that should contain the access token!
			userName = Employee.checkToken(self.request.cookies.get('our_token'))

		
		template_variables = {}
		
		if userName:
			template_variables['userName'] = userName.userName
			dates =  Dates(template_variables)
			template_variables = dates.nextTwoWeeks()
				
	

			html = template.render("web/templates/ConstrainsInputPage.html", template_variables)
			self.response.write(html)
		
class AddConstrain(webapp2.RequestHandler):
	def get(self):
		constrain_date = self.request.get('constrain_date')
		if not constrain_date:
			self.response.write("Choose shift first!") 
			return

class GetConstrainsHandler(webapp2.RequestHandler):
	def get(self):
		userName = None
		if self.request.cookies.get('our_token'):    #the cookie that should contain the access token!
			userName = Employee.checkToken(self.request.cookies.get('our_token'))
	
		constrNo = Constrain.getUserConstraintsAndNotes(userName)
	
		if constrNo:
			self.response.write(json.dumps({'status':'ok','constrainAndNotes':constrNo}))
		else:
			self.response.write(json.dumps({'status':'error','constrainAndNotes':constrNo}))

class SaveConstrainsHandler(webapp2.RequestHandler):
	def get(self):
	
		userName = None
		if self.request.cookies.get('our_token'):    #the cookie that should contain the access token!
			userName = Employee.checkToken(self.request.cookies.get('our_token'))
		
		Constrain.deleteEmployeesConstrains(userName.userName)
		
		constrains = json.loads(self.request.get('constrains'))
		i = 0
		if constrains:
			for constrain in constrains:
				insertConstrain = Constrain()
				insertConstrain.employeeUN = userName.userName
				
				#calculate the date of the constrain
				day = date.today()
				day = day + timedelta(days = 14)
				if(int(day.strftime("%U"))%2 == 0):
					day = day - timedelta(days = 7)
				if i > 20:
					day = day + timedelta(days = 7)
				if day.weekday() != 6 and day.weekday() != 0:
					day = day - timedelta(days=(day.weekday()))
				
				if day.weekday() == 6:
					day = day + timedelta(days=1)
				if i == 21 or i == 28 or i == 35 or i == 0 or i == 7 or i == 14:
					day = day - timedelta(days = 1)
				if i == 23 or i ==30 or i == 37 or i == 2 or i == 9 or i == 16:
					day = day + timedelta(days = 1)
				if i == 24 or i ==31 or i == 38 or i == 3 or i == 10 or i == 17:
					day = day + timedelta(days = 2)
				if i == 25 or i ==32 or i == 39 or i == 4 or i == 11 or i == 18:
					day = day + timedelta(days = 3)
				if i == 26 or i ==33 or i == 40 or i == 5 or i == 12 or i == 19:
					day = day + timedelta(days = 4)
				if i == 27 or i ==34 or i == 41 or i == 6 or i == 13 or i == 20:
					day = day + timedelta(days = 5)
				
					
				insertConstrain.constrainDate = day
				
				#calculate the shift type
				if((i > 34) or (i> 13 and i<21)):
					insertConstrain.ShiftType = 2
				if((i>27 and i<35)or(i>6 and i<14)):
					insertConstrain.ShiftType = 1
				if((i<7)or(i<28 and i>20)):
					insertConstrain.ShiftType = 0
					
				insertConstrain.constrainKind = constrain[0]
				insertConstrain.notes = constrain[1]
				insertConstrain.put()
				
				i = i + 1
			self.response.write(json.dumps({'status':'ok'}))
			

		
		
app = webapp2.WSGIApplication([
    ('/ConstrainsInputPage', MainHandler),
	('/save_constrains', SaveConstrainsHandler),
	('/get_constrains', GetConstrainsHandler)
], debug=True)
