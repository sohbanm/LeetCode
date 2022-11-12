class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1
        res = [-1,-1]
        while l <= r:
            mid = (l+r)//2
            if nums[mid]>target:
                r = mid - 1
            elif nums[mid]<target:
                l = mid + 1
            else:
                first = last = mid
                while first>-1 and nums[first]==target:
                    res[0] = first
                    first-=1
                while last<len(nums) and nums[last]==target:
                    res[1] = last
                    last+=1
                break
        return res
    