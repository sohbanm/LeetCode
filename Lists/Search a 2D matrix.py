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
                

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        check = []

        while l <= r:
            m = (l + r) // 2
            if matrix[m][0] > target:
                r = m - 1
            elif matrix[m][-1] < target:
                l = m + 1
            else:
                check = matrix[m]

        l, r = 0, len(check) - 1
        while l <= r:
            m = (l + r) // 2
            if check[m] > target:
                r = m - 1
            elif check[m] < target:
                l = m + 1
            else:
                return True
        
        return False
        
s1 = Solution()
print(s1.searchMatrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 10))
