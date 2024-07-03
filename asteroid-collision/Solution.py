// https://leetcode.com/problems/asteroid-collision

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        stack = []

        for x in asteroids:
            if not stack or x > 0:
                stack.append(x)
            else:
                while 1:
                    peek = stack[-1]
                    if peek < 0:
                        stack.append(x)
                        break
                    elif peek == -x:
                        stack.pop()
                        break
                    elif peek > -x:
                        break
                    else:
                        stack.pop()
                        if not stack:
                            stack.append(x)
                            break
        return stack