import nltk
import numpy
import re,math
from collections import Hashable
from nltk.tree import Tree
from collections import Counter
WORD = re.compile(r'\w+')
def iNeedACosine(v1, v2):
    intersection = set(v1.keys()) & set(v2.keys())
    nume = sum([v1[x] * v2[x] for x in intersection])
    test1 = sum([v1[x]**2 for x in v1.keys()])
    test2 = sum([v2[x]**2 for x in v2.keys()])
    den = math.sqrt(test1) * math.sqrt(test2)
    if not den:
        return 0.0
    else:
        return float(nume) / den
        
def iNeedAVector(text):
     words = WORD.findall(text)
     return Counter(words)
     
     
     
def getEntityList(en_list):
    c=0
    for entity in en_list :
        if type(entity) is nltk.tree.Tree:
            c=c+1
            #print entity.leaves()
            for leaf in entity.leaves():
                #leaf.append(en._label)
                #print type(leaf)
                en_list.append(leaf)
                #print type(leaf)
            del en_list[en_list.index(entity)]
    if c==0:
        return en_list
    else:
        getEntityList(en_list)
sentence = """At eight o'clock on Thursday morning Arthur didn't feel very good."""
se2 = "Avoiding peak hour traffic snarls and inconvenience to commuters, Prime Minister once again took the Delhi Metro, this time to South Delhi, on his way to the Gita Aradhana Mahotsav"


#c1,c2 = getCounters(sentence,se2)
import twitter
api = twitter.Api(consumer_key='7WpfZGdrvuhsBf8n2Sa27xb7g',
                  consumer_secret='a5YE6A0DXwNEByvSkxA9WzT8IyoYjPX5xSBmZK9DlSP2mCspua',
                  access_token_key='1086125916051464192-LkOrybTgdCO6GYL0JW2ZAscv5q79H2',
                  access_token_secret='JNEfKGiDifQElw1YUMuvKPqkXCKI7IEyTnS7RaswQGW6u')


user_screen_name = '@htTweets'
timeline = api.GetUserTimeline(screen_name= user_screen_name, count=200)
#print timeline[0].text
#for i in range(200):
    #print i
    #print "Tweet Score :"+getTweetScore(timeline[i].text)

for i in range(190):
    print i
    tokens = nltk.word_tokenize(timeline[i].text)
    tagged = nltk.pos_tag(tokens)
    entities = nltk.chunk.ne_chunk(tagged)
    list1 = getEntityList(entities)
    l = Counter(list1)
    

