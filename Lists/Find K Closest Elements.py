# I don't even understand this tbh, neetcode solution
#more intuitive is to find the closest element with binary search then using 2 pointers go away from the value

class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        l, r = 0, len(arr) - k

        while l < r:
            m = (l + r) // 2
            if x - arr[m] > arr[m + k] - x:
                l = m + 1
            else:
                r = m

        return arr[l:l+k]
