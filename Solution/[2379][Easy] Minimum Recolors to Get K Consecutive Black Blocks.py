class Solution:
    def minimumRecolors(self, blocks, k):
        num_whites = blocks[:k].count("W")
        answer     = num_whites
        for idx in range(k, len(blocks)):
            num_whites += int(blocks[idx]   == "W")
            num_whites -= int(blocks[idx-k] == "W")
            answer = min(answer, num_whites)
        return answer