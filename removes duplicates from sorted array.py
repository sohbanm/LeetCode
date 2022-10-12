from typing import Counter


class Solution:
    def removeDuplicates(self, nums):
        count = Counter(nums)
        distinct = list(count.keys())
        distinct.sort()
        
        return distinct
        
sol = Solution()

print(sol.removeDuplicates([1,1,2]))