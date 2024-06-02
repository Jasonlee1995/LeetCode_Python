class Solution:
    def countVowelSubstrings(self, word):
        vowels_idx = {v : -1 for v in 'aeiou'}
        non_vowel_idx = -1
        answer = 0
        for idx, abc in enumerate(word):
            if abc not in vowels_idx:
                non_vowel_idx = idx
            else:
                vowels_idx[abc] = idx
                answer += max(0, min(vowels_idx.values()) - non_vowel_idx)
        return answer