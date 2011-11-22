'''
Created on 09.11.2011

@author: AnLuedeke
'''

class BaseView(object):

    def update(self):
        raise NotImplementedError;

class MinimalView(BaseView):

    status = ""
    message = ""

    view = "./view/minimalSystem.html"

    def __init__(self, name, host, port=80, path="/"):
        self.name = name
        self.host = host
        self.port = port
        self.path = path
        self.url = "http://%s:%d%s" % (host, port, path)

    def _on_success(self, message=""):
        self.status = "OK"
        self.message = message

    def _on_error(self, message="?"):
        self.status = "ERROR"
        self.message = message

class ExtendedView(MinimalView):

    failures = 0

    view = "./view/extendedSystem.html"

class MinimalTeamcityView(MinimalView):

    def __init__(self, name, host, port=80, path="/", teamcity=None):
        MinimalView.__init__(self, name, host, port, path)
        self.teamcity = teamcity

    def update(self):
        if self.teamcity != None:
            failures = self.teamcity._determine_number_of_failures()
            if failures == 0 :
                self._on_success("%d Errors" % failures)
            elif failures == -1:
                self._on_success()
            else:
                    self._on_error("%d Errors" % failures)

class EmtyMinimalView(MinimalView):
    name = "-"
    status = "OK"
    message = ""

    def __init__(self, name="-"):
        self.name = name

    def update(self):
        return

class EmtyExtendedView(ExtendedView):
    name = "-"
    status = "OK"
    message = ""
    failures = -1

    def __init__(self, name="-"):
        self.name = name

    def update(self):
        return
