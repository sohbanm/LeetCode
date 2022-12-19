class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        
        prefix = 1
        for n in nums[0:-1]:
            prefix *= n
            res.append(prefix)

        postfix = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]

        return res