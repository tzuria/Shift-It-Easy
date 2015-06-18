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
from models.currentSchedule import CurrentSchedule
from models.employee import Employee
import json
import time
from Dates import Dates
from datetime import date
from datetime import timedelta
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
		userName = None
		if self.request.cookies.get('our_token'):    #the cookie that should contain the access token!
			userName = Employee.checkToken(self.request.cookies.get('our_token'))

		today = date.today()
		today = today 
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
			dates =  Dates(template_variables)
			template_variables = dates.theseTwoWeeks()

			

			#### First week ####
			
			
			sunday0date = date(sunday0.year, sunday0.month, sunday0.day)
			
			# Sunday0 night info:
			assignBeforeHead = CurrentSchedule.checkIfAssignAlready(sunday0date, 0, 0)
			assignBeforeSecond = CurrentSchedule.checkIfAssignAlready(sunday0date, 0, 1)
			assignBeforeStandBy = CurrentSchedule.checkIfAssignAlready(sunday0date, 0, 3)
			
			if assignBeforeHead:
				template_variables['Sunday0NightAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Sunday0NightAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Sunday0NightAssignBeforeStandBy'] = assignBeforeStandBy
			
			# Sunday0 morning info:	
			assignBeforeHead = CurrentSchedule.checkIfAssignAlready(sunday0date, 1, 0)
			assignBeforeSecond = CurrentSchedule.checkIfAssignAlready(sunday0date, 1, 1)
			assignBeforeStandBy = CurrentSchedule.checkIfAssignAlready(sunday0date, 1, 3)
			
			if assignBeforeHead:
				template_variables['Sunday0MorningAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Sunday0MorningAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Sunday0MorningAssignBeforeStandBy'] = assignBeforeStandBy

				
			# Sunday0 noon info:
			assignBeforeHead = CurrentSchedule.checkIfAssignAlready(sunday0date, 2, 0)
			assignBeforeSecond = CurrentSchedule.checkIfAssignAlready(sunday0date, 2, 1)
			assignBeforeStandBy = CurrentSchedule.checkIfAssignAlready(sunday0date, 2, 3)
			
			if assignBeforeHead:
				template_variables['Sunday0NoonAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Sunday0NoonAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Sunday0NoonAssignBeforeStandBy'] = assignBeforeStandBy
			
			
			
			
			monday0date = date(monday0.year, monday0.month, monday0.day)	
			
				
			# Monday0 night info:
			assignBeforeHead = CurrentSchedule.checkIfAssignAlready(monday0date, 0, 0)
			assignBeforeSecond = CurrentSchedule.checkIfAssignAlready(monday0date, 0, 1)
			assignBeforeStandBy = CurrentSchedule.checkIfAssignAlready(monday0date, 0, 3)
			
			if assignBeforeHead:
				template_variables['Monday0NightAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Monday0NightAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Monday0NightAssignBeforeStandBy'] = assignBeforeStandBy
				
			# Monday0 morning info:
			assignBeforeHead = CurrentSchedule.checkIfAssignAlready(monday0date, 1, 0)
			assignBeforeSecond = CurrentSchedule.checkIfAssignAlready(monday0date, 1, 1)
			assignBeforeStandBy = CurrentSchedule.checkIfAssignAlready(monday0date, 1, 3)
			
			if assignBeforeHead:
				template_variables['Monday0MorningAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Monday0MorningAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Monday0MorningAssignBeforeStandBy'] = assignBeforeStandBy
			
			# Monday0 noon info:		
			assignBeforeHead = CurrentSchedule.checkIfAssignAlready(monday0date, 2, 0)
			assignBeforeSecond = CurrentSchedule.checkIfAssignAlready(monday0date, 2, 1)
			assignBeforeStandBy = CurrentSchedule.checkIfAssignAlready(monday0date, 2, 3)
			
			if assignBeforeHead:
				template_variables['Monday0NoonAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Monday0NoonAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Monday0NoonAssignBeforeStandBy'] = assignBeforeStandBy
			
			

			tuesday0date = date(tuesday0.year, tuesday0.month, tuesday0.day)
			
				
			# Tuesday0 night info:
			assignBeforeHead = CurrentSchedule.checkIfAssignAlready(tuesday0date, 0, 0)
			assignBeforeSecond = CurrentSchedule.checkIfAssignAlready(tuesday0date, 0, 1)
			assignBeforeStandBy = CurrentSchedule.checkIfAssignAlready(tuesday0date, 0, 3)
			
			if assignBeforeHead:
				template_variables['Tuesday0NightAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Tuesday0NightAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Tuesday0NightAssignBeforeStandBy'] = assignBeforeStandBy
			
			# Tuesday0 morning info:
			assignBeforeHead = CurrentSchedule.checkIfAssignAlready(tuesday0date, 1, 0)
			assignBeforeSecond = CurrentSchedule.checkIfAssignAlready(tuesday0date, 1, 1)
			assignBeforeThird = CurrentSchedule.checkIfAssignAlready(tuesday0date, 1, 2)
			assignBeforeStandBy = CurrentSchedule.checkIfAssignAlready(tuesday0date, 1, 3)
			
			if assignBeforeHead:
				template_variables['Tuesday0MorningAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Tuesday0MorningAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeThird:
				template_variables['Tuesday0MorningAssignBeforeThird'] = assignBeforeThird
				
			if assignBeforeStandBy:
				template_variables['Tuesday0MorningAssignBeforeStandBy'] = assignBeforeStandBy

			# Tuesday0 noon info:
			assignBeforeHead = CurrentSchedule.checkIfAssignAlready(tuesday0date, 2, 0)
			assignBeforeSecond = CurrentSchedule.checkIfAssignAlready(tuesday0date, 2, 1)
			assignBeforeStandBy = CurrentSchedule.checkIfAssignAlready(tuesday0date, 2, 3)
			
			if assignBeforeHead:
				template_variables['Tuesday0NoonAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Tuesday0NoonAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Tuesday0NoonAssignBeforeStandBy'] = assignBeforeStandBy
			

			
			wednesday0date = date(wednesday0.year, wednesday0.month, wednesday0.day)
		
		
			# Wednesday0 night info:	
			assignBeforeHead = CurrentSchedule.checkIfAssignAlready(wednesday0date, 0, 0)
			assignBeforeSecond = CurrentSchedule.checkIfAssignAlready(wednesday0date, 0, 1)
			assignBeforeStandBy = CurrentSchedule.checkIfAssignAlready(wednesday0date, 0, 3)
			
			if assignBeforeHead:
				template_variables['Wednesday0NightAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Wednesday0NightAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Wednesday0NightAssignBeforeStandBy'] = assignBeforeStandBy
			
			# Wednesday0 morning info:
			assignBeforeHead = CurrentSchedule.checkIfAssignAlready(wednesday0date, 1, 0)
			assignBeforeSecond = CurrentSchedule.checkIfAssignAlready(wednesday0date, 1, 1)
			assignBeforeStandBy = CurrentSchedule.checkIfAssignAlready(wednesday0date, 1, 3)
			
			if assignBeforeHead:
				template_variables['Wednesday0MorningAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Wednesday0MorningAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Wednesday0MorningAssignBeforeStandBy'] = assignBeforeStandBy
			
			# Wednesday0 noon info:
			assignBeforeHead = CurrentSchedule.checkIfAssignAlready(wednesday0date, 2, 0)
			assignBeforeSecond = CurrentSchedule.checkIfAssignAlready(wednesday0date, 2, 1)
			assignBeforeStandBy = CurrentSchedule.checkIfAssignAlready(wednesday0date, 2, 3)
			
			if assignBeforeHead:
				template_variables['Wednesday0NoonAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Wednesday0NoonAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Wednesday0NoonAssignBeforeStandBy'] = assignBeforeStandBy
			
			
			
			thursday0date = date(thursday0.year, thursday0.month, thursday0.day)
				
				
			# Thursday0 night info:
			assignBeforeHead = CurrentSchedule.checkIfAssignAlready(thursday0date, 0, 0)
			assignBeforeSecond = CurrentSchedule.checkIfAssignAlready(thursday0date, 0, 1)
			assignBeforeStandBy = CurrentSchedule.checkIfAssignAlready(thursday0date, 0, 3)
			
			if assignBeforeHead:
				template_variables['Thursday0NightAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Thursday0NightAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Thursday0NightAssignBeforeStandBy'] = assignBeforeStandBy
				
			# Thursday0 morning info:
			assignBeforeHead = CurrentSchedule.checkIfAssignAlready(thursday0date, 1, 0)
			assignBeforeSecond = CurrentSchedule.checkIfAssignAlready(thursday0date, 1, 1)
			assignBeforeThird = CurrentSchedule.checkIfAssignAlready(thursday0date, 1, 2)
			assignBeforeStandBy = CurrentSchedule.checkIfAssignAlready(thursday0date, 1, 3)
			
			if assignBeforeHead:
				template_variables['Thursday0MorningAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Thursday0MorningAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeSecond:
				template_variables['Thursday0MorningAssignBeforeThird'] = assignBeforeThird
				
			if assignBeforeStandBy:
				template_variables['Thursday0MorningAssignBeforeStandBy'] = assignBeforeStandBy
			
			# Thursday0 noon info:
			assignBeforeHead = CurrentSchedule.checkIfAssignAlready(thursday0date, 2, 0)
			assignBeforeSecond = CurrentSchedule.checkIfAssignAlready(thursday0date, 2, 1)
			assignBeforeStandBy = CurrentSchedule.checkIfAssignAlready(thursday0date, 2, 3)
			
			if assignBeforeHead:
				template_variables['Thursday0NoonAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Thursday0NoonAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Thursday0NoonAssignBeforeStandBy'] = assignBeforeStandBy
			
			
			
			friday0date = date(friday0.year, friday0.month, friday0.day)
				
				
			# Friday0 night info:
			assignBeforeHead = CurrentSchedule.checkIfAssignAlready(friday0date, 0, 0)
			assignBeforeSecond = CurrentSchedule.checkIfAssignAlready(friday0date, 0, 1)
			assignBeforeStandBy = CurrentSchedule.checkIfAssignAlready(friday0date, 0, 3)
			
			if assignBeforeHead:
				template_variables['Friday0NightAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Friday0NighAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Friday0NighAssignBeforeStandBy'] = assignBeforeStandBy
			
			# Friday0 morning info:
			assignBeforeHead = CurrentSchedule.checkIfAssignAlready(friday0date, 1, 0)
			assignBeforeSecond = CurrentSchedule.checkIfAssignAlready(friday0date, 1, 1)
			assignBeforeStandBy = CurrentSchedule.checkIfAssignAlready(friday0date, 1, 3)
			
			if assignBeforeHead:
				template_variables['Friday0MorningAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Friday0MorningAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Friday0MorningAssignBeforeStandBy'] = assignBeforeStandBy

			# Friday0 noon info:
			assignBeforeHead = CurrentSchedule.checkIfAssignAlready(friday0date, 2, 0)
			assignBeforeSecond = CurrentSchedule.checkIfAssignAlready(friday0date, 2, 1)
			assignBeforeStandBy = CurrentSchedule.checkIfAssignAlready(friday0date, 2, 3)
			
			if assignBeforeHead:
				template_variables['Friday0NoonAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Friday0NoonAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Friday0NoonAssignBeforeStandBy'] = assignBeforeStandBy
			
			
			
			saturday0date = date(saturday0.year, saturday0.month, saturday0.day)
				
				
			# Saturday0 night info:
			assignBeforeHead = CurrentSchedule.checkIfAssignAlready(saturday0date, 0, 0)
			assignBeforeSecond = CurrentSchedule.checkIfAssignAlready(saturday0date, 0, 1)
			assignBeforeStandBy = CurrentSchedule.checkIfAssignAlready(saturday0date, 0, 3)
			
			if assignBeforeHead:
				template_variables['Saturday0NightAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Saturday0NightAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Saturday0NightAssignBeforeStandBy'] = assignBeforeStandBy
			
			# Saturday0 morning info:
			assignBeforeHead = CurrentSchedule.checkIfAssignAlready(saturday0date, 1, 0)
			assignBeforeSecond = CurrentSchedule.checkIfAssignAlready(saturday0date, 1, 1)
			assignBeforeStandBy = CurrentSchedule.checkIfAssignAlready(saturday0date, 1, 3)
			
			if assignBeforeHead:
				template_variables['Saturday0MorningAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Saturday0MorningAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Saturday0MorningAssignBeforeStandBy'] = assignBeforeStandBy
			
			# Saturday0 noon info:
			assignBeforeHead = CurrentSchedule.checkIfAssignAlready(saturday0date, 2, 0)
			assignBeforeSecond = CurrentSchedule.checkIfAssignAlready(saturday0date, 2, 1)
			assignBeforeStandBy = CurrentSchedule.checkIfAssignAlready(saturday0date, 2, 3)
			
			if assignBeforeHead:
				template_variables['Saturday0NoonAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Saturday0NoonAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Saturday0NoonAssignBeforeStandBy'] = assignBeforeStandBy

				
			#### Second week ####
				

			sunday1date = date(sunday1.year, sunday1.month, sunday1.day)
				
			# Sunday1 night info:
			assignBeforeHead = CurrentSchedule.checkIfAssignAlready(sunday1date, 0, 0)
			assignBeforeSecond = CurrentSchedule.checkIfAssignAlready(sunday1date, 0, 1)
			assignBeforeStandBy = CurrentSchedule.checkIfAssignAlready(sunday1date, 0, 3)
			
			if assignBeforeHead:
				template_variables['Sunday1NightAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Sunday1NightAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Sunday1NightAssignBeforeStandBy'] = assignBeforeStandBy
			
			# Sunday1 morning info:
			assignBeforeHead = CurrentSchedule.checkIfAssignAlready(sunday1date, 1, 0)
			assignBeforeSecond = CurrentSchedule.checkIfAssignAlready(sunday1date, 1, 1)
			assignBeforeStandBy = CurrentSchedule.checkIfAssignAlready(sunday1date, 1, 3)
			
			if assignBeforeHead:
				template_variables['Sunday1MorningAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Sunday1MorningAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Sunday1MorningAssignBeforeStandBy'] = assignBeforeStandBy
				
			# Sunday1 noon info:
			assignBeforeHead = CurrentSchedule.checkIfAssignAlready(sunday1date, 2, 0)
			assignBeforeSecond = CurrentSchedule.checkIfAssignAlready(sunday1date, 2, 1)
			assignBeforeStandBy = CurrentSchedule.checkIfAssignAlready(sunday1date, 2, 3)
			
			if assignBeforeHead:
				template_variables['Sunday1NoonAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Sunday1NoonAssignBeforeSecond'] = assignBeforeSecond
			
			

			monday1date = date(monday1.year, monday1.month, monday1.day)	
				
				
			# Monday1 night info:
			assignBeforeHead = CurrentSchedule.checkIfAssignAlready(monday1date, 0, 0)
			assignBeforeSecond = CurrentSchedule.checkIfAssignAlready(monday1date, 0, 1)
			assignBeforeStandBy = CurrentSchedule.checkIfAssignAlready(monday1date, 0, 3)
			
			if assignBeforeHead:
				template_variables['Monday1NightAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Monday1NightAssignBeforeSecond'] = assignBeforeSecond
			
			# Monday1 morning info:
			assignBeforeHead = CurrentSchedule.checkIfAssignAlready(monday1date, 1, 0)
			assignBeforeSecond = CurrentSchedule.checkIfAssignAlready(monday1date, 1, 1)
			assignBeforeStandBy = CurrentSchedule.checkIfAssignAlready(monday1date, 1, 3)
			
			if assignBeforeHead:
				template_variables['Monday1MorningAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Monday1MorningAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Monday1MorningAssignBeforeStandBy'] = assignBeforeStandBy
			
			# Monday1 noon info:
			assignBeforeHead = CurrentSchedule.checkIfAssignAlready(monday1date, 2, 0)
			assignBeforeSecond = CurrentSchedule.checkIfAssignAlready(monday1date, 2, 1)
			assignBeforeStandBy = CurrentSchedule.checkIfAssignAlready(monday1date, 2, 3)
			
			if assignBeforeHead:
				template_variables['Monday1NoonAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Monday1NoonAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Monday1NoonAssignBeforeStandBy'] = assignBeforeStandBy
			
			
			
			tuesday1date = date(tuesday1.year, tuesday1.month, tuesday1.day)
				
				
			# Tuesday1 night info:
			assignBeforeHead = CurrentSchedule.checkIfAssignAlready(tuesday1date, 0, 0)
			assignBeforeSecond = CurrentSchedule.checkIfAssignAlready(tuesday1date, 0, 1)
			assignBeforeStandBy = CurrentSchedule.checkIfAssignAlready(tuesday1date, 0, 3)
			
			if assignBeforeHead:
				template_variables['Tuesday1NightAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Tuesday1NightAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Tuesday1NightAssignBeforeStandBy'] = assignBeforeStandBy
			
			# Tuesday1 morning info:
			assignBeforeHead = CurrentSchedule.checkIfAssignAlready(tuesday1date, 1, 0)
			assignBeforeSecond = CurrentSchedule.checkIfAssignAlready(tuesday1date, 1, 1)
			assignBeforeThird = CurrentSchedule.checkIfAssignAlready(tuesday1date, 1, 2)
			assignBeforeStandBy = CurrentSchedule.checkIfAssignAlready(tuesday1date, 1, 3)
			
			if assignBeforeHead:
				template_variables['Tuesday1MorningAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Tuesday1MorningAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeThird:
				template_variables['Tuesday1MorningAssignBeforeThird'] = assignBeforeThird
				
			if assignBeforeStandBy:
				template_variables['Tuesday1MorningAssignBeforeStandBy'] = assignBeforeStandBy
			
			# Tuesday1 noon info:
			assignBeforeHead = CurrentSchedule.checkIfAssignAlready(tuesday1date, 2, 0)
			assignBeforeSecond = CurrentSchedule.checkIfAssignAlready(tuesday1date, 2, 1)
			assignBeforeStandBy = CurrentSchedule.checkIfAssignAlready(tuesday1date, 2, 3)
			
			if assignBeforeHead:
				template_variables['Tuesday1NoonAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Tuesday1NoonAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Tuesday1NoonAssignBeforeStandBy'] = assignBeforeStandBy
			
			
			
			wednesday1date = date(wednesday1.year, wednesday1.month, wednesday1.day)
			
			
			# Wednesday1 night info:
			assignBeforeHead = CurrentSchedule.checkIfAssignAlready(wednesday1date, 0, 0)
			assignBeforeSecond = CurrentSchedule.checkIfAssignAlready(wednesday1date, 0, 1)
			assignBeforeStandBy = CurrentSchedule.checkIfAssignAlready(wednesday1date, 0, 3)
			
			if assignBeforeHead:
				template_variables['Wednesday1NightAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Wednesday1NightAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Wednesday1NightAssignBeforeStandBy'] = assignBeforeStandBy
			
			# Wednesday1 morning info:
			assignBeforeHead = CurrentSchedule.checkIfAssignAlready(wednesday1date, 1, 0)
			assignBeforeSecond = CurrentSchedule.checkIfAssignAlready(wednesday1date, 1, 1)
			assignBeforeStandBy = CurrentSchedule.checkIfAssignAlready(wednesday1date, 1, 3)
			
			if assignBeforeHead:
				template_variables['Wednesday1MorningAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Wednesday1MorningAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Wednesday1MorningAssignBeforeStandBy'] = assignBeforeStandBy
			
			# Wednesday1 noon info:
			assignBeforeHead = CurrentSchedule.checkIfAssignAlready(wednesday1date, 2, 0)
			assignBeforeSecond = CurrentSchedule.checkIfAssignAlready(wednesday1date, 2, 1)
			assignBeforeStandBy = CurrentSchedule.checkIfAssignAlready(wednesday1date, 2, 3)
			
			if assignBeforeHead:
				template_variables['Wednesday1NoonAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Wednesday1NoonAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Wednesday1NoonAssignBeforeStandBy'] = assignBeforeStandBy
			

			thursday1date = date(thursday1.year, thursday1.month, thursday1.day)
				
				
			# Thursday1 night info:
			assignBeforeHead = CurrentSchedule.checkIfAssignAlready(thursday1date, 0, 0)
			assignBeforeSecond = CurrentSchedule.checkIfAssignAlready(thursday1date, 0, 1)
			assignBeforeStandBy = CurrentSchedule.checkIfAssignAlready(thursday1date, 0, 3)
			
			if assignBeforeHead:
				template_variables['Thursday1NightAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Thursday1NightAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Thursday1NightAssignBeforeStandBy'] = assignBeforeStandBy
			
			# Thursday1 morning info:
			assignBeforeHead = CurrentSchedule.checkIfAssignAlready(thursday1date, 1, 0)
			assignBeforeSecond = CurrentSchedule.checkIfAssignAlready(thursday1date, 1, 1)
			assignBeforeThird = CurrentSchedule.checkIfAssignAlready(thursday1date, 1, 2)
			assignBeforeStandBy = CurrentSchedule.checkIfAssignAlready(thursday1date, 1, 3)
			
			if assignBeforeHead:
				template_variables['Thursday1MorningAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Thursday1MorningAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeSecond:
				template_variables['Thursday1MorningAssignBeforeThird'] = assignBeforeThird
				
			if assignBeforeStandBy:
				template_variables['Thursday1MorningAssignBeforeStandBy'] = assignBeforeStandBy
			
			# Thursday1 noon info:
			assignBeforeHead = CurrentSchedule.checkIfAssignAlready(thursday1date, 2, 0)
			assignBeforeSecond = CurrentSchedule.checkIfAssignAlready(thursday1date, 2, 1)
			assignBeforeStandBy = CurrentSchedule.checkIfAssignAlready(thursday1date, 2, 3)
			
			if assignBeforeHead:
				template_variables['Thursday1NoonAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Thursday1NoonAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Thursday1NoonAssignBeforeStandBy'] = assignBeforeStandBy
			
			

			friday1date = date(friday1.year, friday1.month, friday1.day)
				
				
			# Friday1 night info:
			assignBeforeHead = CurrentSchedule.checkIfAssignAlready(friday1date, 0, 0)
			assignBeforeSecond = CurrentSchedule.checkIfAssignAlready(friday1date, 0, 1)
			assignBeforeStandBy = CurrentSchedule.checkIfAssignAlready(friday1date, 0, 3)
			
			if assignBeforeHead:
				template_variables['Friday1NightAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Friday1NighAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Friday1NighAssignBeforeStandBy'] = assignBeforeStandBy
			
			# Friday1 morning info:
			assignBeforeHead = CurrentSchedule.checkIfAssignAlready(friday1date, 1, 0)
			assignBeforeSecond = CurrentSchedule.checkIfAssignAlready(friday1date, 1, 1)
			assignBeforeStandBy = CurrentSchedule.checkIfAssignAlready(friday1date, 1, 3)
			
			if assignBeforeHead:
				template_variables['Friday1MorningAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Friday1MorningAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Friday1MorningAssignBeforeStandBy'] = assignBeforeStandBy
			
			# Friday1 noon info:
			assignBeforeHead = CurrentSchedule.checkIfAssignAlready(friday1date, 2, 0)
			assignBeforeSecond = CurrentSchedule.checkIfAssignAlready(friday1date, 2, 1)
			assignBeforeStandBy = CurrentSchedule.checkIfAssignAlready(friday1date, 2, 3)
			
			if assignBeforeHead:
				template_variables['Friday1NoonAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Friday1NoonAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Friday1NoonAssignBeforeStandBy'] = assignBeforeStandBy
			
			
			
			saturday1date = date(saturday1.year, saturday1.month, saturday1.day)	
				
				
			# Saturday1 night info:
			assignBeforeHead = CurrentSchedule.checkIfAssignAlready(saturday1date, 0, 0)
			assignBeforeSecond = CurrentSchedule.checkIfAssignAlready(saturday1date, 0, 1)
			assignBeforeStandBy = CurrentSchedule.checkIfAssignAlready(saturday1date, 0, 3)
			
			if assignBeforeHead:
				template_variables['Saturday1NightAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Saturday1NightAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Saturday1NightAssignBeforeStandBy'] = assignBeforeStandBy
			
			# Saturday1 morning info:
			assignBeforeHead = CurrentSchedule.checkIfAssignAlready(saturday1date, 1, 0)
			assignBeforeSecond = CurrentSchedule.checkIfAssignAlready(saturday1date, 1, 1)
			assignBeforeStandBy = CurrentSchedule.checkIfAssignAlready(saturday1date, 1, 3)
			
			if assignBeforeHead:
				template_variables['Saturday1MorningAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Saturday1MorningAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Saturday1MorningAssignBeforeStandBy'] = assignBeforeStandBy
			
			# Saturday1 noon info:
			assignBeforeHead = CurrentSchedule.checkIfAssignAlready(saturday1date, 2, 0)
			assignBeforeSecond = CurrentSchedule.checkIfAssignAlready(saturday1date, 2, 1)
			assignBeforeStandBy = CurrentSchedule.checkIfAssignAlready(saturday1date, 2, 3)
			
			if assignBeforeHead:
				template_variables['Saturday1NoonAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Saturday1NoonAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Saturday1NoonAssignBeforeStandBy'] = assignBeforeStandBy
			
			
		html = template.render("web/templates/MainEmployee.html", template_variables)
		self.response.write(html)
			
		if not userName:
			html = template.render("web/templates/LoginPage.html", template_variables)
			self.response.write(html)

app = webapp2.WSGIApplication([
    ('/MainEmployee', MainHandler)
], debug=True)
