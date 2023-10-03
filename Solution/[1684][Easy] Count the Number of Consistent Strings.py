class Solution:
    def countConsistentStrings(self, allowed, words):
        allowed = set(allowed)
        answer = 0
        for word in words:
            left = set(word) - allowed
            if len(left) == 0:
                answer += 1
        return answer