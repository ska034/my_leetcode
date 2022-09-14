# https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        new_path = []
        print(path, "\n")
        for i in range(len(path)):
            if path[i] == "":
                if i == 0:
                    new_path.append("/")
                elif new_path[-1] == "/":
                    continue

            elif path[i] == ".":
                continue

            elif path[i] == "..":
                if new_path[-1] == "/":
                    if len(new_path) > 1:
                        new_path.pop()
                        new_path.pop()
                    else:
                        continue
                else:
                    new_path.pop()
            else:
                new_path.append(path[i])
                new_path.append("/")
        if new_path[-1] == "/" and len(new_path) > 1:
            new_path.pop()

        return "".join(new_path)
