class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        output = []
        i,j = 0,0
        nums1.sort()
        nums2.sort()
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                i+=1
            elif nums1[i]> nums2[j]:
                j+=1
            else:
                output.append(nums1[i])
                i+=1
                j+=1
        
        return output

sol = Solution()
sol.intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4])