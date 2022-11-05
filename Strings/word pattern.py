class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        low, high = min(len(pattern),len(s)), max(len(pattern),len(s)) 
        hash = {}
        i = 0
        while i<low:
            if pattern[i] not in hash:
                if s[i] in hash.values():
                    return False
                hash    [pattern[i]] = s[i]
            if hash[pattern[i]] != s[i]:
                return False
            i+=1
        
        if i<high:
            return False
        return True