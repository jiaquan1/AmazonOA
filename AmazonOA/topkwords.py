
 
from re import sub
from collections import defaultdict
import heapq
def top_k(keywords,reviews,k):
    if not k or not keywords or not reviews:
        return []
    for i,keyword in enumerate(keywords1):
        keywords1[i] = keyword.lower()
    keys = set(keywords1)
    wordcount = defaultdict(int)
    for rev in reviews:
        words = rev.lower().split(" ")
        added = set()
        for word in words:
            #print(word)
            word = sub("[^a-z]","",word)
            #print(word)
            if word in keys and word not in added:
                wordcount[word] +=1
                added.add(word)

    result = sorted(wordcount.keys(),key = lambda x: (-wordcount[x],x))
    return result[:k]



reviews1 = [
  "Anacell provides the best services in the city",
  "betacellular has awesome services",
  "Best services provided by anacell, everyone should use anacell",
]
k = 2
print(top_k(keywords1,reviews1,k))