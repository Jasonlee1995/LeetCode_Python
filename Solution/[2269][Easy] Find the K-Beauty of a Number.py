class Solution:
    def divisorSubstrings(self, num, k):
        str_num = str(num)
        answer = 0
        for idx in range(len(str_num)-k+1):
            sub_num = int(str_num[idx:idx+k])
            if sub_num and (num % sub_num == 0):
                answer += 1
        return answer