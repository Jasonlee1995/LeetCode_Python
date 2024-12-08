class Solution:
    def repeatedCharacter(self, s):
        stack = set()
        for abc in s:
            if abc in stack: return abc
            else: stack.add(abc)