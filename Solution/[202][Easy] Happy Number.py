class Solution:
    def isHappy(self, n):
        cal = lambda nums: sum(int(num) ** 2 for num in str(nums))
        node1, node2 = cal(n), cal(cal(n))
        while node1 != node2:
            node1, node2 = cal(node1), cal(cal(node2))
        return node1 == 1
