class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0: return ''
        answer = strs[0]
        for i in range(1, len(strs)):
            if len(answer) == 0: return ''
            for j in range(len(strs[i]), 0, -1):
                if strs[i].startswith(answer[:j]):
                    answer = answer[:j]
                    break
            else: return ''
        return answer
