#Brute force -- TLE
# class Solution:
#     def climbStairs(self, n: int) -> int:
        
#         def stairHelper(n, num):
#             print(num)
#             if num==n:
#                 return 1
#             if num+2<=n:
#                 return stairHelper(n, num+2) + stairHelper(n,num+1)
#             else:
#                 return stairHelper(n,num+1)
        
#         return stairHelper(n, 0)
    
#DP - Bottom up
class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1,1

        for i in range(n-1):
            temp = one
            one+=two
            two = temp

        return one