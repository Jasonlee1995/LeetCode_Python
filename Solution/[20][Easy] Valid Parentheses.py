class Solution:
    def isValid(self, s):
        infos = {'(' : ')', '{' : '}', '[' : ']'}
        stack = []
        for character in s:
            if character in infos: stack.append(character)
            elif (len(stack) == 0) or (infos[stack[-1]] != character): return False
            else: stack.pop()
        if len(stack) == 0: return True
        return False
