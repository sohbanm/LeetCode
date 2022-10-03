#Brute Force
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         palindromes = s[0]
#         for i in range(len(s)):
#             for j in range(len(s),i+1,-1):
#                 sub = s[i:j]
#                 if sub[::-1] == sub and len(sub)>len(palindromes):
#                     palindromes = sub
#         print(palindromes)
#         return palindromes

#instead of flipping string to check palindrome, checking to see if characters going outwards are the same
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=''
        resLen = 0

        for i in range(len(s)):
            #odd length
            l,r = i, i
            while (l >= 0) and (r < len(s)) and (s[l] == s[r]):
                if(r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l +1
                l -= 1
                r += 1
            
            #even length
            l,r = i, i+1
            while (l >= 0) and (r < len(s)) and (s[l] == s[r]):
                if(r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l +1
                l -= 1
                r += 1
        
        return res

sol = Solution()
sol.longestPalindrome(s = "cbbd")
                    