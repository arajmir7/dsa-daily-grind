class Solution:
    def groupAnalgrams(self, strs):
        analgram_map = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in analgram_map:
                analgram_map[key] = []
            analgram_map[key].append(word)
        return list(analgram_map.values())