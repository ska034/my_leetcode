# https://leetcode.com/problems/summary-ranges/

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        st = []
        res = []

        if not nums:
            return []

        for i in nums:
            if not st:
                st.append(i)
            else:
                if i - 1 != st[-1]:
                    if st[0] != st[-1]:
                        res.append(f"{st[0]}->{st[-1]}")
                    else:
                        res.append(str(st[0]))
                    st = []
                st.append(i)

        if st[0] != st[-1]:
            res.append(f"{st[0]}->{st[-1]}")
        else:
            res.append(str(st[0]))

        return res
