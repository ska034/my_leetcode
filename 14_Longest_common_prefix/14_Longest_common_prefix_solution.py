# https://leetcode.com/problems/longest-common-prefix/


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        sorted_strs = sorted(strs)
        start = sorted_strs[0]
        end = sorted_strs[-1]
        i = 0
        while i < len(start):
            if start[i] == end[i]:
                i += 1
            else:
                break
        if i > 0:
            return start[:i]
        else:
            return ""
