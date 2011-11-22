import urllib2

from util.BeautifulSoup import BeautifulSoup

class SoupRequestWrapper (object):

    def get_url_as_soup(self, teamcity, path):
        url = self._get_url(teamcity, path)
        return BeautifulSoup(url)

    def _get_url(self, teamcity, path):
        url = teamcity.url + path
        passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
        passman.add_password(None, url, teamcity.username, teamcity.password)
        authhandler = urllib2.HTTPBasicAuthHandler(passman)
        opener = urllib2.build_opener(authhandler)
        urllib2.install_opener(opener)
        return urllib2.urlopen(url, data=None, timeout=60).read()
