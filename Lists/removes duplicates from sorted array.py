# from typing import Counter


# class Solution:
#     def removeDuplicates(self, nums):
#         count = Counter(nums)
#         distinct = list(count.keys())
#         distinct.sort()
        
#         return distinct

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l,r = 0,1
        
        while r<len(nums):
            if nums[l]==nums[r]:
                nums.pop(r)
            else:
                l+=1
                r+=1
        return len(nums)
        
        
sol = Solution()

print(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))