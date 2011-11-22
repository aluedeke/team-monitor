TEAMCITY_HOST = [None]

class TeamCityHost(object):

    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password

from sets import Set
from util.SoupRequestWrapper import SoupRequestWrapper

class Teamcity(object):

    def __init__(self, projects=[], buildTypes=[]):
        self.buildTypes = Set()
        self.buildTypes = Set(buildTypes).union(self.__get_buildtypes(projects))

    def _determine_number_of_failures(self):
        if TEAMCITY_HOST[0] == None:
            return -1

        return self.__get_number_of_failing_builds()

    def __get_buildtypes(self, projects):
        buildTypes = Set()
        for project in projects:
            for buildType in self.__get_buildtypes_for_project(project):
                buildTypes.add(buildType)

        return buildTypes

    def __get_buildtypes_for_project(self, project):
        buildTypes = []
        soup = SoupRequestWrapper().get_url_as_soup(TEAMCITY_HOST[0], "/httpAuth/app/rest/projects/id:%s" % (project))
        if (soup is not None and soup.project is not None and soup.project.buildtypes is not None):
            for buildType in soup.project.buildtypes:
                buildTypes.append(buildType['id'])

        return buildTypes

    def __get_number_of_failing_builds(self):
        if self.buildTypes != None and len(self.buildTypes) == 0:
            return -1

        failingBuilds = 0
        for buildTypeId in self.buildTypes:
            buildType = self.__get_last_build_status(buildTypeId)
            if not buildType:
                failingBuilds += 1

        return failingBuilds

    def __get_last_build_status(self, buildType):
        soup = SoupRequestWrapper().get_url_as_soup(TEAMCITY_HOST[0], "/httpAuth/app/rest/buildTypes/id:%s/builds/count:1" % (buildType))

        if soup is not None and hasattr(soup, 'build') and soup.build['status'] == 'SUCCESS':
            return True
        else:
            return False
