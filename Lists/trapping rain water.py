# O(n) space and O(n) time
class Solution:
    def trap(self, height: list[int]) -> int:
        mLeft = []
        high = 0
        for i in range(len(height)):
            if i==0:
                mLeft.append(0)
            else:
                high = max(high, height[i-1])
                mLeft.append(high)
        mRight = []
        high = 0
        for i in reversed(range(len(height))):
            if i==(len(height)-1):
                mRight.append(0)
            else:
                high = max(high, height[i+1])
                mRight.append(high)
        
        mRight.reverse()

        total = 0
        for i in range(len(height)):
            temp = min(mLeft[i], mRight[i]) - height[i]
            if temp > 0:
                total += temp



        return total
    

# O(1) space and O(n) time 
class Solution:
    def trap(self, height: list[int]) -> int:
        maxL, maxR = height[0], height[-1]
        l, r = 0, len(height) - 1
        total = 0

        while l<r:
            if maxL <= maxR:
                l += 1
                temp = maxL - height[l]
                maxL = max(maxL, height[l])

                if temp > 0:
                    total += temp
            else:
                r -= 1
                temp = maxR - height[r]
                maxR = max(maxR, height[r])

                if temp > 0:
                    total += temp
        
        return total


