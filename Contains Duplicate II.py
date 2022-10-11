class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        checked = {}
        
        for i in range(len(nums)):
            if nums[i] in checked and abs(checked[nums[i]] - i) <=k:
                return True
            else:
                checked[nums[i]] = i
            
        return False