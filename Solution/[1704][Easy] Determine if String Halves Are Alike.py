import collections

class Solution:
    def halvesAreAlike(self, s):
        counter_a, counter_b = collections.Counter(s[:len(s)//2]), collections.Counter(s[len(s)//2:])
        vowels = 'aeiouAEIOU'

        a_vowels, b_vowels = sum(counter_a[v] for v in vowels), sum(counter_b[v] for v in vowels)
        return a_vowels == b_vowels