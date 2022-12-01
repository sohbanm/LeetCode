class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowel = {"a","e","i","o","u"}
        s = s.lower()
        one = two = 0
        i = 0
        first, second = s[:len(s)//2], s[len(s)//2:]
        while i<len(s)//2:
            if first[i] in vowel:
                one+=1
            if second[i] in vowel:
                two+=1
            i+=1
                
        return one==two
    
            