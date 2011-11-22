'''
Created on 06.09.2011

@author: AnLuedeke
'''
import os
import datetime

import team.api as settings

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

class Dashboard(webapp.RequestHandler):

	def get(self):
		title = settings.TITLE
		systems = settings.SYSTEMS

		self.__update(systems)

		template_values = {
					 'title' : title,
		             'systems': systems,
					 'last_loaded': datetime.datetime.now().strftime("%b %d %I:%M %p ")
		}

		path = os.path.join(os.path.dirname(__file__), 'Dashboard.html')
		self.response.out.write(template.render(path, template_values))

	def __update(self, systems):
		for system_row in systems:
			for system in system_row:
				system.update()
