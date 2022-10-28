class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def rob1(nums):
            rob1,rob2 = 0,0

            for n in nums:
                temp = max(n + rob1, rob2)
                rob1 = rob2
                rob2 = temp

            return rob2
        
        return max(nums[0], rob1(nums[:-1]), rob1(nums[1:]))