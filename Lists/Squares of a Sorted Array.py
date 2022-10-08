class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        l, r = 0, len(nums) -1
        squares = []
 
        while l<= r:
            left,right = nums[l], nums[r]
            print(squares)
            if abs(left) > abs(right):
                squares.append(left**2)
                l+=1
            else:
                squares.append(right**2)
                r-=1
        print(squares[::-1])
        return squares[::-1]

sol = Solution()
sol.sortedSquares(nums = [-4,-1,0,3,10])