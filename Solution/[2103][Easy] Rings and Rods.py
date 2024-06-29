class Solution:
    def countPoints(self, rings):
        rods = [set() for _ in range(10)]
        for idx in range(0, len(rings), 2):
            color, rod = rings[idx:idx+2]
            rods[int(rod)].add(color)
        return sum(len(rod) == 3 for rod in rods)