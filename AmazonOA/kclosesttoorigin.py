class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        n = len(points)
        if n<=K:
            return points
        heap = []
        for i in range(n):
            dist = (points[i][0]**2+points[i][1]**2)**0.5
            heapq.heappush(heap,(dist,i))
        res = []
        for i in range(K):
            res.append(points[heapq.heappop(heap)[1]])
        return res
        








