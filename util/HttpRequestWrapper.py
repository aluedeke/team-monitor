import httplib

class HttpRequestWrapper (object):
    """represents an Http Request"""
    def __init__(self):
        self.response = None

    def get_url(self, hostname, port=80, path="/"):
        connection = httplib.HTTPConnection(hostname, port)
        connection.request("GET", path)
        self.response = connection.getresponse()
        connection.close();

        return self.response;
