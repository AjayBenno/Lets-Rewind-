
from urllib2 import Request, urlopen, URLError
import simplejson as json
import types,time

key="?api_key=8ec0f7d1-2a67-4cc9-a0d5-30042337ad49"
pre="https://na.api.pvp.net/"
def attempt(request):
	try:
		response = urlopen(request)
		fromWeb = response.read()		
		return fromWeb
	except URLError, e:
		print 'No kittez. Got an error code:', e
def nameAPI(name):
	request = Request(pre+"/api/lol/na/v1.4/summoner/by-name/"+name+key)
	ret=attempt(request)
	if ret!=None:
		result_object = json.loads(ret)
		return result_object
	else:
		print ("Input was bad")
def statsAPI(ID):
	request = Request(pre+"/api/lol/na/v1.3/stats/by-summoner/"+str(ID)+"/summary"+key)
	ret=attempt(request)
	if ret!=None:
		result_object = json.loads(ret)
		return result_object
	else:
		print ("Input was bad")
def getSummonerID(target):
	keys=list(target)
	return target[keys[0]]["id"]
def getSummonerLevel(target):
	keys=list(target)
	return target[keys[0]]["summonerLevel"]

name=raw_input("Put in a summoner name: ")
start=time.time()
nameAPI=nameAPI(name)
stats=statsAPI(getSummonerID(nameAPI))
obs= stats[list(stats)[0]]

totalKills=0

for ob in obs:	
	try:
		print str(ob["aggregatedStats"]["totalChampionKills"]) +" kills in "+ob["playerStatSummaryType"]
	except KeyError, e:
		continue

print totalKills
#print getSummonerID(nameAPI)
#print getSummonerLevel(nameAPI)

print "Time elapse was: "+str(time.time()-start)+" seconds"
#print "Summoner Level is: "+str(getSummonerLevel(name))32963033