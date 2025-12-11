# 128. Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/

# my solution
#  this was n log n because of the sort, so it can be better

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0

        nums = list(set(nums))
        nums.sort()
        print(nums)

        high = 1
        temp = 1

        for i in range(1, len(nums)):
            if nums[i] - 1 == nums[i - 1]:
                temp += 1
            else:
                high = max(high, temp)
                temp = 1

        return max(high, temp)

# better solution from neetcode
# this one is o(n) using a set to check for starts of sequences
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in numSet: # only start counting if n is the start of a sequence
                temp = 0
                while (n + temp) in numSet: # count up from n until the sequence ends, temp is growing
                    temp += 1
                longest = max(temp, longest)

        return longest