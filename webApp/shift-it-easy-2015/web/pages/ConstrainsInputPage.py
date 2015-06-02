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

class MainHandler(webapp2.RequestHandler):
    def get(self):
		userName = None
		if self.request.cookies.get('our_token'):    #the cookie that should contain the access token!
			userName = Employee.checkToken(self.request.cookies.get('our_token'))

		template_variables = {}
		if userName:
			template_variables['userName'] = userName.userName
		
		
		html = template.render("web/templates/ConstrainsInputPage.html", template_variables)
		self.response.write(html)
		
class AddConstrain(webapp2.RequestHandler):
	def get(self):
		constrain_date = self.request.get('constrain_date')
		if not constrain_date:
			self.response.write("Choose shift first!") 
			return
		
class saveConstrains(webapp2.RequestHandler):
	def post(self):
		userName = None
		if self.request.cookies.get('our_token'):    #the cookie that should contain the access token!
			userName = Employee.checkToken(self.request.cookies.get('our_token'))

		constrain = Constrain()
		template_variables = {}
		if userName:
			constrain.employee = userName.key.id
			
			
			
			
			
			
			
			#constrain.constrianDay = 
			#constrain.constrianWeek = 
			#constrain.ShiftType = 
			#constrain.constrainKind = 
			#constrain.notes = 
			
		constrains = self.request.get('colors')
		if not constrains:
			self.response.write("bad constrains!!") 
			return
		else:
			constrain = Constrain()
			constrain.put()
			self.response.write(json.dumps({'status':'OK'}))
		
		
app = webapp2.WSGIApplication([
    ('/ConstrainsInputPage', MainHandler),
	('/save_constrains', saveConstrains),
	
], debug=True)
