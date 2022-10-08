class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        l, r = 1, n-1
        
        while True:
            if '0' in str(l) or '0' in str(r):
                l += 1
                r -= 1
            else:
                return [l, r]
