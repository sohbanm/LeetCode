import heapq
import math

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        distances = []

        for i in range(len(points)):
            x, y = points[i]
            distances.append((math.sqrt(x**2 + y**2), i))
        
        heapq.heapify(distances)
        res = []
        for i in range(k):
            res.append(points[heapq.heappop(distances)[-1]])
        
        return res