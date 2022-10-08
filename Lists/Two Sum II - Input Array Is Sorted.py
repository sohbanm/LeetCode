#Two Pointers method
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        l,r = 0, len(nums)-1

        while l<=r:
            sum = nums[l] + nums[r]
            if sum > target:
                r-=1
            elif sum < target:
                l+=1
            else:
                return [l+1,r+1]
        
sol= Solution()
sol.twoSum(nums = [-1,0], target = -1)