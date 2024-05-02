class Solution:
    def twoOutOfThree(self, nums1, nums2, nums3):
        s1, s2, s3 = set(nums1), set(nums2), set(nums3)
        return (s1 & s2) | (s1 & s3) | (s2 & s3)