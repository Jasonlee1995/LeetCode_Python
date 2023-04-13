class Solution:
    def reformat(self, s):
        abcs = [c for c in s if c.isalpha()]
        nums = [c for c in s if c.isnumeric()]
        
        if abs(len(abcs) - len(nums)) > 1:
            return ''
        
        answer = ''
        for abc, num in zip(abcs, nums):
            answer += abc + num

        if len(abcs) > len(nums): answer += abcs[-1]
        elif len(abcs) < len(nums): answer = nums[-1] + answer

        return answer