class Solution:
    def maxRepeating(self, sequence, word):
        check_sequence = []
        n = len(word)
        for i in range(len(sequence)):
            if sequence[i:i+n] == word:
                check_sequence.append(1)
            else:
                check_sequence.append(0)
        
        for i in range(len(check_sequence)):
            if check_sequence[i] > 0:
                if (i+n < len(check_sequence)) and (check_sequence[i+n] > 0):
                    check_sequence[i+n] += check_sequence[i]

        return max(check_sequence)