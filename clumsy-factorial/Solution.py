// https://leetcode.com/problems/clumsy-factorial

class Solution:
    def clumsy(self, n: int) -> int:
        order = {
            0: "*",
            1: "//",
            2: "+",
            3: "-"
        }

        count = 0
        fact = 1
        stack = []
        for i in range(n, 0, -1):
            stack.append(str(i))
            stack.append(order[count % 4])
            count += 1
            if count == 4:
                count = 0
        stack.pop()
        return eval("".join(stack))   