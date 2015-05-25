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
		html = template.render("web/templates/LoginPage.html", template_params)
		self.response.write(html)
		
		

class LoginManagerHandler(webapp2.RequestHandler):
	def get(self):
		userName = self.request.get('userName')
		password = self.request.get('password')
		employee = Employee.query(Employee.userName == userName).get()
		if not employee or not employee.checkPassword(password) or not employee.isManager:
			self.response.write("Wrong username or password or you are not manager")
			return
		
		self.response.write(json.dumps({'status':'OK'}))
		
		
class LoginEmployeeHandler(webapp2.RequestHandler):
	def get(self):
		userName = self.request.get('userName')
		passwore = self.request.get('password')
		employee = Employee.query(Employee.userName == userName).get()
		if not employee or not employee.checkPassword(password) or employee.isManager:
			self.response.write("Wrong username or password or you are manager")
			return
		
		self.response.write(json.dumps({'status':'OK'}))
		
app = webapp2.WSGIApplication([
	('/login_as__manager', LoginManagerHandler),
	('/login_as__employee', LoginEmployeeHandler),
	('/', MainHandler)
], debug=True)
