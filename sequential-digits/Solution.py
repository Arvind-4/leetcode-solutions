// https://leetcode.com/problems/sequential-digits

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []        
        queue = deque([i for i in range(1, 10)])
        while queue:
            num = queue.popleft()
            if low <= num <= high:
                res.append(num)
            last_digit = num % 10
            if last_digit + 1 <= 9:
                queue.append(num * 10 + (last_digit + 1))
        
        return res