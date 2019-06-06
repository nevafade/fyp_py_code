import twitter
import json
import requests
import datetime
import os
api = twitter.Api(consumer_key='7WpfZGdrvuhsBf8n2Sa27xb7g',
                  consumer_secret='a5YE6A0DXwNEByvSkxA9WzT8IyoYjPX5xSBmZK9DlSP2mCspua',
                  access_token_key='1086125916051464192-LkOrybTgdCO6GYL0JW2ZAscv5q79H2',
                  access_token_secret='JNEfKGiDifQElw1YUMuvKPqkXCKI7IEyTnS7RaswQGW6u')


searchKeywordsFile = "certified_accounts.txt"

def archive_del():
    f = open('current.txt')
    d = f.readline()
    os.remove(d)
    print 'ARCHIVED'

def archive():
    f = open('current.txt')
    d = f.readline()
    with open(d) as json_file:
        data = json.load(json_file)
        for i in range(len(data)):
            API_ENDPOINT = "https://fakenews19-4d94a.firebaseio.com/"+d[0:len(d)-5]+"/"+str(i) 
            API_ENDPOINT_URL = API_ENDPOINT+ ".json"
            print API_ENDPOINT_URL
            r = requests.put(url = API_ENDPOINT+ ".json", data = "{ \"foo\" : \"foo\"}")
            result = r.text 
            print result
            for j in range(len(data[i])):
                API_ENDPOINT_URL = API_ENDPOINT+ "/" + str(j) + ".json"
                print API_ENDPOINT_URL
                print json.dumps(data[i][j])
                r = requests.put(url = API_ENDPOINT+ "/" + str(j) + ".json", data = json.dumps(data[i][j])) 
                result = r.text 
                print result
    
searchRespArr = []

def getSearchKeywords():
    keywordSet = ["@narendramodi","@INCIndia","@BJP4India","@BJP4Gujrat","@timesofindia","@TimesNow","@ndtv","@SpokespersonECI","@arunjaitley","@ArvindKejriwal","@SheilaDikshit","@nsitharaman","@DefenceMinIndia","@PMOIndia", "@nitin_gadkari","@OfficeOfNG","@SushmaSwaraj","@MEAIndia","@Mayawati","@MamataOfficial","@nstomar","@rajnathsingh","@PIB_India","@IAF_MCC","@IndianDiplomacy","@crpfindia","@airnewsalerts","@airnewsalerts","@DDNewsLive","@mygovindia","@rashtrapatibhvn","@MIB_India","@PiyushGoyal","@DG_PIB","@IndianExpress", "@kgahlot" , "@htTweets" ,"@the_hindu" , "@htdelhi" , "@AamAadmiParty" ,"@aajtak" ,"@IndiaToday", "@FinMinIndia", "@rajeevkumr", "@RBI", "@FollowCII","@cbic_india", "@arivalayam","@ShivSena","@AUThackeray"]
    return keywordSet
    
def triggerSearches(searchTermSet):
     for term in searchTermSet:
        tweetSearch(term)
                
def tweetSearch(searchTerm):
    if searchTerm:
        data=api.GetUserTimeline(screen_name=searchTerm, count=200)
        data_array = []
        for tweet in data:
            data_array.append(tweet._json)
        searchRespArr.append(data_array);
        print "Done fetching search results for ",searchTerm," keyword."
    else:
        print "_tweetSearch_ Search term is null or undefined."      
    
def writeAllSearchRespOnDisk(dumpFile):
    with open(dumpFile, "w") as write_file:
        json.dump(searchRespArr, write_file)


def refresh():
    archive_del()
    now = datetime.datetime.now()
    dumpFile = "true_post_dump_"+str(now)+".json"
    print dumpFile
    f = open('current.txt','w')
    f.write(dumpFile)
    dataKey = open(searchKeywordsFile)
    searchTermSet = getSearchKeywords()
    triggerSearches(searchTermSet)
    writeAllSearchRespOnDisk(dumpFile);
    
    
refresh()
  