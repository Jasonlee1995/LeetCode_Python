import re

class Solution:
    def countValidWords(self, sentence):
        def check_valid_word(word):
            check_dig  = not re.search(r'[0-9]', word)
            check_hyp0 = not re.search(r'-',  word)
            check_hyp1 = (len(re.findall(r'-',  word)) == 1) and bool(re.search(r'[a-z]-[a-z]',  word))
            check_pun0 = not re.search(r'[!.,]',  word)
            check_pun1 = (len(re.findall(r'[!.,]',  word)) == 1) and (not re.search(r'[!.,][a-z]',  word))

            return check_dig and (check_hyp0 or check_hyp1) and (check_pun0 or check_pun1)

        return sum(check_valid_word(word) for word in sentence.split())