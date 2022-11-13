class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        low = nums[0]
        
        while l<=r:
            mid = (l+r)//2
            low = min(low, nums[mid])
            
            if nums[l] <= nums[mid]:
                if l!=0 and nums[l] < low:
                    return nums[l]
                l = mid + 1
            else:
                r = mid - 1
        
        return low