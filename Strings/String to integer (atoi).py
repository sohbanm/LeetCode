class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        numbers = {"0","1","2","3","4","5","6","7","8","9"}
        negative = False
        if not s:
            return 0
        elif s[0] == "-":
            negative = True
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]
        if not s:
            return 0
            
        if s[0] not in numbers:
            return 0 
        
        for x in range(len(s)):
            if s[x] not in numbers:
                s = s[0:x]
                break
                
        if negative == True:
            s = int(s) * -1
        if int(s) > 2147483647:
            return 2147483647
        elif int(s) < -2147483648:
            return -2147483648
        return int(s)