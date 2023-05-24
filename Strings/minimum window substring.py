from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = Counter(t)

        l = 0
        sub = {}
        res = None
        low = float("inf")

        for r in range(len(s)):
            if sub == freq:
                while s[l] not in sub:
                    l += 1
                if s[r] in freq and s[r] == s[l]: #might not need first part
                    l += 1
                if low > (r - l + 1):
                    res = s[l:r]
                    low = r - l + 1

                # res = max(res, r - l + 1)
                    # del sub[s[l]]
                    
            else:
                if s[r] in freq:
                    sub[s[r]] = sub.get(s[r], 0) + 1
            

        return res