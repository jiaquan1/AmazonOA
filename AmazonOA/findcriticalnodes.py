
def isconnected(graph):
    trav= set()
    start = None
    for k in graph:
        start = k
        break
    def dfs(node):
        trav.add(node)
        for child in graph[node]:
            if child not in trav:
                dfs(child)
        return
    dfs(start)
    if len(trav)== len(graph):
        return True
    return False

def getgraph(numnode,edges):
    g = {}
    for n in range(numnode):
        g[n]=[]
    for edge in edges:
        g[edge[0]].append(edge[1])
        g[edge[1]].append(edge[0])
    return g

def findcriticalnodes(numnode,edges):
    ans = []
    for n in range(numnode):
        g= getgraph(numnode,edges)
        del g[n]
        for node in g:
            if n in g[node]:
                g[node].remove(n)
        if not isconnected(g):
            ans.append(n)
    return ans

numnode = 7
edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]
print(findcriticalnodes(numnode,edges))