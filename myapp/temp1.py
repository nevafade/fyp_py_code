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
     

k = iNeedAVector("Hi im called suchismita banerjee");
print k