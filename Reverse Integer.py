class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            end = -1
        else:
            end = 1    
        x = abs(x)
        length = len(str(x))-1
    
        out = 0
        while x:
            out += (x%10) * (10**length)
            length -= 1
            x = x//10
        
        if out > (2**31)-1:
            return 0
        return out * end
        