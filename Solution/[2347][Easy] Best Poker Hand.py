import collections

class Solution:
    def bestHand(self, ranks, suits):
        if min(suits) == max(suits): return "Flush"
        
        num = max(collections.Counter(ranks).values())
        if   num >= 3: return "Three of a Kind"
        elif num == 2: return "Pair"
        else:          return "High Card"
