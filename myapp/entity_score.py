import nltk
import pandas as pd
import re, math
from collections import Counter


class StringList(object): 
 
 def __init__(self, val):
    self.val = val 
 
 def __hash__(self):
    return hash(str(self.val)) 
 
 def __repr__(self):
    # Bonus: define this method to get clean output
    return str(self.val) 
 
 def __eq__(self, other):
    return str(self.val) == str(other.val)


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
        
def __leveling(sc):
    sc.sort()
    for gh in sc:
        lev = 0
        level_vector = []
        while (gh>5):
            gh=gh/5
            lev = lev + 1
        
        level_vector.append(lev)
    return level_vector

        
def __splitter(sm,val):
    l1 = sm 
    damage = 0
    en_r = []
    sm_r =[]
    sc_r =[]
    en_invalid = []
    sm_invalid = []
    sc_invalid = []
    for i in range(len(sm[0])):
        if (sm[2][i]<val):
            en_r.append(sm[0][i])
            sm_r.append(sm[1][i])
            sc_r.append(sm[2][i])
        if (sm[2][i]<0):
            en_invalid.append(sm[0][i])
            sm_invalid.append(sm[1][i])
            sc_invalid.append(sm[2][i])
            
    sm[0] = [item for item in sm[0] if item not in en_r]
    sm[1] = [item for item in sm[1] if item not in sm_r]
    sm[2] = [item for item in sm[2] if item not in sc_r]
    l_set = []
    k_set = []
    l_r_set = []
    k_r_set = []
    for i in true_entity_set :
        k = []
        l = []
        k_r = []
        l_r = []
        for en_ in sm[0]:
            if (i.count(en_)>0):
                k.append(i)
                l.append(en_)
        
        for en_ in en_r:
            if(i.count(en_)>0):
                k_r.append(i)
                l_r.append(en_)
                
        if (len(l)>0):
            l_set.append(StringList(l))
            k_set.append(StringList(k))
            
        if (len(l_r)>0):
            l_r_set.append(StringList(l_r))
            k_r_set.append(StringList(k_r))
            
    print Counter(l_r_set)
    print Counter(l_set)
    if ( ((set(k_set)& set(k_r_set))==[]) | (len(en_r)==len(en_invalid)) ):
            print 'intersection'
    else:
            damage = 1
        #for en_ in sm_r:
        #   if (i.count(en_)>0):
    
    #for en_ in sm[0]:
    #    print en_,':'
    #   for k in k_set:
    #       for k_item in k:
    #           if k_item[2]==en_ :
    #               print '...'
    
    counter_items = Counter(l_set).items()
    for item in counter_items :
        if ((len(item[0].val)>1) & (item[1]>=1)):
            for nlp_item in item[0].val:
                index = sm[0].index(nlp_item)
                sm[2][index] = sm[2][index] + item[1]*300
                
    
    sm[0].extend(en_r)
    sm[1].extend(sm_r)
    sm[2].extend(sc_r)
    if ((damage == 1)&(len(en_r)>0)):
        for i in range(len(sm[0])):
            if (sm[2][i]>0) : sm[2][i] = 0
    return sm
     
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
        return getEntityList(en_list)
        

        
true_set = pd.read_csv('true_database_4_6_2019.csv');
true_entity_set = [] 
#sentence2 = "The Prime Minister travelled back by boarding delhi Metro from Kailash Colony station at 5:45pm and leaving from Khan Market Metro station at 5:56pm"
for sentence2 in true_set['news']:
    tokens2 = nltk.word_tokenize(sentence2)
    tagged2 = nltk.pos_tag(tokens2)
    e2 = nltk.chunk.ne_chunk(tagged2)
    true_entity_set.append(getEntityList(list(e2)))
    
        
        


sentence = "In the run up to the Lok Sabha elections this year, the term vote bank politics has been used many times by politicians, journalists, election"
tokens = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)
e = nltk.chunk.ne_chunk(tagged)
x = []
e_score = []
g = getEntityList(list(e));
g_r = []
for nlp_entity in g:
    if ((nlp_entity[1] == 'IN') |(nlp_entity[1] == 'CC')|(nlp_entity[1] == 'DT')| (nlp_entity[1] == '.')|(nlp_entity[1] == ',')|(nlp_entity[1] == ':')):
        g_r.append(nlp_entity)
g = [item for item in g if item not in g_r]
for e in g:
    count = 0
    similar_entity_set = []
    score = 0
    for i in true_entity_set :
        count = count + i.count(e)
        if i.count(e) > 0:
            similar_entity_set.append(i)
    print count
    if (count == 0):
        score = score - 5000
    x.append(similar_entity_set)
    e_score.append(score)

sm = []
sm.append(g)
sm.append(x)
sm.append(e_score)
for i in range(len(sm[0])):
    for j in sm[1][i]:
        if (iNeedACosine(Counter(g),Counter(j))>0.09) :
            sm[2][i] = sm[2][i] + 60

print '.........................................................................'
for i in range(len(sm[0])):
    print sm[0][i], ':' ,sm[2][i]
print '.........................................................................'
sm = __splitter(sm,0)
for i in range(len(sm[0])):
   print sm[0][i], ':' ,sm[2][i]
   
level_vector=__leveling(sm[2])
priveledge = sum([p for p in sm[2] if p>0])
cookie_jar_full = 25000.00
cookie_jar = 25000

def __eat_cookies(jar,level,priveledge):
    cut = 12-level
    cookies = priveledge/(cut*cut)
    jar = jar - cookies
    return jar
    
    
for lev in level_vector: cookie_jar=__eat_cookies(cookie_jar,lev,priveledge) 
print cookie_jar_full-cookie_jar
print ((cookie_jar_full-cookie_jar)/cookie_jar_full)*100

    


#search_score,similar_set = getSearchScore( entity )
#relevence_score = getRelevenceScore()