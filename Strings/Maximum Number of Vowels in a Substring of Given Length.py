class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = "aeiou"
        l, r = 0, k
        high = 0

        for i in range(l, r):
            if s[i] in vowel:
                high += 1
        l += 1

        temp = high
        while r < len(s):
            if s[l - 1] in vowel:
                temp -= 1
            
            if s[r] in vowel:
                temp += 1
            high = max(high, temp)
            l += 1
            r += 1
        
        return high
    
# neetcode
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = {"a","e","i","o","u"}

        l, cnt, res = 0, 0, 0
        for r in range(len(s)):
            cnt += 1 if s[r] in vowel else 0

            if r - l + 1 > k:
                cnt -= 1 if s[l] in vowel else 0
                l += 1
                
            res = max(res, cnt)
        
        return res