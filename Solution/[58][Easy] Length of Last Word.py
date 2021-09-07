class Solution:
    def lengthOfLastWord(self, s):
        splits = s.split(' ')
        for i in range(len(splits)-1, -1, -1):
            if len(splits[i]) != 0: return len(splits[i])
        return 0
