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
from models.preparingSchdule import PreparingSchedule
from models.submittedShifts import SubmittedShifts
import json
import time
from datetime import date
from datetime import timedelta
from Dates import Dates
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
			
			
			#### First week ####
			
			
			sunday0date = dates.createDateObject(0,1)
			monday0date = dates.createDateObject(0,2)
			tuesday0date = dates.createDateObject(0,3)
			wednesday0date = dates.createDateObject(0,4)
			thursday0date = dates.createDateObject(0,5)
			friday0date = dates.createDateObject(0,6)
			saturday0date = dates.createDateObject(0,7)
			
			sunday1date = dates.createDateObject(1,1)
			monday1date = dates.createDateObject(1,2)
			tuesday1date = dates.createDateObject(1,3)
			wednesday1date = dates.createDateObject(1,4)
			thursday1date = dates.createDateObject(1,5)
			friday1date = dates.createDateObject(1,6)
			saturday1date = dates.createDateObject(1,7)
			
			
			# Add default "white" constrains to employees who hasn't added constrains on their side.
			employees = Employee.query().fetch()
			if employees:
				for e in employees:
					constrains = Constrain.query(Constrain.employeeUN == e.userName).fetch()
					if not constrains:
						Constrain.addConstrains(e.userName,sunday0date)
			
			
			# Sunday0 night info:
			head_nurse_want = Constrain.getShiftHeads(sunday0date, 0, 1)
			head_nurse_dont_care = Constrain.getShiftHeads(sunday0date, 0, 0)
			head_nurse_prefer_not = Constrain.getShiftHeads(sunday0date, 0, 2)
			head_nurse_cant = Constrain.getShiftHeads(sunday0date, 0, 3)
			
			want = Constrain.getCrew(sunday0date, 0, 1)
			dont_care = Constrain.getCrew(sunday0date, 0, 0)
			prefer_not = Constrain.getCrew(sunday0date, 0, 2)
			cant = Constrain.getCrew(sunday0date, 0, 3)
			
			assignBeforeHead = PreparingSchedule.checkIfAssignAlready(sunday0date, 0, 0)
			assignBeforeSecond = PreparingSchedule.checkIfAssignAlready(sunday0date, 0, 1)
			assignBeforeStandBy = PreparingSchedule.checkIfAssignAlready(sunday0date, 0, 3)
			
			if assignBeforeHead:
				template_variables['Sunday0NightAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Sunday0NightAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Sunday0NightAssignBeforeStandBy'] = assignBeforeStandBy
			
			if head_nurse_want:
				template_variables['HeadNurseWhoWantSunday0Night'] = head_nurse_want
				
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
			

			
			# Sunday0 morning info:
			head_nurse_want = Constrain.getShiftHeads(sunday0date, 1, 1)
			head_nurse_dont_care = Constrain.getShiftHeads(sunday0date, 1, 0)
			head_nurse_prefer_not = Constrain.getShiftHeads(sunday0date, 1, 2)
			head_nurse_cant = Constrain.getShiftHeads(sunday0date, 1, 3)
			
			want = Constrain.getCrew(sunday0date, 1, 1)
			dont_care = Constrain.getCrew(sunday0date, 1, 0)
			prefer_not = Constrain.getCrew(sunday0date, 1, 2)
			cant = Constrain.getCrew(sunday0date, 1, 3)
			
			assignBeforeHead = PreparingSchedule.checkIfAssignAlready(sunday0date, 1, 0)
			assignBeforeSecond = PreparingSchedule.checkIfAssignAlready(sunday0date, 1, 1)
			assignBeforeStandBy = PreparingSchedule.checkIfAssignAlready(sunday0date, 1, 3)
			
			if assignBeforeHead:
				template_variables['Sunday0MorningAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Sunday0MorningAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Sunday0MorningAssignBeforeStandBy'] = assignBeforeStandBy
			
			if head_nurse_want:
				template_variables['HeadNurseWhoWantSunday0Morning'] = head_nurse_want
				
			if head_nurse_dont_care:
				template_variables['HeadNurseWhoDontCareSunday0Morning'] = head_nurse_dont_care
				
			if head_nurse_prefer_not:
				template_variables['HeadNurseWhoPreferNotSunday0Morning'] = head_nurse_prefer_not
				
			if head_nurse_cant:
				template_variables['HeadNurseWhoCantSunday0Morning'] = head_nurse_cant
				
			if want:
				template_variables['NurseWhoWantSunday0Morning'] = want
				
			if dont_care:
				template_variables['NurseWhoDontCareSunday0Morning'] = dont_care
				
			if prefer_not:
				template_variables['NurseWhoPreferNotSunday0Morning'] = prefer_not
				
			if cant:
				template_variables['NurseWhoCantSunday0Morning'] = cant
				
			
			
			# Sunday0 noon info:
			head_nurse_want = Constrain.getShiftHeads(sunday0date, 2, 1)
			head_nurse_dont_care = Constrain.getShiftHeads(sunday0date, 2, 0)
			head_nurse_prefer_not = Constrain.getShiftHeads(sunday0date, 2, 2)
			head_nurse_cant = Constrain.getShiftHeads(sunday0date, 2, 3)
			
			want = Constrain.getCrew(sunday0date, 2, 1)
			dont_care = Constrain.getCrew(sunday0date, 2, 0)
			prefer_not = Constrain.getCrew(sunday0date, 2, 2)
			cant = Constrain.getCrew(sunday0date, 2, 3)
			
			assignBeforeHead = PreparingSchedule.checkIfAssignAlready(sunday0date, 2, 0)
			assignBeforeSecond = PreparingSchedule.checkIfAssignAlready(sunday0date, 2, 1)
			assignBeforeStandBy = PreparingSchedule.checkIfAssignAlready(sunday0date, 2, 3)
			
			if assignBeforeHead:
				template_variables['Sunday0NoonAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Sunday0NoonAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Sunday0NoonAssignBeforeStandBy'] = assignBeforeStandBy
			
			if head_nurse_want:
				template_variables['HeadNurseWhoWantSunday0Noon'] = head_nurse_want
				
			if head_nurse_dont_care:
				template_variables['HeadNurseWhoDontCareSunday0Noon'] = head_nurse_dont_care
				
			if head_nurse_prefer_not:
				template_variables['HeadNurseWhoPreferNotSunday0Noon'] = head_nurse_prefer_not
				
			if head_nurse_cant:
				template_variables['HeadNurseWhoCantSunday0Noon'] = head_nurse_cant
				
			if want:
				template_variables['NurseWhoWantSunday0Noon'] = want
				
			if dont_care:
				template_variables['NurseWhoDontCareSunday0Noon'] = dont_care
				
			if prefer_not:
				template_variables['NurseWhoPreferNotSunday0Noon'] = prefer_not
				
			if cant:
				template_variables['NurseWhoCantSunday0Noon'] = cant
			
	
				
			# Monday0 night info:
			head_nurse_want = Constrain.getShiftHeads(monday0date, 0, 1)
			head_nurse_dont_care = Constrain.getShiftHeads(monday0date, 0, 0)
			head_nurse_prefer_not = Constrain.getShiftHeads(monday0date, 0, 2)
			head_nurse_cant = Constrain.getShiftHeads(monday0date, 0, 3)
			
			want = Constrain.getCrew(monday0date, 0, 1)
			dont_care = Constrain.getCrew(monday0date, 0, 0)
			prefer_not = Constrain.getCrew(monday0date, 0, 2)
			cant = Constrain.getCrew(monday0date, 0, 3)
			
			assignBeforeHead = PreparingSchedule.checkIfAssignAlready(monday0date, 0, 0)
			assignBeforeSecond = PreparingSchedule.checkIfAssignAlready(monday0date, 0, 1)
			assignBeforeStandBy = PreparingSchedule.checkIfAssignAlready(monday0date, 0, 3)
			
			if assignBeforeHead:
				template_variables['Monday0NightAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Monday0NightAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Monday0NightAssignBeforeStandBy'] = assignBeforeStandBy
			
			if head_nurse_want:
				template_variables['HeadNurseWhoWantMonday0Night'] = head_nurse_want
				
			if head_nurse_dont_care:
				template_variables['HeadNurseWhoDontCareMonday0Night'] = head_nurse_dont_care
				
			if head_nurse_prefer_not:
				template_variables['HeadNurseWhoPreferNotMonday0Night'] = head_nurse_prefer_not
				
			if head_nurse_cant:
				template_variables['HeadNurseWhoCantMonday0Night'] = head_nurse_cant
				
			if want:
				template_variables['NurseWhoWantMonday0Night'] = want
				
			if dont_care:
				template_variables['NurseWhoDontCareMonday0Night'] = dont_care
				
			if prefer_not:
				template_variables['NurseWhoPreferNotMonday0Night'] = prefer_not
				
			if cant:
				template_variables['NurseWhoCantMonday0Night'] = cant
			

			
			# Monday0 morning info:
			head_nurse_want = Constrain.getShiftHeads(monday0date, 1, 1)
			head_nurse_dont_care = Constrain.getShiftHeads(monday0date, 1, 0)
			head_nurse_prefer_not = Constrain.getShiftHeads(monday0date, 1, 2)
			head_nurse_cant = Constrain.getShiftHeads(monday0date, 1, 3)
			
			want = Constrain.getCrew(monday0date, 1, 1)
			dont_care = Constrain.getCrew(monday0date, 1, 0)
			prefer_not = Constrain.getCrew(monday0date, 1, 2)
			cant = Constrain.getCrew(monday0date, 1, 3)
			
			assignBeforeHead = PreparingSchedule.checkIfAssignAlready(monday0date, 1, 0)
			assignBeforeSecond = PreparingSchedule.checkIfAssignAlready(monday0date, 1, 1)
			assignBeforeStandBy = PreparingSchedule.checkIfAssignAlready(monday0date, 1, 3)
			
			if assignBeforeHead:
				template_variables['Monday0MorningAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Monday0MorningAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Monday0MorningAssignBeforeStandBy'] = assignBeforeStandBy
			
			if head_nurse_want:
				template_variables['HeadNurseWhoWantMonday0Morning'] = head_nurse_want
				
			if head_nurse_dont_care:
				template_variables['HeadNurseWhoDontCareMonday0Morning'] = head_nurse_dont_care
				
			if head_nurse_prefer_not:
				template_variables['HeadNurseWhoPreferNotMonday0Morning'] = head_nurse_prefer_not
				
			if head_nurse_cant:
				template_variables['HeadNurseWhoCantMonday0Morning'] = head_nurse_cant
				
			if want:
				template_variables['NurseWhoWantMonday0Morning'] = want
				
			if dont_care:
				template_variables['NurseWhoDontCareMonday0Morning'] = dont_care
				
			if prefer_not:
				template_variables['NurseWhoPreferNotMonday0Morning'] = prefer_not
				
			if cant:
				template_variables['NurseWhoCantMonday0Morning'] = cant
				
			
			
			# Monday0 noon info:
			head_nurse_want = Constrain.getShiftHeads(monday0date, 2, 1)
			head_nurse_dont_care = Constrain.getShiftHeads(monday0date, 2, 0)
			head_nurse_prefer_not = Constrain.getShiftHeads(monday0date, 2, 2)
			head_nurse_cant = Constrain.getShiftHeads(monday0date, 2, 3)
			
			want = Constrain.getCrew(monday0date, 2, 1)
			dont_care = Constrain.getCrew(monday0date, 2, 0)
			prefer_not = Constrain.getCrew(monday0date, 2, 2)
			cant = Constrain.getCrew(monday0date, 2, 3)
			
			assignBeforeHead = PreparingSchedule.checkIfAssignAlready(monday0date, 2, 0)
			assignBeforeSecond = PreparingSchedule.checkIfAssignAlready(monday0date, 2, 1)
			assignBeforeStandBy = PreparingSchedule.checkIfAssignAlready(monday0date, 2, 3)
			
			if assignBeforeHead:
				template_variables['Monday0NoonAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Monday0NoonAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Monday0NoonAssignBeforeStandBy'] = assignBeforeStandBy
			
			if head_nurse_want:
				template_variables['HeadNurseWhoWantMonday0Noon'] = head_nurse_want
				
			if head_nurse_dont_care:
				template_variables['HeadNurseWhoDontCareMonday0Noon'] = head_nurse_dont_care
				
			if head_nurse_prefer_not:
				template_variables['HeadNurseWhoPreferNotMonday0Noon'] = head_nurse_prefer_not
				
			if head_nurse_cant:
				template_variables['HeadNurseWhoCantMonday0Noon'] = head_nurse_cant
				
			if want:
				template_variables['NurseWhoWantMonday0Noon'] = want
				
			if dont_care:
				template_variables['NurseWhoDontCareMonday0Noon'] = dont_care
				
			if prefer_not:
				template_variables['NurseWhoPreferNotMonday0Noon'] = prefer_not
				
			if cant:
				template_variables['NurseWhoCantMonday0Noon'] = cant
				
			
				
			# Tuesday0 night info:
			head_nurse_want = Constrain.getShiftHeads(tuesday0date, 0, 1)
			head_nurse_dont_care = Constrain.getShiftHeads(tuesday0date, 0, 0)
			head_nurse_prefer_not = Constrain.getShiftHeads(tuesday0date, 0, 2)
			head_nurse_cant = Constrain.getShiftHeads(tuesday0date, 0, 3)
			
			want = Constrain.getCrew(tuesday0date, 0, 1)
			dont_care = Constrain.getCrew(tuesday0date, 0, 0)
			prefer_not = Constrain.getCrew(tuesday0date, 0, 2)
			cant = Constrain.getCrew(tuesday0date, 0, 3)
			
			assignBeforeHead = PreparingSchedule.checkIfAssignAlready(tuesday0date, 0, 0)
			assignBeforeSecond = PreparingSchedule.checkIfAssignAlready(tuesday0date, 0, 1)
			assignBeforeStandBy = PreparingSchedule.checkIfAssignAlready(tuesday0date, 0, 3)
			
			if assignBeforeHead:
				template_variables['Tuesday0NightAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Tuesday0NightAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Tuesday0NightAssignBeforeStandBy'] = assignBeforeStandBy
			
			if head_nurse_want:
				template_variables['HeadNurseWhoWantTuesday0Night'] = head_nurse_want
				
			if head_nurse_dont_care:
				template_variables['HeadNurseWhoDontCareTuesday0Night'] = head_nurse_dont_care
				
			if head_nurse_prefer_not:
				template_variables['HeadNurseWhoPreferNotTuesday0Night'] = head_nurse_prefer_not
				
			if head_nurse_cant:
				template_variables['HeadNurseWhoCantTuesday0Night'] = head_nurse_cant
				
			if want:
				template_variables['NurseWhoWantTuesday0Night'] = want
				
			if dont_care:
				template_variables['NurseWhoDontCareTuesday0Night'] = dont_care
				
			if prefer_not:
				template_variables['NurseWhoPreferNotTuesday0Night'] = prefer_not
				
			if cant:
				template_variables['NurseWhoCantTuesday0Night'] = cant
			

			
			# Tuesday0 morning info:
			head_nurse_want = Constrain.getShiftHeads(tuesday0date, 1, 1)
			head_nurse_dont_care = Constrain.getShiftHeads(tuesday0date, 1, 0)
			head_nurse_prefer_not = Constrain.getShiftHeads(tuesday0date, 1, 2)
			head_nurse_cant = Constrain.getShiftHeads(tuesday0date, 1, 3)
			
			want = Constrain.getCrew(tuesday0date, 1, 1)
			dont_care = Constrain.getCrew(tuesday0date, 1, 0)
			prefer_not = Constrain.getCrew(tuesday0date, 1, 2)
			cant = Constrain.getCrew(tuesday0date, 1, 3)
			
			assignBeforeHead = PreparingSchedule.checkIfAssignAlready(tuesday0date, 1, 0)
			assignBeforeSecond = PreparingSchedule.checkIfAssignAlready(tuesday0date, 1, 1)
			assignBeforeThird = PreparingSchedule.checkIfAssignAlready(tuesday0date, 1, 2)
			assignBeforeStandBy = PreparingSchedule.checkIfAssignAlready(tuesday0date, 1, 3)
			
			if assignBeforeHead:
				template_variables['Tuesday0MorningAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Tuesday0MorningAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeThird:
				template_variables['Tuesday0MorningAssignBeforeThird'] = assignBeforeThird
				
			if assignBeforeStandBy:
				template_variables['Tuesday0MorningAssignBeforeStandBy'] = assignBeforeStandBy
			
			if head_nurse_want:
				template_variables['HeadNurseWhoWantTuesday0Morning'] = head_nurse_want
				
			if head_nurse_dont_care:
				template_variables['HeadNurseWhoDontCareTuesday0Morning'] = head_nurse_dont_care
				
			if head_nurse_prefer_not:
				template_variables['HeadNurseWhoPreferNotTuesday0Morning'] = head_nurse_prefer_not
				
			if head_nurse_cant:
				template_variables['HeadNurseWhoCantTuesday0Morning'] = head_nurse_cant
				
			if want:
				template_variables['NurseWhoWantTuesday0Morning'] = want
				
			if dont_care:
				template_variables['NurseWhoDontCareTuesday0Morning'] = dont_care
				
			if prefer_not:
				template_variables['NurseWhoPreferNotTuesday0Morning'] = prefer_not
				
			if cant:
				template_variables['NurseWhoCantTuesday0Morning'] = cant
			

			
			# Tuesday0 noon info:
			head_nurse_want = Constrain.getShiftHeads(tuesday0date, 2, 1)
			head_nurse_dont_care = Constrain.getShiftHeads(tuesday0date, 2, 0)
			head_nurse_prefer_not = Constrain.getShiftHeads(tuesday0date, 2, 2)
			head_nurse_cant = Constrain.getShiftHeads(tuesday0date, 2, 3)
			
			want = Constrain.getCrew(tuesday0date, 2, 1)
			dont_care = Constrain.getCrew(tuesday0date, 2, 0)
			prefer_not = Constrain.getCrew(tuesday0date, 2, 2)
			cant = Constrain.getCrew(tuesday0date, 2, 3)
			
			assignBeforeHead = PreparingSchedule.checkIfAssignAlready(tuesday0date, 2, 0)
			assignBeforeSecond = PreparingSchedule.checkIfAssignAlready(tuesday0date, 2, 1)
			assignBeforeStandBy = PreparingSchedule.checkIfAssignAlready(tuesday0date, 2, 3)
			
			if assignBeforeHead:
				template_variables['Tuesday0NoonAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Tuesday0NoonAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Tuesday0NoonAssignBeforeStandBy'] = assignBeforeStandBy
			
			if head_nurse_want:
				template_variables['HeadNurseWhoWantTuesday0Noon'] = head_nurse_want
				
			if head_nurse_dont_care:
				template_variables['HeadNurseWhoDontCareTuesday0Noon'] = head_nurse_dont_care
				
			if head_nurse_prefer_not:
				template_variables['HeadNurseWhoPreferNotTuesday0Noon'] = head_nurse_prefer_not
				
			if head_nurse_cant:
				template_variables['HeadNurseWhoCantTuesday0Noon'] = head_nurse_cant
				
			if want:
				template_variables['NurseWhoWantTuesday0Noon'] = want
				
			if dont_care:
				template_variables['NurseWhoDontCareTuesday0Noon'] = dont_care
				
			if prefer_not:
				template_variables['NurseWhoPreferNotTuesday0Noon'] = prefer_not
				
			if cant:
				template_variables['NurseWhoCantTuesday0Noon'] = cant
				
			

				
			# Wednesday0 night info:
			head_nurse_want = Constrain.getShiftHeads(wednesday0date, 0, 1)
			head_nurse_dont_care = Constrain.getShiftHeads(wednesday0date, 0, 0)
			head_nurse_prefer_not = Constrain.getShiftHeads(wednesday0date, 0, 2)
			head_nurse_cant = Constrain.getShiftHeads(wednesday0date, 0, 3)
			
			want = Constrain.getCrew(wednesday0date, 0, 1)
			dont_care = Constrain.getCrew(wednesday0date, 0, 0)
			prefer_not = Constrain.getCrew(wednesday0date, 0, 2)
			cant = Constrain.getCrew(wednesday0date, 0, 3)
			
			assignBeforeHead = PreparingSchedule.checkIfAssignAlready(wednesday0date, 0, 0)
			assignBeforeSecond = PreparingSchedule.checkIfAssignAlready(wednesday0date, 0, 1)
			assignBeforeStandBy = PreparingSchedule.checkIfAssignAlready(wednesday0date, 0, 3)
			
			if assignBeforeHead:
				template_variables['Wednesday0NightAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Wednesday0NightAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Wednesday0NightAssignBeforeStandBy'] = assignBeforeStandBy
			
			if head_nurse_want:
				template_variables['HeadNurseWhoWantWednesday0Night'] = head_nurse_want
				
			if head_nurse_dont_care:
				template_variables['HeadNurseWhoDontCareWednesday0Night'] = head_nurse_dont_care
				
			if head_nurse_prefer_not:
				template_variables['HeadNurseWhoPreferNotWednesday0Night'] = head_nurse_prefer_not
				
			if head_nurse_cant:
				template_variables['HeadNurseWhoCantWednesday0Night'] = head_nurse_cant
				
			if want:
				template_variables['NurseWhoWantWednesday0Night'] = want
				
			if dont_care:
				template_variables['NurseWhoDontCareWednesday0Night'] = dont_care
				
			if prefer_not:
				template_variables['NurseWhoPreferNotWednesday0Night'] = prefer_not
				
			if cant:
				template_variables['NurseWhoCantWednesday0Night'] = cant
			

			
			# Wednesday0 morning info:
			head_nurse_want = Constrain.getShiftHeads(wednesday0date, 1, 1)
			head_nurse_dont_care = Constrain.getShiftHeads(wednesday0date, 1, 0)
			head_nurse_prefer_not = Constrain.getShiftHeads(wednesday0date, 1, 2)
			head_nurse_cant = Constrain.getShiftHeads(wednesday0date, 1, 3)
			
			want = Constrain.getCrew(wednesday0date, 1, 1)
			dont_care = Constrain.getCrew(wednesday0date, 1, 0)
			prefer_not = Constrain.getCrew(wednesday0date, 1, 2)
			cant = Constrain.getCrew(wednesday0date, 1, 3)
			
			assignBeforeHead = PreparingSchedule.checkIfAssignAlready(wednesday0date, 1, 0)
			assignBeforeSecond = PreparingSchedule.checkIfAssignAlready(wednesday0date, 1, 1)
			assignBeforeStandBy = PreparingSchedule.checkIfAssignAlready(wednesday0date, 1, 3)
			
			if assignBeforeHead:
				template_variables['Wednesday0MorningAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Wednesday0MorningAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Wednesday0MorningAssignBeforeStandBy'] = assignBeforeStandBy
			
			if head_nurse_want:
				template_variables['HeadNurseWhoWantWednesday0Morning'] = head_nurse_want
				
			if head_nurse_dont_care:
				template_variables['HeadNurseWhoDontCareWednesday0Morning'] = head_nurse_dont_care
				
			if head_nurse_prefer_not:
				template_variables['HeadNurseWhoPreferNotWednesday0Morning'] = head_nurse_prefer_not
				
			if head_nurse_cant:
				template_variables['HeadNurseWhoCantWednesday0Morning'] = head_nurse_cant
				
			if want:
				template_variables['NurseWhoWantWednesday0Morning'] = want
				
			if dont_care:
				template_variables['NurseWhoDontCareWednesday0Morning'] = dont_care
				
			if prefer_not:
				template_variables['NurseWhoPreferNotWednesday0Morning'] = prefer_not
				
			if cant:
				template_variables['NurseWhoCantWednesday0Morning'] = cant
				
			
			
			# Wednesday0 noon info:
			head_nurse_want = Constrain.getShiftHeads(wednesday0date, 2, 1)
			head_nurse_dont_care = Constrain.getShiftHeads(wednesday0date, 2, 0)
			head_nurse_prefer_not = Constrain.getShiftHeads(wednesday0date, 2, 2)
			head_nurse_cant = Constrain.getShiftHeads(wednesday0date, 2, 3)
			
			want = Constrain.getCrew(wednesday0date, 2, 1)
			dont_care = Constrain.getCrew(wednesday0date, 2, 0)
			prefer_not = Constrain.getCrew(wednesday0date, 2, 2)
			cant = Constrain.getCrew(wednesday0date, 2, 3)
			
			assignBeforeHead = PreparingSchedule.checkIfAssignAlready(wednesday0date, 2, 0)
			assignBeforeSecond = PreparingSchedule.checkIfAssignAlready(wednesday0date, 2, 1)
			assignBeforeStandBy = PreparingSchedule.checkIfAssignAlready(wednesday0date, 2, 3)
			
			if assignBeforeHead:
				template_variables['Wednesday0NoonAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Wednesday0NoonAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Wednesday0NoonAssignBeforeStandBy'] = assignBeforeStandBy
			
			if head_nurse_want:
				template_variables['HeadNurseWhoWantWednesday0Noon'] = head_nurse_want
				
			if head_nurse_dont_care:
				template_variables['HeadNurseWhoDontCareWednesday0Noon'] = head_nurse_dont_care
				
			if head_nurse_prefer_not:
				template_variables['HeadNurseWhoPreferNotWednesday0Noon'] = head_nurse_prefer_not
				
			if head_nurse_cant:
				template_variables['HeadNurseWhoCantWednesday0Noon'] = head_nurse_cant
				
			if want:
				template_variables['NurseWhoWantWednesday0Noon'] = want
				
			if dont_care:
				template_variables['NurseWhoDontCareWednesday0Noon'] = dont_care
				
			if prefer_not:
				template_variables['NurseWhoPreferNotWednesday0Noon'] = prefer_not
				
			if cant:
				template_variables['NurseWhoCantWednesday0Noon'] = cant
				
		
				
			# Thursday0 night info:
			head_nurse_want = Constrain.getShiftHeads(thursday0date, 0, 1)
			head_nurse_dont_care = Constrain.getShiftHeads(thursday0date, 0, 0)
			head_nurse_prefer_not = Constrain.getShiftHeads(thursday0date, 0, 2)
			head_nurse_cant = Constrain.getShiftHeads(thursday0date, 0, 3)
			
			want = Constrain.getCrew(thursday0date, 0, 1)
			dont_care = Constrain.getCrew(thursday0date, 0, 0)
			prefer_not = Constrain.getCrew(thursday0date, 0, 2)
			cant = Constrain.getCrew(thursday0date, 0, 3)
			
			assignBeforeHead = PreparingSchedule.checkIfAssignAlready(thursday0date, 0, 0)
			assignBeforeSecond = PreparingSchedule.checkIfAssignAlready(thursday0date, 0, 1)
			assignBeforeStandBy = PreparingSchedule.checkIfAssignAlready(thursday0date, 0, 3)
			
			if assignBeforeHead:
				template_variables['Thursday0NightAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Thursday0NightAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Thursday0NightAssignBeforeStandBy'] = assignBeforeStandBy
			
			if head_nurse_want:
				template_variables['HeadNurseWhoWantThursday0Night'] = head_nurse_want
				
			if head_nurse_dont_care:
				template_variables['HeadNurseWhoDontCareThursday0Night'] = head_nurse_dont_care
				
			if head_nurse_prefer_not:
				template_variables['HeadNurseWhoPreferNotThursday0Night'] = head_nurse_prefer_not
				
			if head_nurse_cant:
				template_variables['HeadNurseWhoCantThursday0Night'] = head_nurse_cant
				
			if want:
				template_variables['NurseWhoWantThursday0Night'] = want
				
			if dont_care:
				template_variables['NurseWhoDontCareThursday0Night'] = dont_care
				
			if prefer_not:
				template_variables['NurseWhoPreferNotThursday0Night'] = prefer_not
				
			if cant:
				template_variables['NurseWhoCantThursday0Night'] = cant
			

			
			# Thursday0 morning info:
			head_nurse_want = Constrain.getShiftHeads(thursday0date, 1, 1)
			head_nurse_dont_care = Constrain.getShiftHeads(thursday0date, 1, 0)
			head_nurse_prefer_not = Constrain.getShiftHeads(thursday0date, 1, 2)
			head_nurse_cant = Constrain.getShiftHeads(thursday0date, 1, 3)
			
			want = Constrain.getCrew(thursday0date, 1, 1)
			dont_care = Constrain.getCrew(thursday0date, 1, 0)
			prefer_not = Constrain.getCrew(thursday0date, 1, 2)
			cant = Constrain.getCrew(thursday0date, 1, 3)
			
			assignBeforeHead = PreparingSchedule.checkIfAssignAlready(thursday0date, 1, 0)
			assignBeforeSecond = PreparingSchedule.checkIfAssignAlready(thursday0date, 1, 1)
			assignBeforeThird = PreparingSchedule.checkIfAssignAlready(thursday0date, 1, 2)
			assignBeforeStandBy = PreparingSchedule.checkIfAssignAlready(thursday0date, 1, 3)
			
			if assignBeforeHead:
				template_variables['Thursday0MorningAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Thursday0MorningAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeSecond:
				template_variables['Thursday0MorningAssignBeforeThird'] = assignBeforeThird
				
			if assignBeforeStandBy:
				template_variables['Thursday0MorningAssignBeforeStandBy'] = assignBeforeStandBy
			
			if head_nurse_want:
				template_variables['HeadNurseWhoWantThursday0Morning'] = head_nurse_want
				
			if head_nurse_dont_care:
				template_variables['HeadNurseWhoDontCareThursday0Morning'] = head_nurse_dont_care
				
			if head_nurse_prefer_not:
				template_variables['HeadNurseWhoPreferNotThursday0Morning'] = head_nurse_prefer_not
				
			if head_nurse_cant:
				template_variables['HeadNurseWhoCantThursday0Morning'] = head_nurse_cant
				
			if want:
				template_variables['NurseWhoWantThursday0Morning'] = want
				
			if dont_care:
				template_variables['NurseWhoDontCareThursday0Morning'] = dont_care
				
			if prefer_not:
				template_variables['NurseWhoPreferNotThursday0Morning'] = prefer_not
				
			if cant:
				template_variables['NurseWhoCantThursday0Morning'] = cant
				
			
			
			# Thursday0 noon info:
			head_nurse_want = Constrain.getShiftHeads(thursday0date, 2, 1)
			head_nurse_dont_care = Constrain.getShiftHeads(thursday0date, 2, 0)
			head_nurse_prefer_not = Constrain.getShiftHeads(thursday0date, 2, 2)
			head_nurse_cant = Constrain.getShiftHeads(thursday0date, 2, 3)
			
			want = Constrain.getCrew(thursday0date, 2, 1)
			dont_care = Constrain.getCrew(thursday0date, 2, 0)
			prefer_not = Constrain.getCrew(thursday0date, 2, 2)
			cant = Constrain.getCrew(thursday0date, 2, 3)
			
			assignBeforeHead = PreparingSchedule.checkIfAssignAlready(thursday0date, 2, 0)
			assignBeforeSecond = PreparingSchedule.checkIfAssignAlready(thursday0date, 2, 1)
			assignBeforeStandBy = PreparingSchedule.checkIfAssignAlready(thursday0date, 2, 3)
			
			if assignBeforeHead:
				template_variables['Thursday0NoonAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Thursday0NoonAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Thursday0NoonAssignBeforeStandBy'] = assignBeforeStandBy
			
			if head_nurse_want:
				template_variables['HeadNurseWhoWantThursday0Noon'] = head_nurse_want
				
			if head_nurse_dont_care:
				template_variables['HeadNurseWhoDontCareThursday0Noon'] = head_nurse_dont_care
				
			if head_nurse_prefer_not:
				template_variables['HeadNurseWhoPreferNotThursday0Noon'] = head_nurse_prefer_not
				
			if head_nurse_cant:
				template_variables['HeadNurseWhoCantThursday0Noon'] = head_nurse_cant
				
			if want:
				template_variables['NurseWhoWantThursday0Noon'] = want
				
			if dont_care:
				template_variables['NurseWhoDontCareThursday0Noon'] = dont_care
				
			if prefer_not:
				template_variables['NurseWhoPreferNotThursday0Noon'] = prefer_not
				
			if cant:
				template_variables['NurseWhoCantThursday0Noon'] = cant
				
	
				
			# Friday0 night info:
			head_nurse_want = Constrain.getShiftHeads(friday0date, 0, 1)
			head_nurse_dont_care = Constrain.getShiftHeads(friday0date, 0, 0)
			head_nurse_prefer_not = Constrain.getShiftHeads(friday0date, 0, 2)
			head_nurse_cant = Constrain.getShiftHeads(friday0date, 0, 3)
			
			want = Constrain.getCrew(friday0date, 0, 1)
			dont_care = Constrain.getCrew(friday0date, 0, 0)
			prefer_not = Constrain.getCrew(friday0date, 0, 2)
			cant = Constrain.getCrew(friday0date, 0, 3)
			
			assignBeforeHead = PreparingSchedule.checkIfAssignAlready(friday0date, 0, 0)
			assignBeforeSecond = PreparingSchedule.checkIfAssignAlready(friday0date, 0, 1)
			assignBeforeStandBy = PreparingSchedule.checkIfAssignAlready(friday0date, 0, 3)
			
			if assignBeforeHead:
				template_variables['Friday0NightAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Friday0NighAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Friday0NighAssignBeforeStandBy'] = assignBeforeStandBy
			
			if head_nurse_want:
				template_variables['HeadNurseWhoWantFriday0Night'] = head_nurse_want
				
			if head_nurse_dont_care:
				template_variables['HeadNurseWhoDontCareFriday0Night'] = head_nurse_dont_care
				
			if head_nurse_prefer_not:
				template_variables['HeadNurseWhoPreferNotFriday0Night'] = head_nurse_prefer_not
				
			if head_nurse_cant:
				template_variables['HeadNurseWhoCantFriday0Night'] = head_nurse_cant
				
			if want:
				template_variables['NurseWhoWantFriday0Night'] = want
				
			if dont_care:
				template_variables['NurseWhoDontCareFriday0Night'] = dont_care
				
			if prefer_not:
				template_variables['NurseWhoPreferNotFriday0Night'] = prefer_not
				
			if cant:
				template_variables['NurseWhoCantFriday0Night'] = cant
			

			
			# Friday0 morning info:
			head_nurse_want = Constrain.getShiftHeads(friday0date, 1, 1)
			head_nurse_dont_care = Constrain.getShiftHeads(friday0date, 1, 0)
			head_nurse_prefer_not = Constrain.getShiftHeads(friday0date, 1, 2)
			head_nurse_cant = Constrain.getShiftHeads(friday0date, 1, 3)
			
			want = Constrain.getCrew(friday0date, 1, 1)
			dont_care = Constrain.getCrew(friday0date, 1, 0)
			prefer_not = Constrain.getCrew(friday0date, 1, 2)
			cant = Constrain.getCrew(friday0date, 1, 3)
			
			assignBeforeHead = PreparingSchedule.checkIfAssignAlready(friday0date, 1, 0)
			assignBeforeSecond = PreparingSchedule.checkIfAssignAlready(friday0date, 1, 1)
			assignBeforeStandBy = PreparingSchedule.checkIfAssignAlready(friday0date, 1, 3)
			
			if assignBeforeHead:
				template_variables['Friday0MorningAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Friday0MorningAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Friday0MorningAssignBeforeStandBy'] = assignBeforeStandBy
			
			if head_nurse_want:
				template_variables['HeadNurseWhoWantFriday0Morning'] = head_nurse_want
				
			if head_nurse_dont_care:
				template_variables['HeadNurseWhoDontCareFriday0Morning'] = head_nurse_dont_care
				
			if head_nurse_prefer_not:
				template_variables['HeadNurseWhoPreferNotFriday0Morning'] = head_nurse_prefer_not
				
			if head_nurse_cant:
				template_variables['HeadNurseWhoCantFriday0Morning'] = head_nurse_cant
				
			if want:
				template_variables['NurseWhoWantFriday0Morning'] = want
				
			if dont_care:
				template_variables['NurseWhoDontCareFriday0Morning'] = dont_care
				
			if prefer_not:
				template_variables['NurseWhoPreferNotFriday0Morning'] = prefer_not
				
			if cant:
				template_variables['NurseWhoCantFriday0Morning'] = cant
				
			
			
			# Friday0 noon info:
			head_nurse_want = Constrain.getShiftHeads(friday0date, 2, 1)
			head_nurse_dont_care = Constrain.getShiftHeads(friday0date, 2, 0)
			head_nurse_prefer_not = Constrain.getShiftHeads(friday0date, 2, 2)
			head_nurse_cant = Constrain.getShiftHeads(friday0date, 2, 3)
			
			want = Constrain.getCrew(friday0date, 2, 1)
			dont_care = Constrain.getCrew(friday0date, 2, 0)
			prefer_not = Constrain.getCrew(friday0date, 2, 2)
			cant = Constrain.getCrew(friday0date, 2, 3)
			
			assignBeforeHead = PreparingSchedule.checkIfAssignAlready(friday0date, 2, 0)
			assignBeforeSecond = PreparingSchedule.checkIfAssignAlready(friday0date, 2, 1)
			assignBeforeStandBy = PreparingSchedule.checkIfAssignAlready(friday0date, 2, 3)
			
			if assignBeforeHead:
				template_variables['Friday0NoonAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Friday0NoonAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Friday0NoonAssignBeforeStandBy'] = assignBeforeStandBy
			
			if head_nurse_want:
				template_variables['HeadNurseWhoWantFriday0Noon'] = head_nurse_want
				
			if head_nurse_dont_care:
				template_variables['HeadNurseWhoDontCareFriday0Noon'] = head_nurse_dont_care
				
			if head_nurse_prefer_not:
				template_variables['HeadNurseWhoPreferNotFriday0Noon'] = head_nurse_prefer_not
				
			if head_nurse_cant:
				template_variables['HeadNurseWhoCantFriday0Noon'] = head_nurse_cant
				
			if want:
				template_variables['NurseWhoWantFriday0Noon'] = want
				
			if dont_care:
				template_variables['NurseWhoDontCareFriday0Noon'] = dont_care
				
			if prefer_not:
				template_variables['NurseWhoPreferNotFriday0Noon'] = prefer_not
				
			if cant:
				template_variables['NurseWhoCantFriday0Noon'] = cant
				
			
				
			# Saturday0 night info:
			head_nurse_want = Constrain.getShiftHeads(saturday0date, 0, 1)
			head_nurse_dont_care = Constrain.getShiftHeads(saturday0date, 0, 0)
			head_nurse_prefer_not = Constrain.getShiftHeads(saturday0date, 0, 2)
			head_nurse_cant = Constrain.getShiftHeads(saturday0date, 0, 3)
			
			want = Constrain.getCrew(saturday0date, 0, 1)
			dont_care = Constrain.getCrew(saturday0date, 0, 0)
			prefer_not = Constrain.getCrew(saturday0date, 0, 2)
			cant = Constrain.getCrew(saturday0date, 0, 3)
			
			assignBeforeHead = PreparingSchedule.checkIfAssignAlready(saturday0date, 0, 0)
			assignBeforeSecond = PreparingSchedule.checkIfAssignAlready(saturday0date, 0, 1)
			assignBeforeStandBy = PreparingSchedule.checkIfAssignAlready(saturday0date, 0, 3)
			
			if assignBeforeHead:
				template_variables['Saturday0NightAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Saturday0NightAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Saturday0NightAssignBeforeStandBy'] = assignBeforeStandBy
			
			if head_nurse_want:
				template_variables['HeadNurseWhoWantSaturday0Night'] = head_nurse_want
				
			if head_nurse_dont_care:
				template_variables['HeadNurseWhoDontCareSaturday0Night'] = head_nurse_dont_care
				
			if head_nurse_prefer_not:
				template_variables['HeadNurseWhoPreferNotSaturday0Night'] = head_nurse_prefer_not
				
			if head_nurse_cant:
				template_variables['HeadNurseWhoCantSaturday0Night'] = head_nurse_cant
				
			if want:
				template_variables['NurseWhoWantSaturday0Night'] = want
				
			if dont_care:
				template_variables['NurseWhoDontCareSaturday0Night'] = dont_care
				
			if prefer_not:
				template_variables['NurseWhoPreferNotSaturday0Night'] = prefer_not
				
			if cant:
				template_variables['NurseWhoCantSaturday0Night'] = cant
			

			
			# Saturday0 morning info:
			head_nurse_want = Constrain.getShiftHeads(saturday0date, 1, 1)
			head_nurse_dont_care = Constrain.getShiftHeads(saturday0date, 1, 0)
			head_nurse_prefer_not = Constrain.getShiftHeads(saturday0date, 1, 2)
			head_nurse_cant = Constrain.getShiftHeads(saturday0date, 1, 3)
			
			want = Constrain.getCrew(saturday0date, 1, 1)
			dont_care = Constrain.getCrew(saturday0date, 1, 0)
			prefer_not = Constrain.getCrew(saturday0date, 1, 2)
			cant = Constrain.getCrew(saturday0date, 1, 3)
			
			assignBeforeHead = PreparingSchedule.checkIfAssignAlready(saturday0date, 1, 0)
			assignBeforeSecond = PreparingSchedule.checkIfAssignAlready(saturday0date, 1, 1)
			assignBeforeStandBy = PreparingSchedule.checkIfAssignAlready(saturday0date, 1, 3)
			
			if assignBeforeHead:
				template_variables['Saturday0MorningAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Saturday0MorningAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Saturday0MorningAssignBeforeStandBy'] = assignBeforeStandBy
			
			if head_nurse_want:
				template_variables['HeadNurseWhoWantSaturday0Morning'] = head_nurse_want
				
			if head_nurse_dont_care:
				template_variables['HeadNurseWhoDontCareSaturday0Morning'] = head_nurse_dont_care
				
			if head_nurse_prefer_not:
				template_variables['HeadNurseWhoPreferNotSaturday0Morning'] = head_nurse_prefer_not
				
			if head_nurse_cant:
				template_variables['HeadNurseWhoCantSaturday0Morning'] = head_nurse_cant
				
			if want:
				template_variables['NurseWhoWantSaturday0Morning'] = want
				
			if dont_care:
				template_variables['NurseWhoDontCareSaturday0Morning'] = dont_care
				
			if prefer_not:
				template_variables['NurseWhoPreferNotSaturday0Morning'] = prefer_not
				
			if cant:
				template_variables['NurseWhoCantSaturday0Morning'] = cant
				
			
			
			# Saturday0 noon info:
			head_nurse_want = Constrain.getShiftHeads(saturday0date, 2, 1)
			head_nurse_dont_care = Constrain.getShiftHeads(saturday0date, 2, 0)
			head_nurse_prefer_not = Constrain.getShiftHeads(saturday0date, 2, 2)
			head_nurse_cant = Constrain.getShiftHeads(saturday0date, 2, 3)
			
			want = Constrain.getCrew(saturday0date, 2, 1)
			dont_care = Constrain.getCrew(saturday0date, 2, 0)
			prefer_not = Constrain.getCrew(saturday0date, 2, 2)
			cant = Constrain.getCrew(saturday0date, 2, 3)
			
			assignBeforeHead = PreparingSchedule.checkIfAssignAlready(saturday0date, 2, 0)
			assignBeforeSecond = PreparingSchedule.checkIfAssignAlready(saturday0date, 2, 1)
			assignBeforeStandBy = PreparingSchedule.checkIfAssignAlready(saturday0date, 2, 3)
			
			if assignBeforeHead:
				template_variables['Saturday0NoonAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Saturday0NoonAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Saturday0NoonAssignBeforeStandBy'] = assignBeforeStandBy
			
			if head_nurse_want:
				template_variables['HeadNurseWhoWantSaturday0Noon'] = head_nurse_want
				
			if head_nurse_dont_care:
				template_variables['HeadNurseWhoDontCareSaturday0Noon'] = head_nurse_dont_care
				
			if head_nurse_prefer_not:
				template_variables['HeadNurseWhoPreferNotSaturday0Noon'] = head_nurse_prefer_not
				
			if head_nurse_cant:
				template_variables['HeadNurseWhoCantSaturday0Noon'] = head_nurse_cant
				
			if want:
				template_variables['NurseWhoWantSaturday0Noon'] = want
				
			if dont_care:
				template_variables['NurseWhoDontCareSaturday0Noon'] = dont_care
				
			if prefer_not:
				template_variables['NurseWhoPreferNotSaturday0Noon'] = prefer_not
				
			if cant:
				template_variables['NurseWhoCantSaturday0Noon'] = cant
				
			
			#### Second week ####
				

				
			# Sunday1 night info:
			head_nurse_want = Constrain.getShiftHeads(sunday1date, 0, 1)
			head_nurse_dont_care = Constrain.getShiftHeads(sunday1date, 0, 0)
			head_nurse_prefer_not = Constrain.getShiftHeads(sunday1date, 0, 2)
			head_nurse_cant = Constrain.getShiftHeads(sunday1date, 0, 3)
			
			want = Constrain.getCrew(sunday1date, 0, 1)
			dont_care = Constrain.getCrew(sunday1date, 0, 0)
			prefer_not = Constrain.getCrew(sunday1date, 0, 2)
			cant = Constrain.getCrew(sunday1date, 0, 3)
			
			assignBeforeHead = PreparingSchedule.checkIfAssignAlready(sunday1date, 0, 0)
			assignBeforeSecond = PreparingSchedule.checkIfAssignAlready(sunday1date, 0, 1)
			assignBeforeStandBy = PreparingSchedule.checkIfAssignAlready(sunday1date, 0, 3)
			
			if assignBeforeHead:
				template_variables['Sunday1NightAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Sunday1NightAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Sunday1NightAssignBeforeStandBy'] = assignBeforeStandBy
			
			if head_nurse_want:
				template_variables['HeadNurseWhoWantSunday1Night'] = head_nurse_want
				
			if head_nurse_dont_care:
				template_variables['HeadNurseWhoDontCareSunday1Night'] = head_nurse_dont_care
				
			if head_nurse_prefer_not:
				template_variables['HeadNurseWhoPreferNotSunday1Night'] = head_nurse_prefer_not
				
			if head_nurse_cant:
				template_variables['HeadNurseWhoCantSunday1Night'] = head_nurse_cant
				
			if want:
				template_variables['NurseWhoWantSunday1Night'] = want
				
			if dont_care:
				template_variables['NurseWhoDontCareSunday1Night'] = dont_care
				
			if prefer_not:
				template_variables['NurseWhoPreferNotSunday1Night'] = prefer_not
				
			if cant:
				template_variables['NurseWhoCantSunday1Night'] = cant
			

			
			# Sunday1 morning info:
			head_nurse_want = Constrain.getShiftHeads(sunday1date, 1, 1)
			head_nurse_dont_care = Constrain.getShiftHeads(sunday1date, 1, 0)
			head_nurse_prefer_not = Constrain.getShiftHeads(sunday1date, 1, 2)
			head_nurse_cant = Constrain.getShiftHeads(sunday1date, 1, 3)
			
			want = Constrain.getCrew(sunday1date, 1, 1)
			dont_care = Constrain.getCrew(sunday1date, 1, 0)
			prefer_not = Constrain.getCrew(sunday1date, 1, 2)
			cant = Constrain.getCrew(sunday1date, 1, 3)
			
			assignBeforeHead = PreparingSchedule.checkIfAssignAlready(sunday1date, 1, 0)
			assignBeforeSecond = PreparingSchedule.checkIfAssignAlready(sunday1date, 1, 1)
			assignBeforeStandBy = PreparingSchedule.checkIfAssignAlready(sunday1date, 1, 3)
			
			if assignBeforeHead:
				template_variables['Sunday1MorningAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Sunday1MorningAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Sunday1MorningAssignBeforeStandBy'] = assignBeforeStandBy
			
			if head_nurse_want:
				template_variables['HeadNurseWhoWantSunday1Morning'] = head_nurse_want
				
			if head_nurse_dont_care:
				template_variables['HeadNurseWhoDontCareSunday1Morning'] = head_nurse_dont_care
				
			if head_nurse_prefer_not:
				template_variables['HeadNurseWhoPreferNotSunday1Morning'] = head_nurse_prefer_not
				
			if head_nurse_cant:
				template_variables['HeadNurseWhoCantSunday1Morning'] = head_nurse_cant
				
			if want:
				template_variables['NurseWhoWantSunday1Morning'] = want
				
			if dont_care:
				template_variables['NurseWhoDontCareSunday1Morning'] = dont_care
				
			if prefer_not:
				template_variables['NurseWhoPreferNotSunday1Morning'] = prefer_not
				
			if cant:
				template_variables['NurseWhoCantSunday1Morning'] = cant
				
			
			
			# Sunday1 noon info:
			head_nurse_want = Constrain.getShiftHeads(sunday1date, 2, 1)
			head_nurse_dont_care = Constrain.getShiftHeads(sunday1date, 2, 0)
			head_nurse_prefer_not = Constrain.getShiftHeads(sunday1date, 2, 2)
			head_nurse_cant = Constrain.getShiftHeads(sunday1date, 2, 3)
			
			want = Constrain.getCrew(sunday1date, 2, 1)
			dont_care = Constrain.getCrew(sunday1date, 2, 0)
			prefer_not = Constrain.getCrew(sunday1date, 2, 2)
			cant = Constrain.getCrew(sunday1date, 2, 3)
			
			assignBeforeHead = PreparingSchedule.checkIfAssignAlready(sunday1date, 2, 0)
			assignBeforeSecond = PreparingSchedule.checkIfAssignAlready(sunday1date, 2, 1)
			assignBeforeStandBy = PreparingSchedule.checkIfAssignAlready(sunday1date, 2, 3)
			
			if assignBeforeHead:
				template_variables['Sunday1NoonAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Sunday1NoonAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Sunday1NoonAssignBeforeStandBy'] = assignBeforeStandBy
			
			if head_nurse_want:
				template_variables['HeadNurseWhoWantSunday1Noon'] = head_nurse_want
				
			if head_nurse_dont_care:
				template_variables['HeadNurseWhoDontCareSunday1Noon'] = head_nurse_dont_care
				
			if head_nurse_prefer_not:
				template_variables['HeadNurseWhoPreferNotSunday1Noon'] = head_nurse_prefer_not
				
			if head_nurse_cant:
				template_variables['HeadNurseWhoCantSunday1Noon'] = head_nurse_cant
				
			if want:
				template_variables['NurseWhoWantSunday1Noon'] = want
				
			if dont_care:
				template_variables['NurseWhoDontCareSunday1Noon'] = dont_care
				
			if prefer_not:
				template_variables['NurseWhoPreferNotSunday1Noon'] = prefer_not
				
			if cant:
				template_variables['NurseWhoCantSunday1Noon'] = cant
				
			
				
			# Monday1 night info:
			head_nurse_want = Constrain.getShiftHeads(monday1date, 0, 1)
			head_nurse_dont_care = Constrain.getShiftHeads(monday1date, 0, 0)
			head_nurse_prefer_not = Constrain.getShiftHeads(monday1date, 0, 2)
			head_nurse_cant = Constrain.getShiftHeads(monday1date, 0, 3)
			
			want = Constrain.getCrew(monday1date, 0, 1)
			dont_care = Constrain.getCrew(monday1date, 0, 0)
			prefer_not = Constrain.getCrew(monday1date, 0, 2)
			cant = Constrain.getCrew(monday1date, 0, 3)
			
			assignBeforeHead = PreparingSchedule.checkIfAssignAlready(monday1date, 0, 0)
			assignBeforeSecond = PreparingSchedule.checkIfAssignAlready(monday1date, 0, 1)
			assignBeforeStandBy = PreparingSchedule.checkIfAssignAlready(monday1date, 0, 3)
			
			if assignBeforeHead:
				template_variables['Monday1NightAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Monday1NightAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Monday1NightAssignBeforeStandBy'] = assignBeforeStandBy
			
			if head_nurse_want:
				template_variables['HeadNurseWhoWantMonday1Night'] = head_nurse_want
				
			if head_nurse_dont_care:
				template_variables['HeadNurseWhoDontCareMonday1Night'] = head_nurse_dont_care
				
			if head_nurse_prefer_not:
				template_variables['HeadNurseWhoPreferNotMonday1Night'] = head_nurse_prefer_not
				
			if head_nurse_cant:
				template_variables['HeadNurseWhoCantMonday1Night'] = head_nurse_cant
				
			if want:
				template_variables['NurseWhoWantMonday1Night'] = want
				
			if dont_care:
				template_variables['NurseWhoDontCareMonday1Night'] = dont_care
				
			if prefer_not:
				template_variables['NurseWhoPreferNotMonday1Night'] = prefer_not
				
			if cant:
				template_variables['NurseWhoCantMonday1Night'] = cant
			

			
			# Monday1 morning info:
			head_nurse_want = Constrain.getShiftHeads(monday1date, 1, 1)
			head_nurse_dont_care = Constrain.getShiftHeads(monday1date, 1, 0)
			head_nurse_prefer_not = Constrain.getShiftHeads(monday1date, 1, 2)
			head_nurse_cant = Constrain.getShiftHeads(monday1date, 1, 3)
			
			want = Constrain.getCrew(monday1date, 1, 1)
			dont_care = Constrain.getCrew(monday1date, 1, 0)
			prefer_not = Constrain.getCrew(monday1date, 1, 2)
			cant = Constrain.getCrew(monday1date, 1, 3)
			
			assignBeforeHead = PreparingSchedule.checkIfAssignAlready(monday1date, 1, 0)
			assignBeforeSecond = PreparingSchedule.checkIfAssignAlready(monday1date, 1, 1)
			assignBeforeStandBy = PreparingSchedule.checkIfAssignAlready(monday1date, 1, 3)
			
			if assignBeforeHead:
				template_variables['Monday1MorningAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Monday1MorningAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Monday1MorningAssignBeforeStandBy'] = assignBeforeStandBy
			
			if head_nurse_want:
				template_variables['HeadNurseWhoWantMonday1Morning'] = head_nurse_want
				
			if head_nurse_dont_care:
				template_variables['HeadNurseWhoDontCareMonday1Morning'] = head_nurse_dont_care
				
			if head_nurse_prefer_not:
				template_variables['HeadNurseWhoPreferNotMonday1Morning'] = head_nurse_prefer_not
				
			if head_nurse_cant:
				template_variables['HeadNurseWhoCantMonday1Morning'] = head_nurse_cant
				
			if want:
				template_variables['NurseWhoWantMonday1Morning'] = want
				
			if dont_care:
				template_variables['NurseWhoDontCareMonday1Morning'] = dont_care
				
			if prefer_not:
				template_variables['NurseWhoPreferNotMonday1Morning'] = prefer_not
				
			if cant:
				template_variables['NurseWhoCantMonday1Morning'] = cant
				
			
			
			# Monday1 noon info:
			head_nurse_want = Constrain.getShiftHeads(monday1date, 2, 1)
			head_nurse_dont_care = Constrain.getShiftHeads(monday1date, 2, 0)
			head_nurse_prefer_not = Constrain.getShiftHeads(monday1date, 2, 2)
			head_nurse_cant = Constrain.getShiftHeads(monday1date, 2, 3)
			
			want = Constrain.getCrew(monday1date, 2, 1)
			dont_care = Constrain.getCrew(monday1date, 2, 0)
			prefer_not = Constrain.getCrew(monday1date, 2, 2)
			cant = Constrain.getCrew(monday1date, 2, 3)
			
			assignBeforeHead = PreparingSchedule.checkIfAssignAlready(monday1date, 2, 0)
			assignBeforeSecond = PreparingSchedule.checkIfAssignAlready(monday1date, 2, 1)
			assignBeforeStandBy = PreparingSchedule.checkIfAssignAlready(monday1date, 2, 3)
			
			if assignBeforeHead:
				template_variables['Monday1NoonAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Monday1NoonAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Monday1NoonAssignBeforeStandBy'] = assignBeforeStandBy
			
			if head_nurse_want:
				template_variables['HeadNurseWhoWantMonday1Noon'] = head_nurse_want
				
			if head_nurse_dont_care:
				template_variables['HeadNurseWhoDontCareMonday1Noon'] = head_nurse_dont_care
				
			if head_nurse_prefer_not:
				template_variables['HeadNurseWhoPreferNotMonday1Noon'] = head_nurse_prefer_not
				
			if head_nurse_cant:
				template_variables['HeadNurseWhoCantMonday1Noon'] = head_nurse_cant
				
			if want:
				template_variables['NurseWhoWantMonday1Noon'] = want
				
			if dont_care:
				template_variables['NurseWhoDontCareMonday1Noon'] = dont_care
				
			if prefer_not:
				template_variables['NurseWhoPreferNotMonday1Noon'] = prefer_not
				
			if cant:
				template_variables['NurseWhoCantMonday1Noon'] = cant
				
			
				
			# Tuesday1 night info:
			head_nurse_want = Constrain.getShiftHeads(tuesday1date, 0, 1)
			head_nurse_dont_care = Constrain.getShiftHeads(tuesday1date, 0, 0)
			head_nurse_prefer_not = Constrain.getShiftHeads(tuesday1date, 0, 2)
			head_nurse_cant = Constrain.getShiftHeads(tuesday1date, 0, 3)
			
			want = Constrain.getCrew(tuesday1date, 0, 1)
			dont_care = Constrain.getCrew(tuesday1date, 0, 0)
			prefer_not = Constrain.getCrew(tuesday1date, 0, 2)
			cant = Constrain.getCrew(tuesday1date, 0, 3)
			
			assignBeforeHead = PreparingSchedule.checkIfAssignAlready(tuesday1date, 0, 0)
			assignBeforeSecond = PreparingSchedule.checkIfAssignAlready(tuesday1date, 0, 1)
			assignBeforeStandBy = PreparingSchedule.checkIfAssignAlready(tuesday1date, 0, 3)
			
			if assignBeforeHead:
				template_variables['Tuesday1NightAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Tuesday1NightAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Tuesday1NightAssignBeforeStandBy'] = assignBeforeStandBy
			
			if head_nurse_want:
				template_variables['HeadNurseWhoWantTuesday1Night'] = head_nurse_want
				
			if head_nurse_dont_care:
				template_variables['HeadNurseWhoDontCareTuesday1Night'] = head_nurse_dont_care
				
			if head_nurse_prefer_not:
				template_variables['HeadNurseWhoPreferNotTuesday1Night'] = head_nurse_prefer_not
				
			if head_nurse_cant:
				template_variables['HeadNurseWhoCantTuesday1Night'] = head_nurse_cant
				
			if want:
				template_variables['NurseWhoWantTuesday1Night'] = want
				
			if dont_care:
				template_variables['NurseWhoDontCareTuesday1Night'] = dont_care
				
			if prefer_not:
				template_variables['NurseWhoPreferNotTuesday1Night'] = prefer_not
				
			if cant:
				template_variables['NurseWhoCantTuesday1Night'] = cant
			

			
			# Tuesday1 morning info:
			head_nurse_want = Constrain.getShiftHeads(tuesday1date, 1, 1)
			head_nurse_dont_care = Constrain.getShiftHeads(tuesday1date, 1, 0)
			head_nurse_prefer_not = Constrain.getShiftHeads(tuesday1date, 1, 2)
			head_nurse_cant = Constrain.getShiftHeads(tuesday1date, 1, 3)
			
			want = Constrain.getCrew(tuesday1date, 1, 1)
			dont_care = Constrain.getCrew(tuesday1date, 1, 0)
			prefer_not = Constrain.getCrew(tuesday1date, 1, 2)
			cant = Constrain.getCrew(tuesday1date, 1, 3)
			
			assignBeforeHead = PreparingSchedule.checkIfAssignAlready(tuesday1date, 1, 0)
			assignBeforeSecond = PreparingSchedule.checkIfAssignAlready(tuesday1date, 1, 1)
			assignBeforeThird = PreparingSchedule.checkIfAssignAlready(tuesday1date, 1, 2)
			assignBeforeStandBy = PreparingSchedule.checkIfAssignAlready(tuesday1date, 1, 3)
			
			if assignBeforeHead:
				template_variables['Tuesday1MorningAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Tuesday1MorningAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeThird:
				template_variables['Tuesday1MorningAssignBeforeThird'] = assignBeforeThird
				
			if assignBeforeStandBy:
				template_variables['Tuesday1MorningAssignBeforeStandBy'] = assignBeforeStandBy
			
			if head_nurse_want:
				template_variables['HeadNurseWhoWantTuesday1Morning'] = head_nurse_want
				
			if head_nurse_dont_care:
				template_variables['HeadNurseWhoDontCareTuesday1Morning'] = head_nurse_dont_care
				
			if head_nurse_prefer_not:
				template_variables['HeadNurseWhoPreferNotTuesday1Morning'] = head_nurse_prefer_not
				
			if head_nurse_cant:
				template_variables['HeadNurseWhoCantTuesday1Morning'] = head_nurse_cant
				
			if want:
				template_variables['NurseWhoWantTuesday1Morning'] = want
				
			if dont_care:
				template_variables['NurseWhoDontCareTuesday1Morning'] = dont_care
				
			if prefer_not:
				template_variables['NurseWhoPreferNotTuesday0Morning'] = prefer_not
				
			if cant:
				template_variables['NurseWhoCantTuesday1Morning'] = cant
				
			
			
			# Tuesday1 noon info:
			head_nurse_want = Constrain.getShiftHeads(tuesday1date, 2, 1)
			head_nurse_dont_care = Constrain.getShiftHeads(tuesday1date, 2, 0)
			head_nurse_prefer_not = Constrain.getShiftHeads(tuesday1date, 2, 2)
			head_nurse_cant = Constrain.getShiftHeads(tuesday1date, 2, 3)
			
			want = Constrain.getCrew(tuesday1date, 2, 1)
			dont_care = Constrain.getCrew(tuesday1date, 2, 0)
			prefer_not = Constrain.getCrew(tuesday1date, 2, 2)
			cant = Constrain.getCrew(tuesday1date, 2, 3)
			
			assignBeforeHead = PreparingSchedule.checkIfAssignAlready(tuesday1date, 2, 0)
			assignBeforeSecond = PreparingSchedule.checkIfAssignAlready(tuesday1date, 2, 1)
			assignBeforeStandBy = PreparingSchedule.checkIfAssignAlready(tuesday1date, 2, 3)
			
			if assignBeforeHead:
				template_variables['Tuesday1NoonAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Tuesday1NoonAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Tuesday1NoonAssignBeforeStandBy'] = assignBeforeStandBy
			
			if head_nurse_want:
				template_variables['HeadNurseWhoWantTuesday1Noon'] = head_nurse_want
				
			if head_nurse_dont_care:
				template_variables['HeadNurseWhoDontCareTuesday1Noon'] = head_nurse_dont_care
				
			if head_nurse_prefer_not:
				template_variables['HeadNurseWhoPreferNotTuesday1Noon'] = head_nurse_prefer_not
				
			if head_nurse_cant:
				template_variables['HeadNurseWhoCantTuesday1Noon'] = head_nurse_cant
				
			if want:
				template_variables['NurseWhoWantTuesday1Noon'] = want
				
			if dont_care:
				template_variables['NurseWhoDontCareTuesday1Noon'] = dont_care
				
			if prefer_not:
				template_variables['NurseWhoPreferNotTuesday1Noon'] = prefer_not
				
			if cant:
				template_variables['NurseWhoCantTuesday1Noon'] = cant
				
			
				
			# Wednesday1 night info:
			head_nurse_want = Constrain.getShiftHeads(wednesday1date, 0, 1)
			head_nurse_dont_care = Constrain.getShiftHeads(wednesday1date, 0, 0)
			head_nurse_prefer_not = Constrain.getShiftHeads(wednesday1date, 0, 2)
			head_nurse_cant = Constrain.getShiftHeads(wednesday1date, 0, 3)
			
			want = Constrain.getCrew(wednesday1date, 0, 1)
			dont_care = Constrain.getCrew(wednesday1date, 0, 0)
			prefer_not = Constrain.getCrew(wednesday1date, 0, 2)
			cant = Constrain.getCrew(wednesday1date, 0, 3)
			
			assignBeforeHead = PreparingSchedule.checkIfAssignAlready(wednesday1date, 0, 0)
			assignBeforeSecond = PreparingSchedule.checkIfAssignAlready(wednesday1date, 0, 1)
			assignBeforeStandBy = PreparingSchedule.checkIfAssignAlready(wednesday1date, 0, 3)
			
			if assignBeforeHead:
				template_variables['Wednesday1NightAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Wednesday1NightAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Wednesday1NightAssignBeforeStandBy'] = assignBeforeStandBy
			
			if head_nurse_want:
				template_variables['HeadNurseWhoWantWednesday0Night'] = head_nurse_want
			
			if head_nurse_want:
				template_variables['HeadNurseWhoWantWednesday1Night'] = head_nurse_want
				
			if head_nurse_dont_care:
				template_variables['HeadNurseWhoDontCareWednesday1Night'] = head_nurse_dont_care
				
			if head_nurse_prefer_not:
				template_variables['HeadNurseWhoPreferNotWednesday1Night'] = head_nurse_prefer_not
				
			if head_nurse_cant:
				template_variables['HeadNurseWhoCantWednesday1Night'] = head_nurse_cant
				
			if want:
				template_variables['NurseWhoWantWednesday1Night'] = want
				
			if dont_care:
				template_variables['NurseWhoDontCareWednesday1Night'] = dont_care
				
			if prefer_not:
				template_variables['NurseWhoPreferNotWednesday1Night'] = prefer_not
				
			if cant:
				template_variables['NurseWhoCantWednesday1Night'] = cant
			

			
			# Wednesday1 morning info:
			head_nurse_want = Constrain.getShiftHeads(wednesday1date, 1, 1)
			head_nurse_dont_care = Constrain.getShiftHeads(wednesday1date, 1, 0)
			head_nurse_prefer_not = Constrain.getShiftHeads(wednesday1date, 1, 2)
			head_nurse_cant = Constrain.getShiftHeads(wednesday1date, 1, 3)
			
			want = Constrain.getCrew(wednesday1date, 1, 1)
			dont_care = Constrain.getCrew(wednesday1date, 1, 0)
			prefer_not = Constrain.getCrew(wednesday1date, 1, 2)
			cant = Constrain.getCrew(wednesday1date, 1, 3)
			
			assignBeforeHead = PreparingSchedule.checkIfAssignAlready(wednesday1date, 1, 0)
			assignBeforeSecond = PreparingSchedule.checkIfAssignAlready(wednesday1date, 1, 1)
			assignBeforeStandBy = PreparingSchedule.checkIfAssignAlready(wednesday1date, 1, 3)
			
			if assignBeforeHead:
				template_variables['Wednesday1MorningAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Wednesday1MorningAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Wednesday1MorningAssignBeforeStandBy'] = assignBeforeStandBy
			
			if head_nurse_want:
				template_variables['HeadNurseWhoWantWednesday1Morning'] = head_nurse_want
				
			if head_nurse_dont_care:
				template_variables['HeadNurseWhoDontCareWednesday1Morning'] = head_nurse_dont_care
				
			if head_nurse_prefer_not:
				template_variables['HeadNurseWhoPreferNotWednesday1Morning'] = head_nurse_prefer_not
				
			if head_nurse_cant:
				template_variables['HeadNurseWhoCantWednesday1Morning'] = head_nurse_cant
				
			if want:
				template_variables['NurseWhoWantWednesday1Morning'] = want
				
			if dont_care:
				template_variables['NurseWhoDontCareWednesday1Morning'] = dont_care
				
			if prefer_not:
				template_variables['NurseWhoPreferNotWednesday1Morning'] = prefer_not
				
			if cant:
				template_variables['NurseWhoCantWednesday1Morning'] = cant
				
			
			
			# Wednesday1 noon info:
			head_nurse_want = Constrain.getShiftHeads(wednesday1date, 2, 1)
			head_nurse_dont_care = Constrain.getShiftHeads(wednesday1date, 2, 0)
			head_nurse_prefer_not = Constrain.getShiftHeads(wednesday1date, 2, 2)
			head_nurse_cant = Constrain.getShiftHeads(wednesday1date, 2, 3)
			
			want = Constrain.getCrew(wednesday1date, 2, 1)
			dont_care = Constrain.getCrew(wednesday1date, 2, 0)
			prefer_not = Constrain.getCrew(wednesday1date, 2, 2)
			cant = Constrain.getCrew(wednesday1date, 2, 3)
			
			assignBeforeHead = PreparingSchedule.checkIfAssignAlready(wednesday1date, 2, 0)
			assignBeforeSecond = PreparingSchedule.checkIfAssignAlready(wednesday1date, 2, 1)
			assignBeforeStandBy = PreparingSchedule.checkIfAssignAlready(wednesday1date, 2, 3)
			
			if assignBeforeHead:
				template_variables['Wednesday1NoonAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Wednesday1NoonAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Wednesday1NoonAssignBeforeStandBy'] = assignBeforeStandBy
			
			if head_nurse_want:
				template_variables['HeadNurseWhoWantWednesday1Noon'] = head_nurse_want
				
			if head_nurse_dont_care:
				template_variables['HeadNurseWhoDontCareWednesday1Noon'] = head_nurse_dont_care
				
			if head_nurse_prefer_not:
				template_variables['HeadNurseWhoPreferNotWednesday1Noon'] = head_nurse_prefer_not
				
			if head_nurse_cant:
				template_variables['HeadNurseWhoCantWednesday1Noon'] = head_nurse_cant
				
			if want:
				template_variables['NurseWhoWantWednesday1Noon'] = want
				
			if dont_care:
				template_variables['NurseWhoDontCareWednesday1Noon'] = dont_care
				
			if prefer_not:
				template_variables['NurseWhoPreferNotWednesday1Noon'] = prefer_not
				
			if cant:
				template_variables['NurseWhoCantWednesday1Noon'] = cant
				
			
				
			# Thursday1 night info:
			head_nurse_want = Constrain.getShiftHeads(thursday1date, 0, 1)
			head_nurse_dont_care = Constrain.getShiftHeads(thursday1date, 0, 0)
			head_nurse_prefer_not = Constrain.getShiftHeads(thursday1date, 0, 2)
			head_nurse_cant = Constrain.getShiftHeads(thursday1date, 0, 3)
			
			want = Constrain.getCrew(thursday1date, 0, 1)
			dont_care = Constrain.getCrew(thursday1date, 0, 0)
			prefer_not = Constrain.getCrew(thursday1date, 0, 2)
			cant = Constrain.getCrew(thursday1date, 0, 3)
			
			assignBeforeHead = PreparingSchedule.checkIfAssignAlready(thursday1date, 0, 0)
			assignBeforeSecond = PreparingSchedule.checkIfAssignAlready(thursday1date, 0, 1)
			assignBeforeStandBy = PreparingSchedule.checkIfAssignAlready(thursday1date, 0, 3)
			
			if assignBeforeHead:
				template_variables['Thursday1NightAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Thursday1NightAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Thursday1NightAssignBeforeStandBy'] = assignBeforeStandBy
			
			if head_nurse_want:
				template_variables['HeadNurseWhoWantThursday1Night'] = head_nurse_want
				
			if head_nurse_dont_care:
				template_variables['HeadNurseWhoDontCareThursday1Night'] = head_nurse_dont_care
				
			if head_nurse_prefer_not:
				template_variables['HeadNurseWhoPreferNotThursday1Night'] = head_nurse_prefer_not
				
			if head_nurse_cant:
				template_variables['HeadNurseWhoCantThursday1Night'] = head_nurse_cant
				
			if want:
				template_variables['NurseWhoWantThursday1Night'] = want
				
			if dont_care:
				template_variables['NurseWhoDontCareThursday1Night'] = dont_care
				
			if prefer_not:
				template_variables['NurseWhoPreferNotThursday1Night'] = prefer_not
				
			if cant:
				template_variables['NurseWhoCantThursday1Night'] = cant
			

			
			# Thursday1 morning info:
			head_nurse_want = Constrain.getShiftHeads(thursday1date, 1, 1)
			head_nurse_dont_care = Constrain.getShiftHeads(thursday1date, 1, 0)
			head_nurse_prefer_not = Constrain.getShiftHeads(thursday1date, 1, 2)
			head_nurse_cant = Constrain.getShiftHeads(thursday1date, 1, 3)
			
			want = Constrain.getCrew(thursday1date, 1, 1)
			dont_care = Constrain.getCrew(thursday1date, 1, 0)
			prefer_not = Constrain.getCrew(thursday1date, 1, 2)
			cant = Constrain.getCrew(thursday1date, 1, 3)
			
			assignBeforeHead = PreparingSchedule.checkIfAssignAlready(thursday1date, 1, 0)
			assignBeforeSecond = PreparingSchedule.checkIfAssignAlready(thursday1date, 1, 1)
			assignBeforeThird = PreparingSchedule.checkIfAssignAlready(thursday1date, 1, 2)
			assignBeforeStandBy = PreparingSchedule.checkIfAssignAlready(thursday1date, 1, 3)
			
			if assignBeforeHead:
				template_variables['Thursday1MorningAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Thursday1MorningAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeSecond:
				template_variables['Thursday1MorningAssignBeforeThird'] = assignBeforeThird
				
			if assignBeforeStandBy:
				template_variables['Thursday1MorningAssignBeforeStandBy'] = assignBeforeStandBy
			
			if head_nurse_want:
				template_variables['HeadNurseWhoWantThursday1Morning'] = head_nurse_want
				
			if head_nurse_dont_care:
				template_variables['HeadNurseWhoDontCareThursday1Morning'] = head_nurse_dont_care
				
			if head_nurse_prefer_not:
				template_variables['HeadNurseWhoPreferNotThursday1Morning'] = head_nurse_prefer_not
				
			if head_nurse_cant:
				template_variables['HeadNurseWhoCantThursday1Morning'] = head_nurse_cant
				
			if want:
				template_variables['NurseWhoWantThursday1Morning'] = want
				
			if dont_care:
				template_variables['NurseWhoDontCareThursday1Morning'] = dont_care
				
			if prefer_not:
				template_variables['NurseWhoPreferNotThursday1Morning'] = prefer_not
				
			if cant:
				template_variables['NurseWhoCantThursday1Morning'] = cant
				
			
			
			# Thursday1 noon info:
			head_nurse_want = Constrain.getShiftHeads(thursday1date, 2, 1)
			head_nurse_dont_care = Constrain.getShiftHeads(thursday1date, 2, 0)
			head_nurse_prefer_not = Constrain.getShiftHeads(thursday1date, 2, 2)
			head_nurse_cant = Constrain.getShiftHeads(thursday1date, 2, 3)
			
			want = Constrain.getCrew(thursday1date, 2, 1)
			dont_care = Constrain.getCrew(thursday1date, 2, 0)
			prefer_not = Constrain.getCrew(thursday1date, 2, 2)
			cant = Constrain.getCrew(thursday1date, 2, 3)
			
			assignBeforeHead = PreparingSchedule.checkIfAssignAlready(thursday1date, 2, 0)
			assignBeforeSecond = PreparingSchedule.checkIfAssignAlready(thursday1date, 2, 1)
			assignBeforeStandBy = PreparingSchedule.checkIfAssignAlready(thursday1date, 2, 3)
			
			if assignBeforeHead:
				template_variables['Thursday1NoonAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Thursday1NoonAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Thursday1NoonAssignBeforeStandBy'] = assignBeforeStandBy
			
			if head_nurse_want:
				template_variables['HeadNurseWhoWantThursday1Noon'] = head_nurse_want
				
			if head_nurse_dont_care:
				template_variables['HeadNurseWhoDontCareThursday1Noon'] = head_nurse_dont_care
				
			if head_nurse_prefer_not:
				template_variables['HeadNurseWhoPreferNotThursday1Noon'] = head_nurse_prefer_not
				
			if head_nurse_cant:
				template_variables['HeadNurseWhoCantThursday1Noon'] = head_nurse_cant
				
			if want:
				template_variables['NurseWhoWantThursday1Noon'] = want
				
			if dont_care:
				template_variables['NurseWhoDontCareThursday1Noon'] = dont_care
				
			if prefer_not:
				template_variables['NurseWhoPreferNotThursday1Noon'] = prefer_not
				
			if cant:
				template_variables['NurseWhoCantThursday1Noon'] = cant
				
			
			
			# Friday1 night info:
			head_nurse_want = Constrain.getShiftHeads(friday1date, 0, 1)
			head_nurse_dont_care = Constrain.getShiftHeads(friday1date, 0, 0)
			head_nurse_prefer_not = Constrain.getShiftHeads(friday1date, 0, 2)
			head_nurse_cant = Constrain.getShiftHeads(friday1date, 0, 3)
			
			want = Constrain.getCrew(friday1date, 0, 1)
			dont_care = Constrain.getCrew(friday1date, 0, 0)
			prefer_not = Constrain.getCrew(friday1date, 0, 2)
			cant = Constrain.getCrew(friday1date, 0, 3)
			
			assignBeforeHead = PreparingSchedule.checkIfAssignAlready(friday1date, 0, 0)
			assignBeforeSecond = PreparingSchedule.checkIfAssignAlready(friday1date, 0, 1)
			assignBeforeStandBy = PreparingSchedule.checkIfAssignAlready(friday1date, 0, 3)
			
			if assignBeforeHead:
				template_variables['Friday1NightAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Friday1NighAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Friday1NighAssignBeforeStandBy'] = assignBeforeStandBy
			
			if head_nurse_want:
				template_variables['HeadNurseWhoWantFriday1Night'] = head_nurse_want
				
			if head_nurse_dont_care:
				template_variables['HeadNurseWhoDontCareFriday1Night'] = head_nurse_dont_care
				
			if head_nurse_prefer_not:
				template_variables['HeadNurseWhoPreferNotFriday1Night'] = head_nurse_prefer_not
				
			if head_nurse_cant:
				template_variables['HeadNurseWhoCantFriday1Night'] = head_nurse_cant
				
			if want:
				template_variables['NurseWhoWantFriday1Night'] = want
				
			if dont_care:
				template_variables['NurseWhoDontCareFriday1Night'] = dont_care
				
			if prefer_not:
				template_variables['NurseWhoPreferNotFriday1Night'] = prefer_not
				
			if cant:
				template_variables['NurseWhoCantFriday1Night'] = cant
			

			
			# Friday1 morning info:
			head_nurse_want = Constrain.getShiftHeads(friday1date, 1, 1)
			head_nurse_dont_care = Constrain.getShiftHeads(friday1date, 1, 0)
			head_nurse_prefer_not = Constrain.getShiftHeads(friday1date, 1, 2)
			head_nurse_cant = Constrain.getShiftHeads(friday1date, 1, 3)
			
			want = Constrain.getCrew(friday1date, 1, 1)
			dont_care = Constrain.getCrew(friday1date, 1, 0)
			prefer_not = Constrain.getCrew(friday1date, 1, 2)
			cant = Constrain.getCrew(friday1date, 1, 3)
			
			assignBeforeHead = PreparingSchedule.checkIfAssignAlready(friday1date, 1, 0)
			assignBeforeSecond = PreparingSchedule.checkIfAssignAlready(friday1date, 1, 1)
			assignBeforeStandBy = PreparingSchedule.checkIfAssignAlready(friday1date, 1, 3)
			
			if assignBeforeHead:
				template_variables['Friday1MorningAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Friday1MorningAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Friday1MorningAssignBeforeStandBy'] = assignBeforeStandBy
			
			if head_nurse_want:
				template_variables['HeadNurseWhoWantFriday1Morning'] = head_nurse_want
				
			if head_nurse_dont_care:
				template_variables['HeadNurseWhoDontCareFriday1Morning'] = head_nurse_dont_care
				
			if head_nurse_prefer_not:
				template_variables['HeadNurseWhoPreferNotFriday1Morning'] = head_nurse_prefer_not
				
			if head_nurse_cant:
				template_variables['HeadNurseWhoCantFriday1Morning'] = head_nurse_cant
				
			if want:
				template_variables['NurseWhoWantFriday1Morning'] = want
				
			if dont_care:
				template_variables['NurseWhoDontCareFriday1Morning'] = dont_care
				
			if prefer_not:
				template_variables['NurseWhoPreferNotFriday1Morning'] = prefer_not
				
			if cant:
				template_variables['NurseWhoCantFriday1Morning'] = cant
				
			
			
			# Friday1 noon info:
			head_nurse_want = Constrain.getShiftHeads(friday1date, 2, 1)
			head_nurse_dont_care = Constrain.getShiftHeads(friday1date, 2, 0)
			head_nurse_prefer_not = Constrain.getShiftHeads(friday1date, 2, 2)
			head_nurse_cant = Constrain.getShiftHeads(friday1date, 2, 3)
			
			want = Constrain.getCrew(friday1date, 2, 1)
			dont_care = Constrain.getCrew(friday1date, 2, 0)
			prefer_not = Constrain.getCrew(friday1date, 2, 2)
			cant = Constrain.getCrew(friday1date, 2, 3)
			
			assignBeforeHead = PreparingSchedule.checkIfAssignAlready(friday1date, 2, 0)
			assignBeforeSecond = PreparingSchedule.checkIfAssignAlready(friday1date, 2, 1)
			assignBeforeStandBy = PreparingSchedule.checkIfAssignAlready(friday1date, 2, 3)
			
			if assignBeforeHead:
				template_variables['Friday1NoonAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Friday1NoonAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Friday1NoonAssignBeforeStandBy'] = assignBeforeStandBy
			
			if head_nurse_want:
				template_variables['HeadNurseWhoWantFriday1Noon'] = head_nurse_want
				
			if head_nurse_dont_care:
				template_variables['HeadNurseWhoDontCareFriday1Noon'] = head_nurse_dont_care
				
			if head_nurse_prefer_not:
				template_variables['HeadNurseWhoPreferNotFriday1Noon'] = head_nurse_prefer_not
				
			if head_nurse_cant:
				template_variables['HeadNurseWhoCantFriday1Noon'] = head_nurse_cant
				
			if want:
				template_variables['NurseWhoWantFriday1Noon'] = want
				
			if dont_care:
				template_variables['NurseWhoDontCareFriday1Noon'] = dont_care
				
			if prefer_not:
				template_variables['NurseWhoPreferNotFriday1Noon'] = prefer_not
				
			if cant:
				template_variables['NurseWhoCantFriday1Noon'] = cant
				
			
				
			# Saturday1 night info:
			head_nurse_want = Constrain.getShiftHeads(saturday1date, 0, 1)
			head_nurse_dont_care = Constrain.getShiftHeads(saturday1date, 0, 0)
			head_nurse_prefer_not = Constrain.getShiftHeads(saturday1date, 0, 2)
			head_nurse_cant = Constrain.getShiftHeads(saturday1date, 0, 3)
			
			want = Constrain.getCrew(saturday1date, 0, 1)
			dont_care = Constrain.getCrew(saturday1date, 0, 0)
			prefer_not = Constrain.getCrew(saturday1date, 0, 2)
			cant = Constrain.getCrew(saturday1date, 0, 3)
			
			assignBeforeHead = PreparingSchedule.checkIfAssignAlready(saturday1date, 0, 0)
			assignBeforeSecond = PreparingSchedule.checkIfAssignAlready(saturday1date, 0, 1)
			assignBeforeStandBy = PreparingSchedule.checkIfAssignAlready(saturday1date, 0, 3)
			
			if assignBeforeHead:
				template_variables['Saturday1NightAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Saturday1NightAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Saturday1NightAssignBeforeStandBy'] = assignBeforeStandBy
			
			if head_nurse_want:
				template_variables['HeadNurseWhoWantSaturday1Night'] = head_nurse_want
				
			if head_nurse_dont_care:
				template_variables['HeadNurseWhoDontCareSaturday1Night'] = head_nurse_dont_care
				
			if head_nurse_prefer_not:
				template_variables['HeadNurseWhoPreferNotSaturday1Night'] = head_nurse_prefer_not
				
			if head_nurse_cant:
				template_variables['HeadNurseWhoCantSaturday1Night'] = head_nurse_cant
				
			if want:
				template_variables['NurseWhoWantSaturday1Night'] = want
				
			if dont_care:
				template_variables['NurseWhoDontCareSaturday1Night'] = dont_care
				
			if prefer_not:
				template_variables['NurseWhoPreferNotSaturday1Night'] = prefer_not
				
			if cant:
				template_variables['NurseWhoCantSaturday1Night'] = cant
			

			
			# Saturday1 morning info:
			head_nurse_want = Constrain.getShiftHeads(saturday1date, 1, 1)
			head_nurse_dont_care = Constrain.getShiftHeads(saturday1date, 1, 0)
			head_nurse_prefer_not = Constrain.getShiftHeads(saturday1date, 1, 2)
			head_nurse_cant = Constrain.getShiftHeads(saturday1date, 1, 3)
			
			want = Constrain.getCrew(saturday1date, 1, 1)
			dont_care = Constrain.getCrew(saturday1date, 1, 0)
			prefer_not = Constrain.getCrew(saturday1date, 1, 2)
			cant = Constrain.getCrew(saturday1date, 1, 3)
			
			assignBeforeHead = PreparingSchedule.checkIfAssignAlready(saturday1date, 1, 0)
			assignBeforeSecond = PreparingSchedule.checkIfAssignAlready(saturday1date, 1, 1)
			assignBeforeStandBy = PreparingSchedule.checkIfAssignAlready(saturday1date, 1, 3)
			
			if assignBeforeHead:
				template_variables['Saturday1MorningAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Saturday1MorningAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Saturday1MorningAssignBeforeStandBy'] = assignBeforeStandBy
			
			if head_nurse_want:
				template_variables['HeadNurseWhoWantSaturday1Morning'] = head_nurse_want
				
			if head_nurse_dont_care:
				template_variables['HeadNurseWhoDontCareSaturday1Morning'] = head_nurse_dont_care
				
			if head_nurse_prefer_not:
				template_variables['HeadNurseWhoPreferNotSaturday1Morning'] = head_nurse_prefer_not
				
			if head_nurse_cant:
				template_variables['HeadNurseWhoCantSaturday1Morning'] = head_nurse_cant
				
			if want:
				template_variables['NurseWhoWantSaturday1Morning'] = want
				
			if dont_care:
				template_variables['NurseWhoDontCareSaturday1Morning'] = dont_care
				
			if prefer_not:
				template_variables['NurseWhoPreferNotSaturday1Morning'] = prefer_not
				
			if cant:
				template_variables['NurseWhoCantSaturday1Morning'] = cant
				
			
			
			# Saturday1 noon info:
			head_nurse_want = Constrain.getShiftHeads(saturday1date, 2, 1)
			head_nurse_dont_care = Constrain.getShiftHeads(saturday1date, 2, 0)
			head_nurse_prefer_not = Constrain.getShiftHeads(saturday1date, 2, 2)
			head_nurse_cant = Constrain.getShiftHeads(saturday1date, 2, 3)
			
			want = Constrain.getCrew(saturday1date, 2, 1)
			dont_care = Constrain.getCrew(saturday1date, 2, 0)
			prefer_not = Constrain.getCrew(saturday1date, 2, 2)
			cant = Constrain.getCrew(saturday1date, 2, 3)
			
			assignBeforeHead = PreparingSchedule.checkIfAssignAlready(saturday1date, 2, 0)
			assignBeforeSecond = PreparingSchedule.checkIfAssignAlready(saturday1date, 2, 1)
			assignBeforeStandBy = PreparingSchedule.checkIfAssignAlready(saturday1date, 2, 3)
			
			if assignBeforeHead:
				template_variables['Saturday1NoonAssignBeforeHead'] = assignBeforeHead
				
			if assignBeforeSecond:
				template_variables['Saturday1NoonAssignBeforeSecond'] = assignBeforeSecond
				
			if assignBeforeStandBy:
				template_variables['Saturday1NoonAssignBeforeStandBy'] = assignBeforeStandBy
			
			if head_nurse_want:
				template_variables['HeadNurseWhoWantSaturday1Noon'] = head_nurse_want
				
			if head_nurse_dont_care:
				template_variables['HeadNurseWhoDontCareSaturday1Noon'] = head_nurse_dont_care
				
			if head_nurse_prefer_not:
				template_variables['HeadNurseWhoPreferNotSaturday1Noon'] = head_nurse_prefer_not
				
			if head_nurse_cant:
				template_variables['HeadNurseWhoCantSaturday1Noon'] = head_nurse_cant
				
			if want:
				template_variables['NurseWhoWantSaturday1Noon'] = want
				
			if dont_care:
				template_variables['NurseWhoDontCareSaturday1Noon'] = dont_care
				
			if prefer_not:
				template_variables['NurseWhoPreferNotSaturday1Noon'] = prefer_not
				
			if cant:
				template_variables['NurseWhoCantSaturday1Noon'] = cant
				
					
			
			html = template.render("web/templates/MainManager.html", template_variables)
			self.response.write(html)
		
		if not userName:
			html = template.render("web/templates/LoginPage.html", template_variables)
			self.response.write(html)
			
class SaveScheduleHandler(webapp2.RequestHandler):
    def get(self):
		selectedNurse_userName = self.request.get('selectedNurse_userName')
		day = self.request.get('day')
		shift = self.request.get('shift')
		week = self.request.get('week')
		rule = self.request.get('rule')
		
		
		preparingSchedule = PreparingSchedule()
		preparingSchedule.rule = int(rule)
		preparingSchedule.nurseUserName = selectedNurse_userName
		preparingSchedule.ShiftType = int(shift)
		
		selectedDate = date.today()
		
		selectedDate = selectedDate + timedelta(days = 14)
		if(int(selectedDate.strftime("%U"))%2 == 0):
			selectedDate = selectedDate - timedelta(days = 7)
			
		
		
		if int(week) == 1:
			selectedDate = selectedDate + timedelta(days = 7)
			
		
		if selectedDate.weekday() != 6:
			selectedDate = selectedDate - timedelta(days=(selectedDate.weekday()))
			
		
		if selectedDate.weekday() == 6:
			selectedDate = selectedDate + timedelta(days=1)
			
		if int(day) == 6:
			selectedDate = selectedDate - timedelta(days=1)
		if int(day) != 6:
			selectedDate = selectedDate + timedelta(days=int(day))
		
			
		
		preparingSchedule.date = selectedDate
		
		allreadyAssign = preparingSchedule.checkIfAssignAlready1(preparingSchedule.date, int(shift), int(rule))
		
		if allreadyAssign:
			allreadyAssign.key.delete()
		
		if not preparingSchedule.checkLegalAssign_Same_Shift():
			self.response.write("Illegal! Already assigned today")
			if preparingSchedule.nurseUserName != "":
				preparingSchedule.put()
			return
			
		
		if not preparingSchedule.checkLegalAssign_Night_After_Night():
			self.response.write("Illegal! Night After Night")
			if preparingSchedule.nurseUserName != "":
				preparingSchedule.put()
			return
			
		if not preparingSchedule.checkLegalAssign_Noon_Morning_Night():
			self.response.write("Illegal! Noon-Morning-Night")
			if preparingSchedule.nurseUserName != "":
				preparingSchedule.put()
			return
			
		if not preparingSchedule.checkLegalAssign_Following_Shifts():
			self.response.write("Illegal! Following shifts ")
			if preparingSchedule.nurseUserName != "":
				preparingSchedule.put()
			return
			
		employee = Employee.getEmployeeByUserName(selectedNurse_userName)
		sunday = date.today()
		saturday = date.today()
		
		if selectedDate.weekday() == 0:
			sunday = selectedDate - timedelta(days=1)
			saturday = selectedDate + timedelta(days=5)
		if selectedDate.weekday() == 1:
			sunday = selectedDate - timedelta(days=2)
			saturday = selectedDate + timedelta(days=4)
		if selectedDate.weekday() == 2:
			sunday = selectedDate - timedelta(days=3)
			saturday = selectedDate + timedelta(days=3)
		if selectedDate.weekday() == 3:
			sunday = selectedDate - timedelta(days=4)
			saturday = selectedDate + timedelta(days=2)
		if selectedDate.weekday() == 4:
			sunday = selectedDate - timedelta(days=5)
			saturday = selectedDate + timedelta(days=1)
		if selectedDate.weekday() == 5:
			sunday = selectedDate - timedelta(days=6)
			saturday = selectedDate
		if selectedDate.weekday() == 6:
			sunday = selectedDate
			saturday = selectedDate + timedelta(days=6)
			
		if employee:
			if(employee.percentJob == 66):
				if not PreparingSchedule.checkLegalAssign_66_precent(employee.userName, sunday, saturday):
					self.response.write("Illegal! 66% - 3 shifts already")
					if preparingSchedule.nurseUserName != "":
						preparingSchedule.put()
					return
				
			if(employee.percentJob == 88):
				if not PreparingSchedule.checkLegalAssign_88_precent(employee.userName, sunday, saturday):
					self.response.write("Illegal! 88% - 4 shifts already")
					if preparingSchedule.nurseUserName != "":
						preparingSchedule.put()
					return
			
			if(employee.percentJob == 100):
				if not PreparingSchedule.checkLegalAssign_100_precent(employee.userName, sunday, saturday):
					self.response.write("Illegal! 100% - 5 shifts already")
					if preparingSchedule.nurseUserName != "":
						preparingSchedule.put()
					return
			
		
		preparingSchedule.put()
		
		constrain = Constrain.query(Constrain.employeeUN == preparingSchedule.nurseUserName, Constrain.constrainDate == preparingSchedule.date, Constrain.ShiftType == preparingSchedule.ShiftType).get()
		if constrain:
			self.response.write(json.dumps({'status':'OK','note': constrain.notes}))
		elif not constrain:
			self.response.write(json.dumps({'status':'OK','note':constrain}))
		
		
class SubmitScheduleHandler(webapp2.RequestHandler):
	def get(self):
		if not PreparingSchedule.checkLegalAssign_Assign_Head_Nurses():
			self.response.write("Must assign all head nurses")
			return
		
		allNewAssignments = PreparingSchedule.Get_All_Assignments()
		allOldAssignments = SubmittedShifts.Get_All_Assignments()
		
		if allOldAssignments:
			for a in allOldAssignments:
				a.deleteItem()
		
		if allNewAssignments:
			for a in allNewAssignments:
				submitted = SubmittedShifts()
				submitted.date = a.date
				submitted.ShiftType = a.ShiftType
				submitted.nurseUserName = a.nurseUserName
				submitted.rule = a.rule
				submitted.put()
				
		self.response.write(json.dumps({'status':'OK'}))

		
class checkSubmitSessionHandler(webapp2.RequestHandler):
	def get(self):
		isSubmitSession = Dates.submitSession()
		self.response.write(json.dumps({'status':'OK','isSubmitSession':isSubmitSession}))
		
app = webapp2.WSGIApplication([
    ('/MainManager', MainHandler),
	('/saveSchedule', SaveScheduleHandler),
	('/submitSchedule', SubmitScheduleHandler),
	('/check_submit_session', checkSubmitSessionHandler)
], debug=True)
