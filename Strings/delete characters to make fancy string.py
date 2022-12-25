class Solution:
    def makeFancyString(self, s: str) -> str:
        i = 1
        res=s[0]
        length = 1
        while i<len(s):
            if s[i] == res[-1]:
                if length==2:
                    while i<len(s) and s[i]==res[-1]:
                        i+=1
                else:
                    res+= s[i]
                    length += 1
            else:
                res+= s[i]
                i+=1
                length=1
        
        return res