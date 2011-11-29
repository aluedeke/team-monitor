'''
Created on 22.11.2011

@author: AnLuedeke
'''
from model.Systems import ExtendedView

import urllib2
import simplejson

class JenkinsView(ExtendedView):

    def __init__(self, name, host, path, job):
        self.name = name
        self.host = host
        self.path = path
        self.job = job

    def update(self):
        response = urllib2.urlopen('http://%s%s/job/%s/lastBuild/api/json?tree=actions[failCount],result' % (self.host, self.path, self.job))
        responseObject = simplejson.load(response)

        if(responseObject['result'] == 'SUCCESS'):
            self._on_success("OK")
        else:
            self._on_error("ERROR")

        for action in responseObject['actions']:
            if action != None and action.get('failCount') != None:
                self.failures = action['failCount']



