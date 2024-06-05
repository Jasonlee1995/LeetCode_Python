import collections

class Solution:
    def checkAlmostEquivalent(self, word1, word2):
        cnt1 = collections.Counter(word1)
        cnt2 = collections.Counter(word2)

        left = (cnt1 - cnt2) + (cnt2 - cnt1)
        for abc in left:
            if left[abc] > 3:
                return False
        return True