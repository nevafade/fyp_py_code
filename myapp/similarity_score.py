import nltk
import pandas as pd
import re, math
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


def getCounters(sentence,se2):
    #print se2
    tokens = nltk.word_tokenize(sentence)
    token2 = nltk.word_tokenize(se2)
    tagged = nltk.pos_tag(tokens)
    tag2 = nltk.pos_tag(token2)
    entities = nltk.chunk.ne_chunk(tagged)
    entity2 = nltk.chunk.ne_chunk(tag2)
    list1 = getEntityList(list(entities))
    list2 = getEntityList(list(entity2))
    #print list2
    c1 =  Counter(list1)
    c2 = Counter(list2)
    return c1,c2
#score = iNeedACosine(iNeedAVector("Avoiding peak hour traffic snarls and inconvenience to commuters, Prime Minister once again took the Delhi Metro, this time to South Delhi, on his way to the Gita Aradhana Mahotsav."),iNeedAVector("The Prime Minister travelled back by boarding delhi Metro from Kailash Colony station at 5:45pm and leaving from Khan Market Metro station at 5:56pm"))
#print(score)
def check_score(tweet,true_set):
    a = []
    for news in true_set['news']:
        score = iNeedACosine(iNeedAVector(news),iNeedAVector(tweet));
        a.append(score);
    true_set['Cosine'] = a;
    return true_set;
    
    
def getEntitySmilarityScore(tweet,similar_set,tweet_score):
    #print(tweet_score)
    for headline in similar_set['news']:
        #raw_input('press enter to continue')
        cvector1,cvector2 = getCounters(tweet,headline)
        similarity_score = iNeedACosine(cvector1,cvector2)
        #print(similarity_score)
        if similarity_score == 1 :
            tweet_score = tweet_score + 40
        elif similarity_score > 0.5 :
            tweet_score = tweet_score + 10
        elif similarity_score > 0.1 :
            tweet_score = tweet_score + 5
        #print(tweet_score)
        if tweet_score >= 150 :
            tweet_score = 100
    if(tweet_score >= 100):
        tweet_score=100
    return tweet_score
    
def getTweetScore(tweet):
    tweetscore = 0      
    true_set = pd.read_csv('true_database.csv');
    #tweet = "It is regrettable that Pakistan still continues to deny Jaish-e-Mohammed's own claim of taking ownership of Pulwama attack, says MEA's Raveesh Kumar."
    true_set = check_score(tweet,true_set);
    a = true_set['Cosine']
    a = a[ a > 0.25 ]
    similar_set = true_set[ true_set['Cosine'] > 0.25 ]
    tweetscore = tweetscore + len(similar_set)*10
    #print(similar_set)
    tweetscore = getEntitySmilarityScore(tweet,similar_set,tweetscore)
    return tweetscore


import twitter
api = twitter.Api(consumer_key='7WpfZGdrvuhsBf8n2Sa27xb7g',
                  consumer_secret='a5YE6A0DXwNEByvSkxA9WzT8IyoYjPX5xSBmZK9DlSP2mCspua',
                  access_token_key='1086125916051464192-LkOrybTgdCO6GYL0JW2ZAscv5q79H2',
                  access_token_secret='JNEfKGiDifQElw1YUMuvKPqkXCKI7IEyTnS7RaswQGW6u')


user_screen_name = '@IamAnjanDey'
timeline = api.GetUserTimeline(screen_name= user_screen_name, count=200)
#print timeline[0].text
t = 0
u = 0
for i in range(200):
    x = getTweetScore(timeline[i].text)
    if x <= 50:
        t = 1
    elif x <= 70:
        t = 9
    elif x <= 90:
        t = 10
    elif x <= 99:
        t = 11
    elif x == 100:
        t = 12
    u = (u+t)/2
    
print 'user_score :'
print u



