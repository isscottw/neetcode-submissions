class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = defaultdict(list)

        for word in strs:
            counter = [0] * 26
            for letter in word:
                counter[ord(letter) - ord('a')] +=1
            anagrams[tuple(counter)].append(word)
        return list(anagrams.values())
