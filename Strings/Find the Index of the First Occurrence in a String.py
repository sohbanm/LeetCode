class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack==needle: return 0
        l,r = 0,len(needle)
        
        while r<=len(haystack):
            if haystack[l:r]==needle:
                return l
            l+=1
            r+=1
            
        return -1