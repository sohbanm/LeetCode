from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = Counter(s1)
        k = len(s1)
        perm = {}
        l = 0

        for r in range(len(s2)):
            perm[s2[r]] = perm.get(s2[r], 0) + 1

            if (r - l + 1) == k:
                if freq == perm:
                    return True

                else:
                    perm[s2[l]] -= 1
                    if perm[s2[l]] == 0:
                        del perm[s2[l]]

                    l += 1
        
        return False
                    
