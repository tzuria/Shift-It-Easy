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
		

class LoginHandler(webapp2.RequestHandler):
	def get(self):
		userName = self.request.get('userName')
		passwore = self.request.get('password')
		employee = Employee.query(Employee.userName == userName).get()
		if not employee:
			return
		self.response.write(json.dumps({'status':'OK'}))
		
		
app = webapp2.WSGIApplication([
	('/login', LoginHandler),
	('/', MainHandler)
], debug=True)
