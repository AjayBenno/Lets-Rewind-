import urllib2
import json
import types,time

key="?api_key=8ec0f7d1-2a67-4cc9-a0d5-30042337ad49"
pre="https://na.api.pvp.net/"
def nameAPI(name):
	request = pre+"/api/lol/na/v1.4/summoner/by-name/"+name+key
	try:
		json_obj= json.load(urllib2.urlopen(request))
		return json_obj
	except urllib2.HTTPError,e:
		raise ValueError('Exception raised '+ str(e))
def getSummonerID(target):
	keys=list(target)
	return target[keys[0]]["id"]
def leagueAPI(ID):
	request= pre+'/api/lol/na/v2.5/league/by-summoner/'+str(ID)+key
	try:
		json_obj= json.load(urllib2.urlopen(request))
		return json_obj
	except urllib2.HTTPError,e:
		raise ValueError('Exception raised '+ str(e) +' This summoner is most likely not ranked.')
input = raw_input("Enter a ranked summoner name: ")
ID=getSummonerID(nameAPI(input)) #gets you summoner ID. If you need to make more calls to nameAPI then have nameAPI go straight into an object
league_obj=leagueAPI(ID)
people= league_obj[str(ID)][0]["entries"]
toprint=None
for person in people:#prints current tier/div of player
	if person["playerOrTeamName"]==input:
		line= "%s %s, %d wins and %d losses"%(league_obj[str(ID)][0]["tier"], person["division"], person["wins"], person["losses"])
		print line
		print "This summoner's id is %d"%(person["
