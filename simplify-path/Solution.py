// https://leetcode.com/problems/simplify-path

class Solution:
    def simplifyPath(self, path: str) -> str:
        directories = path.split("/")
        objs = []
        for dirs in directories:
            if dirs == "." or not dirs:
                continue
            elif dirs == "..":
                if objs:
                    objs.pop()
            else:
                objs.append(dirs)
        string = "/" + "/".join(objs)
        return string