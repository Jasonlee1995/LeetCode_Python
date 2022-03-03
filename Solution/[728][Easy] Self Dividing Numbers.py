class Solution:
    def selfDividingNumbers(self, left, right):
        answer = []
        for num in range(left, right+1):
            num_str = str(num)
            for letter in num_str:
                if (int(letter) == 0) or (num % int(letter) != 0):
                    break
            else:
                answer.append(num)
        return answer
