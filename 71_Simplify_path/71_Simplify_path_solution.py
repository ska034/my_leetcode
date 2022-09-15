# https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        new_path = []
        for i in path:
            if i == "" or i == ".":
                continue
            elif i == "..":
                if new_path:
                    new_path.pop()
                else:
                    continue
            else:
                new_path.append(i)

        return "/" + "/".join(new_path)
