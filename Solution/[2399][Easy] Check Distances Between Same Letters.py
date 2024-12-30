class Solution:
    def checkDistances(self, s, distance):
        abc2idx = {}
        for idx, abc in enumerate(s):
            if abc not in abc2idx: abc2idx[abc] = []
            abc2idx[abc].append(idx)

        for abc in abc2idx:
            dist = abc2idx[abc][1] - abc2idx[abc][0] - 1
            num = ord(abc) - ord("a")
            if distance[num] != dist:
                return False
        return True