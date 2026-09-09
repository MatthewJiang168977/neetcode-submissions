class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for i in strs: 
            group = [0] * 26
            for j in i: 
                group[ord(j) - ord("a")] += 1 
            anagrams[tuple(group)].append(i)
        return anagrams.values()