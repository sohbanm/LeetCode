# class Solution:
#     def minCost(self, colors: str, neededTime: List[int]) -> int:
#         last = ""
#         streak = []
#         sum = 0
#         for i in range(len(colors)):
#             if colors[i] == last:
#                 streak.append(neededTime[i])
#                 minTime = min(streak)
#                 streak.remove(minTime)
#                 sum+= minTime
#             else:
#                 last = colors[i]
#                 streak.clear()
#                 streak.append(neededTime[i])
                
#         return sum

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        totalTime = 0
        n = len(colors)
        sumTime, maxTime = 0, 0
        for i in range(n):
            if (i > 0) and (colors[i - 1] != colors[i]):
                totalTime += sumTime - maxTime
                sumTime = 0
                maxTime = 0
            sumTime += neededTime[i]
            maxTime = max(maxTime, neededTime[i])

        totalTime += sumTime - maxTime
        return totalTime