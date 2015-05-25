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
    def get(self, args=None):
		template_params = {"args":args}
		html = template.render("web/templates/AddRemoveEmployee.html", template_params)
		self.response.write(html)
		

class AddEmployeeHandler(webapp2.RequestHandler):
	def get(self):
		employee_id = self.request.get('employee_id')
		firstName = self.request.get('firstName')
		lastName = self.request.get('lastName')
		appointment = self.request.get('appointment')
		username = self.request.get('username')
		passwore = self.request.get('password')
		
		
		if not employee_id or not firstName or not lastName or not appointment or not username or not password:
			self.response.write("one or more fields are empty!")
			return
		
		employee = Employee.query(Employee.username == username).get()
		
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
		employee.shiftHead = False
		employee.isManager = False
		employee.put()
		
		self.response.write(json.dumps({'status':'OK'}))
		
		


app = webapp2.WSGIApplication([
	('/add_new_employee', AddEmployeeHandler),
    ('/AddRemoveEmployee', MainHandler)
], debug=True)
