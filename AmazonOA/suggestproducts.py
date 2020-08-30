class Trie:
    def __init__(self):
        self.sub = {}
        self.suggestions = []
class Solution:
    def suggestedProducts(self, products, searchWord):
        root = Trie()
        for product in sorted(products):
            trie = root
            for char in product:
                if char not in trie.sub:
                    trie.sub[char]=Trie()
                trie=trie.sub[char]
                if len(trie.suggestions)<3:
                    trie.suggestions.append(product)
        res=[]
        for w in searchWord:
            if root:
                
                root = root.sub.get(w,None)
            res.append(root.suggestions if root else [])
        return res

products = ["bags","baggage","banner","box","cloths"]
searchWord = "bags"
a= Solution()
b = a.suggestedProducts(products,searchWord)
print(b)
                

