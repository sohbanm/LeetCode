#Hashmap Method
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_map={}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums_map.keys():
                return [nums_map[diff]+1, i+1]
            nums_map[nums[i]] = i

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