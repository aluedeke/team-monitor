#Your TeamCity Base URL. No trailing slash. Example: http://www.yourname.com
BASE_TC_URL = "http://devtcy.rz.is24.loc:8111"

#Team City user login information
TC_USERNAME = "user"
TC_PW = "password"

#HTML <EMBED> code of a sound file to play if there is a build error
#Example: <embed src="http://www.sounds.com/yoursound.wav"  autoplay="true" autostart="True" type="audio/wav" style="width:1px;height:1px" loop="true" />"""
EMBED_SOUND_HTML = """<embed src="yoursound.wav"  autoplay="true" autostart="True" type="audio/wav" style="width:1px;height:1px" loop="true" />"""

#List of TeamCity build ids that you want to track
TRACKED_BUILD_IDS = []

TRACKED_SYSTEMS = ["Production|rest.immobilienscout24.de", "Sandbox|sandbox.immobilienscout24.de", "Devbas 03|devbas03.be.test.is24.loc:9120", "Preview 1|rest.preview1.de", "Preview 2|rest.preview2.de"]

#Google API key used to generate graphs. 
#You may need to generate your own if you have not already done so on google
GOOGLE_API_KEY = ""
