# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         l,r = 0, len(matrix)-1
        
#         while l<=r:
#             mid = (l+r) // 2
#             if matrix[mid][0]<target:
#                 left, right = 0, len(matrix[mid])-1
#                 while left<=right:
#                     middle = (left+right)//2
#                     if matrix[mid][middle]==target:
#                         return True
#                     if matrix[mid][middle]<target:
#                         left = middle+1
#                     else:
#                         right = middle-1 
#                 l = mid + 1
#             elif matrix[mid][0]>target:
#                 r = mid - 1
#             else:
#                 return True
            
#         return False
print(0//1)