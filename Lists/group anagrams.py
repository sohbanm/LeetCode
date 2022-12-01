#All anagrams share the same frequency of letters
#Originally thought of using Counter() to get frequency of strings
#used sorted() because to avoid more heavy operations

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = {}
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            
            if sorted_word not in anagram_groups:
                anagram_groups[sorted_word] = []
            anagram_groups[sorted_word].append(word)
            
        return anagram_groups.values()