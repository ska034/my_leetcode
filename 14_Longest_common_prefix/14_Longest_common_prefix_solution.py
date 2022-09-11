# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        section_s_first = []
        i = 0
        for symbol in s:
            section_s_second = []
            for symbol in s[i:]:
                if symbol not in section_s_second:
                    section_s_second.append(symbol)
                else:
                    break
            if len(section_s_second) > len(section_s_first):
                section_s_first = section_s_second
            i += 1
        return len(section_s_first)

