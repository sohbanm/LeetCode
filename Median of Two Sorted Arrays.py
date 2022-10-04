class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        evenIndex = None
        oddIndex = None
        total = len(nums1) + len(nums2)
        if total%2 != 0:
            oddIndex= total // 2
        else:
            evenIndex = total//2

        count, count1, count2 = 0, 0, 0
        
        newArr = []
        while True:
            A = nums1[count1] if count1 < len(nums1) else float("infinity")
            B = nums2[count2] if count2 < len(nums2) else float("infinity")

            if A < B:
                newArr.append(A)
                count1 += 1
            elif (A > B):
                newArr.append(B)
                count2 += 1
            else:
                newArr.append(A)
                count1 += 1
                newArr.append(B)
                count2 += 1
            if count == oddIndex:
                return newArr[count]
            if count == evenIndex:
                return (newArr[count] + newArr[count-1]) /2 
            count+=1
