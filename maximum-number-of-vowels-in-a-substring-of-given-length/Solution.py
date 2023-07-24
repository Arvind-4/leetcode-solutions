// https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        maxVowels, currentVowels, left = 0, 0, 0
        vowels = "aeiou"
        for right in range(n):
            if s[right] in vowels:
                currentVowels += 1
            if right - left + 1 > k:
                if s[left] in vowels:
                    currentVowels -= 1
                left += 1
            
            maxVowels = max(currentVowels, maxVowels)
        return maxVowels