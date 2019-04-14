import json
import csv
import re


def ___handle__error(text,lang):
    if((lang == 'en')|(lang == 'in')|(lang == 'ro')|(lang == 'sv')|(lang == 'da')|(lang == 'et')|(lang == 'tl')):
        try:
            writer.writerow({'news': text,'fakeness':'1'})
        except UnicodeEncodeError as e :
            out_of_bound_char = text[e.start]
            ___handle__error(re.sub(out_of_bound_char,'?',text),lang)
         
f = open('true_post_4_6_2019.txt','r');
f_debug = open('debug.txt','a');
tweet_array_data = f.read();
tweet_django_array = [];
#tweet_array_data = "{\"glossary\":{\"title\": \"example glossary\",\"GlossDiv\":{\"title\": \"S\",\"GlossList\":{\"GlossEntry\":{\"ID\": \"SGML\",\"SortAs\": \"SGML\",\"GlossTerm\": \"Standard Generalized Markup Language\",\"Acronym\": \"SGML\",\"Abbrev\": \"ISO 8879:1986\",\"GlossDef\":{\"para\": \"A meta-markup language, used to create markup languages such as DocBook.\",\"GlossSeeAlso\": [\"GML\", \"XML\"]},\"GlossSee\": \"markup\"}}}}}"
tweet_array = json.loads(tweet_array_data)
print len(tweet_array)
for tweet_sub_array in tweet_array:
    print len(tweet_sub_array)
    for tweet in tweet_sub_array:
        tweet_django_array.append([tweet['text'],tweet['lang']])
        

with open('true_database_4_6_2019.csv', 'w') as csvfile:
    fieldnames = ['news', 'fakeness']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    u2026_char = tweet_django_array[2][0][115]
    u20b9_char = tweet_django_array[12][0][38]
    for ob in tweet_django_array :
        print tweet_django_array.index(ob)
        ___handle__error(ob[0],ob[1])
        

         
         
         