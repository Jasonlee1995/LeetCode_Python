class Solution:
    def countMatches(self, items, ruleKey, ruleValue):
        keys = ['type', 'color', 'name']
        idx  = keys.index(ruleKey)
        return sum(item[idx] == ruleValue for item in items)