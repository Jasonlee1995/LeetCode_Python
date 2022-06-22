class Solution:
    def isAlienSorted(self, words, order):
        dic = {letter : i for i, letter in enumerate(order)}
        
        for i in range(len(words)-1):
            for j in range(len(words[i])):
                if j == len(words[i+1]):
                    return False
                
                if dic[words[i][j]] > dic[words[i+1][j]]:
                    return False
                elif dic[words[i][j]] < dic[words[i+1][j]]:
                    break
            
        return True