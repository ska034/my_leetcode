# https://leetcode.com/problems/goal-parser-interpretation/

class Solution:
    def interpret(self, command: str) -> str:
        st = []
        res = []
        for i in command:
            if i == "G":
                res.append("G")
            elif i == "(" or i == "a" or i == "l":
                st.append(i)

            elif i == ")":
                if st[-1] == "(":
                    res.append("o")
                    st.pop()
                else:
                    res.append("al")
                    st = []

        return "".join(res)
