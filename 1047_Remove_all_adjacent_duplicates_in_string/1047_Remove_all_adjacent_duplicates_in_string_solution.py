# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/

class Solution:
    def removeDuplicates(self, s: str) -> str:
        st = []
        for i in s:
            if not st:
                st.append(i)
            elif st[-1] == i:
                st.pop()
            else:
                st.append(i)
        return "".join(st)
