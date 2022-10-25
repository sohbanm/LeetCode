class Solution:
    def maxArea(self, height: List[int]) -> int:
        high = 0
        l,r = 0,len(height)-1
        while l<r:
            high = max(min(height[l],height[r])*(r-l), high)
            if height[l] > height[r]:
                r-=1
            else:
                l+=1
        return high