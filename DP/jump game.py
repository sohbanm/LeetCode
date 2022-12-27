class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        
        for i in reversed(range(len(nums))):
            if nums[i] + i >= goal:
                goal = i
        
        if goal == 0: return True
        return False
