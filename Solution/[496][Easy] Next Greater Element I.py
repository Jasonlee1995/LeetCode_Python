class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack, dic = [], {}
        for num in nums2:
            while stack and (stack[-1] < num): dic[stack.pop()] = num
            stack.append(num)

        answer = []
        for num in nums1:
            if num not in dic: answer.append(-1)
            else: answer.append(dic[num])
        return answer
