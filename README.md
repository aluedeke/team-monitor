Team Monitor
===============

Shows a dashbord with the
- availability states and the
- teamcity results
for the relevant API systems/hosts.
 

Installation
------------

1. Local development installation
---------------------------------
a) Install Python >= 2.7
b) Install Latest GAE (Google App Engine) SDK
c) Install Eclipse with the plugins 
   - PyDev 
   + GAE
	 + Subclipse
d) Checkout svn://svn.iscout.local/intern/spielwiese/team-api/org/team-monitor
e) Adapt .pydevproject:
	 + set your own GOOGLE_APP_ENGINE path

2. Runtime system
-----------------
a) Install Python >= 2.7
b) Install GAE SDK
c) Checkout svn://svn.iscout.local/intern/spielwiese/team-api/org/team-monitor
b) user --use_sqlite parameter for better performance

	 
Usage
-----
1. Run locally in development environment
-----------------------------------------
a) Eclipse/PyDev Perspective: Run as -> PyDev Google App Run
   
   This starts the local webservice 
   		${GOOGLE_APP_ENGINE}/dev_appserver.py
   at localhost:8080. 
   The port can be changed in the run-configuration with the --port option.

b) Browser: 
	 http://localhost:8080/
	 
2. Runtime system
------------------
a) Start the local webservice 
   		${GOOGLE_APP_ENGINE}/dev_appserver.py
   at localhost:8080. 
   The port can be changed in the run-configuration with the --port option.

b) Browser: 
	 http://localhost:8080/


Classes
-------
1. Application logic
	 main.py <- configuration: settings.py
		-> AvailibilityReport.py (Model) + AvailibilityReport.html (View)
		
2. Runtime configuration:
	 - app.yaml
	 - cron.yaml
		
3. Helpers:
	 - BeautifulSoup.py: XML/HTML parser


Testing
-------
TODO 


Original Source:
-----------------
This code is adapted from:
http://github.com/socialize


