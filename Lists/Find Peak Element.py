class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        
        while l<=r:
            mid = (l+r)//2
            
            left = nums[mid-1] if mid-1!=-1 else float("-inf")
            right = nums[mid+1] if mid+1!=len(nums) else float("-inf")
            if left<nums[mid]:
                if nums[mid]>right:
                    return mid
                else:
                    l = mid + 1
            else:
                r = mid - 1
                
                
                