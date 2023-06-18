// https://leetcode.com/problems/top-k-frequent-words

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d, l = {}, []
        for i in words:
            if i in d: 
                d[i] += 1
            else: 
                d[i] = 1
        dsorted = dict(sorted(d.items(), key = lambda item: item[1], reverse = True))
        newd = {}
        for key, value in dsorted.items():
            if value not in newd.keys():
                newd[value] = [key]
            else:
                newd[value].append(key)
                newd[value].sort()
        for value in newd.values():
            l.extend(value)

        return l[:k]
            