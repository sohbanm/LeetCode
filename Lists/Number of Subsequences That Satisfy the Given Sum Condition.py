class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        nums.sort()
        res = 0
        mod = (10**9 + 7)

        r = len(nums) - 1
        for l, left in enumerate(nums):
            while left + nums[r] > target and l <= r:
                r -= 1
            if l <= r:
                res += 2** (r - l) 
                res %= mod

        return res 