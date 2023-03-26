# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         nums.sort()

#         for i,a in enumerate(nums):
#             if i>0 and a==nums[i - 1]:
#                 continue

#             l,r = i+1, len(nums)-1
#             while l<r:
#                 threeSum = a + nums[l] + nums[r]
#                 if threeSum > 0:
#                     r-=1
#                 elif threeSum<0:
#                     l+=1
#                 else:
#                     res.append([a,nums[l],nums[r]])
#                     l+=1
#                     while nums[l] == nums[l-1] and l<r:
#                         l+=1

#         return res
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
