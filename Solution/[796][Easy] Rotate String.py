class Solution:
    def rotateString(self, s, goal):
        return (len(s) == len(goal)) and (s in goal*2)
