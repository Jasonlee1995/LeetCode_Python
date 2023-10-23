class Solution:
    def decode(self, encoded, first):
        arr = [first]
        for xor in encoded:
            arr.append(arr[-1] ^ xor)
        return arr