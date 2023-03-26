# #still dont understand this properly
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         dp = [False] * (len(s) + 1)
#         dp[len(s)] = True

#         for i in range(len(s) - 1, -1, -1):
#             for w in wordDict:
#                 if (i + len(w)) <= len(s) and s[i:i + len(w)] == w:
#                     dp[i] = dp[i + len(w)]
#                 if dp[i]:
#                     break

#         return dp[0]
def sumOf2DArray(nums2D):
    visited = set()

    def bfs(x, y):
        if ((x,y) in visited) or (x == len(nums2D) or x < 0) or (y == len(nums2D[0]) or y < 0):
            return 0
        print(x,y)
        visited.add((x,y))
        return bfs(x, y+1) + bfs(x, y-1) + bfs(x+1, y) + bfs(x-1, y) + nums2D[x][y]
    
    return bfs(0,0)

array =[ \
    [1,2,3], \
    [1,2,3], \
    [1,2,3] \
]
print(array)
print(sumOf2DArray(array))
