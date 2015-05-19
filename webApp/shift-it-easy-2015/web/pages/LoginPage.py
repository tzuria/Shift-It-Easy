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
from models.employee import employee
from google.appengine.ext.webapp import template
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self, args=None):
		template_params = {"args":args}
		html = template.render("web/templates/LoginPage.html", template_params)
		self.response.write(html)
		
		e = employee()
		e.workerID = "123"
		e.workerType = "manager"
		e.firstName = "Tzuria"
		e.lastName = "Rinenberg"
		e.userName = "Tzurish"
		e.password = "1234"
		e.percentJob = 12.5
		e.shiftHead = True
		e.put()
		
app = webapp2.WSGIApplication([
    ('/(.*)', MainHandler)
], debug=True)
