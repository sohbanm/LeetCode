class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1: return ""
        
        alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        
        
        for j in range(26):
            for i in range(len(palindrome)):
                tempA = palindrome[:i] + alpha[j] + palindrome[i+1:]
                oppI = len(palindrome) - i
                diff = oppI - i-1
                tempB = palindrome[:diff] + alpha[j] + palindrome[diff+1:]
                if tempA != tempA[::-1]:
                    return min(tempA,tempB)
        
        

sol = Solution()

sol.breakPalindrome(palindrome = "abccba")
