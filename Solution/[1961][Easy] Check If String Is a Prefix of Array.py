class Solution:
    def isPrefixString(self, s, words):
        stack = ''
        for word in words:
            stack += word
            if stack == s:
                return True
        return False