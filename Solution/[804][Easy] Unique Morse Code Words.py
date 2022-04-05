class Solution:
    def uniqueMorseRepresentations(self, words):
        MORSE = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.',
                 '....', '..', '.---', '-.-', '.-..', '--', '-.',
                 '---', '.--.', '--.-', '.-.', '...', '-', '..-',
                 '...-', '.--', '-..-', '-.--', '--..']

        answer = {''.join(MORSE[ord(letter) - ord('a')] for letter in word)
                  for word in words}
        return len(answer)
