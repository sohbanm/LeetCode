class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        first = len(s)-1
        count=0
        resA=""
        while first>-1:
            if s[first]=="#":
                count+=1
            elif count==0:
                    resA= s[first] + resA
            else:
                count-=1
            first-=1
            
        second = len(t)-1
        count = 0
        resB=""
        while second>-1:
            if t[second]=="#":
                count+=1
            elif count==0:
                    resB= t[second] + resB
            else:
                count-=1
            second-=1
        return resA==resB