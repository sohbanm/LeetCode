class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        cur = 0
        prefixSums = { 0 : 1}

        for n in nums:
            cur += n
            diff = cur - k

            res += prefixSums.get(diff, 0)
            prefixSums[cur] = 1 + prefixSums.get(cur, 0)

        return res