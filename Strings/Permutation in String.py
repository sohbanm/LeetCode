class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:        
        perms = Counter(s1)
        
        for x in range(len(s2)):
            if Counter(s2[x:len(s1)+x]) == perms:
                return True
        return False