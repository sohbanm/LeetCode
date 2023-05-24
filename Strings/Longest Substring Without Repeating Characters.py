class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in letters:
                letters.remove(s[l])
                l += 1
            else:
                letters.add(s[r])
                res = max(res, r - l + 1)
            
        return res

print(Solution().lengthOfLongestSubstring(s = "pwwkew"))