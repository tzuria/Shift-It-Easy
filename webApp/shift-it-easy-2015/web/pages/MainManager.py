#!/usr/bin/env python
#
# Copyright 2006 Google Inc.
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
from models.constrain import Constrain
import time
from datetime import date
from datetime import timedelta
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
		userName = None
		if self.request.cookies.get('our_token'):    #the cookie that should contain the access token!
			userName = Employee.checkToken(self.request.cookies.get('our_token'))
			
		today = date.today()
		today = today + timedelta(days = 14)
		if(int(today.strftime("%U"))%2 == 0):
			today = today - timedelta(days = 7)
		sunday0 = today
		monday0 = today
		tuesday0 = today
		wednesday0 = today
		thursday0 = today
		friday0 = today
		saturday0 = today
		
		if (today.weekday() == 6):
			sunday0 = today
			monday0 = sunday0 + timedelta(days=1)
			tuesday0 = monday0 + timedelta(days=1)
			wednesday0 = tuesday0 + timedelta(days = 1)
			thursday0 = wednesday0 + timedelta(days = 1)
			friday0 = thursday0 + timedelta(days = 1)
			saturday0 = friday0 + timedelta(days = 1)
			
		if (today.weekday() == 0):
			monday0 = today
			tuesday0 = monday0 + timedelta(days=1)
			wednesday0 = tuesday0 + timedelta(days = 1)
			thursday0 = wednesday0 + timedelta(days = 1)
			friday0 = thursday0 + timedelta(days = 1)
			saturday0 = friday0 + timedelta(days = 1)
			sunday0 = saturday0 - timedelta(days = 6)
			
		if (today.weekday() == 1):
			tuesday0 = today
			wednesday0 = tuesday0 + timedelta(days = 1)
			thursday0 = wednesday0 + timedelta(days = 1)
			friday0 = thursday0 + timedelta(days = 1)
			saturday0 = friday0 + timedelta(days = 1)
			sunday0 = saturday0 - timedelta(days = 6)
			monday0 = sunday0 + timedelta(days=1)
			
		if (today.weekday() == 2):
			wednesday0 = today
			thursday0 = wednesday0 + timedelta(days = 1)
			friday0 = thursday0 + timedelta(days = 1)
			saturday0 = friday0 + timedelta(days = 1)
			sunday0 = saturday0 - timedelta(days = 6)
			monday0 = sunday0 + timedelta(days=1)
			tuesday0 = monday0 + timedelta(days=1)
			
		if (today.weekday() == 3):
			thursday0 = today
			friday0 = thursday0 + timedelta(days = 1)
			saturday0 = friday0 + timedelta(days = 1)
			sunday0 = saturday0 - timedelta(days = 6)
			monday0 = sunday0 + timedelta(days=1)
			tuesday0 = monday0 + timedelta(days=1)
			wednesday0 = tuesday0 + timedelta(days = 1)
			
		if (today.weekday() == 4):
			friday0 = today
			saturday0 = friday0 + timedelta(days = 1)
			sunday0 = saturday0 - timedelta(days = 6)
			monday0 = sunday0 + timedelta(days=1)
			tuesday0 = monday0 + timedelta(days=1)
			wednesday0 = tuesday0 + timedelta(days = 1)
			thursday0 = wednesday0 + timedelta(days = 1)
			
		if (today.weekday() == 5):
			saturday0 = today
			sunday0 = saturday0 - timedelta(days = 6)
			monday0 = sunday0 + timedelta(days=1)
			tuesday0 = monday0 + timedelta(days=1)
			wednesday0 = tuesday0 + timedelta(days = 1)
			thursday0 = wednesday0 + timedelta(days = 1)
			friday0 = thursday0 + timedelta(days = 1)		
		
		if saturday0:
			sunday1 = saturday0 + timedelta(days=1)
			monday1 = saturday0 + timedelta(days=2)
			tuesday1 = saturday0 + timedelta(days=3)
			wednesday1 = saturday0 + timedelta(days=4)
			thursday1 = saturday0 + timedelta(days=5)
			friday1 = saturday0 + timedelta(days=6)
			saturday1 = saturday0 + timedelta(days=7)
		
		template_variables = {}
		
		if userName:
			template_variables['userName'] = userName.userName
			template_variables['sunday0'] = "%d/%d"%(sunday0.day ,sunday0.month)
			template_variables['monday0'] = "%d/%d"%(monday0.day ,monday0.month)
			template_variables['tuesday0'] = "%d/%d"%(tuesday0.day ,tuesday0.month)
			template_variables['wednesday0'] = "%d/%d"%(wednesday0.day ,wednesday0.month)
			template_variables['thursday0'] = "%d/%d"%(thursday0.day ,thursday0.month)
			template_variables['friday0'] = "%d/%d"%(friday0.day ,friday0.month)
			template_variables['saturday0'] = "%d/%d"%(saturday0.day ,saturday0.month)
			template_variables['sunday1'] = "%d/%d"%(sunday1.day ,sunday1.month)
			template_variables['monday1'] = "%d/%d"%(monday1.day ,monday1.month)
			template_variables['tuesday1'] = "%d/%d"%(tuesday1.day ,tuesday1.month)
			template_variables['wednesday1'] = "%d/%d"%(wednesday1.day ,wednesday1.month)
			template_variables['thursday1'] = "%d/%d"%(thursday1.day ,thursday1.month)
			template_variables['friday1'] = "%d/%d"%(friday1.day ,friday1.month)
			template_variables['saturday1'] = "%d/%d"%(saturday1.day ,saturday1.month)
			
			#Sunday0 night info:
			head_nurse_want = Constrain.getShiftHeads(sunday0.day,(int(sunday0.strftime("%U"))), 0, 1)
			head_nurse_dont_care = Constrain.getShiftHeads(sunday0.day,(int(sunday0.strftime("%U"))), 0, 0)
			head_nurse_prefer_not = Constrain.getShiftHeads(sunday0.day,(int(sunday0.strftime("%U"))), 0, 2)
			head_nurse_cant = Constrain.getShiftHeads(sunday0.day,(int(sunday0.strftime("%U"))), 0, 3)
			
			want = Constrain.getCrew(sunday0.day,(int(sunday0.strftime("%U"))), 0, 1)
			dont_care = Constrain.getCrew(sunday0.day,(int(sunday0.strftime("%U"))), 0, 0)
			prefer_not = Constrain.getCrew(sunday0.day,(int(sunday0.strftime("%U"))), 0, 2)
			cant = Constrain.getCrew(sunday0.day,(int(sunday0.strftime("%U"))), 0, 3)
			
			if head_nurse_want:
				template_variables['HeadNurseWhoWantSunday0'] = head_nurse_want
				
			if head_nurse_dont_care:
				template_variables['HeadNurseWhoDontCareSunday0Night'] = head_nurse_dont_care
				
			if head_nurse_prefer_not:
				template_variables['HeadNurseWhoPreferNotSunday0Night'] = head_nurse_prefer_not
				
			if head_nurse_cant:
				template_variables['HeadNurseWhoCantSunday0Night'] = head_nurse_cant
				
			if want:
				template_variables['NurseWhoWantSunday0Night'] = want
				
			if dont_care:
				template_variables['NurseWhoDontCareSunday0Night'] = dont_care
				
			if prefer_not:
				template_variables['NurseWhoPreferNotSunday0Night'] = prefer_not
				
			if cant:
				template_variables['NurseWhoCantSunday0Night'] = cant
				
			#Sunday0 morning info:
			head_nurse_want = Constrain.getShiftHeads(monday0.day,(int(monday0.strftime("%U"))), 1, 1)
			head_nurse_dont_care = Constrain.getShiftHeads(monday0.day,(int(monday0.strftime("%U"))), 1, 0)
			head_nurse_prefer_not = Constrain.getShiftHeads(monday0.day,(int(monday0.strftime("%U"))), 1, 2)
			head_nurse_cant = Constrain.getShiftHeads(monday0.day,(int(monday0.strftime("%U"))), 1, 3)
			
			want = Constrain.getCrew(sunday0.day,(int(sunday0.strftime("%U"))), 1, 1)
			dont_care = Constrain.getCrew(sunday0.day,(int(sunday0.strftime("%U"))), 1, 0)
			prefer_not = Constrain.getCrew(sunday0.day,(int(sunday0.strftime("%U"))), 1, 2)
			cant = Constrain.getCrew(sunday0.day,(int(sunday0.strftime("%U"))), 1, 3)
			
			if head_nurse_want:
				template_variables['HeadNurseWhoWant'] = head_nurse_want
				
			if head_nurse_dont_care:
				template_variables['HeadNurseWhoDontCare'] = head_nurse_dont_care
				
			if head_nurse_prefer_not:
				template_variables['HeadNurseWhoPreferNot'] = head_nurse_prefer_not
				
			if head_nurse_cant:
				template_variables['HeadNurseWhoCant'] = head_nurse_cant
				
			if want:
				template_variables['NurseWhoWant'] = want
				
			if dont_care:
				template_variables['NurseWhoDontCare'] = dont_care
				
			if prefer_not:
				template_variables['NurseWhoPreferNot'] = prefer_not
				
			if cant:
				template_variables['NurseWhoCant'] = cant
			
			html = template.render("web/templates/MainManager.html", template_variables)
			self.response.write(html)
		
		if not userName:
			html = template.render("web/templates/LoginPage.html", template_variables)
			self.response.write(html)
		

app = webapp2.WSGIApplication([
    ('/MainManager', MainHandler)
], debug=True)
