class Solution:
    def reorderSpaces(self, text):
        words = text.strip().split()
        num_word  = len(words)
        num_blank = text.count(' ')
        
        if num_word > 1:
            blanks = ' ' * (num_blank // (num_word-1))
            return blanks.join(words) + ' ' * (num_blank % (num_word-1))
        else:
            return text.strip() + ' ' * num_blank