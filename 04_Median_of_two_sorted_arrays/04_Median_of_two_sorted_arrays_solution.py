# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution(object):
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        new_array = nums1 + nums2
        n = len(new_array)
        i = n // 2
        if n % 2:
            return (sorted(new_array)[i])
        else:
            return sum(sorted(new_array)[i - 1:i + 1]) / 2
