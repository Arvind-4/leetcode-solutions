// https://leetcode.com/problems/camelcase-matching

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        l = []

        for query in queries:
            i = j = 0
            while i < len(query):
                if j < len(pattern) and query[i] == pattern[j]:
                    i += 1
                    j += 1
                elif query[i].isupper():
                    break
                else:
                    i += 1
            if i == len(query) and j == len(pattern):
                l.append(True)
            else: l.append(False)
        return l
            
