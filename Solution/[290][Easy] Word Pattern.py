class Solution:
    def wordPattern(self, pattern, s):
        if len(pattern) != len(s.split()): return False
        letter2word, word2letter = {}, {}
        for letter, word in zip(pattern, s.split()):
            if letter2word.get(letter) == None: letter2word[letter] = word
            if word2letter.get(word) == None: word2letter[word] = letter
            if (letter2word[letter] != word) or (word2letter[word] != letter): return False
        return True
