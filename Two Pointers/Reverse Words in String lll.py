class Solution:
    def reverseWords(self, s: str) -> str:
        sArray = s.split()

        for i in range(len(sArray)):
            sArray[i] = (sArray[i])[::-1]

        print(" ".join(sArray))

sol = Solution()
sol.reverseWords(s = "Let's take LeetCode contest")