class Solution:
    def getLucky(self, s, k):
        num = ''.join(str(ord(abc) - ord('a') + 1) for abc in s)
        
        for _ in range(k):
            num = str(sum(int(letter) for letter in num))
        return int(num)