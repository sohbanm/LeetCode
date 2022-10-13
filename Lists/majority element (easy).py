class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for k,v in count.items():
            if len(nums)/2 <=v:
                return k
        