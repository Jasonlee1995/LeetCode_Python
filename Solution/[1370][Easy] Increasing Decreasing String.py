class Solution:
    def sortString(self, s):
        abc_dic = {i : 0 for i in range(97, 123)}
        for abc in s:
            abc_dic[ord(abc)] += 1
        
        answer = ''
        while len(answer) < len(s):
            for abc in range(97, 123):
                if abc_dic[abc] > 0:
                    answer += chr(abc)
                    abc_dic[abc] -= 1
            
            for abc in range(122, 96, -1):
                if abc_dic[abc] > 0:
                    answer += chr(abc)
                    abc_dic[abc] -= 1

        return answer