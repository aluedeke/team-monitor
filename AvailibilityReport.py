'''
Created on 06.09.2011

@author: AnLuedeke
'''

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
import datetime
import httplib
import os

import settings


class System(object):
	print

def get_url(host, path):
	connection = httplib.HTTPConnection(host)
	connection.request("GET", path)
	response = connection.getresponse()
	connection.close();
	
	return response;
	
def get_url_availibility(host, path):
	response = get_url(host, path);
	return response.status

def get_system_availibility(host):
	api = get_url_availibility(host, "/restapi/api/search/v1.0/internal")
	mt = get_url_availibility(host, "/restapi/api/search/v1.0/internal/mt")
	db = get_url_availibility(host, "/restapi/api/search/v1.0/internal/db")

	if api == 200 & mt == 200 & db ==200:
		return "SUCCESS"
	else:
 		status = "ERROR"
		if api != 200:
			status = api
		if mt != 200:
			status = mt
		if db != 200:
			status = db
		return status

def get_system_version(host):
	response = get_url(host, "/restapi/api/search/v1.0/internal/version")
	version = response.read();
	
	return version;

def get_latest_system_status():
	systemNames = settings.TRACKED_SYSTEMS
	systems = []
	for systemname in systemNames:
		system = System()
		systemsetting = systemname.split("|")
		system.name = systemsetting[0];
		try:
			system.url = "http://" + systemsetting[1] + "/restapi/api/search/v1.0/internal"
			system.status = get_system_availibility(systemsetting[1]);
			system.version = get_system_version(systemsetting[1])
		except Exception:
			system.status = "ERROR"
			
		if system.status == "SUCCESS":
			system.status_color = "green"
		else:
			system.version = system.status
			system.status = "ERROR"
			system.status_color = "red"
		
		
		systems.append(system)

	return systems;

class AvailibilityReport(webapp.RequestHandler):
			
	def get(self):
		systems = get_latest_system_status()
		
		template_values = {
		             'systems': systems,
					 'last_loaded': datetime.datetime.now().strftime("%b %d %I:%M %p ")
		}
		
		path = os.path.join(os.path.dirname(__file__), 'dashboardAvailibility.html')
		self.response.out.write(template.render(path, template_values))
