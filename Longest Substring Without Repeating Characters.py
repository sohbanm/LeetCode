#Sliding Window and Two Pointers
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l=0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        
        return res




sol = Solution()

sol.lengthOfLongestSubstring(s = "dvdf")