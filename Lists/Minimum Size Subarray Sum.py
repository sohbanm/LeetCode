# class Solution:
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         total, low = 0, float('inf')
#         last = []  #recording the last subarray
#         i = 0
#         while i<len(nums):
#             if nums[i]>=target:
#                 return 1
#             if (total + nums[i])>target:
#                 low = min(low, len(last)+1)
#                 total -= last.pop(0)
#                 continue
#             last.append(nums[i])
#             if(total + nums[i] == target):
#                 low = min(low, len(last))
#             total += nums[i]
#             i+=1
            
#         if low == float('inf'):
#             return 0
#         return low

#Same Method as above except taken advantage of the while loop and used 2 pointers decreasing the memory
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total = 0, 0
        res = float("inf")

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(r - l + 1, res)
                total -= nums[l]
                l+=1
        
        return 0 if res== float('inf') else res