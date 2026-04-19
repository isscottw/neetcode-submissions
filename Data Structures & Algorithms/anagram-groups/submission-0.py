class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = defaultdict(list)

        for word in strs:
            sorted_key = ''.join(sorted(word))
            anagrams[sorted_key].append(word)

        return list(anagrams.values())
