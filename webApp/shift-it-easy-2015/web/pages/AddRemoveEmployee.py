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
from models.employee import Employee
import webapp2
import json

class MainHandler(webapp2.RequestHandler):
    def get(self):
		userName = None
		if self.request.cookies.get('our_token'):    #the cookie that should contain the access token!
			userName = Employee.checkToken(self.request.cookies.get('our_token'))

		template_variables = {}
		if userName:
			template_variables['userName'] = userName.userName
		
	
		html = template.render("web/templates/AddRemoveEmployee.html", template_variables)
		self.response.write(html)
		
class RemoveEmployee(webapp2.RequestHandler):
	def get(self, args=None):
		employee_id = self.request.get('employee_id')
		if not employee_id:
			self.response.write("the id field is empty!")
			return
		
		employee = Employee.query(Employee.workerID == employee_id).get()
		
		if not employee:
			self.response.write("there is no employee with this id number!")
			return
			
		employee.key.delete()
		
		self.response.write(json.dumps({'status':'OK'}))
		

class AddEmployeeHandler(webapp2.RequestHandler):
	def get(self, args=None):
		employee_id = self.request.get('employee_id')
		firstName = self.request.get('firstName')
		lastName = self.request.get('lastName')
		appointment = self.request.get('appointment')
		username = self.request.get('username')
		password = self.request.get('password')
		shiftHead = self.request.get('shiftHead')
		
		
		if not employee_id or not firstName or not lastName or not appointment or not username or not password:
			self.response.write("one or more fields are empty!")
			return
		
		employee = Employee.query(Employee.userName == username).get()
		
		if employee:
			self.response.write('This username already exist!')
			return
			
		employee = Employee()
		employee.workerID = employee_id
		employee.firstName = firstName
		employee.lastName = lastName
		employee.userName = username
		employee.setPassword(password)
		employee.percentJob = appointment
		if shiftHead == 'true':
			employee.shiftHead = True
		if shiftHead == 'false':
			employee.shiftHead = False
			
		employee.isManager = False
		employee.put()
		
		self.response.write(json.dumps({'status':'OK'}))
		
		


app = webapp2.WSGIApplication([
	('/add_new_employee', AddEmployeeHandler),
    ('/AddRemoveEmployee', MainHandler),
	('/remove_employee', RemoveEmployee),
	('/', MainHandler)
], debug=True)
