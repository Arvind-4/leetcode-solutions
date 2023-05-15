// https://leetcode.com/problems/perfect-squares

class Solution:
	def numSquares(self, n: int) -> int:
		squares = [i * i for i in range(1, int(n ** 0.5) + 1)]

		values = set()
		values.add((0, 0))

		while values:
			newValues = set()
			for rank, index in values:
				for square in squares:
					if index + square == n: return rank + 1
					newValues.add((rank + 1, index + square))

				values = newValues