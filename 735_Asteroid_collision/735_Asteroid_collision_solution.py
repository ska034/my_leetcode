# https://leetcode.com/problems/asteroid-collision/

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for i in asteroids:
            if not res:
                res.append(i)
            elif i < 0:
                if res[-1] < 0:
                    res.append(i)
                elif res[-1] + i < 0:
                    while res and res[-1] > 0 and res[-1] + i < 0:
                        res.pop()
                    if not res or res[-1] < 0:
                        res.append(i)
                    elif res[-1] + i == 0:
                        res.pop()
                elif res[-1] + i == 0:
                    res.pop()
            else:
                res.append(i)

        return (res)
