class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        total = 0
        for i in range(1, max(a,b)+1):
            if a%i == 0 and b%i == 0:
                total += 1
                
        return total