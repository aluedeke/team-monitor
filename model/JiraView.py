'''
Created on 25.11.2011

@author: AnLuedeke
'''
from model.Systems import ExtendedView
from google.appengine.api import urlfetch
from util.BeautifulSoup import BeautifulSoup

class JiraView(ExtendedView):

    #

    def __init__(self, name, host, username, password, filterId):
        self.name = name
        self.host = host
        self.username = username
        self.password = password
        self.failures = ""
        self.filterId = filterId

    def update(self):
        response = urlfetch.fetch("https://%s/sr/jira.issueviews:searchrequest-xml/%s/SearchRequest-%s.xml?tempMax=50&os_username=%s&os_password=%s" % (self.host, self.filterId, self.filterId, self.username, self.password), validate_certificate=False)
        soup = BeautifulSoup(response.content)

        itemCount = 0
        for item in soup.rss.channel:
            itemCount = itemCount + 1

        if itemCount == 0:
            self._on_success(itemCount)
        else:
            self._on_error(itemCount)
