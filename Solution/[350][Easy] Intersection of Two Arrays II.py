import collections


class Solution(object):
    def intersect(self, nums1, nums2):
        intersection = collections.Counter(nums1) & collections.Counter(nums2)
        answer = []
        for num in intersection:
            answer += [num] * intersection[num]
        return answer
