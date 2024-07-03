// https://leetcode.com/problems/flipping-an-image

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        flip = []
        for i in range(len(image)):
            flipped = image[i][::-1]
            for i in range(len(flipped)):
                if flipped[i] == 1:
                    flipped[i] = 0
                else:
                    flipped[i] = 1
            flip.append(flipped)
        return flip
        