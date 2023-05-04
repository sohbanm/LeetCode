import heapq

#would be optimal solution if heapq just implemented a _heappush_max function
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heapq._heapify_max(stones)
        while len(stones) > 1:
            y = heapq._heappop_max(stones)
            x = heapq._heappop_max(stones)
            if y != x:
                heapq._heappush_max(stones, y - x)
        
        if len(stones) == 0:
            return 0
        return stones[0]

#cringe solution cuz i have to heapify again
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heapq._heapify_max(stones)
        while len(stones) > 1:
            y = heapq._heappop_max(stones)
            x = heapq._heappop_max(stones)
            if y != x:
                heapq.heappush(stones, y - x)
                heapq._heapify_max(stones)
        
        if len(stones) == 0:
            return 0
        return stones[0]

#another solution to use a min heap would be multiplying all values by -1
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0])

# sol = Solution()
# print(sol.lastStoneWeight(stones = [2,7,4,1,8,1]))

