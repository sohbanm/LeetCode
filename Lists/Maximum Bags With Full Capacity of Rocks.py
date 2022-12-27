class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], addRs: int) -> int:
        diff = [] #number of rocks short each bag is
        for i in range(len(rocks)):
            diff.append(capacity[i] - rocks[i])
        
        diff.sort()
        total = 0
        
        for num in diff:
            if num == 0:
                total += 1
            elif addRs - num >= 0:
                addRs -= num
                total += 1
            else:
                break
        
        return total