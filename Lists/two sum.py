class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        allNums = {}
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in allNums:
                return [allNums[diff],i]
            else:
                allNums[nums[i]] = i 