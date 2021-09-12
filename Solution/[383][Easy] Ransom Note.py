import collections


class Solution:
    def canConstruct(self, ransomNote, magazine):
        left = collections.Counter(ransomNote) - collections.Counter(magazine)
        if len(list(left.elements())) == 0: return True
        return False
