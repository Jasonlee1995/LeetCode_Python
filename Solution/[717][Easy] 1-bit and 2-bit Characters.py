class Solution:
    def isOneBitCharacter(self, bits):
        answer = True
        for bit in bits[-2::-1]:
            if bit: answer = not answer
            else: break
        return answer
