class Solution:
    def finalValueAfterOperations(self, operations):
        dic = {'++X':1, 'X++':1, '--X':-1, 'X--':-1}
        return sum(dic[operation] for operation in operations)