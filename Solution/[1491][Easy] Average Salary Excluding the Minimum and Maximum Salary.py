class Solution:
    def average(self, salary):
        a, b = salary[0], salary[0]
        total = 0
        for s in salary:
            a, b = min(a, s), max(b, s)
            total += s
        return (total - a - b) / (len(salary) - 2)