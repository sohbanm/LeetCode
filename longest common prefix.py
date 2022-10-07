class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        output = prefix = strs[0]
        
        for i in range(1, len(strs)):
            
            for j in range(len(strs[i])):
                string = strs[i][:j+1]
                if not prefix.startswith(string):
                    prefix = strs[i][:j]
                    break
            if output.startswith(prefix):
                output = prefix
        return prefix