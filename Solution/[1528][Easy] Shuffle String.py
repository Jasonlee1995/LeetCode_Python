class Solution:
    def restoreString(self, s, indices):
        answer = [None] * len(indices)
        for letter, idx in zip(s, indices):
            answer[idx] = letter
        return ''.join(answer)