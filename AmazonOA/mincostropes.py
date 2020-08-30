import heapq
def mincostropes(ropes):
    if not ropes or len(ropes)==1:
        return 0
    minheap = []
    for rope in ropes:
        heapq.heappush(minheap,rope)
    cost = 0
    while len(minheap)>1:
        a, b =heapq.heappop(minheap),heapq.heappop(minheap)
        cost += a+b
        heapq.heappush(minheap,a+b)
    return cost 

ropes = [2, 2, 3, 3]

print(mincostropes(ropes))



