# 853. Car Fleet
# https://leetcode.com/problems/car-fleet/

# my answer, has to do 2 passes to compute the times first
class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        combined = sorted(zip(position, speed))
        
        reached = []
        for i in range(len(position)):
            reached.append((target - combined[i][0]) / combined[i][1])
        
        i = len(reached) - 2
        fleets = len(reached)

        while i >= 0:
            if reached[i] <= reached[i + 1]:
                reached.pop(i)
                fleets -= 1
            i -= 1
            
        return fleets


# better answer, does it in one pass using a stack

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        combined = sorted(zip(position, speed))

        stack = []
        for p, s in combined[::-1]:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)