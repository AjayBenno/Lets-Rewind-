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
input = raw_input("Enter a summoner name: ")

nameOBJ= nameAPI(input) #gets you summoner ID. If you need to make more calls to nameAPI then have nameAPI go straight into an object
LEVEL=nameOBJ[list(nameOBJ)[0]]["summonerLevel"]
ID=getSummonerID(nameOBJ)
if LEVEL<30:
	print '%s is currently at level %d and is unranked'%(input,LEVEL)
	quit()
league_obj=leagueAPI(ID)
people= league_obj[str(ID)][0]["entries"]

for person in people:#prints current tier/div of player
	if person["playerOrTeamId"] == league_obj[str(ID)][0]["participantId"]:
		line= "%s is currently in %s %s with %d wins and %d losses"%(person["playerOrTeamName"],league_obj[str(ID)][0]["tier"], person["division"], person["wins"], person["losses"])
		print line
		line2 = 'This summoner has %dLP' %(person["leaguePoints"])
		if(person["leaguePoints"] ==100):
			line2 += ' and is in Promos. Currently has %d wins and %d losses and needs %d wins to advance.'%(person['miniSeries']['wins'],person['miniSeries']['losses'],person['miniSeries']['target'])
		print line2
		#print "This summoner's id is %s"%(league_obj[str(ID)][0]["participantId"])
		break
